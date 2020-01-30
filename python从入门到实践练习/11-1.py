#coding=gbk
def con(city,country,population=''):
	if population:
		address = city+','+country+'-人口:'+population
	else:
		address = city+','+country
	return address.title()
add1 = con('株洲','中国','50000')
add2 = con('株洲','中国')
print(add1)
print(add2)
