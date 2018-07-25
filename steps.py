import urllib.request
import json
from urllib.parse import quote
import string
import re
import xlwt

table = xlwt.Workbook()
sheet = table.add_sheet('sheet1')


service = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'SECRET'

counter = 0
while True:
	ori = input("Start: ").replace(' ','+')
	des = input("End: ").replace(' ','+')
	if ori=='' and des=='':
		break;

	sd = ori+'-'+des
	sheet.write(counter,0,sd)
	counter = counter + 2
	
	nav_request = 'origin={}&destination={}&key={}'.format(ori,des,api_key)
	optional = '&alternatives=true'
	request = service + nav_request + optional 
	url = quote(request,safe=string.printable)
	#print(url) 

	response = urllib.request.urlopen(url).read()
	ans = json.loads(response)
	#print(ans)
	routes =ans['routes']
	print('\n路徑總數:',len(routes))
	print()
	total_routes = len(routes)
	

	re_words = re.compile(u"[\u4e00-\u9fa5]+[0-9]*[\u4e00-\u9fa5]+")
	
	for ct in range(total_routes):
		sum = routes[ct]['summary']
		sheet.write(counter,0,sum)
		counter = counter + 1
		tempa=routes[ct]['legs']		
		tt = len(tempa[0]['steps'])
		for ctt in range(tt):
			#print(tempa[0]['steps'][ctt]['html_instructions'])
			print(tempa[0]['steps'][ctt]['distance']['text'])
			str=tempa[0]['steps'][ctt]['html_instructions']
			rest = re.findall(re_words,str)
			rd =''
			for rt in rest:
				#print(rt,end='')
				print(rt)
				rd+=(rt+' ')
			sheet.write(counter,1,rd)
			sheet.write(counter,2,tempa[0]['steps'][ctt]['distance']['text'])
			counter = counter + 1			
				
		print('/')	
	print('/')		


table.save('road_and_distance.xls')	
	

