import requests
import xmltodict
import json
# from xml.etree import ElementTree
# import ctypes

response = requests.get("http://restapi.adequateshop.com/api/Traveler/")
repurpose = xmltodict.parse(response.text)
# tree = ElementTree.fromstring(response.content)
# tree = ElementTree.iterparse(response.raw)
# d= id(tree)
# c = ctypes.cast(d,ctypes.py_object).value
# print(d)
# print(tree, c)
# print(response.content)
# print(repurpose.get('TravelerinformationResponse',0).get('travelers',0).get('Travelerinformation',0))
travelers_output = repurpose.get('TravelerinformationResponse',0).get('travelers',0).get('Travelerinformation',0)

final_traveler_output=[]
# i realized the key names coming in through the APi were mispelled and also not to my liking.
# I changed things up by creating a new list full of dictionaries with 'keys' updated.(field_list)
for i in range(len(travelers_output)):
    field_list = ['id','name','email','address','creation_date']
    final_traveler_output.append((dict(zip(field_list, travelers_output[i].values()))))
# print((travelers_output))
# print(final_traveler_output)
with open("output.text",'w') as outputfile:
    outputfile.write(json.dumps(final_traveler_output)) 
# print("This is the status code: " + str(response.status_code))