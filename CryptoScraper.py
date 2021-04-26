#Adam Kuiken
#Crypto-Coin Webscrapper
#Disclaimer:
#Code Inspired by tutorial Below###
#https://www.thepythoncode.com/article/convert-html-tables-into-csv-files-in-python



import requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import matplotlib as plt

lis = ['BTC','ETH','XRP','USDT','BCH','LINK','BSV','ADA','LTC','BNB','CRO','EOS','XTZ','XLM','XMR','TRX','LEO','VET','USDC','ATOM','HT','MIOTA','DASH','NEO','ZEC','ETC','MKR','XEM','ONT','HEDG','LEND','DOGE','COMP','BAT','DGB','SNX','DAI','OKB','KNC','ALGO','FTT','ERD','ZRX','BAND','HYN','THETA','BTT','QTUM','ZIL']
coinName = ['bitcoin','ethereum','xrp','tether','bitcoin-cash','chainlink','bitcoin-sv','cardano','litecoin','binance-coin','crypto-com-coin','eos','tezos','stellar','monero','tron','unus-sed-leo','vechain','usd-coin','cosmos','huobi-token','iota','dash','neo','zcash','ethereum-classic','maker','nem','ontology','hedgetrade','aave','dogecoin','compound','basic-attention-token','digibyte','synthetix-network-token','dai','okb','khyber-network','algorand','ftx-token','elrond','ox','band-protocol','hyperion','theta','bittorrent','qtum','zilliqa']


def get_all_tables(soup):
    """Extracts and returns all tables in a soup object"""
    return soup.find_all("table")

def get_table_headers(table):
    """Given a table soup, returns all the headers"""
    headers = []
    for th in table.find("tr").find_all("th"):
        headers.append(th.text.strip())
    return headers


def get_table_rows(table):
    """Given a table, returns all its rows"""
    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = []
        # grab all td tags in this table row
        tds = tr.find_all("td")
        if len(tds) == 0:
            # if no td tags, search for th tags
            # can be found especially in wikipedia tables below the table
            ths = tr.find_all("th")
            for th in ths:
                cells.append(th.text.strip())
        else:
            # use regular td tags
            for td in tds:
                cells.append(td.text.strip())
        rows.append(cells)
    return rows

def save_as_csv(table_name, headers, rows):
    pd.DataFrame(rows, columns=headers).to_csv(f"{table_name}.csv")


def main(url,key):
    # get the soup
    
    # extract all the tables from the web page
    tables = get_all_tables(soup)
    
    # iterate over all tables
    for i, table in enumerate(tables, start=1):
        if i ==3:
            # get the table headers
            headers = get_table_headers(table)
            # get all the rows of the table
            rows = get_table_rows(table)
            # save table as csv file
            table_name = key + '.csv'
            print(f"[+] Saving {table_name}")
            save_as_csv(table_name, headers, rows)

driver = webdriver.Chrome()
i = 0
for i in range(len(coinName)):
    
    url = 'https://coinmarketcap.com/currencies/'+ coinName[i] + '/historical-data/?start=20200101&end=20200810'
    driver.get(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    main(url,lis[i])

