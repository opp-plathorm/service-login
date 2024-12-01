from config_kafka import consumer,producer
import requests

def process_message(message):
    print("6")
    url = 'http://api-data-base:8001/api-data-base/login'
    auth_request = {
        'login': message.value['login'],  # Убираем фигурные скобки
        'password': message.value['password']  # Убираем фигурные скобки
    }
    print("6")
    response = requests.post(url, json=auth_request)
    if response.status_code == 200:
        print("7")
        data = response.json()
        return data.get("exists", False)  # Используем get для безопасного доступа
    else:
        print(f'Error: {response.status_code} - {response.text}')
        return "400"


def main():
    print("1")
    for message in consumer:
        print("2")
        # Обрабатываем сообщение и получаем результат
        result = process_message(message)
        print(result)
        print("3")
        # Отправляем результат обратно в Kafka
        producer.send("login-topic", {'login': message.value['login'], 'success': result})
        print("4")
        producer.flush()
        print("5")
        
if __name__ == "__main__":
    main()
