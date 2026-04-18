import json
data={
    "sepalLength": 5.1, "sepalWidth": 3.5, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"
}
# with open("iris1.json","w") as f:
#     json.dump(data,f)

# with open("iris1.json","w") as f:
#     json.dump(data,f,indent=1)

with open("iris.json","r") as f:
    data2=(json.load(f))
    # print(data[0])
print([f2["sepalWidth"] for f2 in data2])