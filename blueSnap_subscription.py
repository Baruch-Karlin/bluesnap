import os
import requests
from requests.auth import HTTPBasicAuth
import json
import argparse

BLUESNAP_PASSWORD = os.environ.get('BLUESNAP_PASSWORD')
BLUESNAP_USER = os.environ.get('BLUESNAP_USER')

USER_JSON = {
            "payerInfo": {
                "zip": 12345,
                "firstName": "Allen",
                "lastName": "A",
                "phone": "210-999-0000"
            },
            "paymentSource":{  
                "creditCardInfo":{  
                    "creditCard":{  
                        "cardNumber":"5555555555554444",
                        "securityCode":"111",
                        "cardType":"MASTERCARD",
                        "expirationMonth":"07",
                        "expirationYear":"2025"
                    },
                    "billingContactInfo":{  
                        "firstName":"BiFirstName",
                        "lastName":"BiLastName",
                        "address1":"BiAddress1",
                        "address2":"BiAddress2",
                        "city":"BiCity",
                        "state":"CA",
                        "country":"us",
                        "zip":"BiZip"
                    }
                }
            },
            "planId": 2709483
        }


def create_subscription(users_json):
    response = requests.post(
        "https://sandbox.bluesnap.com/services/2/recurring/subscriptions",
        auth=HTTPBasicAuth(BLUESNAP_USER, BLUESNAP_PASSWORD),
        json=users_json
        ).json()
    
    return response

response = create_subscription(USER_JSON)

print(json.dumps(response, indent=2))