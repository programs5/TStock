import tinvest

TOKEN = "t.p9teY6ksRakzPRTJTbPfzLBlU0omtco99uyM8KOVYzOrpMVG___MyOyFjQ3328aRoPcz2ThYe3zjGRFJxtOecw"


def greeting():
    client = tinvest.SyncClient(TOKEN)
    api = tinvest.PortfolioApi(client)

    response = api.portfolio_get()  # requests.Response
    if response.status_code == 200:
        print(response.parse_json())  # tinvest.PortfolioResponse
