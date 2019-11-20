cars = {
  "car1" : {
    "name" : "Nissan nismo 370z",
    "color": "red",
    "year" : "2009"
  },
  "car2" : {
    "name" : "Toyota supra",
    "color": "black",
    "year" : "2020"
  },
  "car3" : {
    "name" : "Koenisegg agera",
    "color": "white and black",
    "year" : "2011"
  }
}
for tag, g in cars.items():
    if g['year'] == '2009':
        print(g['name'])
