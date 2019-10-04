from boltiot import Bolt
api_key = "b1bba2fd-6b2e-42e6-98e0-ddfb295736f8"
device_id  = "BOLT5647738"
mybolt = Bolt(api_key, device_id)
inp =input()
if(inp=='ON' or inp=='on'):
    response = mybolt.digitalWrite('0','HIGH')
elif(inp=='OFF' or inp=='off'):
    response = mybolt.digitalWrite('0','LOW')
else:
    print("Not a valid input")
    exit()    
print (response)