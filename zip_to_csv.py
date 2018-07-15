import pandas as pd
import zipfile

# Unzip the 2017 flight data
flight_files = ['flight-data-Q1Q2-2017.zip', 'flight-data-Q3Q4-2017.zip']
for myfile in flight_files:
    with zipfile.ZipFile(myfile, 'r') as myzip:
        myzip.extractall()

# Combine individual csv files
filenames = ['01_2017.csv', '02_2017.csv', '03_2017.csv', '04_2017.csv',\
            '05_2017.csv', '06_2017.csv', '07_2017.csv', '08_2017.csv', \
            '09_2017.csv', '10_2017.csv', '11_2017.csv', '12_2017.csv']
combined_csv = pd.concat( [ pd.read_csv(f) for f in filenames ] )

# Output a single combined csv file for Tableau import
combined_csv.to_csv( "2017_flight_data.csv", index=False )