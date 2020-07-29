import requests

API_KEY = ''
DOMAIN = ''
response_offer = requests.get(f'{DOMAIN}/3.0/partner/offers', headers={"API-Key": API_KEY})
json_response_offers = response_offer.json()['offers']


def get_json_conversions():
    response_conversions = requests.get(f'{DOMAIN}/3.0/stats/conversions',
                                        headers={"API-Key": API_KEY},
                                        params={"offer[]": id,
                                                "date_from": "1990-01-01",
                                                "date_to": "2020-07-29"})
    return response_conversions.json()['conversions']


for offer in json_response_offers:
    id = offer['id']
    title = offer['title']
    payments = offer['payments']
    countries = sum(list(payment.get('countries') for payment in payments), [])

    conversions = get_json_conversions()
    conversion = conversions[0] if conversions else {}
    click_id = conversion.get('clickid')
    action_id = conversion.get('action_id')

    text = f"id : {id} \n" \
           f"title :{title} \n" \
           f"countries: {countries} \n" \
           f"click_id: {click_id} \n" \
           f"action_id: {action_id}"
    print(text)
