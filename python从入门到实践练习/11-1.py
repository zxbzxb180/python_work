#coding=gbk
def con(city,country,population=''):
	if population:
		address = city+','+country+'-�˿�:'+population
	else:
		address = city+','+country
	return address.title()
add1 = con('����','�й�','50000')
add2 = con('����','�й�')
print(add1)
print(add2)
