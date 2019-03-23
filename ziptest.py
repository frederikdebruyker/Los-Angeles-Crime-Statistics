from uszipcode import SearchEngine

search = SearchEngine(simple_zipcode=True)
result = search.by_coordinates(34.0079, -118.2842, radius=5, returns=1)
print(result)