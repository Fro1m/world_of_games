import requests
import json

def dollar_to_ils(amount):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=ILS&from=USD&amount={amount}"

    payload = {}
    headers = {
        "apikey": "IQbCLxXRf0QqY9ZYOnnu4Nd4Vpvx5IjR"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text
    result_in_text = json.loads(result)
    return result_in_text["result"]



