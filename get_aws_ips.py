
import requests

ip_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['prefixes']
#amazon_ips = [item['ip_prefix'] for item in ip_ranges if item["service"] == "AMAZON"]
amazon_ips = [item['ip_prefix'] for item in ip_ranges]
#ec2_ips = [item['ip_prefix'] for item in ip_ranges if item["service"] == "EC2"]

#amazon_ips_less_ec2=[]
amazon_ips_all=[]
     
for ip in amazon_ips:
#    if ip not in ec2_ips:
#        amazon_ips_less_ec2.append(ip)
        amazon_ips_all.append(ip)


#for ip in amazon_ips_less_ec2: print(str(ip))

with open('amazon_ips.txt', 'w') as file:
    for ip in amazon_ips_all:
        file.write(str(ip) + '\n')
