# Reconciliation Report Automation

This project automates the generation of a reconciliation report using data pulled from the Revel API's sales summary endpoint. The report provides a detailed breakdown of the payment types used across all establishments under the corporate umbrella, simplifying what was once a manual and time-consuming process. The script automatically collects and formats the data into a single, easy-to-read report, which is sent via email to designated recipients.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Scheduling Logic](#scheduling)
- [Improvements](#improvements)

## Introduction

The reconciliation report provides a breakdown of payment types used during a specific time frame across multiple establishments. Previously, this report had to be generated manually for each establishment, which was inefficient, especially during busy seasons when it needed to be run several times per week.
This script automates the process by pulling sales summary data from the Revel API for all establishments and compiling it into a single .xlsx report. The raw data is linked to a secondary .xlsx file that uses pivot tables for formatting, ensuring the report is easy to read. Once the report is generated, it is emailed automatically to anyone on the recipient list.
The project runs as a scheduled task on Windows, adjusting based on the time of year (off-season vs. in-season) and the number of days the report should cover. This scheduling logic ensures the script runs consistently without manual intervention, even during the off-season.

## Features

- Automates the pulling of sales summary data from the Revel API for all establishments.
- Generates a single .xlsx report with a breakdown of payment types.
- Uses a secondary .xlsx file with pivot tables to format the report.
- Automatically emails the final report to recipients.
- Runs as a scheduled task with dynamic date ranges based on the time of year.



## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/BLibs/Revel_Reconciliation_Auto_Report.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Revel_Reconciliation_Auto_Report
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Update the `config.py` file in the project directory and define the following variables:

```python
API_KEY = “Add API key here”
EXCEL_PW = "Excel file password goes here"
PATH = r"C:\PATH TO FILE GOES HERE"

# Email based variables
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'Gmail account address would go here (sender)'
EMAIL_PASSWORD = 'Gmail account password goes here'
RECIPIENT_EMAIL = ['Recipient email address goes here (can be a list of multiple recipients)']
```

## Usage 

The script can either be ran directly as a Python file or compiled into an .exe with Pyinstaller
- Run the script to start the automation process:
    ```sh
    python main.py
    ```
- Compile the .exe which can then be ran in any environment.
    ```sh
    pyinstaller --onefile --clean main.py

## Scheduling

The script operates differently depending on whether it is the off-season (September to April) or in-season (May to August).
### Off-Season (September to April)
	-	Runs every Monday and generates a report for the entire previous week.
	-	Date range: 0 to 7 days back.
### In-Season (May to August)
	-	Runs twice a week:
	-	Monday: Generates a report for Thursday, Friday, Saturday, and Sunday.
	-	Date range: 0 to 4 days back.
	-	Thursday: Generates a report for Monday, Tuesday, and Wednesday.
	-	Date range: 0 to 3 days back.
This dynamic scheduling setup ensures that reports are consistently generated during both the busy and off-season without needing to disable the task.

## Improvements

1. Provide option for client to generate these reports on their end as well as receiving the automatically generated reports. 
