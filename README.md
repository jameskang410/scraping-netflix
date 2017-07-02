# Scraping Netflix - The Unofficial Way!
A Python class that scrapes information about Netflix movies that are available for streaming. Used by [www.tomatoflix.com][1]

# Warning: Netflix's APIs have changed and this package has not yet been updated to follow those changes.

# Why? 
This project started because I wanted to create [Tomatoflix][1], an interactive website that helps lazy people like me find random Netflix movies to watch.
I was surprised to find out that Netflix privatized their API. I took matters into my own hands and decided to forge a Netflix API of my own.

# Requirements
* Python 3
* Modules: 
    * BeautifulSoup
    * Requests
    * Fuzzywuzzy (Not very impressed with this one... Open to fuzzy matching alternatives. But it'll do for now.)

# Installation
Git clone this to your local computer and it should be good to go.
Currently working on making this installable via Pip.

# Instructions
```python
from netflix import *

# Insert netflix ID as a raw string
# To find Netflix ID:
# Sign into Netflix > Chrome Developer Tools > Resources > Cookies > www.netflix.com > NetflixId
netflix_id = r'INSERT NETFLIX ID HERE'

movie = Netflix(netflix_id)

# Initialization only has to be done once.
# This method creates jsons for all of the major genres that will be used to pull data from
movie.initialize()

"""
>Genres were successfully downloaded as JSON files
"""

# search() looks to see if the movie is available on Netflix streaming.
# other methods are chained to search() and returns specific information about the movie.
movie.search('Jerry Maguire').duration()
movie.search('Jerry Maguire').netflix_rating()

"""
>Movie was found
>2hr 18m
>3.6 stars
"""
```
Check out the example.py file. E-mail any specific questions to <jameskang410@gmail.com>

# All Available Functions
<table class="tg">
  <tr>
    <th class="tg-s6z2">__Functions__</th>
    <th class="tg-s6z2">__Return Data Type__</th>
    <th class="tg-s6z2">__Description__</th>
  </tr>
  <tr>
    <td class="tg-s6z2">initialize(_netflix\_id\_as\_string_)</td>
    <td class="tg-s6z2">None</td>
    <td class="tg-s6z2">Creates a JSON file for each movie, organized by genre. This method has to be run __only once__ and __should not be run after the JSON files have been pulled successfully__. This will minimize your chances of getting "caught" by Netflix (as if they don't know what we're up to...).</td>
  </tr>
  <tr>
    <td class="tg-s6z2">all\_titles()</td>
    <td class="tg-s6z2">List</td>
    <td class="tg-s6z2">Returns a list of every title that's available for streaming on Netflix. Loop through this list to get information about every movie.</td>
  </tr>
  <tr>
    <td class="tg-s6z2">search(_movie\_string_)</td>
    <td class="tg-s6z2">None</td>
    <td class="tg-s6z2">Checks if the string is a movie that is currently available on Netflix. Will return one of the following messages: ```Movie was found``` or ```Movie could not be found. Did you mean any of the following movies?```. If movie is not found, a list of movies that paritially matched the search string will be printed to the console. __In order to find specific information about a movie, the algorithm must find a movie match.__</td>
  </tr>
  <tr>
    <td class="tg-s6z2">movie\_number()</td>
    <td class="tg-s6z2">Int</td>
    <td class="tg-s6z2">Returns the Netflix movie ID number</td>
  </tr>
  <tr>
    <td class="tg-s6z2">genres()</td>
    <td class="tg-s6z2">List</td>
    <td class="tg-s6z2">Returns a list of genres the movie belongs to on Netflix</td>
  </tr>
  <tr>
    <td class="tg-s6z2">title()</td>
    <td class="tg-s6z2">String</td>
    <td class="tg-s6z2">Returns the title of the movie</td>
  </tr>
  <tr>
    <td class="tg-s6z2">tv\_show()</td>
    <td class="tg-s6z2">String</td>
    <td class="tg-s6z2">Returns a _"Y"_ if the movie is considered a TV show. Returns a _"N"_ if it is only a movie.</td>
  </tr>
  <tr>
    <td class="tg-s6z2">synopsis()</td>
    <td class="tg-s6z2">String</td>
    <td class="tg-s6z2">Returns the synopsis for the movie.</td>
  </tr>
  <tr>
    <td class="tg-s6z2">year()</td>
    <td class="tg-s6z2">Int</td>
    <td class="tg-s6z2">Returns the year the movie was made. NOTE: This year does not always match the year listed on other movie websites like Rotten Tomatoes.</td>
  </tr>
  <tr>
    <td class="tg-s6z2">netflix\_rating()</td>
    <td class="tg-s6z2">String</td>
    <td class="tg-s6z2">Returns the average Netflix rating for the movie.</td>
  </tr>
  <tr>
    <td class="tg-s6z2">cert\_rating()</td>
    <td class="tg-s6z2">String</td>
    <td class="tg-s6z2">Returns the maturity rating for the movie.</td>
  </tr>
  <tr>
    <td class="tg-s6z2">actors\_list()</td>
    <td class="tg-s6z2">List</td>
    <td class="tg-s6z2">Returns a list of the prominent actors in the movie.</td>
  </tr>
  <tr>
    <td class="tg-s6z2">actors\_string()</td>
    <td class="tg-s6z2">String</td>
    <td class="tg-s6z2">Returns a string of the prominent actors in the movie.</td>
  </tr>
  <tr>
    <td class="tg-s6z2">url()</td>
    <td class="tg-s6z2">String</td>
    <td class="tg-s6z2">Returns the non Netflix member friendly URL for the movie.</td>
  </tr>
  <tr>
    <td class="tg-s6z2">duration()</td>
    <td class="tg-s6z2">String</td>
    <td class="tg-s6z2">Returns the duration (hours and minutes or number of seasons) of the movie or TV show.</td>
  </tr>
  <tr>
    <td class="tg-s6z2">box\_art()</td>
    <td class="tg-s6z2">String</td>
    <td class="tg-s6z2">Returns the URL for the small box art of the movie.</td>
  </tr>
  <tr>
    <td class="tg-s6z2">large\_box\_art()</td>
    <td class="tg-s6z2">String</td>
    <td class="tg-s6z2">Returns the URL for the large box art of the movie. NOTE: Because of the different layout of Netflix movie pages, this method does not always work.</td>
  </tr>
[1]: http://www.tomatoflix.com
