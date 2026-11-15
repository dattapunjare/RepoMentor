# 📂 RepoMentor
### AI-Powered GitHub Repository Intelligence Platform

RepoMentor is an AI-powered platform designed to help developers and students understand, explore, and analyze GitHub repositories.

It allows users to enter a public GitHub repository URL, explore its files, inspect source code, analyze Python code structure, and receive AI-generated code explanations using a locally running Qwen model.

The goal of RepoMentor is to make understanding unfamiliar codebases easier, faster, and more accessible.

---

## 🚀 Features

### 1. GitHub Repository Explorer
- Enter a public GitHub repository URL.
- Fetch repository information using the GitHub REST API.
- Display repository description, stars, forks, and open issues.
- Explore the repository's file structure.
- Search for specific files.

### 2. Source Code Viewer
- Select files from the repository.
- Fetch and display their source code.
- View code directly inside the Streamlit application.

### 3. Python Architecture Analysis
Analyze individual Python files using Python's Abstract Syntax Tree (AST).

Extract:
- Imported modules
- Function definitions
- Class definitions

### 4. AI Code Explanation
- Uses Qwen 3 (1.7B) through Ollama.
- Explains source code in simple language.
- Identifies the purpose of code.
- Explains important functions, classes, and programming concepts.
- Provides a step-by-step explanation of how the code works.

### 5. Repository-Wide Architecture Analysis
- Fetch Python source files from a GitHub repository.
- Analyze multiple Python files.
- Calculate total imports, functions, and classes.
- Display file-wise architecture information.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| GitHub REST API | Repository and source code retrieval |
| Ollama | Local LLM execution |
| Qwen 3 (1.7B) | AI-powered code explanation |
| Python AST | Static code structure analysis |
| Requests | HTTP API communication |
| Git & GitHub | Version control and project hosting |

---

## 📁 Project Structure

```text
RepoMentor/
│
├── app.py
├── github_service.py
├── ai_service.py
├── architecture_analyzer.py
├── test_architecture.py
├── requirements.txt
├── .gitignore
└── README.md
```

### File Description

| File | Description |
|---|---|
| `app.py` | Main Streamlit application |
| `github_service.py` | GitHub API integration and repository file retrieval |
| `ai_service.py` | Qwen-powered code explanation |
| `architecture_analyzer.py` | Python AST-based architecture analysis |
| `test_architecture.py` | Tests repository-wide architecture analysis |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Excludes virtual environments and sensitive files |

---

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or later
- Git
- Ollama
- Internet connection
- Windows, Linux, or macOS

### Step 1: Clone the Repository

```bash
git clone https://github.com/dattapunjare/RepoMentor.git
```

```bash
cd RepoMentor
```

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Install and Run Ollama

Download Ollama from:

https://ollama.com/

Pull the Qwen model:

```bash
ollama pull qwen3:1.7b
```

Run the model:

```bash
ollama run qwen3:1.7b
```

Keep the Ollama service running when using AI code explanation.

### Step 5: Run RepoMentor

Open another terminal in the project directory, activate the virtual environment, and run:

```bash
python -m streamlit run app.py
```

Open the local application:

```text
http://localhost:8501
```

---

## 🧪 Example Usage

1. Open RepoMentor in your browser.
2. Enter a public GitHub repository URL.

Example:

```text
https://github.com/psf/requests
```

3. Click **Analyze Repository**.
4. Explore the repository files.
5. Select a Python file to view its source code.
6. Run Python Architecture Analysis.
7. Use Qwen AI to explain the selected source code.
8. Run Repository-Wide Architecture Analysis to inspect multiple Python files.

---

## 🔍 Current Project Status

**Implemented Features**

- [x] GitHub repository information retrieval
- [x] Repository file explorer
- [x] Source code viewer
- [x] Single-file Python architecture analysis
- [x] AI-powered code explanation using Qwen
- [x] Repository-wide Python architecture analysis

**Planned Features**

- [ ] Repository dependency analysis
- [ ] Module relationship visualization
- [ ] RAG-based repository question answering
- [ ] Repository-specific learning quiz
- [ ] Code quality and reproducibility checks
- [ ] Architecture visualization

---

## ⚠️ Current Limitations

- Currently supports public GitHub repositories.
- Architecture analysis focuses on Python files.
- AI code explanation requires Ollama and the Qwen model to be available locally.
- Large repositories may take longer to analyze.
- GitHub API rate limits and file-size restrictions may affect retrieval.
- Repository code is analyzed statically; it is not executed.

---

## 🎯 Project Objective

RepoMentor aims to go beyond basic GitHub repository browsing by combining static code analysis and local large language models to help users understand unfamiliar software projects.

It is being developed as an AI/ML engineering capstone project with a focus on repository intelligence, code understanding, and student learning.

---

