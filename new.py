
from selenium import webdriver
from selenium.webdriver.support.ui import Select


import glob, os
import time
print("[Taking Input]")
HINP = input("Input Hall. Eg: \"Hall 1\"(without quotes) ")

WINP = input("Input Wing. Eg: \"B\"(without quotes) ")
RINP = input("Input Room. Eg: \"116\"(without quotes) ")
print("[Input : done]")
print("[Opening gecko driver]")
browser = webdriver.Firefox();
url = "https://www.iitk.ac.in/ccnew/IP_Details/Hostel_IP_Address_Details.html";
browser.get(url) 

Hall = Select(browser.find_element_by_name("firstlevel"))

Hall.select_by_visible_text(HINP)





Wing = browser.find_element_by_name("secondlevel")
Wing.send_keys(WINP)

Room = browser.find_element_by_name("thirdlevel")
Room.send_keys(RINP)

submitButton = browser.find_element_by_tag_name("input")
submitButton.click()

   
alert = browser.switch_to_alert()
#print("[Writing Output]")
msg=alert.text
#print (msg)
browser.quit()
print("[trimming and cutting output]")
print("[Finding IP]")
tofind1 = ":"
for_ip1 = msg.find(tofind1)
for_ip1 = for_ip1+1

tofind2 = "Other Network Parameters :"
for_ip2 = msg.find(tofind2)


ip_final = msg[for_ip1:for_ip2]
ip_final = ''.join(ip_final.split())
print(ip_final)
print("[Finding Subnet Mask]")

tofind1 = "Subnet Mask :"
for_mask1 = msg.find(tofind1) + 13


tofind2 = "Gateway :"
for_mask2 = msg.find(tofind2)

mask_final = msg[for_mask1:for_mask2]
mask_final = ''.join(mask_final.split())
print(mask_final)

print("[Finding Gateway]")
tofind1 = "Gateway : "
for_gateway1 = msg.find(tofind1) + 10
tofind2 = "Domain"
for_gateway2 = msg.find(tofind2)
gateway_final = msg[for_gateway1:for_gateway2]
gateway_final = ''.join(gateway_final.split())
print(gateway_final)

#print("[Finding Domain]")
tofind1 = "Domain :"
for_domain1 = msg.find(tofind1)
tofind2 = "DNS"
for_domain2 = msg.find(tofind2)
domain_final = msg[for_domain1:for_domain2]
domain_final= ''.join(domain_final.split())
#print(domain_final)

print("[Finding DNS 1]")
tofind1 = "DNS :"
for_dns1 = msg.find(tofind1) + 5
tofind2 = ","
for_dns2 = msg.find(tofind2)
dns1 = msg[for_dns1:for_dns2]
dns1 = ''.join(dns1.split())
print(dns1)

print("[Finding DNS 2]")
tofind1 = ","
for_dns21 = msg.find(tofind1)+1
tofind2 = "DNS Search"
for_dns22 = msg.find(tofind2)
dns2 = msg[for_dns21:for_dns22]
dns2 = ''.join(dns2.split())
print(dns2)

print("[flushing the output to temp.txt]")

f = open('temp.txt','w')
f.write(ip_final+" "+mask_final+" "+gateway_final)
f.close()

print("[flushing the output to DNS1.txt]")
f = open('DNS1.txt','w')
f.write(dns1)
f.close()

print("[flushing the output to DNS2.txt]")
f = open('DNS2.txt','w')
f.write(dns2)
f.close()

for fn in glob.glob("netset.bat"):
    os.startfile(fn)



