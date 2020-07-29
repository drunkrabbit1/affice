import requests

API_KEY = 'e60a98867d363b0d43b9e7c58ec498ed'
response_offer = requests.get('http://api.cpanomer1.affise.com/3.0/offers', headers={"API-Key": API_KEY})
json_response_offers = response_offer.json()['offers']

for offer in json_response_offers:
    id = offer['id']
    title = offer['title']
    payments = offer['payments']
    countries = sum(list(payment.get('countries') for payment in payments), [])
    countries_set = set(list(countre for countre in countries))
    response_stats_by_offer = requests.get('http://api.cpanomer1.affise.com/3.0/stats/getbyprogram',
                                       params={
                                           "filter[date_from]": "1990-01-01",
                                           "filter[date_to]": "2020-07-29",
                                       },
                                       headers={"API-Key": API_KEY})
    json_response_stats_by_offer = response_stats_by_offer.json()['stats'][0]['slice']['offer']
    # if json_response_stats_by_offer['pagination']['total_count']:
    #     print(response_stats_by_offer.text)
    print(json_response_stats_by_offer['id'])

    # print([country['countries'] for country in offer['payments']])
# print(response3.json()['stats'][0])
# json_response2 = response2.json()
# for res in json_response2['conversions']:
#     print(res['offer'])
# print(json_response2)
