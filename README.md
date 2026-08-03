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

User
   │
   ▼
Planner Agent
   │
   ▼
Retrieval Agent
   │
   ▼
ChromaDB
   │
   ▼
Inventory Expert Agent (Groq)
   │
   ▼
Reflection Agent
   │
   ▼
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

User Query
      │
      ▼
Planner Agent
      │
      ▼
Retrieval Agent
      │
Retrieved Context
      │
      ▼
Inventory Expert Agent
      │
Generated Answer
      │
      ▼
Reflection Agent
      │
Reviewed Answer
      │
      ▼
User
---

# Model Selection Strategy

| Sub-task          | Model              | Cost | Latency   | Reason                 |
| ----------------- | ------------------ | ---- | --------- | ---------------------- |
| Planning          | Rule-based Planner | Free | Very Fast | Intent analysis        |
| Embeddings        | all-MiniLM-L6-v2   | Free | Fast      | Semantic search        |
| Answer Generation | Groq (Llama 3)     | Low  | Very Fast | High-quality reasoning |


---

# Retrieval Evaluation

The retrieval system was tested using five inventory-related queries.

| Query | Retrieval Result |
|--------|------------------|
| What is inventory management? | Relevant |
| Explain EOQ | Relevant |
| What is FIFO? | Relevant |
| Explain Safety Stock | Relevant |
| What is ABC Analysis? | Relevant |

The retrieved document chunks were relevant to the user queries and enabled the LLM to generate accurate responses.

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
├── chroma_db/ (generated automatically)
│
├── requirements.txt
├── README.md
└── .gitignore
---


# Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jineshini/smart-inventory-ai.git
cd smart-inventory-ai
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Key

Create a `.env` file:

```text
GROQ_API_KEY=your_api_key
```

### 6. Run the application

```bash
streamlit run app.py
```

---

# Testing

Example Queries

Example Queries

- What is EOQ?
- Explain Safety Stock.
- What is FIFO?
- Explain ABC Analysis.
- What is Reorder Point?
- What is inventory management?

Generated Response:

Inventory management is a specialized branch of business management that involves strategic planning and control of inventories.

The response is reviewed by the Reflection Agent before displaying to the user.
---

# Deployment

Streamlit Community Cloud

Live URL:

https://smart-inventory-ai-niqv5edtbvhz7bpzqv97vw.streamlit.app/

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
