import json

def deserialize():  
    
    f = open('data.json')

    data = json.load(f)

    ret = data['batters']['batter'][0]
    
    f.close()

    return ret

def serialize():
    pass

data = deserialize()
print("\n\n")
print(data)
print("\n\n")