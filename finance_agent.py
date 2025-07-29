from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from stock_utils import get_stock_symbol

load_dotenv()

finance_agent  = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), get_stock_symbol],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Use tables to display data.",
        "If you need to find the symbol for a company, use the get_stock_symbol tool."
        ], # system prompt
    debug_mode=True
)

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

agent_team = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[finance_agent, web_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("Summarize and compare analyst recommendations and fundamentals for SPOT and CRM and share the latest news for SPOT", stream=True) # user prompt