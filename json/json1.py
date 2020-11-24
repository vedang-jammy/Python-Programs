# this is small example of json
import json

data = """{
"name" : "jammy",
"age" : "20",
"phone" : {
    "type" : "intl",
    "number" : "+91 355 843 2354"
},
"email":{
    "hide" : "yes"
}
}"""

info = json.loads(
    data
)  # it genetrates the dictionary like here in example 'info' is a dictionary
print("name:", info["name"])
print("email:", info["email"]["hide"])
