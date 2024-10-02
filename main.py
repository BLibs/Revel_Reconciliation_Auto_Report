from config import *
from datetime import datetime
from email_file import send_report_email
from file_handling import handle_file
from get_data import get_data, get_dates
import pandas as pd
import time


''' Using Revel API to pull data from sales summary endpoint. Using this data to generate a reconciliation report,
    breaking down the payment types that were used throughout a given timespan. Data is collected for all establishments
    under the corporate umbrella and put into a single report. Without this script, this report had to be ran manually
    for all establishments one by one, multiple times a week during the busy season. This delivers a single report with
    all information in an easy to read format. 
    
    Once data is collected and sorted, it is output to an .xlsx file, which is then linked to another .xlsx file 
    utilizing pivot tables for formatting. This formatted version of the report is then automatically emailed to anyone
    on the recipient list. 
    
    Script is ran as a scheduled Windows task. There are a few conditions outlined below that we accounted for 
    throughout development.'''


''' Off season runs 0 to 7 days. Mondays run from 0 to 4 days in season, and Thur 0 - 3'''

''' Off season setup used because the script needs to be scheduled once and continue to work automatically. By
    declaring when not to run the script, we can keep it active without needing to disable the scheduled task. 
    There are a few rules for how the script is supposed to work. 
    
    OFF SEASON: 
        Runs every Monday for the entire previous week. 
        Only between September and April [9, 10, 11, 12, 1, 2, 3, 4]
        Range from: 0 days
        Range to:   7 days
    IN SEASON:
        Runs twice a week.
        Runs between May and August [5, 6, 7, 8]
        On Mondays, it is run for Thursday, Friday, Saturday, and Sunday
        Range from: 0 days
        Range to:   4 days
        On Thursdays, it is run for Monday, Tuesday, and Wednesday
        Range from: 0 days
        Range to:   3 days'''


''' These variables allow for quick edits when compiling or running the script. Instead of tracking down variables 
    and changing conditions, we simply say whether it is the off season, and if it is not, whether we are running
    this script for a 3-day window or a 4-day window'''
OFF_SEASON = False
OFFSET = 4  # Set this to either 3 or 4 depending on which configuration is needed during in-season


# Main functionality
def main():

    # Months that are going to receive the weekly report. Weekly will not run during outside months
    off_season_months = [9, 10, 11, 12, 1, 2, 3, 4]
    # Get today's date to check against the off season months
    today_date = datetime.now().date()

    def process_data(offset):
        # Populate data in dataframe
        dataframe = get_data(offset)
        # Printing the dataframe to the console
        print("Data Frame")
        print(dataframe)
        # Export to Excel file
        output_path = 'data_files/output.xlsx'
        with pd.ExcelWriter(output_path) as writer:
            dataframe.to_excel(writer, index=False)
        # Calling the handle file function to open, close, and save the file
        handle_file(PATH)
        time.sleep(5)
        # Calling again to make sure the data is updating. Using Excel refresh on open settings with data connection
        handle_file(PATH)
        time.sleep(10)
        # Sending the email. Passing the file path string, and the subject of the email
        send_report_email(PATH, f"{ABR_EST_NAME} Reconciliation File " + get_dates(1))

    ''' Main logic for how the script will run the process_data function depending on variables '''
    # If the script is running in off season mode, and it is an off season month...
    if OFF_SEASON:
        if today_date.month in off_season_months:
            # Run the main script with a date offset of 7, which would get the entire week
            process_data(7)
        else:
            # Otherwise, output that the script is running on the in season schedule
            print("This script is running on the in season delivery schedule")
            time.sleep(2)

    # If the script is running on in season mode, and the month is not an off season month...
    if not OFF_SEASON:
        if today_date.month not in off_season_months:
            process_data(OFFSET)
        else:
            print("This script is running on the off season delivery schedule")
            time.sleep(2)


if __name__ == "__main__":
    main()
