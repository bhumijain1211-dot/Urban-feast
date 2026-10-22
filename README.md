# 🍽️ Urban Feast: AI-Powered Restaurant Booking Agent

Urban Feast is an AI-powered restaurant booking application that lets users interact with a booking system through a conversational interface. It combines a Streamlit frontend, a FastAPI backend, and a Groq-powered LLM (LLaMA 3.3 70B) to understand user requests and work with restaurant availability data.

## ✨ Features

- 💬 **Conversational booking:** book a table using natural language
- 🤖 **AI-powered understanding:** an LLM interprets requests and generates relevant responses
- 📅 **Availability data:** restaurant availability is read from CSV files
- 🔗 **Frontend and backend integration:** Streamlit UI connected to a FastAPI backend
- ⚡ **Fast inference:** Groq API with the LLaMA 3.3 70B model

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| Frontend | Streamlit |
| Backend API | FastAPI + Uvicorn |
| AI / LLM | Groq API (LLaMA 3.3 70B) |
| Data storage | CSV files |

## ⚙️ How It Works

1. The user sends a booking request through the Streamlit interface.
2. The FastAPI backend receives the request.
3. The LLM interprets the user's natural-language input.
4. The app checks the CSV availability data.
5. The response is returned to the frontend and shown to the user.

## 🏗️ Architecture

```text
User → Streamlit Frontend → FastAPI Backend → Groq LLM (LLaMA 3.3 70B)
                                  │
                                  └→ CSV Availability Data
                                  │
User ← Streamlit Frontend ← Booking Response
```

## 📁 Project Structure

```text
urban-feast/
├── frontend/
│   └── app.py              # Streamlit user interface
├── backend/
│   └── main.py             # FastAPI backend
├── data/
│   └── availability.csv    # Restaurant availability data
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- A [Groq API key](https://console.groq.com)
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/urban-feast.git
cd urban-feast

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate           # Windows
# source venv/bin/activate      # macOS / Linux

# 3. Install dependencies
pip install streamlit fastapi uvicorn python-dotenv groq requests pandas
```

### Configuration

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

### Run the App

Start the backend (from the project root):

```bash
uvicorn backend.main:app --reload --port 8000
```

In a second terminal, start the frontend:

```bash
streamlit run frontend/app.py
```

Then open **http://localhost:8501** in your browser.

## 🔌 API Documentation

With the backend running, interactive docs are available at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🔒 Security

- Keep your API key in `.env` and never commit it to GitHub.
- Make sure `.env` and `venv/` are listed in `.gitignore`.

## ⚠️ Limitations

- Availability is stored in CSV files, not a database.
- This is a demo project and is not connected to live restaurant systems.

## 🗺️ Future Improvements

- Database for persistent booking storage
- Booking confirmation and cancellation
- Better input validation and error handling
- Automated tests for the API and booking logic
- Deployment with secure environment configuration
