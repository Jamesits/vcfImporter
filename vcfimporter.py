data  = '''name;company;home;mobile;mobile:work;;
'''

output = '''BEGIN:VCARD
VERSION:2.1
FN:%s
ORG:%s
TEL;WORK;VOICE:%s
TEL;HOME;VOICE:%s
END:VCARD
'''

s = data.split("\n")
for i in s:

	d = i.split(";")
	d = [x.replace(" ","") for x in d]
	print(output % (d[0], d[1], d[2], d[3]))
