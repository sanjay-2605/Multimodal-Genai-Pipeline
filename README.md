# Multimodal GenAI Pipeline

Enterprise-grade multimodal GenAI system combining:
- Hybrid Retrieval-Augmented Generation (RAG)
- Image generation workflows
- Async orchestration with Kafka
- LangChain + LangGraph pipelines
- FastAPI microservices
- Kubernetes deployment
- LLM routing using OpenAI + Ollama

## Features

- Hybrid retrieval (BM25 + dense retrieval)
- Cross-encoder re-ranking
- Multimodal generation (text + image)
- Kafka-based async orchestration
- LangGraph workflow orchestration
- ChromaDB + FAISS vector stores
- OpenAI + Ollama routing
- Docker + Kubernetes deployment
- RAGAS evaluation pipelines
- MLflow monitoring support

## Tech Stack

### AI / LLM
- OpenAI GPT-4
- Ollama
- Stable Diffusion
- LangChain
- LangGraph
- Hugging Face

### Vector Databases
- ChromaDB
- FAISS

### Backend
- FastAPI
- Kafka
- Redis

### Deployment
- Docker
- Kubernetes
- AWS EC2
- GCP Cloud Run
- Terraform

---

# Architecture

![Architecture](architecture/architecture.png)

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/multimodal-genai-pipeline.git
cd multimodal-genai-pipeline
