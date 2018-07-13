import urllib.request
import json
from urllib.parse import quote
import string
service = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = '不告訴你<3'

while True:
	ori = input("Start: ").replace(' ','+')
	des = input("End: ").replace(' ','+')
	if ori=='' and des=='':
		break;
	nav_request = 'origin={}&destination={}&key={}'.format(ori,des,api_key)
	optional = '&alternatives=true'
	request = service + nav_request + optional 
	url = quote(request,safe=string.printable)
	#print(url) --OK

	response = urllib.request.urlopen(url).read()
	ans = json.loads(response)
	#print(ans)
	routes =ans['routes']
	print('\n路徑總數:',len(routes))
	print()
	total_routes = len(routes)

	for r in range(total_routes):
		print(routes[r]['summary'])
		leg = routes[r]['legs']
		print(leg[0]['distance']['text'])
		print(leg[0]['duration']['text'])
		#print('/',end='')
		print('/')

#leg1 = routes[0]['legs']
#print(leg1[0]['distance']['text'])
#leg2 = routes[1]['legs']
#print(leg2[0]['distance']['text'])
#sum1 = routes[0]['summary']
#print(sum1)
