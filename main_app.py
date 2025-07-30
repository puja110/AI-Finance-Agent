import streamlit as st
from agents.finance_agent import FinanceAgent
from helpers.finance_helper import FinanceHelper
from helpers.stock_utils import get_stock_symbol

class FinanceApp:
    def __init__(self):
        self.agent = FinanceAgent()

    def run(self):
        st.set_page_config(page_title="AI Finance Assistant", layout="centered")
        st.title("AI Finance Agent")

        with st.form("stock_form"):
            company_input = st.text_input("Enter stock symbol or company name:", placeholder="e.g., SPOT or Infosys")
            include_news = st.checkbox("Include Latest News", value=True)
            submitted = st.form_submit_button("Get Financial Report")

        if submitted and company_input:
            symbol = get_stock_symbol(company_input.strip()) if len(company_input.strip()) > 4 else company_input.strip().upper()

            prompt = f"Summarize and compare analyst recommendations and fundamentals for {symbol}."
            if include_news:
                prompt += f" Also share the latest news for {symbol}."

            with st.spinner("Analyzing..."):
                try:
                    response = self.agent.get_report(prompt)
                    final_output = str(response.content) if hasattr(response, "content") else str(response)

                    st.markdown("### Full Report")
                    st.code(final_output)

                    FinanceHelper.render_finance_output(final_output)

                except Exception as e:
                    st.error(f" An error occurred: {e}")

        st.caption("Try these sample inputs: `SPOT`, `CRM`, `Infosys`, `Tesla`, or `Apple`.")

if __name__ == "__main__":
    app = FinanceApp()
    app.run()
