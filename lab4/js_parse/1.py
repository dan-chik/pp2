import json

with open('sample-data.json') as file:
    js_data = json.load(file)

    print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")

    imdata = js_data["imdata"]
    
    for item in imdata:
        nest = item["l1PhysIf"]
        attribs = nest["attributes"]
        dn = attribs["dn"]
        spd = attribs["speed"]
        mtu = attribs["mtu"]
        output = ""
        
        output += dn + "                              " + spd + "  " + mtu
    
        print(output)