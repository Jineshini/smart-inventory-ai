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
| Planning | Rule-based Planner Agent | Efficient task analysis and workflow coordination |
| Embeddings | Hugging Face Embedding Model | Converts documents into semantic vectors |
| Final Answer Generation | Groq LLM | Fast and accurate AI response generation |

---

# Retrieval-Augmented Generation (RAG)

## Knowledge Base

The system uses inventory-related PDF documents as the knowledge source.

Current knowledge base:

- Inventory Management Document
- Inventory planning concepts
- Stock control information
- Inventory optimization guidelines
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
| Programming Language | Python |
| User Interface | Streamlit |
| Agent Framework | LangGraph |
| LLM Provider | Groq LLM |
| RAG Framework | LangChain |
| Embedding Model | Hugging Face Embeddings |
| Vector Database | ChromaDB |
| Version Control | GitHub |

---

# Project Structure

smart-inventory-ai/

│
├── app.py
├── workflow.py
│
├── agents/
│   ├── planner_agent.py
│   ├── retrieval_agent.py
│   ├── inventory_expert_agent.py
│   └── reflection_agent.py
│
├── graph/
│   └── workflow_graph.py
│
├── rag/
│   ├── embeddings.py
│   └── test_embeddings.py
│
├── knowledge/
│   └── InventoryManagement.pdf
│
├── chroma_db/
│
├── requirements.txt
├── README.md
└── .gitignore
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
What is inventory management?

Generated Response:

Inventory management is a specialized branch of business management that involves strategic planning and control of inventories.

The response is reviewed by the Reflection Agent before displaying to the user.
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

Name:Jineshini

Student ID:ITBIN-2211-0199

Module:

IT41043 – Intelligent Systems (Agentic AI)

Horizon Campus
