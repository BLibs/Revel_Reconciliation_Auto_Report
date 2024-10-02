import requests
from datetime import timedelta, datetime
from config import API_KEY, ESTABLISHMENT_MAPPING, ESTABLISHMENT_NAME
import pandas as pd


# Returns the date in mm/dd/yy format after taking an offset
def get_dates(offset):
    today_date = datetime.now().date()
    adjusted_date = today_date - timedelta(offset)
    # Changing the format to fit the query param requirements of URL
    return adjusted_date.strftime('%m/%d/%y')


# Function is used to pull data from all sites and map to a dataframe. Returns the dataframe object
def get_data(offset):
    # Used to hold the data that we will return
    data_container = []

    # Starting establishment
    est = 1

    # Get the dates that we will pass to the data endpoint
    range_from = get_dates(offset)
    range_to = get_dates(0)

    # For loop goes through all sites and grabs the data one by one
    for _ in range(21):
        # If est is 2 or 3, skip since these are not real establishments
        if est != 2 and est != 3:

            # URL for API endpoint. Company name redacted
            url = f"https://{ESTABLISHMENT_NAME}.revelup.com/reports/sales_summary/json/"

            querystring = {"establishment": est, "range_from": range_from, "range_to": range_to, "posstation": "",
                           "employee": "", "show_unpaid": "1", "show_irregular": "1"}

            headers = {
                "API-AUTHENTICATION": API_KEY
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            data = response.json()

            # Endpoint returns a list. Grabbing the first index in the list to enable the .get functionality
            data = data[0]

            # Pulling the data for the required keys (cash, credit, paper gift certs, total, and net)
            # If value is None, replace the value with 0
            cash_total = data.get('cash_total')
            if cash_total is None:
                cash_total = 0
            credit_total = data.get('credit_total')
            if credit_total is None:
                credit_total = 0
            gift_cert_total = data.get('other_total')
            if gift_cert_total is None:
                gift_cert_total = 0
            total_payments = data.get('total_payments')
            if total_payments is None:
                total_payments = 0
            net_account = data.get('net_account_for')
            if net_account is None:
                net_account = 0

            # Mapping each data point to the list item
            data_container.append({'Establishment': est, 'Cash Total': cash_total, 'Credit Total': credit_total,
                                   'Paper Gift Certs': gift_cert_total, 'Total Payments': total_payments,
                                   'Net Account': net_account})

        # Iterate on the est variable to get the next site
        est += 1

    # When outside for loop, all data collected. Convert to dataframe, map est names, and return it
    df = pd.DataFrame(data_container)
    df['Establishment'] = df['Establishment'].map(ESTABLISHMENT_MAPPING).fillna(df['Establishment'])

    return df
