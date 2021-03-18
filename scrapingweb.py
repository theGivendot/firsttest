from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen, Request
import httplib2
import urllib
import mechanicalsoup
browser = mechanicalsoup.Browser()
 
# put urls into the array as objects
url = [ 
    "https://www.nytimes.com/2021/03/17/us/atlanta-shooting-spa.html?action=click&module=Spotlight&pgtype=Homepage", 
    "https://www.nytimes.com/2021/03/17/us/asian-women-victims-atlanta-shootings.html?action=click&module=Spotlight&pgtype=Homepage", 
    "https://www.nytimes.com/2021/03/17/world/middleeast/israel-election-netanyahu.html", 
    "https://www.nytimes.com/2021/03/18/nyregion/asian-hate-crimes.html?action=click&module=Spotlight&pgtype=Homepage", 
    "https://www.nytimes.com/live/2021/03/18/us/biden-news-today/?action=click&module=Top%20Stories&pgtype=Homepage", 
    "https://www.nytimes.com/2021/03/18/world/europe/russia-biden-putin-killer.html?action=click&module=Top%20Stories&pgtype=Homepage", 
    "https://www.nytimes.com/2021/03/17/us/politics/russia-elections-trump-intelligence.html?action=click&module=Top%20Stories&pgtype=Homepage", 
    "https://www.nytimes.com/2021/03/16/us/politics/election-interference-russia-2020-assessment.html", 
    "https://www.nytimes.com/2021/03/02/us/politics/biden-putin-navalny-russia.html",   
    "https://www.nytimes.com/1998/12/18/world/on-two-fronts-russia-moscow-orders-us-envoy-home-to-protest-air-strikes.html", 
    "https://www.nytimes.com/2021/03/10/world/europe/russia-twitter.html", 
    "https://www.nytimes.com/2020/12/17/world/europe/russia-putin-navalny-press-conference.html", 
    "https://www.nytimes.com/2018/09/09/world/europe/sergei-skripal-russian-spy-poisoning.html", 
    "https://www.nytimes.com/2019/12/04/world/europe/germany-assassination-russia.html?searchResultPosition=1", 
    ]

urlcount = len(url)
print('scraping ' + str(urlcount) + ' urls...')

var = 0
for i in range(urlcount): # looping through the objects in the array
    page = urlopen(url[var]) # opening each url 
    html = page.read()
    soup = BeautifulSoup(html.decode("utf-8"), "html.parser")
    pagetext = str(soup.find_all('p', {"class" : "css-axufdj evys1bk0"})) # getting the text on the page, different class names to different sites
    urlFix = url[var].replace('/', '') # cleaning up the url so it can be used as a file name
    direct = '/Users/danielluciani/Desktop/webscrapetext/webscrapetest' + urlFix.replace('//', '') + '.txt' # creating the path for the file
    htmlLeft = '<p class="css-axufdj evys1bk0">' # html to clean up 
    pagetextFixed = pagetext.replace('<p class="css-axufdj evys1bk0">', '\n') # replacing the html in the text
    pagetextFixedTwo = pagetextFixed.replace('</p>', '\n \n') # replacing more html left in the text
    pagetextFixedThree = pagetextFixedTwo.replace('</a>', '') # cleaning up the links in the text
    pagetextFixedAgain = pagetextFixedThree.replace('<', '\n \n <') # putting spaces between the text and the links
    pagetextFixedAgainAgain = pagetextFixedAgain.replace('>', '> \n \n') # putting spaces between the text and the links
    pagetextFixedAgainAgainAgain = pagetextFixedAgainAgain.replace('class="css-1g7m0tk" ', '') # cleaning up the html for the links
    file = open(direct, 'w+') # creating a file for each url in the array and wiritng the url's content into the file
    file.write(pagetextFixedAgainAgainAgain) 
    file.close
    var += 1
    # it works!