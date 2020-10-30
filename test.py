import tinvest

TOKEN = ""


def greeting():
    client = tinvest.SyncClient(TOKEN)
    api = tinvest.PortfolioApi(client)

    response = api.portfolio_get()  # requests.Response
    if response.status_code == 200:
        print(response.parse_json())  # tinvest.PortfolioResponse
