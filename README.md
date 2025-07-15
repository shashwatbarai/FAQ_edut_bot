# FAQ Educational Bot

An intelligent FAQ chatbot for Codebasics educational platform that provides instant answers to student queries using advanced AI and vector search technology.

## Overview

This bot leverages Google's Gemini AI and vector embeddings to answer questions about Codebasics courses, bootcamps, and educational content by searching through a comprehensive FAQ database containing real student questions and expert responses.

## Features

- **AI-Powered Responses**: Uses Google's Gemini 2.0 Flash model for natural language understanding
- **Vector Search**: FAISS vector database for semantic similarity matching
- **Contextual Answers**: Provides detailed responses based on actual FAQ content
- **Educational Focus**: Specialized for data analytics, Power BI, Excel, SQL, and Python courses

## Technology Stack

- **LLM**: Google Gemini 2.0 Flash
- **Embeddings**: Google Generative AI Embeddings (models/embedding-001)
- **Vector Database**: FAISS (Facebook AI Similarity Search)
- **Framework**: LangChain for orchestration
- **Data Source**: CSV file with 100+ FAQ entries

## Project Structure

```
FAQ-edu_bot/
├── main.py                 # Main application file
├── codebasics_faqs.csv    # FAQ dataset (100+ Q&A pairs)
├── README.md              # Project documentation
└── .gitignore            # Git ignore file
```

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd FAQ-edu_bot
   ```

2. **Install dependencies**
   ```bash
   pip install langchain-community langchain-google-genai faiss-cpu python-dotenv click regex
   ```

3. **Environment Setup**
   - Create a `.env` file in the project root
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

4. **Run the application**
   ```bash
   python main.py
   ```

## FAQ Dataset

The bot uses a comprehensive FAQ dataset covering:
- Course prerequisites and requirements
- Bootcamp details and duration
- Technical support and troubleshooting
- Career guidance and job assistance
- Platform-specific questions (Power BI, Excel, SQL)
- Certification and exam preparation
- System requirements and compatibility

## How It Works

1. **Data Loading**: CSV file is loaded using LangChain's CSVLoader
2. **Embedding Generation**: FAQ content is converted to vector embeddings
3. **Vector Storage**: Embeddings stored in FAISS for fast similarity search
4. **Query Processing**: User questions are embedded and matched against FAQ vectors
5. **Response Generation**: Relevant context is passed to Gemini for answer generation

## Example Usage

```python
# Example query
result = chain.invoke("Do you have Javascript courses?")
print(result)
```

## Key Components

- **Retrieval QA Chain**: Combines document retrieval with question answering
- **Custom Prompt Template**: Ensures responses stay within FAQ context
- **Temperature Setting**: Low temperature (0.1) for consistent, factual responses
- **Verbose Mode**: Enabled for debugging and transparency

## Limitations

- Responses limited to information available in the FAQ dataset
- Requires Google API key for Gemini access
- Currently configured for Codebasics-specific content

