import os
import urllib
import requests
from bs4 import BeautifulSoup
import time
import zipfile
from pathlib import Path

# create folder OpenData(xxx.xml) OD(xxx.zip)
os.makedirs('./OpenData',exist_ok=True)
os.makedirs('./OD',exist_ok=True)

# locate the dowload link 
url = "http://opendata.taichung.gov.tw/dataset/3abb91ea-1a9f-11e8-8f43-00155d021202"
html = requests.get(url).text
soup = BeautifulSoup(html,'lxml')
location = soup.find('div',{"class":"btn-group"})
dowload_url = location.a['href']
prefix = "http://opendata.taichung.gov.tw"
complete_dowload_url = prefix+dowload_url

# dowload road dynamic dataset every 5 minutes
# total file's number is 12 (60/5)
counter = 1
while True:
	#path = './OpenData/data'+str(counter)+'.zip'
        path = './OD/data'+str(counter)+'.zip'
        path2 = './OpenData/data'+str(counter)+'.xml'
        urllib.request.urlretrieve(complete_dowload_url,path)
        print('data'+str(counter)+" dowload finished")

        with zipfile.ZipFile(open(path,'rb')) as f:
            for fn in f.namelist():
                e_p = Path(f.extract(fn))
                formatted_time = time.strftime("%Y-%m-%d %H.%M.%S",time.localtime())
                #e_p.rename(path2)
                path3 = './OpenData/'+str(counter)+"_"+formatted_time+'.xml'
                e_p.rename(path3)
        time.sleep(300)
        if counter == 12:
            break
        counter = counter + 1


