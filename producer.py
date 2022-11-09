from kafka import KafkaProducer #  pip install kafka-python
import time

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092', value_serializer=str.encode)
for i in range(100000):
    value = str(i)
    print("sending value = " + value)
    producer.send(topic='test10', value=value)
    time.sleep(0.1)



