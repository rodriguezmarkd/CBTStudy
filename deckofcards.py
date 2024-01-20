import requests
import pprint as pp
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

new_deck_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(new_deck_url, verify=False)
api_data = response.json()
deck_id = api_data["deck_id"]


draw_card_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2"

response = requests.get(draw_card_url, verify = False)
api_data = response.json()

print("Deck ID = ", deck_id)

pp.pprint(api_data)

while api_data["remaining"] > 0:
    print("Curent Pair:")
    response = requests.get(draw_card_url, verify = False)
    api_data = response.json()
    for code in api_data["cards"]:
        pp.pprint(code["code"])
    