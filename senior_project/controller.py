import requests



def make_call(endpoint: str, query: str = "") -> str:
    domain = "https://wizard-world-api.herokuapp.com/"
    url = domain + endpoint 

    response = requests.get(url)
    if response.ok:
        results = format_results(response, endpoint)
    else:
        results = "<p><b><i> Sorry there was a problem connecting to the:"
        results += "database.</i></b></p>"
    return results

def format_results(results, endpoint) -> str:
    results = results.json()
    formatted_results = "<p>"
    for item in results:
        if endpoint == "Houses":
            house = item.get("name")
            colors = item.get("houseColours")
            element = item.get("element")
            animal = item.get("animal")

            formatted_results += f"<b>House</b>: {house}<br><b>colors</b>:"
            formatted_results += f" {colors}"
            formatted_results += f"<br><b>element</b>: {element}<br><b>"
            formatted_results += f"animal</b>: {animal}"
        elif endpoint == "Elixirs":


            formatted_results += "<b>"
        formatted_results += f"</p>"
    return formatted_results

if __name__ == "__main__":
    make_call("Houses")