from config_kafka import consumer,producer

def process_message(message):
    username = message['username']
    password = message['password']
    
    # Проверяем, существует ли пользователь и совпадает ли пароль
    success = username in users_db and users_db[username] == password
    return success

def main():
    for message in consumer:
        # Обрабатываем сообщение и получаем результат
        result = process_message(message.value)
        # Отправляем результат обратно в Kafka
        producer.send("auth-topic", {'username': message.value['username'], 'success': result})
        producer.flush()
    
if __name__ == "__main__":
    main()
