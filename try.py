import re

text3 = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla '''

twitter_extracted = re.findall(r'https://twitter\.com/([A-Za-z0-9_]+)', text3)
print("Number 3\n")
print(twitter_extracted)