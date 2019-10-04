from boltiot import Bolt
api_key = "b1bba2fd-6b2e-42e6-98e0-ddfb295736f8"
device_id  = "BOLT5647738"
mybolt = Bolt(api_key, device_id)
response = mybolt.isOnline()
print(response)