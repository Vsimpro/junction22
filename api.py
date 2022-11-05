# General notes:

# merchant_id': '6364e0008018ce361efafc85'
# api_token_key': 'l9B2nDnGgcc8eilUx-tlw0qG26kqPesiZFH-Qs8nFTw'

#url = "https://restaurant-api.development.dev.woltapi.com/v1/daas-api/merchants/6364e0008018ce361efafc85/delivery-order"
#url = "https://daas-public-api.development.dev.woltapi.com/merchants/6364e0008018ce361efafc85/delivery-fee"

import requests

class Api:
    
    merchant_id = "6364e0008018ce361efafc85" 
    api_token_key = 'Bearer l9B2nDnGgcc8eilUx-tlw0qG26kqPesiZFH-Qs8nFTw'

    base_endpoint = f"/merchants/{merchant_id}/"

    fee_endpoint = f"/merchants/{merchant_id}/delivery-fee"
    order_endpoint = f"/merchants/{merchant_id}/delivery-order"

    api_gateway = "https://daas-public-api.development.dev.woltapi.com/"



    header = {
        "Authorization": "Bearer l9B2nDnGgcc8eilUx-tlw0qG26kqPesiZFH-Qs8nFTw"
    }

    fee_example_json = {
        "pickup": {
            "location": {
                "formatted_address": "Arkadiankatu 3-6"
            }
        },
        "dropoff": {
            "location": {
                "formatted_address": "Otakaari 24, 02150 Espoo"
            }
        }
    }

    
def main():
    url = f"{Api.api_gateway}{Api.fee_endpoint}"
    print("[+] POST" + url)
    #requests.post(url, headers=Api.header, json=Api.order_example_json).text DONE
    print(requests.post(url, headers=Api.header, json=Api.fee_example_json).text)

if __name__ == "__main__":
    main()