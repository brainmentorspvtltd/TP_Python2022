import urllib.request as url
import json

path = "https://data.covid19india.org/states_daily.json"
response = url.urlopen(path)
data = json.load(response)

states = data['states_daily']

confirmed_cases = []
recovered_cases = []
deceased_cases = []

for i in range(len(states)):
    if states[i]['status'] == 'Confirmed':
        confirmed_cases.append(states[i])
    elif states[i]['status'] == 'Recovered':
        recovered_cases.append(states[i])
    else:
        deceased_cases.append(states[i])

conf_sum = 0
rec_sum = 0
dec_sum = 0
for i in range(len(confirmed_cases)):
    conf_sum += int(confirmed_cases[i]['dl'])
    rec_sum += int(recovered_cases[i]['dl'])
    dec_sum += int(deceased_cases[i]['dl'])

print("Total Confirmed Cases in Delhi till 16 Aug 2021 :",conf_sum)
print("Total Recovered Cases in Delhi till 16 Aug 2021 :",rec_sum)
print("Total Deceased Cases in Delhi till 16 Aug 2021 :",dec_sum)








