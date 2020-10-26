import re

#Example-1(Find out correct format phone no's using \w)
phonenos = "408-205-9015,408-215-9165,aaa-bbb-cccc"
phnno = re.findall("\w{3}-\w{3}-\w{4}",phonenos)
for phnno1 in phnno:
    print(phnno1)
#Example-2(Find out correct format phone no's using \d)
phone = "408-205-9015,aaa-bbb-cccc"
phn = re.findall("\d{3}-\d{3}-\d{4}",phone)
if phn:
    print("entered correct phone no")
else:
    print("entered wrong phone no")
#Example-3(Find out given name is valid or not
rawstring = "Manohar Dharmala,DDDDDDD MMMMMMMMM"
rawst = re.findall("\w{2,20}\s\w{2,20}",rawstring)
for rawst1 in rawst:
    print(rawst1)

#Example-4(Find out email address is valid or not)
rawstring1 = "mdharmal@cisco.com manhar336@gmail.com deepika.chinta@gmail.com"
rawst2 = re.findall("\w{0,20}.\w+@\w{0,20}.com",rawstring1)
for email in rawst2:
    print("Email address:",email)
'''
#Example-5(Find out phone no's from web page(Web Scraping))


from  urllib.request import  urlopen

url = "http://www.summet.com/dmsi/html/codesamples/addresses.html"
print(url)
print("1....")
response = urlopen(url)
print("2 ...",response)
html = response.read()
print(html)
htmlstr = html.decode()
pdata = re.findall("(\d{3}) \d{3}-\d{4}",htmlstr)
for item in pdata:
    print(item)
'''