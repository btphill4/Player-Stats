# python scrapper to extract stats
import time
t = time.time()
import requests
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt 
import numpy as np
# Request docs: https://requests.readthedocs.io/en/latest/
# beautiful soup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/ 
# matplotlib docs: https://matplotlib.org/stable/index.html

# =======================================================================================
#                                   Get QB Stats
# =======================================================================================

def get_QBs():
     # print("Hello World")
    # request url and connect it to BS
    NFL_QB_URL = "https://www.fantasypros.com/nfl/stats/qb.php"
    response = requests.get(NFL_QB_URL)

    # Beautiful soup object
    # inspect page and look for div class of what we want
    soup = bs(response.content, "html.parser")

    # gives list of splits containing 
    # takes all stats from ESPN table for All games, home games, and away games
    # QB_Table = soup.find("table", attrs={'class':'table table-bordered table-striped table-hover tablesorter'})
    QB_Table = soup.find('table', id="data")

    QB_Table_Head = QB_Table.find('thead')
    QB_Table_Head_Row = QB_Table_Head.find_all('tr')
    QB_Table_header = []
    for rows in QB_Table_Head_Row:
        # extract all text going by column and iterating down each row after each for iteration
        cols = rows.find_all('th')
        cols = [ele.text.strip() for ele in cols]
        QB_Table_header.append([ele for ele in cols if ele])   # checks for empty values 
        



    QB_Table_Body = QB_Table.find('tbody')
    QB_Table_Body_Rows = QB_Table_Body.find_all('tr')

    QB_Data = []
    # extract the text from each column in the body of the table for each row
    for rows in QB_Table_Body_Rows:
        # extract all text going by column and iterating down each row after each for iteration
        cols = rows.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        QB_Data.append([ele for ele in cols if ele])   # checks for empty values 


    # create final data table
    QB_Data_complete = []
    QB_Data_complete.append(QB_Table_header)

    # Combine header row with table rows
    for rows in  QB_Data:
         QB_Data_complete.append(rows)

    # Remove element at start
    QB_Data_complete.pop(0)
   
    # print basics
    # print(f"Scraping: {NFL_QB_URL}")
    # print("response get code:", response)

    print("Num of Players with QB attempts:",len( QB_Data))
    print("Quaterbacks:")
    print(*QB_Data_complete, sep='\n')
    print("\n============================================================================================================================\n")

    return QB_Data_complete


# =======================================================================================
#                                   Get WR Stats
# =======================================================================================

def get_WRs():
    # print("Hello World")
    # request url and connect it to BS
    # wr_URL = "https://nflsavant.com/WRs.php?rz=all&ddlYear=2023&week=&ddlTeam=&ddlPosition="
    wr_URL = "https://www.fantasypros.com/nfl/stats/wr.php?range=full"
    response = requests.get(wr_URL)

    # Beautiful soup object
    # inspect page and look for div class of what we want
    soup = bs(response.content, "html.parser")

    # Find table
    WRs_Table = soup.find('table', id="data")

    # find header row and append to a header array
    WRs_Table_Head = WRs_Table.find('thead')
    WR_Table_Head_Row = WRs_Table_Head.find_all('tr')
    WRs_data_header = []
    for rows in WR_Table_Head_Row:
        # extract all text going by column and iterating down each row after each for iteration
        cols = rows.find_all('th')
        cols = [ele.text.strip() for ele in cols]
        WRs_data_header.append([ele for ele in cols if ele])   # checks for empty values 


    # find body rows and append to array
    WRs_Table_Body = WRs_Table.find('tbody')
    WR_Table_Body_Rows = WRs_Table_Body.find_all('tr')

    WRs_data = []
    # extract the text from each column in the body of the table for each row
    for rows in WR_Table_Body_Rows:
        # extract all text going by column and iterating down each row after each for iteration
        cols = rows.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        WRs_data.append([ele for ele in cols if ele])   # checks for empty values 

    # create final data table
    WRs_data_complete = []
    WRs_data_complete.append(WRs_data_header)

    # Combine header row with table rows
    for rows in WRs_data:
        WRs_data_complete.append(rows)

    WRs_data_complete.pop(0)
   
    # print basics
    # print(f"Scraping: {wr_URL}")
    # print("response get code:", response)

    # print("Num of comments:",len(WRs_data))
    print("Wide Recievers:")
    print(*WRs_data_complete, sep='\n')
    print("\n============================================================================================================================\n")

    return WRs_data_complete


# =======================================================================================
#                                   Get RB Stats
# =======================================================================================

def get_RBs():
     # print("Hello World")
    # request url and connect it to BS
    WR_URL = "https://www.fantasypros.com/nfl/stats/rb.php"
    response = requests.get(WR_URL)

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

    Rushing_Data_complete.pop(0)
   
    # print basics
    # print(f"Scraping: {WR_URL}")
    # print("response get code:", response)

    print("Num of Players with rushing attempts:",len(Rushing_Data))
    print("Running Backs:")
    print(*Rushing_Data_complete, sep='\n')
    print("\n============================================================================================================================\n")

    return Rushing_Data_complete

# =======================================================================================
#                                   Get RB Stats
# =======================================================================================

def get_TEs():
     # print("Hello World")
    # request url and connect it to BS
    TE_URL = "https://www.fantasypros.com/nfl/stats/te.php"
    response = requests.get(TE_URL)

    # Beautiful soup object
    # inspect page and look for div class of what we want
    soup = bs(response.content, "html.parser")

    # gives list of splits containing 
    # takes all stats from ESPN table for All games, home games, and away games
    # TEs_Table = soup.find("table", attrs={'class':'table table-bordered table-striped table-hover tablesorter'})
    TEs_Table = soup.find('table', id="data")

    TEs_Table_Head = TEs_Table.find('thead')
    TEs_Table_Head_Row = TEs_Table_Head.find_all('tr')
    TEs_Table_header = []
    for rows in TEs_Table_Head_Row:
        # extract all text going by column and iterating down each row after each for iteration
        cols = rows.find_all('th')
        cols = [ele.text.strip() for ele in cols]
        TEs_Table_header.append([ele for ele in cols if ele])   # checks for empty values 
        



    TEs_Table_Body = TEs_Table.find('tbody')
    TEs_Table_Body_Rows = TEs_Table_Body.find_all('tr')

    TEs_Data = []
    # extract the text from each column in the body of the table for each row
    for rows in TEs_Table_Body_Rows:
        # extract all text going by column and iterating down each row after each for iteration
        cols = rows.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        TEs_Data.append([ele for ele in cols if ele])   # checks for empty values 


    # create final data table
    TEs_Data_complete = []
    TEs_Data_complete.append(TEs_Table_header)

    # Combine header row with table rows
    for rows in  TEs_Data:
         TEs_Data_complete.append(rows)

    TEs_Data_complete.pop(0)
   
    # print basics
    # print(f"Scraping: {NFL_TEs_URL}")
    # print("response get code:", response)

    print("Num of Players with TEs attempts:",len( TEs_Data))
    print("Tight Ends:")
    print(*TEs_Data_complete, sep='\n')
    print("\n============================================================================================================================\n")

    return TEs_Data_complete


# =======================================================================================
#                                   Get K Stats
# =======================================================================================

def get_Ks():
     # print("Hello World")
    # request url and connect it to BS
    K_URL = "https://www.fantasypros.com/nfl/stats/k.php?range=full"
    response = requests.get(K_URL)

    # Beautiful soup object
    # inspect page and look for div class of what we want
    soup = bs(response.content, "html.parser")

    # gives list of splits containing 
    # takes all stats from ESPN table for All games, home games, and away games
    # Ks_Table = soup.find("table", attrs={'class':'table table-bordered table-striped table-hover tablesorter'})
    Ks_Table = soup.find('table', id="data")

    Ks_Table_Head = Ks_Table.find('thead')
    Ks_Table_Head_Row = Ks_Table_Head.find_all('tr')
    Ks_Table_header = []
    for rows in Ks_Table_Head_Row:
        # extract all text going by column and iterating down each row after each for iteration
        cols = rows.find_all('th')
        cols = [ele.text.strip() for ele in cols]
        Ks_Table_header.append([ele for ele in cols if ele])   # checks for empty values 
        



    Ks_Table_Body = Ks_Table.find('tbody')
    Ks_Table_Body_Rows = Ks_Table_Body.find_all('tr')

    Ks_Data = []
    # extract the Kxt from each column in the body of the table for each row
    for rows in Ks_Table_Body_Rows:
        # extract all text going by column and iterating down each row after each for iteration
        cols = rows.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        Ks_Data.append([ele for ele in cols if ele])   # checks for empty values 


    # create final data table
    Ks_Data_complete = []
    Ks_Data_complete.append(Ks_Table_header)

    # Combine header row with table rows
    for rows in  Ks_Data:
         Ks_Data_complete.append(rows)

    Ks_Data_complete.pop(0)
   
    # print basics
    # print(f"Scraping: {Ks_URL}")
    # print("response get code:", response)

    print("Num of Players with Ks attempts:",len( Ks_Data))
    print("Kickers:")
    print(*Ks_Data_complete, sep='\n')
    print("\n============================================================================================================================\n")

    return Ks_Data_complete

# =======================================================================================
#                                   Get DST Stats
# =======================================================================================

def get_DSTs():
     # print("Hello World")
    # request url and connect it to BS
    DST_URL = "https://www.fantasypros.com/nfl/stats/dst.php?range=full"
    response = requests.get(DST_URL)

    # Beautiful soup object
    # inspect page and look for div class of what we want
    soup = bs(response.content, "html.parser")

    # gives list of splits containing 
    # takes all stats from ESPN table for All games, home games, and away games
    # Ks_Table = soup.find("table", attrs={'class':'table table-bordered table-striped table-hover tablesorter'})
    DST_Table = soup.find('table', id="data")

    DST_Table_Head = DST_Table.find('thead')
    DST_Table_Head_Row = DST_Table_Head.find_all('tr')
    DST_Table_header = []
    for rows in DST_Table_Head_Row:
        # extract all text going by column and iterating down each row after each for iteration
        cols = rows.find_all('th')
        cols = [ele.text.strip() for ele in cols]
        DST_Table_header.append([ele for ele in cols if ele])   # checks for empty values 
        

    DST_Table_Body = DST_Table.find('tbody')
    DST_Table_Body_Rows = DST_Table_Body.find_all('tr')

    DST_Data = []
    # extract the Kxt from each column in the body of the table for each row
    for rows in DST_Table_Body_Rows:
        # extract all text going by column and iterating down each row after each for iteration
        cols = rows.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        DST_Data.append([ele for ele in cols if ele])   # checks for empty values 


    # create final data table
    DST_Data_complete = []
    DST_Data_complete.append(DST_Table_header)

    # Combine header row with table rows
    for rows in  DST_Data:
         DST_Data_complete.append(rows)

    DST_Data_complete.pop(0)
   
    # print basics
    # print(f"Scraping: {DST_URL}")
    # print("response get code:", response)

    print("Number of Defensive Teams:",len( DST_Data))
    print("Defensive Teams:")
    print(*DST_Data_complete, sep='\n')
    print("\n============================================================================================================================\n")

    return DST_Data_complete

# =======================================================================================
#                       Start of scraper.py main
# =======================================================================================

print("Start scraping tables")

QuaterBacks = get_QBs()
WideRecievers = get_WRs()
RunningBacks = get_RBs()
Tightends = get_TEs()
Kickers = get_Ks()
DefensiveTeams = get_DSTs()



print("End Scraping Tables")

# Check run time at end
# truncates value to 3 decimals
elapsed = '%.3f'%(time.time() - t)
print("Time to run: ", elapsed, "Seconds")