import json
  
# Opening JSON file
f = open('data.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list

print("\n\n")
print(data['batters']['batter'][0])
print("\n\n")
  
# Closing file
f.close()