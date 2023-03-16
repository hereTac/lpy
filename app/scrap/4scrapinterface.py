import requests
import json

url_heroDataWithLeagueID = 'https://prod.comp.smoba.qq.com/leaguesite/league/hero/settle_list/open?league_id=20230001'
r = requests.get(url_heroDataWithLeagueID)
print('-----')
r_j = r.json()
result = r_j["data"]
print(result)
# no need ascii to conversion
result_j = json.dumps(result, ensure_ascii=False, indent=4)
with open('../../snapshot/t.json', 'w') as f:
    # write json str
    f.write(result_j)
    f.close()
