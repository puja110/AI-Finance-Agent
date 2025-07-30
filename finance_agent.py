from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from stock_utils import get_stock_symbol
from dotenv import load_dotenv

load_dotenv()

class FinanceAgent:
    def __init__(self):
        self.agent = Agent(
            name="Finance Assistant",
            model=Groq(id="llama3-8b-8192"),
            tools=[
                YFinanceTools(
                    stock_price=True,
                    analyst_recommendations=True,
                    stock_fundamentals=True
                ),
                DuckDuckGo(),
                get_stock_symbol
            ],
            instructions=[
                "Use get_stock_symbol if the input is a company name.",
                "Use YFinanceTools to get stock fundamentals and analyst recommendations.",
                "Use duckduckgo_news to fetch latest news. Set max_results as an integer (not string).",
                "Use markdown and tables. Do not return tool call logs.",
            ],
            show_tool_calls=False,
            markdown=True
        )

    def get_report(self, prompt: str):
        return self.agent.run(prompt)
