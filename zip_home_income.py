from uszipcode import SearchEngine

search = SearchEngine(simple_zipcode=True)
ziplist = search.by_city("Los Angeles", returns = 200)

zipdata = []
ziplen = len(ziplist)
i = 0

while i < ziplen:
    zip_code = ziplist[i].zipcode
    home_val = ziplist[i].median_home_value
    income = ziplist[i].median_household_income
    zipdata.append({"Zip Code":zip_code, "Median Home Value":home_val, "Median Household Income":income})
    i = i + 1
    
zipdata_df = pd.DataFrame(zipdata)
print(len(zipdata_df))
zipdata_df.to_csv("LA_zip_home_income.csv")