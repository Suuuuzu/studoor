from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urljoin

def main():
    url = "http://studio-museum.com/shinjyuku_aki/booking.cgi"
    data = urllib.request.urlopen(url)
    soup = BeautifulSoup(data, "lxml")
    tables = soup.find_all('table')

    for d in range(0,29):
        num = 14 + 4*d
        print(num)
        tds = tables[num].find_all('td')
        line ='   '
        day = tds[0].text
        for i in range(1,24):
            line += tds[i].text + '  '
        print(day)
        print(line)

        line_a = "   A      "
        for i in range(26,41):
            if tds[i].has_attr('bgcolor'):
                line_a += "   ×   "
            else:
                line_a += "   ○   "
        print(line_a)

        line_a = "   B-2    "
        for i in range(49,64):
            if tds[i].has_attr('bgcolor'):
                line_a += "   ×   "
            else:
                line_a += "   ○   "
        print(line_a)

        line_a = "   C-3    "
        for i in range(72,87):
            if tds[i].has_attr('bgcolor'):
                line_a += "   ×   "
            else:
                line_a += "   ○   "
        print(line_a)

        line_a = "   C-4    "
        for i in range(95,110):
            if tds[i].has_attr('bgcolor'):
                line_a += "   ×   "
            else:
                line_a += "   ○   "
        print(line_a)

        line_a = "   F-1    "
        for i in range(118,133):
            if tds[i].has_attr('bgcolor'):
                line_a += "   ×   "
            else:
                line_a += "   ○   "
        print(line_a)

        print(' ')
        tables = soup.find_all('table')
        num = 16 + 4 * d
        tds = tables[num].find_all('td')
        line_1F ='   1F      '
        for i in range(1,18):
            line_1F += tds[i].text + '  '
        print(line_1F)
        
        line_a = "   B-1    "
        for i in range(23,39):
            if tds[i].has_attr('bgcolor'):
                line_a += "   ×   "
            else:
                line_a += "   ○   "
        print(line_a)    

        line_a = "   C-1    "
        for i in range(45,61):
            if tds[i].has_attr('bgcolor'):
                line_a += "   ×   "
            else:
                line_a += "   ○   "
        print(line_a)

        line_a = "   C-2    "
        for i in range(67,83):
            if tds[i].has_attr('bgcolor'):
                line_a += "   ×   "
            else:
                line_a += "   ○   "
        print(line_a)

        line_a = "   F-1    "
        for i in range(89,105):
            if tds[i].has_attr('bgcolor'):
                line_a += "   ×   "
            else:
                line_a += "   ○   "
        print(line_a)


    
if __name__ == '__main__':
    main()
