from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urljoin

def main():
    url = "https://yoyaku.bassontop.net/RoomSituation.php?pno=5&yyear=2020&ymonth=02&yday=16"
    data = urllib.request.urlopen(url)
    soup = BeautifulSoup(data, "lxml")

    print('2020年02月16日')
    tables = soup.find_all('table')
    time = ''
    trs = tables[6].find_all('tr')
    header = trs[0]
    for th in header.find_all('th'):    
        
        time += ' ' + th.text.strip() + ' |'
    
    print(time)

    for i in range(1,12):
        room = ''
        for th in trs[i].find_all('th'):    
            room += ' ' + th.text.strip() + ' |'
        for td in trs[i].find_all('td'):   
            if td.text.strip() == '':
                room += "  ○ |"
            else:
                room += "  × |"
        print(room) 
    print(time)
if __name__ == '__main__':
    main()
