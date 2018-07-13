# GPro
## 畢業專題 ## 
* 目標1 : 定時爬取 OpenData 並儲入電腦
>　dowload.py

>  每5分鐘 爬取台中市政府資料開放資料/台中市路段動態資訊，並下載至OD(放壓縮檔)並進行解壓縮放入OpenData(放解壓縮檔)

>  附註 : [臺中市路段動態資訊](http://opendata.taichung.gov.tw/dataset/3abb91ea-1a9f-11e8-8f43-00155d021202)

>  ![Demo1](https://i.imgur.com/LvWAf9H.png,dowloadtoComputer)
***

* 目標2 : 將台中市路段靜態資料與台中市路段動態資料做結合，得到 roadsection (路段名稱)及其"速率"
> getValue.py

> 原先 動態資料只有 routeid (路段編號) 及 value (路段速率)等等欄位 ，無從知道路名，在靜態資料裡有其對應關係(routeid <-> roadsection)，

> 先取得靜態的兩個欄位(routeid，roadsection)寫入excel表格，再將動態資料的 routeid 欄位取出比對靜態資料的 routeid ，一樣將動態態資料的 value(速率) 及其 datacollectiontime(資料時間) 寫入excel表格

> 附註 : [臺中市路段靜態資訊](http://opendata.taichung.gov.tw/dataset/3af22636-1a9f-11e8-8f43-00155d021202)

> ![Demo2](https://i.imgur.com/o3XxqZn.png,compare_and_write)
***

* 目標3 : 使用 google maps api / directions api 取得距離(固定)，時間(不固定)，及 路線(途經什麼路...)
> multiroute.py

> 前提: 取得 token 並 啟用 directions api 

> 參閱 : https://developers.google.com/maps/documentation/directions/intro?hl=zh-TW

> 步驟 : 網頁擷取 -> json 解析

> ![Demo3](https://imgur.com/a/FnUAAUr,distance&time&multiroute)
***

