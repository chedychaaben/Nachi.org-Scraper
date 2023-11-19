from bs4 import BeautifulSoup
from .utils import clean_text

# Bs4 Phase
def scrape_list_page(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    tableDiv = soup.find_all("div" ,("class", "tabular"))
    tbody   =   tableDiv[0].find("tbody")
    elements_of_tbody = tbody.find_all("tr")
    elements = []
    for e in elements_of_tbody:
        try:
            fullName    = clean_text(e.select_one("td:nth-child(1) > a > div.font-bold.group-hover\:underline").text) #(font-bold.group-hover\:underline) is just classname
            # cleaning ID from full name #Example : (Removing , # 20404) from (Raul Carrillo Montano, # 20404)
            if ',' in fullName:
                fullName = fullName.split(',')[0]
            
            #Splitting fullName to first and last
            firstName,lastName = fullName.split()
        except:
            fullName = None
            firstName = lastName = ''
        try:
            companyName = clean_text(e.select_one("td:nth-child(1) > a > div.text-gray-400.text-sm.mt-0\.5").text)    #(text-gray-400.text-sm.mt-0\.5) is just classname
        except:
            companyName = None
        try:
            servicing   = clean_text(e.select_one("td:nth-child(2)").text)
        except:
            servicing = None
        try:
            phone   = clean_text(e.select_one("td:nth-child(3)").text)
        except:
            phone = None
        try:
            detailPageURL= clean_text(e.select_one("td:nth-child(4) > a")['href'])
        except:
            detailPageURL = None

        e = [firstName, lastName, companyName, servicing, phone, detailPageURL]
        elements.append(e)
    return elements