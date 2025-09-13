import socket

from datetime import datetime
from confluent_kafka import Producer


def get_time_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def main():
    conf = {"bootstrap.servers": "localhost:9092", "client.id": socket.gethostname()}

    producer = Producer(conf)

    topic = "test-lingarscape"

    def acked(err, msg):
        if err is not None:
            print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
        else:
            print("Message produced: %s" % (str(msg)))

    for i in range(10):
        message = f"[{get_time_now()}] This is a test message {i}"
        producer.produce(topic, key="key", value=message, callback=acked)

    producer.poll(1)


if __name__ == "__main__":
    main()
