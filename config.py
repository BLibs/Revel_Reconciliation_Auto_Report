# Variables that are used throughout the files that make up this project

# API Key for making calls for data
API_KEY = "API key goes here"

# Used to map the names of the establishments in the data (API returns this data with est number, not name)
ESTABLISHMENT_MAPPING = {
        1.0: 'Est 1',
        4.0: 'Est 2',
        5.0: 'Est 3',
        6.0: 'Est 4',
        7.0: 'Est 5',
        8.0: 'Est 6',
        9.0: 'Est 7',
        10.0: 'Est 8',
        11.0: 'Est 9',
        12.0: 'Est 10',
        13.0: 'Est 11',
        14.0: 'Est 12',
        15.0: 'Est 13',
        16.0: 'Est 14',
        17.0: 'Est 15',
        18.0: 'Est 16',
        19.0: 'Est 17',
        20.0: 'Est 18',
        21.0: 'Est 19'

    }

# Excel file PW
EXCEL_PW = "Excel file password goes here"

# Path to the report file with data linkage and pivot tables. This is the one that is sent when ran
PATH = r"C:\PATH TO FILE GOES HERE"

# Email based variables
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'Gmail account address would go here (sender)'
EMAIL_PASSWORD = 'Gmail account password goes here'
RECIPIENT_EMAIL = ['Recipient email address goes here (can be a list of multiple recipients)']

# Establishment name and abbreviated name for use in URL on endpoint and email subject
ESTABLISHMENT_NAME = "Establishment name for URL goes here"
ABR_EST_NAME = "Abbreviated name would go here"
