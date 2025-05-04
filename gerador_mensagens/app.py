import pika
import time
import random
import json
import logging
import signal
import sys
from datetime import datetime

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('gerador')

# Variável para controle de shutdown
should_exit = False

def signal_handler(signum, frame):
    """Handler para captura de sinais de término"""
    global should_exit
    logger.info('Sinal de término recebido. Finalizando...')
    should_exit = True

def conectar_rabbitmq():
    """Estabelece conexão com RabbitMQ com retry"""
    while not should_exit:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host='rabbitmq',
                    heartbeat=600,
                    blocked_connection_timeout=300
                )
            )
            logger.info("Conectado ao RabbitMQ")
            return connection
        except pika.exceptions.AMQPConnectionError:
            logger.warning("Tentando conectar ao RabbitMQ...")
            time.sleep(5)
    return None

def gerar_mensagem():
    """Gera mensagem simulada com metadata"""
    tipos = ['face', 'team']
    tipo = random.choice(tipos)
    
    mensagem = {
        'id': random.randint(1000, 9999),
        'timestamp': datetime.now().isoformat(),
        'tipo': tipo,
        'dados': f"imagem_simulada_{tipo}_{random.randint(1,100)}",
        'metadata': {
            'formato': 'jpg',
            'tamanho': random.randint(100000, 500000),
            'resolucao': '1920x1080'
        }
    }
    
    return tipo, json.dumps(mensagem)

def main():
    # Configuração dos handlers de sinal
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    connection = conectar_rabbitmq()
    if not connection:
        return

    channel = connection.channel()
    
    # Declara exchange
    channel.exchange_declare(
        exchange='imagens',
        exchange_type='topic',
        durable=True
    )
    
    mensagens_enviadas = 0
    inicio = time.time()
    
    try:
        while not should_exit:
            tipo, mensagem = gerar_mensagem()
            
            channel.basic_publish(
                exchange='imagens',
                routing_key=tipo,
                body=mensagem,
                properties=pika.BasicProperties(
                    delivery_mode=2,  # Mensagem persistente
                    content_type='application/json'
                )
            )
            
            mensagens_enviadas += 1
            if mensagens_enviadas % 100 == 0:
                tempo_decorrido = time.time() - inicio
                taxa = mensagens_enviadas / tempo_decorrido
                logger.info(f"Taxa de envio: {taxa:.2f} msgs/s | Total: {mensagens_enviadas}")
            
            time.sleep(0.5)  # 2 mensagens por segundo
            
    except Exception as e:
        logger.error(f"Erro durante execução: {e}")
    finally:
        logger.info("Finalizando conexão...")
        if connection and not connection.is_closed:
            connection.close()

if __name__ == "__main__":
    main()
