# Here is the link to thhe documentation for this project!
# https://pypi.org/project/Wikipedia-API/

# Note that this api requires the use of the wikipedia-api library. 
# How would we install this API into our device? Does anyone remeber? 

import wikipediaapi

wiki_object = wikipediaapi.Wikipedia('en')
page_py = wiki_object.page('Python_(programming_language)')

print("Page - Exists: %s" % page_py.exists())
# Page - Exists: True

page_missing = wiki_page_py = wiki_object.page('NonExistingPageWithStrangeName')
print("Page - Exists: %s" %     page_missing.exists())
# Page - Exists: False

print("Page - Title: %s" % page_py.title)
# Page - Title: Python (programming language)

print("Page - Summary: %s" % page_py.summary[0:60])
# Page - Summary: Python is a widely used high-level programming language for