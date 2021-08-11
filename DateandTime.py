# an app for telling time with regex and beautiful soup
import re
import requests
from bs4 import BeautifulSoup
# requests data from this  date and time site
req = requests.get('https://www.timeanddate.com/worldclock/iran/tehran')
# parsing the html code ( not really needed just wanted to use bs4 :))
soup = BeautifulSoup(req.text, 'html.parser')
# prints all collected data from html
text = str((soup.find_all(id='fsdate')))
# print(text)
x = re.findall(">.*<" , text)
print("today is :", x)
# a fake y/n question and a whileLoop just for fun and keeping the page open in .exe file
print("\n" ,"do you wish to continue?y/n")
listt=[]
x = input()
while (x[0] !='y' or  x[0]!='n'):
    y=input()
    listt.append(y)



