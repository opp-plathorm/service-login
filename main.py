from kafka import KafkaConsumer
# import json
import dotenv 
import os

def main():
    # Создаем потребителя
    dotenv.load_dotenv()
    topic = os.getenv("TOPIC","my_topic")
    bootstrap_servers =os.getenv("BOOTSTRAP_SERVERS","kafka:9092")
    
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset='earliest',  # Начинаем с самого раннего сообщения
        api_version=(0, 10,2),
    )

    print(f"Подписка на тему: {topic}")

    try:
        # Бесконечный цикл для получения сообщений
        for message in consumer:
            print(f"{consumer=}")
            print(f"Получено сообщение: {message.value}")
    except KeyboardInterrupt:
        print("Остановка потребителя...")
    finally:
        consumer.close()
    print(f"{consumer=}")
    
if __name__ == "__main__":
    main()
