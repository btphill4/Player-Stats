# python scrapper to extract stats

import requests
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt 
import numpy as np
# Request docs: https://requests.readthedocs.io/en/latest/
# beautiful soup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/ 
# matplotlib docs: https://matplotlib.org/stable/index.html

def get_Targets():
    # print("Hello World")
    # request url and connect it to BS
    testingURL = "https://nflsavant.com/targets.php?rz=all&ddlYear=2023&week=&ddlTeam=&ddlPosition="
    response = requests.get(testingURL)

    # Beautiful soup object
    # inspect page and look for div class of what we want
    soup = bs(response.content, "html.parser")

    # gives list of splits containing 
    # takes all stats from ESPN table for All games, home games, and away games
    Targets_Table = soup.find("table", attrs={'class':'tablesorter table-bordered table-striped'})

    Targets_Table_Head = Targets_Table.find('thead')
    Target_Table_Head_Row = Targets_Table_Head.find_all('tr')
    targets_data_header = []
    for rows in Target_Table_Head_Row:
        # extract all text going by column and iterating down each row after each for iteration
        cols = rows.find_all('th')
        cols = [ele.text.strip() for ele in cols]
        targets_data_header.append([ele for ele in cols if ele])   # checks for empty values 



    Targets_Table_Body = Targets_Table.find('tbody')
    Target_Table_Body_Rows = Targets_Table_Body.find_all('tr')

    targets_data = []
    # extract the text from each column in the body of the table for each row
    for rows in Target_Table_Body_Rows:
        # extract all text going by column and iterating down each row after each for iteration
        cols = rows.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        targets_data.append([ele for ele in cols if ele])   # checks for empty values 

    # create final data table
    targets_data_complete = []
    targets_data_complete.append(targets_data_header)

    # Combine header row with table rows
    for rows in targets_data:
        targets_data_complete.append(rows)

   
    # print basics
    print(f"Scraping: {testingURL}")
    print("response get code:", response)

    print("Num of comments:",len(targets_data))
    print("All Passing Targets Table:")
    print(*targets_data_complete, sep='\n')


def get_Rushes():
     # print("Hello World")
    # request url and connect it to BS
    NFL_Rushing_URL = "https://www.fantasypros.com/nfl/stats/rb.php"
    response = requests.get(NFL_Rushing_URL)

    # Beautiful soup object
    # inspect page and look for div class of what we want
    soup = bs(response.content, "html.parser")

    # gives list of splits containing 
    # takes all stats from ESPN table for All games, home games, and away games
    # Rushing_Table = soup.find("table", attrs={'class':'table table-bordered table-striped table-hover tablesorter'})
    Rushing_Table = soup.find('table', id="data")

    Rushing_Table_Head = Rushing_Table.find('thead')
    Rushing_Table_Head_Row = Rushing_Table_Head.find_all('tr')
    Rushing_Table_header = []
    for rows in Rushing_Table_Head_Row:
        # extract all text going by column and iterating down each row after each for iteration
        cols = rows.find_all('th')
        cols = [ele.text.strip() for ele in cols]
        Rushing_Table_header.append([ele for ele in cols if ele])   # checks for empty values 
        



    Rushing_Table_Body = Rushing_Table.find('tbody')
    Rushing_Table_Body_Rows = Rushing_Table_Body.find_all('tr')

    Rushing_Data = []
    # extract the text from each column in the body of the table for each row
    for rows in Rushing_Table_Body_Rows:
        # extract all text going by column and iterating down each row after each for iteration
        cols = rows.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        Rushing_Data.append([ele for ele in cols if ele])   # checks for empty values 


    # create final data table
    Rushing_Data_complete = []
    Rushing_Data_complete.append(Rushing_Table_header)

    # Combine header row with table rows
    for rows in  Rushing_Data:
         Rushing_Data_complete.append(rows)

   
    # print basics
    # print(f"Scraping: {NFL_Rushing_URL}")
    # print("response get code:", response)

    print("Num of Players with rushing attempts:",len( Rushing_Data))
    print("All Rushing attempts:")
    print(*Rushing_Data_complete, sep='\n')

    


# get_Targets()
get_Rushes()