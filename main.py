import json

def deserialize():  
    
    f = open('data.json')

    data = json.load(f)

    print("\n\n")
    print(data['batters']['batter'][0])
    print("\n\n")
    
    f.close()

def serialize():
    pass

deserialize()