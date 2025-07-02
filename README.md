# MicroServices-Routes

This repository showcases a complete microservices-based architecture designed to demonstrate modular, scalable, and containerized backend service development.
🔧 What I Built

    Gateway Service – A centralized entry point that routes requests to the appropriate services.

    Authentication Service – Implements secure access using Basic Authentication and JSON Web Tokens (JWT) to protect internal services.

    Queue-Based Asynchronous Communication – Utilizes RabbitMQ to decouple services and handle asynchronous tasks like media processing.

    Video-to-MP3 Converter – A background worker that processes media files and stores output.

    Data Persistence Layer – Managed using both MongoDB (NoSQL) and SQL databases to suit various services.

    Containerization – All services are dockerized using Docker, ensuring consistent deployment and development environments.

    Container Orchestration – Deployed and managed the entire microservices architecture using Kubernetes, with Minikube as the local cluster and K9s as a terminal UI for cluster management.

🛠️ Tech Stack

    Frameworks: Flask (Python)

    Databases: MongoDB, SQL

    Message Broker: RabbitMQ

    Authentication: Basic Auth + JWT

    Containerization: Docker

    Orchestration: Kubernetes (via Minikube)

    Cluster Management: K9s
