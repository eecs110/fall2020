from apis import yelp
# help(yelp)

# Figure this out on your own for Project 2.
data = yelp.get_businesses()
print(data)
html_businesses = yelp.get_formatted_business_table(data[0], reviews=[])