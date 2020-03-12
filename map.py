#%%
import folium
import pandas

# 口罩資料
data = pandas.read_csv('maskdata.csv').loc[0:29]
pos_list = pandas.read_csv('pos_list.csv')

#%%
# 建立地圖並設置初始位置
m = folium.Map((23.583234,120.5825975), tiles="Stamen Terrain",zoom_start=7)

# 口罩資訊標記建立
for i in range(0, len(pos_list)):
    # 資訊內容
    tip_str = data['醫事機構名稱'][i] + "<br>" + \
              data['醫事機構地址'][i] + "<br>" + \
              data['醫事機構電話'][i] + "<br>" + \
              "成人口罩剩餘數: " + str(data['成人口罩剩餘數'][i]) + "<br>" + \
              "兒童口罩剩餘數: " + str(data['兒童口罩剩餘數'][i]) + "<br>" + \
              "來源資料時間: " + data['來源資料時間'][i]
    folium.Marker(
        location=eval(pos_list['經緯度'][i]),
        tooltip=folium.Tooltip(text=tip_str),
        # 點擊後資訊(未來可放圖表)
        #popup=folium.Popup(html=tip_str ,max_width=200).add_child(folium.Vega(vis1, width=450, height=250)),
        icon=folium.Icon(color='green')
    ).add_to(m)
m.save("map.html")
