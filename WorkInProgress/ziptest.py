from uszipcode import SearchEngine

search = SearchEngine(simple_zipcode=True)
ziplist = search.by_state("CA", returns = 2000)
# print(f"Zipcode: {ziplist[0].zipcode}")
# print(f"Median Home Value: {ziplist[0].median_home_value}")
# print(f"Median Income: {ziplist[0].median_household_income}")

# Convert to dict, then dataframe
print(len(ziplist))