from uszipcode import SearchEngine

search = SearchEngine(simple_zipcode=True)
result = search.by_coordinates(29.743257, -95.386397, radius=5, returns=1)
print(result)