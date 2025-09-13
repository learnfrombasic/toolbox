from confluent_kafka import Consumer


def main():
    conf = {
        "bootstrap.servers": "localhost:9092",
        "group.id": "foo",
        "auto.offset.reset": "smallest",
    }
    topic = "test-lingarscape"

    consumer = Consumer(conf)
    consumer.subscribe([topic])

    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: %s" % msg.error())
            continue
        print("Received message: %s" % msg.value().decode("utf-8"))
        consumer.commit()


if __name__ == "__main__":
    main()
