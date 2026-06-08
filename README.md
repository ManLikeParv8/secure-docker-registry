# 🐳 Secure Local Docker Registry & Containerized App

## 📖 Overview
This repository demonstrates a complete Docker deployment workflow. It features a custom, containerized Python web application (`click-counter`) and the complete configuration for a secure local Docker registry. 

The registry is fortified with TLS encryption, custom certificate generation, and `htpasswd` authentication to simulate a production-grade, secure environment.

## ✨ Features
* **Containerized Python Web App:** A custom application packaged and deployed via its own `Dockerfile`.
* **Secure Private Registry:** Hosted locally on port 5001 with enforced HTTPS and Basic Authentication.
* **Data Persistence:** Configured Docker volumes to ensure registry data survives container restarts and deletions.
* **Security First:** Secret keys and password files are intentionally excluded from version control using `.gitignore` to maintain best security practices.

## 🚀 Getting Started

**⚠️ Important Security Note:** Because this project uses real encryption keys and passwords, the `certs/` and `auth/` directories are intentionally ignored by Git. 

To run this project locally, clone the repository and generate your own local security files:
1. Create a `certs/` directory and generate a self-signed `domain.crt` and `domain.key`.
2. Create an `auth/` directory and use an `htpasswd` container to generate your credentials.
3. Launch the secure registry using your generated keys and mapped volumes.
