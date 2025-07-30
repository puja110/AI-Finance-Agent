def get_stock_symbol(company: str) -> str:
    """Fetch the stock symbol for a given company.

    Args:
        company (str): The name of the company.

    Returns:
        str: The stock symbol for the company, or 'Unknown' if not found.
    """
    symbols = {
        "Spotify": "SPOT",
        "Infosys": "INFY",
        "Google": "GOOGL",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Tesla": "TSLA",
        "Salesforce": "CRM",
        "Uber": "UBER",
        "Zoom": "ZM",
    }
    return symbols.get(company, "Unknown")