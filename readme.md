We need to design a web scraper for the PrimeGov agenda hosting platform. Examples of cities that use this software include San Mateo and Pleasanton

Input: a path endpoint or a batch .csv file of endpoints to scrape. This url should point to the specific page on a city website where agendas are listed out for public review.

Output: a .csv table with the following column data for each agenda listed on this page:

{Column} | {Description}
Index | Autoincrement index
City | City or agency name
Meeting Name | Title of government body
Date / Time | Date / time of meeting
Agenda | URL of agenda pdf
Meeting video | URL of meeting video (if available)
Published minutes | URL of minutes pdf (if available)

For reference and examples, please see this scraping walkthrough for Legistar.

As you build this scraper, keep in mind that we will need to eventually add additional features, including:

Accessing past agendas not included on the city’s main page, e.g. past years.

Filtering agenda scraping by Date range

Filtering agenda scraping by Meeting Name

Downloading all agendas from scraped urls into a specified directory

Scraping staff report urls from scraped agendas.