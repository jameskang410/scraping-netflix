from netflix import *

# Insert netflix ID as a raw string
# To find Netflix ID: 
# Chrome Developer Tools > Resources > Cookies > www.netflix.com > NetflixId
netflix_id = r'INSERT NETFLIX ID HERE'

movie = Netflix(netflix_id)

# This only has to be done once.
# This method creates jsons for all of the major genres that will be used to pull data from
movie.initialize()

"""
>>Genres were successfully downloaded as JSON files
"""

# search() looks to see if the movie is available on Netflix streaming.
# duration() gets the length of the movie or TV show 
print(movie.search('Jerry Maguire').duration())

"""
>>Movie was found
>>2hr 18m
"""