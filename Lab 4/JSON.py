import json

print("Interface Status\n================================================================================\nDN                                  x.                Description           Speed    MTU  \n-------------------------------------------------- --------------------  ------  ------")

with open('sample-data.json', 'r') as file:
    datas = json.load(file)
    for data in datas['imdata']:
        print(data['l1PhysIf']['attributes']['dn'], "                              ", data['l1PhysIf']['attributes']['fecMode'], "   ", data['l1PhysIf']['attributes']['mtu'])


