from bs4 import BeautifulSoup
import requests
import time
import json
import math
from fuzzywuzzy import fuzz
import codecs

'''
Anime: 7424

Children and Family: 783
Kids' TV: 27346

Comedies: 6548
Classic Comedies: 31694
Cult Comedies: 9434
TV Comedies: 10375

B-Horror: 7627
Cult Horror: 10944
Horror: 8711
TV Horror: 83059

Cult Sci-Fi: 4734
Classic Sci-Fi: 47147
Sci-Fi and Fantasy: 1492
TV Sci-Fi and Fantasy: 1372

Drama: 5763
Classic Drama: 29809
TV Dramas: 11714

Classic Thriller: 46588
Thrillers: 8933
TV Mysteries: 4366

Documentaries: 6839
Food and Travel TV Shows: 72436
Reality TV: 9833
Science and Nature TV Shows: 52780
TV Documentaries: 10105

Faith and Spirituality: 26835

Foreign: 7462
Korean TV Shows: 67879

Gay and Lesbian: 5977

Romance: 8883

Action and Adventure: 1365
TV Action: 10673
'''

class Netflix:

    genre_dictionary = {
                      'TV Shows' : 83,
                      'Action & Adventure' : 1365,
                      'Anime' : 7424,
                      'Children & Family' : 783,
                      'Classics' : 31574,
                      'Comedies' : 6548,
                      'Cult Movies' : 7627,
                      'Documentaries' : 6839,
                      'Dramas' : 5763,
                      'Faith & Spirituality' : 26835,
                      'Foreign' : 7462,
                      'Gay & Lesbian' : 5977,
                      'Horror' : 8711,
                      'Independent' : 7077,
                      'Music' : 1701,
                      'Musicals' : 13335,
                      'Romance' : 8883,
                      'Sci-Fi & Fantasy' : 1492,
                      'Sports Movies' : 4370,
                      'Thrillers' : 8933
                      }

    def __init__(self, netflix_id):

        self.cookies = {'NetflixId' : netflix_id,
            'profilesNewSession' : '0',
            'profilesNewUser' : '0'
            }

    #Creates all of the genre JSONs
    def initialize(self):

        try:
            genre_dictionary = Netflix.genre_dictionary

            for genre in genre_dictionary:

                txt_file = '%s.json' % genre

                url = 'http://www.netflix.com/api/shakti/90409bc7/wigenre?genreId=%s&full=false&from=0&to=10000' % genre_dictionary.get(genre)

                r = requests.get(url, cookies=self.cookies)

                netflix_json = json.loads(r.text)

                with codecs.open(txt_file, 'w', encoding='utf-8') as json_page:

                    json_page.write(json.dumps(netflix_json))

            print('Genres were successfully downloaded as JSON files')

        except:

            print('Error: Was not able to download JSON data. AJAX URLs may have changed or Netflix ID may be incorrect.')


    def search(self, search_title):
        
        self.search_title = search_title

        genre_list = []

        possible_movies = ''

        possible_list = []

        #flipping through JSON files
        for genre in Netflix.genre_dictionary:

            txt_file = '%s.json' % genre

            with codecs.open(txt_file, 'r', encoding='utf-8') as genre_json:

                netflix_json = json.loads(genre_json.read())

            for num in range(0,len(netflix_json["catalogItems"])):

                title = netflix_json["catalogItems"][num]["title"]

                #cleaning unicode
                title = title.encode('ascii','ignore')
                title = title.decode('utf-8')

                title_string = str(title).replace('\xa0','').replace('\u200b','')


                if fuzz.ratio(title_string.lower().strip(),search_title.lower().strip()) >= 90:

                    self.title_id = netflix_json["catalogItems"][num]["titleId"]

                    box_art = netflix_json["catalogItems"][num]["boxart"]

                    genre_list.append(genre)

                elif fuzz.ratio(title_string.lower().strip(), search_title.lower().strip()) >= 50:

                    if title_string not in possible_list:
                        
                        possible_movies += title_string + '\n'
                        possible_list.append(title_string)

        try:       
            self.url = "http://www.netflix.com/api/shakti/dedd2957/bob?titleid=%s&trackid=13462986&authURL=" % self.title_id

            r = requests.get(self.url, cookies=self.cookies)

            self.netflix_json = json.loads(r.text)

            self.genre_list = genre_list

            self.box_arts = box_art

            self.indiv_url = 'http://www.netflix.com/WiMovie/%s?trkid=' % self.title_id

            print('Movie was found')

            return self

        except:

            print('Movie could not be found.\nDid you mean any of the following movies?\n' + possible_movies)

            return

    def movie_number(self):

        return self.title_id

    def all_titles(self):
        import unicodedata
        #remove duplicates somehow

        all_movies_list = []

        for genre in Netflix.genre_dictionary:

            txt_file = '%s.json' % genre

            with open(txt_file, 'r',errors='backslashreplace') as genre_json: 

                netflix_json = json.loads(genre_json.read())

            for num in range(0,len(netflix_json["catalogItems"])):

                title = netflix_json["catalogItems"][num]["title"]

                #cleaning unicode
                # title = title.encode('ascii','replace')
                # title = title.decode('utf-8')

                title_string = str(title).replace('\xa0','').replace('\u200b','')

                all_movies_list.append(title_string)

        def remove_duplicates(values):
            seen = []
            output = []
            for value in values:
                if value not in seen:
                    output.append(value)
                    seen.append(value)
            return output

        return remove_duplicates(all_movies_list)

    def box_art(self):

        return self.box_arts

    def genres(self):

        return self.genre_list

    def title(self):

        title = self.netflix_json["title"]

        title = title.encode('ascii','ignore')
        title = title.decode('utf-8')

        if "&amp;" in str(self.netflix_json["title"]):
            title = str(self.netflix_json["title"]).replace('&amp;','&')

        return str(title)

    def tv_show(self):

        if self.netflix_json["isShow"]:
            tv_show_string = 'Y'

        else:
            tv_show_string = 'N'

        self.tv_show_string = tv_show_string

        return self.tv_show_string

    def synopsis(self):

        return self.netflix_json["synopsis"]

    def year(self):

        return self.netflix_json["year"]

    def netflix_rating(self):

        return str(self.netflix_json["averageRating"]) + " stars"

    def cert_rating(self):

        return self.netflix_json["maturityLabel"]

    def actors_string(self):

        actor_list = []
        
        for actor in self.netflix_json["actors"]:
            actor_list.append(actor["name"])

        actor_string = ''

        actor_string = ', '.join(actor_list)        
        
        return actor_string

    def actors_list(self):

        actor_list = []
        
        for actor in self.netflix_json["actors"]:
            actor_list.append(actor["name"])       

        return actor_list

    def large_box_art(self):

        r = requests.get(self.indiv_url)

        indiv_soup = BeautifulSoup(r.text)

        try: 
            for img in indiv_soup.findAll('img', attrs={'itemprop' : 'thumbnailUrl'}):

                link = img.get('src')

                return link

        except:
            for img in indiv_soup.findAll('img', attrs={'class' : 'boxShotImg '}):

                #usually it's the first one
                link = img.get('src')
                pass

            return link
        
    def url(self):

        return self.indiv_url

    def duration(self):

        #if TV show
        try: 
            if self.netflix_json["numSeasons"] == 1:
                movie_duration = str(self.netflix_json["numSeasons"]) + " Season"

            else:
                movie_duration = str(self.netflix_json["numSeasons"]) + " Seasons"
            
            return movie_duration

        #if movie
        except:
            duration_int = int(self.netflix_json["runtime"])

            hour, minutes = divmod(duration_int, 60)

            if minutes != 0:
                minutes -= 1

            movie_duration = '%dhr %dm' % (hour, minutes)

            return movie_duration