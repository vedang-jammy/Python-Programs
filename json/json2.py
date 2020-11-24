# another json example
import json

input = """[
{
    "id" : "03",
    "x" : "2",
    "name" : "john"
},
{
    "id" : "09",
    "x" : "5",
    "name" : "jeany"
}
]"""
info = json.loads(input)
print("user Count:", len(info))
for item in info:
    print("name:", item["name"])
    print("id:", item["id"])
    print("attribute:", item["x"])
