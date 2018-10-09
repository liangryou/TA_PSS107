import requests
import json

# Part I. Get Data

# url address
url = 'http://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M'

# get the website using module requests and its method :: get().
result = requests.get(url)

# convert result to pure text and use json.loads() to convert it again to json format.
# noted that json.load() needs file to be .json, yet json.loads() accept text or string as input.
data = json.loads(result.text)
print(type(data))
print(data)


# Part II. Summarizing data

# 1. 該資料集包含幾筆資料
print(len(data))

# 2. 該資料集的主要資料表有哪些「變項」
print(data[0].keys())
print(data[0])
# 3. 用上週與本週所教的「計數counting」運算，統計其中一個變數　→　統計受雇員工人數
count = {}
for i in range(len(data)):
    area = data[i]["cityName"]

    if area not in count:
        count[area] = 1
    else:
        count[area] += 1

print(count)

for name in data:
    print(name)
