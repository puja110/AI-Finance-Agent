import re
import streamlit as st

class FinanceHelper:
    @staticmethod
    def extract_section(output: str, header: str) -> str:
        pattern = rf"\*\*{re.escape(header)}:?\*\*\s*(.*?)(?=\n\*\*|\Z)"
        match = re.search(pattern, output, re.DOTALL | re.IGNORECASE)
        return match.group(1).strip() if match else ""

    @staticmethod
    def render_news_list(news_text: str):
        lines = news_text.strip().split("\n")
        for line in lines:
            if re.match(r"^\d+\.\s", line.strip()):
                if " - " in line:
                    headline, source = line.split(" - ", 1)
                    st.markdown(f"🔹 **{headline.strip()}**  \n*{source.strip()}*")
                else:
                    st.markdown(f"🔹 {line.strip()}")

    @staticmethod
    def render_finance_output(output: str):
        st.markdown("---")

        st.subheader("📊 Analyst Recommendations")
        analyst = FinanceHelper.extract_section(output, "Analyst Recommendations")
        if analyst:
            st.markdown(analyst, unsafe_allow_html=True)

        st.subheader("📈 Stock Fundamentals")
        fundamentals = FinanceHelper.extract_section(output, "Stock Fundamentals")
        if fundamentals:
            st.markdown(fundamentals, unsafe_allow_html=True)

        st.subheader("📰 Latest News")
        news = FinanceHelper.extract_section(output, "Latest News")
        if news:
            if "|" in news:
                st.markdown(news, unsafe_allow_html=True)
            else:
                FinanceHelper.render_news_list(news)

    @staticmethod
    def render_download_button(report_text, filename="financial_report.txt"):
        st.download_button(
            label="Download Final Report",
            data=report_text,
            file_name=filename,
            mime="text/plain"
        )
