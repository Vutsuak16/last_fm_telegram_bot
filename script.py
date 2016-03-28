import pylast


API_KEY = "419e77f212e197c24dc0e935be105898"
API_SECRET = "425b55975eed76058ac220b7b4e8a054"


network = pylast.LastFMNetwork(api_key = API_KEY, api_secret =
    API_SECRET)

track = network.get_track("Money", "Pink Floyd")
print track