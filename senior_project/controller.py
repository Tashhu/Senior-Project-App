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

            formatted_results += f"<b>House</b>: {house}<br>"
            formatted_results += f"<b>Colors</b>: {colors}<br>"
            formatted_results += f"<b>Element</b>: {element}<br>"
            formatted_results += f"<b>Animal</b>: {animal}<br><br>"

        elif endpoint == "Elixirs":
            elixir = item.get("name")
            purpose = item.get("effect")
            ingredients = item.get("ingredients")
            effects = item.get("sideEffects")

            formatted_results += f"<b>Name</b>: {elixir}<br>"
            formatted_results += f"<b>Effect</b>: {purpose}<br>"
            formatted_results += f"<b>Ingredients</b>: {ingredients}<br>"
            formatted_results += f"<b>Side Effects</b>: {effects}<br><br>"

        elif endpoint == "Spells":
            spell = item.get("name")
            chant = item.get("incantation")
            influence = item.get("effect")
            inventor = item.get("creator")

            formatted_results += f"<b>Name</b>: {spell}<br>"
            formatted_results += f"<b>Incantation</b>: {chant}<br>"
            formatted_results += f"<b>Effect</b>: {influence}<br>"
            formatted_results += f"<b>Creator</b>: {inventor}<br><br>"

        formatted_results += f"</p>"
    return formatted_results

if __name__ == "__main__":
    make_call("Houses")