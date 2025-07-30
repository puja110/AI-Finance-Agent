from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from stock_utils import get_stock_symbol

load_dotenv()

finance_agent = Agent(
    name="Finance Assistant",
    model=Groq(id="llama-3.3-70b-versatile"),
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
        "Use duckduckgo_news to fetch latest news. Set `max_results` as an integer (e.g., 5) — not a string.",
        "Use tables for data and markdown for formatting.",
        "Only show final results. Do not return tool call traces or logs."
    ],
    show_tool_calls=False,
    markdown=True
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