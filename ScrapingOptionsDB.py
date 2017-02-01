from urllib.request import urlopen
from bs4 import BeautifulSoup
import sqlite3

list1=['problems-on-trains/','height-and-distance/','simple-interest/',
      'profit-and-loss/','percentage/','calendar/','average/','volume-and-surface-area/',
      'numbers/','problems-on-hcf-and-lcm/','simplification/','surds-and-indices/',
      'chain-rule/','boats-and-streams/','logarithm/','stocks-and-shares/',
      'true-discount/','odd-man-out-and-series/','time-and-distance/','time-and-work/',
      'compound-interest/','partnership/','problems-on-ages/','clock/','area/',
      'permutation-and-combination/','problems-on-numbers/','decimal-fraction/',
      'square-root-and-cube-root/','ratio-and-proportion/','pipes-and-cistern/',
      'alligation-or-mixture/','races-and-games/','probability/','bankers-discount/']


list2=['03800','06900','04600','01800','01700','06200','00600','05800','00100','00200','00400',
       '01600','02800','04200','05300','06400','06700','07000','03600','02900','04900',
       '02400','01200','06300','05400','06500','00900','00300','00500','02300','03300',
       '04500','06100','06600','06800']

list3=[7,2,3,3,3,3,3,3,9,6,3,3,3,3,3,3,3,3,3,6,3,3,3,4,3,3,3,6,3,3,3,3,3,3,3]

print(len(list1))
print(len(list2))
print(len(list3))

conn=sqlite3.connect('MinorProject.db')
c=conn.cursor()

c.execute("CREATE TABLE AptiOptions(SectionId integer, QuestionId integer, Option text)")


list=[]
list4=[]
list5=[]
k=0

for i in range (0,35):
    for j in range (1,list3[i]+1):
        url=urlopen("http://www.indiabix.com/aptitude/"+list1[i]+list2[i]+str(j))
        soup=BeautifulSoup(url,"html.parser")

        for m in soup.find_all(class_="bix-td-option"):               
            list.append(m.get_text().strip())
            list4.append(i+1)


for i in range (1,len(list),2):
    if(list[i-1][0]=="A"):
        k=k+1
    c.execute("INSERT INTO AptiOptions VALUES(?,?,?);",(list4[i],k,list[i]))
    conn.commit()
    

c.execute("SELECT * FROM AptiOptions")
data=c.fetchall()

for row in data:
    print(row)

            


        

