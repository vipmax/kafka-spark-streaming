cd kafka
./bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --topic test10 --partitions=10 --replication-factor=1