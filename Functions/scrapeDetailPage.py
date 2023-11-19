from bs4 import BeautifulSoup
from .utils import clean_text

# Bs4 Phase
def scrape_detail_page(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    mainDiv = soup.find("div" ,("class", "mx-auto max-w-screen-md"))

    # State Abbreviation from the first paragraph
    try:
        firstParagraph    = mainDiv.find("div" ,("class", "flex")).find('p').text
            #Removing text from Certified Professional to the end of p
        endId   = firstParagraph.find('Certified Professional')
        firstParagraph = firstParagraph[:endId]
            # Now getting the id of the highest comma
        CommaId    = firstParagraph.rfind(',')
        StateAbbreviation = firstParagraph[CommaId+1:endId]
            # Cleaning spaces
        StateAbbreviation = clean_text(StateAbbreviation)
            # After some reserch, We know that USA states abbreviations are always 2 letters So we will check
        if len(StateAbbreviation) != 2 :
            StateAbbreviation = None
    except:
        StateAbbreviation = ""

    secondSection   = mainDiv.find("div" ,("class", "flex-1"))

    # Website
    visitWebsiteParagraph   = secondSection.find('p', ('class', 'leading-snug'))
    try:
        website         = visitWebsiteParagraph.find('a')['href']
    except:
        website = ""
    # internachiId
    nachiParagraph  = secondSection.find('p', ('class', 'font-mono font-bold')).text
    nachiParagraph  = clean_text(nachiParagraph)
    wordOcc         = nachiParagraph.find("NACHI")
    internachiId    = nachiParagraph[wordOcc:]

    # Mobile Phones
    phonesParagraph = secondSection.find_all('div', ('class', 'mt-2 tabular-nums'))
    phones  = []
    for phoneParagraph in phonesParagraph:
        phoneParagraph.svg.decompose()
        # Phone Type
        phoneType = phoneParagraph.span
        phoneType = clean_text(phoneType.text)
        # Phone Number
        phoneParagraph.span.decompose()
        phoneNumber = clean_text(phoneParagraph.text)
        # Saving
        phones.append([phoneType,phoneNumber])

    # Additional Inspection Services
    listOfServices  =   secondSection.find("ul", ("class", "flex flex-wrap list-reset"))
    services = []
    try:
        allServices = listOfServices.find_all("li")
        for service in allServices:
            service.svg.decompose()
            services.append(clean_text(service.text))
    except:
        pass
    
    e = [internachiId, website, phones, services, StateAbbreviation]
    return e