import os
import requests
from requests.auth import HTTPBasicAuth
import argparse

BLUESNAP_PASSWORD = os.environ.get('BLUESNAP_PASSWORD')
BLUESNAP_USER = os.environ.get('BLUESNAP_USER')

BRONZE = {
    "chargeFrequency": "MONTHLY",
    "gracePeriodDays": 14,
    "trialPeriodDays": 7,
    "initialChargeAmount": 0,
    "name": "Bronze Plan",
    "currency": "USD",
    "maxNumberOfCharges": 12,
    "recurringChargeAmount": 25,
    "chargeOnPlanSwitch": True
}

SILVER = {
    "chargeFrequency": "MONTHLY",
    "gracePeriodDays": 14,
    "trialPeriodDays": 7,
    "initialChargeAmount": 0,
    "name": "Silver Plan",
    "currency": "USD",
    "maxNumberOfCharges": 12,
    "recurringChargeAmount": 50,
    "chargeOnPlanSwitch": True
}

parser = argparse.ArgumentParser(description="insert plan to func")
parser.add_argument('-t','--type',
                    choices=["BRONZE", "SILVER"],
                    help='inserts plan')       
# group = parser.add_mutually_exclusive_group()
# group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
args = parser.parse_args()

def create_plan(plan):
    response = requests.post(
            "https://sandbox.bluesnap.com/services/2/recurring/plans",
            auth=HTTPBasicAuth(BLUESNAP_USER, BLUESNAP_PASSWORD),
            json=plan
        )
    return response 

if __name__ == "__main__":
    if args.type == "BRONZE":
        response = create_plan(BRONZE)
        print(response.json())
    elif args.type == "SILVER":
        response = create_plan(SILVER)
        print(response.json())