# What is this ?
This script will find all Certified Inspectors in the US listed on the International Association of Certified Home Inspectors's website.

# How it works ?
1) We make a request to the Listing page:
https://www.nachi.org/certified-inspectors/browse/us

2) Retrieve the number of pages, It's the last paggination number which is located in the bootom of the page.

3) Loop through all the pages by number.
https://www.nachi.org/certified-inspectors/browse/us?page={p}

4) Collect all ListPage informations about inspectors while looping.

5) Saving to a CSV file.

6) Looping through details pages.

7) Saving to another CSV file.

## Advantages
1) This script has it's own way to replace missing values for entites that dosen't have any.
2) It gets the job done

# This script was not fully developed as we can still imporve it.
## Disadvantages
1) The user should wait for the script to finish all scraping before recieving data.
2) The user may be interrupted by bot-dedection algorthims. (Hopefully for us this website dosen't have them as for the date of creating)


# Do you like to develop this script further ?