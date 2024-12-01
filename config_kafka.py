from kafka import KafkaProducer,KafkaConsumer
import json

consumer = KafkaConsumer(
    
        'auth-topic',
        bootstrap_servers='kafka:9092',
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest',
        api_version = (0,10,2),
        group_id='0'
    )
#kafka
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',  
    api_version = (0,10,2),
    value_serializer=lambda v: json.dumps(v).encode('utf-8') 
    )