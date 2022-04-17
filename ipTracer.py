import requests
import sys


def ip_tracer(ip_address = ""):
    loc = requests.get("https://ipapi.co/"+ ip_address +"/json/")
    data = loc.json()
    for x in data:
        print(str(x)  + " : " + str(data[x]))

    print("Google map link : https://www.google.com/maps/place/"+ str(data['latitude']) + "+" + str(data['longitude']) )
    print("\n\n")
if len(sys.argv) == 1:
    print('''  
     __| |___________________________| |__ 
    (__| |___________________________| |__)
       | |  IP TRACER SCRIPT:  MODD  | |   
     __| |___________________________| |__ 
    (__|_|___________________________|_|__)''')

    
    print(''' 
    1. Trace IP
    2. Trace my IP


    ''')


    while True:
        option = input("enter option: ")
        if option == "1":
            ip_add= input("Enter IP address: ")
            ip_tracer(ip_add)
            break
        elif option == "2":
            ip_tracer()
            break
        else:
            print("Enter valid option")

else:
    print('''  
     __| |___________________________| |__ 
    (__| |___________________________| |__)
       | |  IP TRACER SCRIPT:  MODD  | |   
     __| |___________________________| |__ 
    (__|_|___________________________|_|__)
    
    
    ''')

    for x in sys.argv:
        if x == sys.argv[0]:
            pass
        else:
            ip_tracer(x)