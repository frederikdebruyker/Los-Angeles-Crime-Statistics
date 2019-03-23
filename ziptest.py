from uszipcode import SearchEngine

search = SearchEngine(simple_zipcode=True)
result = search.by_coordinates(34.0079, -118.2842, radius=5, returns=1)
print(f"Zipcode: {result[0].zipcode}")
print(f"Median Home Value: {result[0].median_home_value}")
print(f"Median Income: {result[0].median_household_income}")