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
logger = logging.getLogger('consumidor_team')

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
            time.sleep(20)
    return None

def processar_time(mensagem):
    """Simula processamento de time com IA"""
    dados = json.loads(mensagem)
    
    # Simula processamento muito mais lento (4-7 segundos)
    tempo_processamento = random.uniform(4.0, 7.0)
    time.sleep(tempo_processamento)
    
    times = {
        'Flamengo': 0.95,
        'Palmeiras': 0.92,
        'Corinthians': 0.88,
        'São Paulo': 0.91
    }
    
    time_identificado = random.choice(list(times.keys()))
    confianca = times[time_identificado]
    
    resultado = {
        'id': dados['id'],
        'timestamp_processamento': datetime.now().isoformat(),
        'time_detectado': time_identificado,
        'confianca': confianca,
        'tempo_processamento': tempo_processamento,
        'dados_originais': dados
    }
    
    return resultado

def callback(ch, method, properties, body):
    """Callback para processar mensagens recebidas"""
    logger.info(f"Recebida mensagem: {body.decode()}")
    
    try:
        resultado = processar_time(body)
        logger.info(f"Processamento concluído: {json.dumps(resultado, indent=2)}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        logger.error(f"Erro no processamento: {str(e)}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

def main():
    # Configuração dos handlers de sinal
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    connection = conectar_rabbitmq()
    if not connection:
        return

    channel = connection.channel()
    
    channel.exchange_declare(
        exchange='imagens',
        exchange_type='topic',
        durable=True
    )
    
    result = channel.queue_declare('', exclusive=True)
    queue_name = result.method.queue
    
    channel.queue_bind(
        exchange='imagens',
        queue=queue_name,
        routing_key='team'
    )
    
    # Configuração de QoS
    channel.basic_qos(prefetch_count=1)
    
    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback
    )
    
    logger.info('Consumidor de times iniciado. Aguardando mensagens...')
    
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    finally:
        if connection and not connection.is_closed:
            connection.close()

if __name__ == "__main__":
    main()
