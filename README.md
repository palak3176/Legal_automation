

```markdown
# Legal Document Automation Engine ⚖️🤖

An asynchronous, AI-powered document processing micro-service built with **FastAPI** and **LangChain**. This engine utilizes multimodal AI agents to extract structural party parameters (Name, Address, ID data) directly from scanned legal documents or identity files and instantly reconstructs finalized, formal legal contracts based on target templates.

---

## ✨ Features

* **Multimodal Identity Extraction:** Processes uploaded images/scans asynchronously using `gemini-1.5-flash` to extract key parameters (`name`, `address`, `id_number`) with high precision.
* **Structural Schema Validation:** Enforces strict parameter verification on data payloads using robust Pydantic schemas.
* **Template Ingestion Pipeline:** Merges validated entity details with structural boilerplates while maintaining precise legal jargon and corporate compliance.

---

## 🛠️ Tech Stack

* **Framework:** FastAPI (Asynchronous Python API runtime)
* **LLM Orchestration:** LangChain (`langchain-google-genai`)
* **AI Core Model:** Google Gemini 1.5 Flash
* **Validation Layer:** Pydantic v2
* **File Processing:** `python-docx` (Document compilation support)

---

## 📂 Project Directory Structure

```text
├── agent.py            # Multimodal LLM wrappers and parsing prompts
├── main.py             # Application startup entry point
├── schemas.py          # Pydantic data models managing contract state
└── requirements_2.txt  # Python environment dependencies

```

---

## ⚡ Setup & Installation

### 1. Configure Local Environment

Ensure you have Python 3.9+ installed. Clone this repository framework and install your core dependencies:

```bash
# Navigate to the workspace directory
cd legal-doc-automation

# Install Python requirements
pip install -r requirements_2.txt

```

### 2. Environment Variables Configuration

Create a secure `.env` file inside the root directory of your project to store your access keys:

```env
GEMINI_API_KEY=your_actual_google_gemini_api_key_here

```

### 3. Start the Server

Launch the application locally via `uvicorn`:

```bash
uvicorn main:app --reload --port 8000

```

Your service endpoint will be up and running locally at **`http://127.0.0.1:8000`**.

---

## 📋 API Workflow Blueprint

1. **`POST /extract-party`**
* **Input:** Form-Data containing identity document file bytes (`image/jpeg` or `image/png`).
* **Process:** Passes the payload asynchronously to `DocumentAgent.extract_party_details()`.
* **Output:** Validated structural JSON properties matching the `Party` model structure.


2. **`POST /generate-agreement`**
* **Input:** Active `AgreementState` compilation containing validated `Party` records alongside target template strings.
* **Process:** Passes parameters to `DocumentAgent.generate_final_text()`.
* **Output:** A professionally completed, ready-to-sign legal contract string.



```

```
