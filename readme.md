# Kafka-Zookeeper-PostgreSQL-Elasticsearch-Kibana Stack with Faker Data Generation

This project demonstrates a setup of a data pipeline using Kafka, Zookeeper, PostgreSQL, Elasticsearch, and Kibana. The application generates fake data every 5 seconds using the Faker library and processes it through Kafka.

## Architecture Overview

- **Kafka**: Distributed streaming platform that handles real-time data feeds.
- **Zookeeper**: Centralized service for maintaining configuration information, naming, and providing distributed synchronization for Kafka.
- **PostgreSQL**: Relational database service for persistent data storage.
- **Elasticsearch**: Search and analytics engine that indexes data from Kafka for fast search and analytics.
- **Kibana**: Visualization tool for Elasticsearch, allowing you to create visual representations of the data.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Services

- **Zookeeper**: Coordinates and manages the Kafka brokers.
- **Kafka Broker**: Manages message streams.
- **PostgreSQL**: Database service.
- **Elasticsearch**: Search and analytics engine.
- **Kibana**: Visualization tool for Elasticsearch data.

### Running the Services

1. Clone the repository:

    ```sh
    git clone <repository-url>
    cd <repository-name>
    ```

2. Start the services using Docker Compose:

    ```sh
    docker-compose up -d
    ```

    This will start all the services defined in the `docker-compose.yml` file.

### Docker Compose Configuration

Here's a brief overview of the `docker-compose.yml` configuration:

#### Zookeeper

Zookeeper coordinates and manages the Kafka brokers. It runs on port 2181 and has a health check to ensure it's running properly.

#### Kafka Broker

The Kafka broker manages message streams. It depends on Zookeeper for coordination and runs on ports 9092 and 9101. It has several environment variables configured for proper operation and a health check to ensure the service is available.

#### PostgreSQL

PostgreSQL is the relational database service running on port 5432. It is configured with a default user, password, and database. A health check ensures that the database is ready to accept connections.

#### Elasticsearch

Elasticsearch is the search and analytics engine, running on port 9200. It is configured for single-node operation with security disabled.

#### Kibana

Kibana is the visualization tool for Elasticsearch, running on port 5601. It depends on Elasticsearch and is configured to connect to it.

### Generating Fake Data

A script using the Faker library is used to generate fake data every 5 seconds and send it to Kafka

### Accessing the Services
Kafka: Running on localhost:9092
PostgreSQL: Running on localhost:5432
Elasticsearch: Running on localhost:9200
Kibana: Access via http://localhost:5601

### Visualizing Data in Kibana
Open Kibana at http://localhost:5601.
Configure the Elasticsearch index pattern to match the data sent by the Kafka producer.
Create visualizations and dashboards to analyze the data.

### Contributing
Contributions are welcome! Please submit a pull request or open an issue for any improvements or suggestions.
