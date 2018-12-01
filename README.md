# CAITA License Info

## About

CATIA License Info scans the DSLS Administration folder logs and prints the 
results to the console screen or web browser.

The DSLS Administrator tool must be configured to log license usage. To do 
this double click on the server and select the button "License usage tracking" 
and check the licenses you wish to track.

## Why?

The script atttempts to provide easy access to license usage for CATIA users 
without having to check with the CATIA Administrator (or shouting across the 
office).


## Requirements
* Python 3.5 >=
* Flask
* For the machine running the script the account must have read only access to 
the DSLS Administration logs folder.


## Running

### First time

The config.json must first be created. To do that:

    c:\python-app\catia_license_info>python run.py --console
    Could not find config.json file. Would you like to create that now?
    Please enter path to log files:

Enter the folder path for DSLS log files.

    Please enter maximum number of config files to parse:

Enter the last 'n' number of files you wish the script to scan.


### General

    To run the webserver for testing purposes.
    
    python run.py --webserver





