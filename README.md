# QueryLens - AI Research Agent

🔍 **QueryLens** is a modular AI research agent built with LangGraph that combines web search, content extraction, and LLM summarization.

## ✨ Features

- **Modular Architecture**: Clean separation of concerns with organized modules
- **LangGraph Workflow**: Advanced agent orchestration with state management
- **Smart Web Search**: Uses Tavily API for relevant sources
- **Content Extraction**: Handles HTML and PDF content
- **AI Summarization**: Groq API with Llama 3.1 8B model
- **Multiple Interfaces**: Streamlit web UI and CLI
- **SQLite Storage**: Automatic report persistence

## 🏗️ Project Structure

```
QueryLens/
├── src/
│   ├── agents/           # Agent workflow and state
│   │   ├── __init__.py
│   │   ├── state.py      # Research state management
│   │   └── workflow.py   # LangGraph workflow
│   ├── services/         # Core services
│   │   ├── __init__.py
│   │   ├── web_search.py      # Tavily search service
│   │   ├── content_extractor.py  # HTML/PDF extraction
│   │   └── llm_service.py      # OpenAI summarization
│   ├── database/         # Database operations
│   │   ├── __init__.py
│   │   └── report_db.py  # SQLite database service
│   ├── web/             # Web interfaces
│   │   ├── __init__.py
│   │   └── streamlit_app.py  # Streamlit web UI
│   └── utils/           # Utilities
│       ├── __init__.py
│       └── cli.py       # Command line interface
├── main.py              # Main entry point
├── requirements.txt     # Dependencies
├── env_template.txt     # Environment template
├── README.md           # This file
└── reports.db          # SQLite database (auto-created)
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up API Keys
Create a `.env` file:
```
GROQ_API_KEY=your_groq_key_here
TAVILY_API_KEY=your_tavily_key_here
```

### 3. Run the Application

**Web Interface:**
```bash
streamlit run main.py
```

**Command Line:**
```bash
python -m src.utils.cli "Latest research on AI in education"
```

## 🔧 Architecture

### Modules Overview

- **`agents/`**: Core agent logic with LangGraph workflow
- **`services/`**: External service integrations (Tavily, OpenAI, content extraction)
- **`database/`**: Data persistence layer
- **`web/`**: User interface components
- **`utils/`**: Utility functions and CLI

### Workflow

1. **Search**: `WebSearchService` finds 3 relevant sources via Tavily
2. **Extract**: `ContentExtractorService` extracts content from HTML/PDF
3. **Summarize**: `LLMService` generates summary + key points via Groq (Llama 3.1 8B)
4. **Save**: `ReportDatabase` stores report in SQLite

## 🎯 Usage

### Web Interface
1. Open `http://localhost:8501`
2. Enter your research query
3. Click "Generate Report"
4. View summary, key points, and sources
5. Browse all reports in the Reports page

### Command Line
```bash
# Single query
python -m src.utils.cli "Impact of climate change on agriculture"

# The CLI will output the full report to console
```

## 🔑 API Keys

- **Groq**: Get from [Groq Console](https://console.groq.com/keys)
- **Tavily**: Get from [Tavily](https://tavily.com/)

## 🛠️ Development

### Adding New Services
1. Create new service in `src/services/`
2. Import and use in `src/agents/workflow.py`
3. Add to workflow nodes as needed

### Extending the Database
1. Modify `src/database/report_db.py`
2. Update schema in `_init_database()`
3. Add new methods as needed

### Custom Interfaces
1. Create new interface in `src/web/` or `src/utils/`
2. Import workflow and database services
3. Implement your interface logic

## 📦 Dependencies

- **LangGraph**: Agent workflow orchestration
- **LangChain**: LLM integration with Groq
- **Streamlit**: Web interface
- **Tavily**: Web search API
- **Trafilatura**: HTML content extraction
- **PyPDF**: PDF content extraction
- **SQLite**: Database storage

---

**QueryLens** - Modular AI Research Agent 🔍