import requests
import pprint
from h_text import owasp_sec_headers

def check_headers(site):
    req=requests.get(site)
    # Dictionary with OWASP main security headers
    owasp_sec_headers
    site_h_list=[]

    header=req.headers
    
    for k, v in header.items():
        site_h_list.append(k)

    #check if the there are missing headers 
    for k,v in owasp_sec_headers.items():
        if k not in site_h_list:
            print ('\n',k,' !!!IS MISSING!!!','\n')
            print (v,'\n')
            print('\n')
    

if __name__=='__main__':
    print("Check Security Response Headers")
    print("Enter the site that you want to check >> ")
    site=input()
    check_headers(site)