from bs4 import BeautifulSoup as bs
import requests as req

def currency(owned,desired,amount):
    url = 'https://www.xe.com/currencyconverter/convert/?Amount='+str(amount)+'&From='+owned+'&To='+desired
    page = req.get(url, headers={'User-Agent':'Mozilla/5.0'})
    soup = bs(page.text,'html.parser')
    finds = soup.find('p',{'class':'result__BigRate-sc-1bsijpp-1 dPdXSB'}).text
    return finds