import requests
from bs4 import BeautifulSoup
from termcolor import colored
import pandas as pd

#Local imports
from Functions.scrapeListPage import scrape_list_page
from Functions.scrapeDetailPage import scrape_detail_page
from Functions.utils import clean_text

# Getting the Total of pages from the bottom paggination
r = requests.get(f'https://www.nachi.org/certified-inspectors/browse/us').text
pagginationPageSoup = BeautifulSoup(r, 'html.parser')
pagginationDiv      = pagginationPageSoup.find(id='listing-pagination')
allLinks            = pagginationDiv.find_all('a')
lastPaggination     = allLinks[len(allLinks)-2].text
lastPagginationInt  = int(clean_text(lastPaggination))

# Looping through all List pages
for p in range(1,lastPagginationInt+1):
    print(colored(f'Scraping Page {p}', 'red'))
    r = requests.get(f'https://www.nachi.org/certified-inspectors/browse/us?page={p}').text
    collected_listing_page_list = scrape_list_page(r) # Returns a list of lists of elements [firstName, lastName, companyName, servicing, phone, detailPageURL]
    print('Listing page OK')


# Saving collected data from list_pages to a CSV Dataframe
listing_page_df = pd.DataFrame(collected_listing_page_list, columns =["First name", "Last name", "Company name", "Servicing", "Phone", "Details page URL"], dtype = str)
listing_page_df.to_csv('output/datasets/Listing_pages.csv', index=False)


collected_details_page_list = []
for i, row in listing_page_df.iterrows():
    print(colored(f'Scraping Details Page {i}', 'red'))
    print(row["Details page URL"])
    r = requests.get(row["Details page URL"]).text
    e = scrape_detail_page(r)
    collected_details_page_list.append(e)
    print('OK')

# Saving collected data from details_pages to a CSV Dataframe
details_page_df = pd.DataFrame(collected_details_page_list, columns =["internachi ID", "Website", "Phones", "Services", "State"], dtype = str)
details_page_df.to_csv('output/datasets/Details_pages.csv', index=False)

