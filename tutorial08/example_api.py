# Now that we've covered what an API is and how to work with them,
# it's time we actually look at one of our own. Surprise! We've actually 
# been using one to keep track of attendance. Let's take a deeper dive into how
# to execute an API request and print out it's response. 

# To get started, we will need the requests and JSON library. We will import 
# them into this file below. 
import json
import requests

# Next, we need to define a URL and some data fields
# For full clarity, we need a name, a TutorialID (TID) and a hash code 
# to properly call this API. 
# You can usually find this information in the API documentation for most API's

name = "Rashed Rifat"
URL = "https://9dontxvnf1.execute-api.us-east-2.amazonaws.com/alpha/record"
TID = "08"
hash_code = "H2aja86Knp"

# Okay, now that we have that set up, we need to create the body of our
# request. Note that this API does not require a header, which other APIs might. 
# Note that most API documentation will have examples of calling their API
# which you can refer to find the format of the body. 
# Here, we have supplied the format for you. 
body = json.dumps({"full_name" : name, "TID" : TID, "hash" : hash_code})

# We can also save our parameters in a parameters dictonary and pass it into
# the params field for an API request. Let's take a look at this now.
parameters = {"full_name" : name, "TID" : TID, "hash" : hash_code}

# Finally, the time has come to execute the request! We can do this 
# through the requests library and store the response in a variable. 
# Can you identify the type of request we are sending?
API_response = requests.post(URL, data=body) 
API_response = requests.post(URL, params=parameters)

# Finally, we can take a look at the response of the API by looking at the JSON
# function of the variable.
print(API_response.json())

# If we just want to check the status of the API_response, we can use thf following. 
print(API_response.ok)

# Okay, that should be a good introduction in an API call. We covered a really simple example.
# Since API's in the wild are highly variable, its up to you to really check out all
# the different API's there are. We really can't quite teach you all the formats there are. 
# The underlying concepts are still the same, so you should be well equipped to deal with 
# everything. Good luck!
# Example prompts are located in the README for this file. 
