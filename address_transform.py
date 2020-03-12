from google_key import GOOGLE_KEY as key
import googlemaps
import pandas

# Google map api
GOOGLE_KEY = key
gmaps = googlemaps.Client(key=GOOGLE_KEY)

# 口罩資料 # Geocoding API 每1000次 $5美元, 注意每月免費額度
data = pandas.read_csv('maskdata.csv').loc[0:1]
loc_data = []
for address in data['醫事機構地址']:
    # 回傳該地址資訊(json)
    result = gmaps.geocode(address)[0]
    # 經緯度
    lat = result['geometry']['location']['lat']
    lng = result['geometry']['location']['lng']
    loc_data.append([lat , lng])
    #print([lat, lng])
    
# 儲存轉換結果
pos_list = pandas.DataFrame({'醫事機構代碼': data['醫事機構代碼'], '經緯度': loc_data})
pos_list.to_csv('pos_list.csv', index=False, header=False, mode="a")