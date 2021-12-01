import requests
from bs4 import BeautifulSoup
import time
import re
import html5lib
import datetime
#Web scraping of weather data.

def extract_number(txt):
    res = re.findall('[0-9.:]', txt)
    res2 = ''
    for x in res:
        res2 += x

    return res2


def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


page = requests.get("https://mausam.imd.gov.in/thiruvananthapuram/",verify=False)

soup = BeautifulSoup(page.content, 'html.parser')
# name = soup.find_all('td', {'align':'left'})


temp = soup.find('div', {'id':'temperature'}).get_text()
rain_chance = soup.find('div', {'id':'temperature1'}).get_text()
sunrise = soup.find('div', {'class':'right-box-equal sun-rise'}).get_text()
sunset = soup.find('div', {'class':'right-box-equal sun-set'}).get_text()
moonrise = soup.find('div', {'class':'right-box-equal moon-rise'}).get_text()
moonset = soup.find('div', {'class':'right-box-equal moon-set'}).get_text()
sun_info = soup.find('li', {'class':'sun-info'}).get_text()

temp = extract_number(temp)
rain_chance = extract_number(rain_chance)
sunrise =extract_number(sunrise)
sunset = extract_number(sunset)
moonrise = extract_number(moonrise)
moonset = extract_number(moonset)
sun_info = extract_number(sun_info)

print("temperature : "+temp)
print("Chance for rain : "+rain_chance)
print("Sunrise : "+sunrise)
print("Sunset : "+sunset)
print("Moonrise : "+moonrise)
print("Moonset : "+moonset)
print("Wind : "+sun_info)

f = open("logdata.txt", "a")
f.write("Updated on "+str(datetime.datetime.now())+"\n")
f.write("temperature : "+temp+"\n"+"Chance for rain : "+rain_chance+"\n")
f.write("Sunrise : "+sunrise+"\n"+"Sunset : "+sunset+"\n")
f.write("Moonrise : "+moonrise+"\n"+"Moonset : "+moonset+"\n")
f.write("Wind : "+sun_info)
f.write("\n--------------------------------\n\n")
f.close()
