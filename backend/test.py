from pprint import pprint
import requests
import folium

m = folium.Map(location=[42.3604, -71.0589], zoom_start=12)

tooltip =  'click here'
folium.Marker([42.36300, -71.0995500], popup='<strong>Location One </strong>', tooltip = tooltip).add_to(m)
m.save('map.html')

# map_search = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query=electric+car+charging+stations+in+delhi&key=AIzaSyCoOv22Ipjh2mNjjpASLlhE47jcMNfWG-Q')

#     # return jsonify({'result': [dict(result) for result in results]})
# result = map_search.json()
# result_length = len(result)
# all_results = []
# for i in range(result_length):
#     lat = result['results'][i]['geometry']['location']['lat']
#     longi = result['results'][i]['geometry']['location']['lng']
#     loc1 = [lat, longi]
#     all_results.append(loc1)
map_search = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json?query=NDMC+delta+EV+chargers+in+delhi&key=AIzaSyCoOv22Ipjh2mNjjpASLlhE47jcMNfWG-Q")
result = map_search.json()
result_length = len(result)
# pprint (result)
all_results = []
for i in range(result_length):
    lat = result['results'][i]['geometry']['location']['lat']
    longi = result['results'][i]['geometry']['location']['lng']
    loc1 = [lat, longi]
    all_results.append(loc1)


pprint(all_results)

