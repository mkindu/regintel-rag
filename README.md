# RegIntel-RAG

Privacy-preserving Retrieval-Augmented Generation (RAG) system for answering questions over regulatory documents using fully local embeddings and LLM inference.

## Overview

This project implements a document question-answering system using Retrieval-Augmented Generation (RAG). The system ingests regulatory documents, indexes them using vector embeddings, and retrieves relevant context to generate grounded answers.

The system is designed to run **fully locally**, ensuring that sensitive documents never leave the host environment.

## Planned Features

- Document ingestion pipeline
- Semantic chunking with overlap
- Persistent vector database
- Hybrid retrieval (vector + BM25)
- Grounded responses with citations
- Local LLM inference
- Evaluation and monitoring pipeline

## Project Status

🚧 Phase 1 in progress – Core RAG pipeline implementation.

## Tech Stack

- Python
- FastAPI
- ChromaDB
- Sentence-Transformers
- Ollama