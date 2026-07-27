# Smart Inventory AI Assistant

## Project Overview

Smart Inventory AI Assistant is an Agentic AI application designed to help users retrieve inventory-related information from an inventory knowledge base. The system combines multiple AI agents with a Retrieval-Augmented Generation (RAG) pipeline to generate accurate and context-aware responses.

---

## Problem Statement

Organizations store inventory manuals, warehouse procedures, purchasing policies, and stock management guidelines across multiple documents. Finding the required information manually is time-consuming.

This project addresses this challenge by providing an intelligent inventory assistant capable of retrieving relevant inventory documents and generating reliable responses.

---

## Objectives

### Main Objective

Develop an Agentic AI-based inventory assistant using Retrieval-Augmented Generation (RAG).

### Specific Objectives

- Build a multi-agent AI system.
- Retrieve information from inventory documents.
- Generate accurate inventory responses.
- Deploy using Streamlit Community Cloud.
- Demonstrate agent-to-agent communication.

---

# System Architecture

(Add architecture diagram here)

Example:

User
↓
Planner Agent
↓
Retrieval Agent (RAG)
↓
Inventory Expert Agent
↓
Reflection Agent
↓
Final Response

---

# Agentic AI Design Patterns

## 1. Planning

Purpose:
Analyze user intent and coordinate the workflow.

---

## 2. Tool Use

Purpose:
Retrieve relevant inventory documents using RAG.

---

## 3. Reflection

Purpose:
Review and improve generated responses before presenting them.

---

# Agent Communication

Planner Agent

↓

Retrieval Agent

↓

Inventory Expert Agent

↓

Reflection Agent

---

# Model Selection Strategy

| Task | Model | Reason |
|------|-------|--------|
| Planning | (Update after implementation) | Fast intent classification |
| Final Answer | (Update after implementation) | Better reasoning |

---

# Retrieval-Augmented Generation (RAG)

## Knowledge Base

The system uses 20+ inventory-related documents.

Examples:

- Inventory Manual
- Warehouse SOP
- EOQ Guide
- Safety Stock Guide
- ABC Analysis Guide
- Purchasing Policy

---

## RAG Workflow

Documents

↓

Chunking

↓

Embeddings

↓

Vector Database

↓

Similarity Search

↓

Retrieved Context

↓

AI Response

---

# Technology Stack

| Component | Technology |
|------------|------------|
| Python | Backend |
| Streamlit | UI |
| LangGraph/CrewAI | Agent Framework |
| Groq/OpenRouter | LLM |
| ChromaDB/FAISS | Vector Database |
| GitHub | Version Control |

---

# Project Structure

smart-inventory-ai/

app.py

agents/

rag/

knowledge/

utils/

README.md

requirements.txt

.gitignore

.env

---

# Installation

1. Clone Repository

2. Create Virtual Environment

3. Install Dependencies

4. Configure API Keys

5. Run Streamlit

---

# Testing

Example Queries

- What is EOQ?
- Explain Safety Stock.
- What is FIFO?
- Explain ABC Analysis.
- What is Reorder Point?

---

# Deployment

Streamlit Community Cloud

Live URL:

(To be added after deployment)

---

# Known Limitations

- Knowledge limited to uploaded documents.
- Internet search not included.
- Response quality depends on document quality.

---

# Future Improvements

- Live inventory database integration.
- Voice assistant.
- Sinhala/Tamil language support.
- Inventory analytics dashboard.

---

# Author

Name:

Student ID:

Module:

IT41043 – Intelligent Systems (Agentic AI)

Horizon Campus
