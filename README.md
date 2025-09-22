# QueryLens

An AI-powered research agent that automates web research and generates comprehensive reports using cutting-edge language models and web scraping technologies.

## How It Works

### Architecture

QueryLens uses a streamlined workflow to transform research queries into actionable reports:

```
User Query → Web Search → Content Extraction → AI Summarization → Report Generation
```

**Core Components:**
- **Web Search Service**: Uses Tavily API for intelligent, context-aware web searching
- **Content Extractor**: Employs Trafilatura for clean, readable text extraction from web pages
- **LLM Service**: Leverages Groq's Grok model for intelligent content analysis and summarization
- **Database**: SQLite-based storage system for reports and metadata
- **Workflow Engine**: LangGraph manages the research pipeline with state management
- **Web Interface**: Streamlit application providing an intuitive user experience

### Data Flow

1. **Query Input**: User submits a research question through the Streamlit web interface
2. **Web Search**: Tavily API searches the web and returns the most relevant sources
3. **Content Extraction**: Trafilatura processes each source URL to extract clean, readable text
4. **AI Analysis**: Grok model analyzes the extracted content and generates a coherent summary with key points
5. **Report Storage**: Complete report (summary, key points, sources) is saved to SQLite database
6. **Display**: Results are presented to the user with options to view full reports

## How to Run

### Prerequisites
- Python 3.8 or higher
- GROQ API key (obtain from [Groq Console](https://console.groq.com/))
- TAVILY API key (obtain from [Tavily](https://tavily.com/))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Likith-Athreya/QueryLens.git
cd QueryLens
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Setup

Create a `.env` file in the root directory with your API keys:
```
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### Running the Application

```bash
python main.py
```

This will start the Streamlit web server. Open your browser to `http://localhost:8501` to access QueryLens.

## Example Results

### Sample Query
```
What are the latest developments in quantum computing?
```

### Sample Report Output

**Summary:**  
Quantum computing has made significant strides in recent years, with major breakthroughs in qubit stability, error correction, and practical applications. Companies like IBM, Google, and startups are racing to achieve quantum advantage, while researchers focus on overcoming decoherence and scaling challenges.

**Key Points:**
- IBM's 127-qubit Eagle processor demonstrates improved error rates and gate fidelities
- Google's Sycamore achieved quantum supremacy in 2019, with recent improvements in error correction
- Error correction techniques using surface codes show promise for fault-tolerant quantum computing
- Hybrid quantum-classical algorithms are being developed for near-term applications in optimization and molecular simulation
- Global investment in quantum computing reached $1.7 billion in 2023, with increased focus on practical applications

**Sources:**
1. [IBM Quantum Computing Progress Report](https://www.ibm.com/quantum) - Latest updates on IBM's quantum roadmap and hardware advancements
2. [Google AI Quantum Research](https://ai.google/research/quantum) - Details on Sycamore processor and quantum error correction research
3. [Nature: Quantum Computing Review](https://www.nature.com/articles/s41586-023-06493-y) - Comprehensive review of current state and remaining challenges

## AI Help

No AI assistance was used in the development of this project. All code was written manually based on official documentation, best practices, and personal expertise. The application itself uses AI (Grok via Groq API) for content summarization as part of its core functionality.
