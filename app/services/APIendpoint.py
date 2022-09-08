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
carebear_output = repurpose
with open("output.text",'w') as outputfile:
    outputfile.write(json.dumps(repurpose)) 
# print(repurpose)
print("This is the status code: " + str(response.status_code))