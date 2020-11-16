from apis import yelp
help(yelp)
data = yelp.get_businesses()
print(data)
html_businesses = yelp.get_formatted_business_table(data[0], reviews=[])