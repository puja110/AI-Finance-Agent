# AI Finance Agent

A powerful AI Agent built with [Streamlit](https://streamlit.io/), [Phidata](https://docs.phidata.com/introduction), and [Groq's LLaMA model](https://console.groq.com/) that summarizes financial data, analyst recommendations, the latest news for any stock symbol or company, and compares stocks in terms of company fundamentals.

---

## Features

- Enter a **stock symbol** (e.g., `SPOT`) or **company name** (e.g., `Spotify`)
- Get **analyst recommendations**, **target prices**, and **average rating**
- View **fundamental data** (e.g., P/E ratio, ROE, market cap)
- Fetch **latest news headlines** from DuckDuckGo
- Organized with a clean component-based structure (Agents, Helpers, UI)
- Built on **Groq’s LLaMA 3 model** using `phidata` agent framework

---

## Project Structure

```bash
AI-Finance-Agent/
├── app/
│   └── main_app.py              # Main Streamlit app entry point
│
├── agents/
│   ├── finance_agent.py         # Sets up the Finance AI agent with tools
│   └── multi_agent.py           # Optional: for future multi-agent systems
│
├── helpers/
│   ├── finance_helper.py        # Parses and renders financial sections
│   └── stock_utils.py           # Utility to resolve company name to stock symbol
│
├── .env                         # Environment variables (API keys, etc.)
├── .gitignore                   # Git ignored files/folders
├── requirements.txt             # Python dependencies
└── README.md                    # Project overview & instructions
```

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/puja110/AI-Finance-Agent.git
cd AI-Finance-Agent
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create .env file

GROQ_API_KEY=your_groq_api_key_here

### 5. Run the Streamlit app

```bash
streamlit run main_app.py
```

## Example Inputs

### Try any of these in the input field:

- SPOT (Spotify)
- Infosys
- CRM (Salesforce)
- Tesla
- Apple

## Application Screenshots

<img width="1251" height="822" alt="financeag1" src="https://github.com/user-attachments/assets/0ef032fe-8d76-4962-b366-9e6529ad2288" />

<img width="1268" height="714" alt="finaceage3" src="https://github.com/user-attachments/assets/33ccc6f5-9689-4576-bcb6-3a8f733bf7d1" />

<img width="1260" height="835" alt="finaceag4" src="https://github.com/user-attachments/assets/7a7d2c4a-5a32-42e2-a001-f0059e398dbc" />

<img width="795" height="758" alt="financestock5" src="https://github.com/user-attachments/assets/2e813120-798b-4a64-8399-8d9c08ab88b2" />

Author
Built by Puja Shrestha
