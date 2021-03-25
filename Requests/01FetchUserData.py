import requests
import json

# API URL
url = "https://api.nasa.gov/planetary/apod?api_key=yCxBef8nbC9bKDFocnwWh9dwj5J0SS1wGyXRfjk6"

url2 = "https://reqres.in/api/users?page=2"

response = requests.get(url)
response2 = requests.get(url2)

print(response, response2)
# <Response [200]> <Response [200]>

# Display response content
print(response.content)
print()
print(response2.content)

# b'{"date":"2021-03-09","explanation":"Is that a fossil?\\u00a0 Looking through recent images of Mars taken by the new Perseverance rover may seem a bit like treasure hunting, with the possibility of fame coming to the first person to correctly identify a petrified bone, a rock imprinted by an ancient plant, or any clear indication that life once existed on Mars.\\u00a0 Unfortunately, even though it is possible that something as spectacular as a skeleton could be identified, most exobiologists think it much more likely that biochemical remnants of ancient single-celled microbes could be found with Perseverance\'s\\u00a0chemical analyzers.\\u00a0 A key reason is that multicellular organisms may take a greater amount of oxygen to evolve than has ever been present on Mars. That said, nobody\'s sure, so please feel free to digitally magnify any Perseverance image that interests you -- including the featured 360-degree zoomable image of the rocks and ridges surrounding Perseverance\'s landing location in Jezero Crater.  And even though NASA-affiliated scientists are themselves studying Perseverance\'s images, if you see anything really unusual, please post it to popular social media. If your sighting turns out to be particularly intriguing, scientifically, it is likely that NASA will hear about it.","media_type":"video","service_version":"v1","title":"Perseverance 360: Unusual Rocks and the Search for Life on Mars","url":"https://mars.nasa.gov/layout/embed/image/mars-panorama/?id=25674"}\n'
#
# b'{"page":2,"per_page":6,"total":12,"total_pages":2,"data":[{"id":7,"email":"michael.lawson@reqres.in","first_name":"Michael","last_name":"Lawson","avatar":"https://reqres.in/img/faces/7-image.jpg"},{"id":8,"email":"lindsay.ferguson@reqres.in","first_name":"Lindsay","last_name":"Ferguson","avatar":"https://reqres.in/img/faces/8-image.jpg"},{"id":9,"email":"tobias.funke@reqres.in","first_name":"Tobias","last_name":"Funke","avatar":"https://reqres.in/img/faces/9-image.jpg"},{"id":10,"email":"byron.fields@reqres.in","first_name":"Byron","last_name":"Fields","avatar":"https://reqres.in/img/faces/10-image.jpg"},{"id":11,"email":"george.edwards@reqres.in","first_name":"George","last_name":"Edwards","avatar":"https://reqres.in/img/faces/11-image.jpg"},{"id":12,"email":"rachel.howell@reqres.in","first_name":"Rachel","last_name":"Howell","avatar":"https://reqres.in/img/faces/12-image.jpg"}],"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}'

# Display only headers of the response.
print(response.headers)
# {'Date': 'Tue, 09 Mar 2021 16:14:20 GMT', 'Content-Type': 'application/json', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'X-RateLimit-Limit': '2000', 'X-RateLimit-Remaining': '1996', 'Access-Control-Allow-Origin': '*', 'Age': '0', 'Via': 'http/1.1 api-umbrella (ApacheTrafficServer [cMsSf ])', 'X-Cache': 'MISS', 'Strict-Transport-Security': 'max-age=31536000; preload', 'Content-Encoding': 'gzip'}

# If you want to pretify the output
# you need to import json module
pretty = json.loads(response2.text)
print(json.dumps(pretty, indent=4, sort_keys=True))

# {
#     "data": [
#         {
#             "avatar": "https://reqres.in/img/faces/7-image.jpg",
#             "email": "michael.lawson@reqres.in",
#             "first_name": "Michael",
#             "id": 7,
#             "last_name": "Lawson"
#         },
#         {
#             "avatar": "https://reqres.in/img/faces/8-image.jpg",
#             "email": "lindsay.ferguson@reqres.in",
#             "first_name": "Lindsay",
#             "id": 8,
#             "last_name": "Ferguson"
#         },
#         {
#             "avatar": "https://reqres.in/img/faces/9-image.jpg",
#             "email": "tobias.funke@reqres.in",
#             "first_name": "Tobias",
#             "id": 9,
#             "last_name": "Funke"
#         },
#         {
#             "avatar": "https://reqres.in/img/faces/10-image.jpg",
#             "email": "byron.fields@reqres.in",
#             "first_name": "Byron",
#             "id": 10,
#             "last_name": "Fields"
#         },
#         {
#             "avatar": "https://reqres.in/img/faces/11-image.jpg",
#             "email": "george.edwards@reqres.in",
#             "first_name": "George",
#             "id": 11,
#             "last_name": "Edwards"
#         },
#         {
#             "avatar": "https://reqres.in/img/faces/12-image.jpg",
#             "email": "rachel.howell@reqres.in",
#             "first_name": "Rachel",
#             "id": 12,
#             "last_name": "Howell"
#         }
#     ],
#     "page": 2,
#     "per_page": 6,
#     "support": {
#         "text": "To keep ReqRes free, contributions towards server costs are appreciated!",
#         "url": "https://reqres.in/#support-heading"
#     },
#     "total": 12,
#     "total_pages": 2
# }

