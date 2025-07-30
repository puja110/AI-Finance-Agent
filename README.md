# AI-Finance-Agent

AI agent which compares stocks in terms of analyst recommendations company fundamentals

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

AI-Finance-Agent/
├── agents/
│ └── finance_agent.py # Sets up the AI agent and tools
| └── multi_agent.py
├── helpers/
│ └── finance_helper.py # Handles parsing and rendering logic
| └── stock_utils.py # Utility to resolve company name to stock symbol
├── main_app.py # Main Streamlit app entry point
├── .env
├── .gitignore
├── requirements.txt
└── README.md

---

## How to Run the Project

### 1. Clone the repository

````bash
git clone https://github.com/puja110/AI-Finance-Agent.git
cd AI-Finance-Agent

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

### 3. Install dependencies
```bash
pip install -r requirements.txt

### 4. Create .env file
GROQ_API_KEY=your_groq_api_key_here


### 5. Run the Streamlit app
```bash
streamlit run main_app.py


## Example Inputs
### Try any of these in the input field:

- SPOT (Spotify)
- Infosys
- CRM (Salesforce)
- Tesla
- Apple


## Application Screenshots


Author
Built by Puja Shrestha
````
