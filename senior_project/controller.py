import requests

domain = "https://wizard-world-api.herokuapp.com/"

def make_call(endpoint: str, query: str = "") -> str:
    url = domain + endpoint 

    response = requests.get(url)
    if response.ok:
        results = format_results(response)

def format_results(results) -> str:
    results = results.json()
    formatted_results = ""
    for item in results:
        title = item.get("title")
        media = item.get("formats")
        formatted_results += "<p><b>"

if __name__ == "__main__":
    make_call("Houses")