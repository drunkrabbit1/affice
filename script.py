import requests

API_KEY = ''
DOMAIN = ''


def get_json_conversions(id):
    response_conversions = requests.get(f'{DOMAIN}/3.0/stats/conversions',
                                        headers={"API-Key": API_KEY},
                                        params={"offer[]": id,
                                                "date_from": "1990-01-01",
                                                "date_to": "2020-07-29"})
    return response_conversions.json()['conversions']


def run(response_offer):
    json_response_offers = response_offer.json()['offers']
    for offer in json_response_offers:
        id = offer['id']
        title = offer['title']
        payments = offer['payments']
        countries = (sum(list(payment.get('countries') for payment in payments), []))
        countries_set = set(countries) if countries else None

        conversions = get_json_conversions(id)
        conversion = conversions[0] if conversions else {}
        click_id = conversion.get('clickid')
        action_id = conversion.get('action_id')

        text = f"offer_id : {id} \n" \
               f"offer_title :{title} \n" \
               f"countries: {countries_set} \n" \
               f"conversion_id: {conversion.get('id')} \n" \
               f"click_id: {click_id} \n"\
               f"action_id: {action_id}"
        print(text, "\n")


partner_offers = requests.get(f'{DOMAIN}/3.0/partner/offers', headers={"API-Key": API_KEY})
offers = requests.get(f'{DOMAIN}/3.0/offers', headers={"API-Key": API_KEY})

run(partner_offers)
print('-----------------------------------------')
run(offers)
