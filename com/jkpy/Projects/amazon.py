import requests
from bs4 import BeautifulSoup
URL = "https://www.amazon.in/dp/B07DJCVTDN/ref=gwdb_bmc_0_OnePlus%207T?pf_rd_s=merchandised-search-5&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=1YRG4E9GCYD68T86875D&pf_rd_p=9535ba6c-ca30-49f0-9dca-fdaf22adf336&th=1"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"}

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content,'html.parser')

# print(soup.prettify())
# title = soup.find(id="productTitle").get_text()

price = soup.find(id = "priceblock_ourprice")
print(price)

# print(soup.find(id="productTitle").get_text())