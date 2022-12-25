# -*- coding: utf-8 -*-
"""web_scraping_imdb.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14sButtXZjREH-yO8Y404o5_yimutmTZB
"""

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# Downloading a list of imdb top 1000 movie's data
url = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'

response = requests.get(url)

# Parse of contet html
context = BeautifulSoup(response.text, "html.parser")

# context.find('title')

def get_topics_page():
    # TODO - add comments
    topic_url = 'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=000&ref_=adv_next'
    response=requests.get(topic_url)
    # check successfull response
    if response.status_code != 200:
        raise Exception(f'Failed to load page {topic_url}')
    # Parse using BeautifulSoup
    doc = BeautifulSoup(response.text, 'html.parser')
    return doc

doc=get_topics_page()

def get_movie_titles(doc):
    
    selection_class="lister-item-header"
    movie_title_tags=doc.find_all('h3',{'class':selection_class})
    movie_titles=[]

    for tag in movie_title_tags:
        title = tag.find('a').text
        movie_titles.append(title)
        
        
    return movie_titles

def get_movie_years(doc):
    
    classes="lister-item-year text-muted unbold"
    movie_years_tags=doc.find_all('span',{'class':classes})
    movie_years=[]

    for tag in movie_years_tags:
        movie_years.append(tag.get_text().strip()[1:5])

    return movie_years

def get_movie_runtime(doc):
    
    classes="runtime"
    movie_runtime_tags=doc.find_all('span',{'class':classes})
    movie_runtime=[]

    for tag in movie_runtime_tags:
        movie_runtime.append(tag.get_text().strip())

    return movie_runtime

def get_movie_ratings(doc):
    
    classes="inline-block ratings-user-rating"
    movie_ratings_tags=doc.find_all('div',{'class':classes})
    movie_ratings=[]

    for tag in movie_ratings_tags:
        movie_ratings.append(tag.get_text().strip())

    return movie_ratings

def get_movie_imdb_ratings(doc):
    
    classes="inline-block ratings-imdb-rating"
    movie_imdb_ratings_tags=doc.find_all('div',{'class':classes})
    movie_imdb_ratings=[]

    for tag in movie_imdb_ratings_tags:
        movie_imdb_ratings.append(tag.get_text().strip())

    return movie_imdb_ratings

def get_movie_genres(doc):
    
    classes="genre"
    movie_genre_tags=doc.find_all('span',{'class':classes})
    movie_genre=[]

    for tag in movie_genre_tags:
        movie_genre.append(tag.get_text().strip())

    return movie_genre

def get_movie_votes(doc):

  # Revisar
    
    classes="genre"
    # movie_votes_tags=doc.find_all('span',{'class':classes})
    movie_votes_tags=doc.find('span', attrs = {'name':'nv'})['data-value']
    movie_votes=[]

    for tag in movie_votes_tags:
        movie_votes.append(movie_votes_tags)

    return movie_votes

get_movie_votes(doc)

def get_movie_genres(doc):
    
    classes="genre"
    movie_genre_tags=doc.find_all('span',{'class':classes})
    movie_genre=[]

    for tag in movie_genre_tags:
        movie_genre.append(tag.get_text().strip())

    return movie_genre

# 'gross':[],

# 'director':[],

# 'stars':[]

def full_pages_imdb_movies():
# Create a dictionary to store data
    movies_dict={
        'titles':[],
        'years':[],
        'runtimes':[],
        # 'ratings':[],
        'imdb_ratings':[],
        'genres':[]
        # 'votes':[]
        # 'gross':[],
        # 'director':[],
        # 'stars':[]
    }
  # We have to scrap more than one page so we want urls of all pages with the help of loop we can get all urls
    for i in range(1,2000,100):
       
        try:
            url = 'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start='+str(i)+'&ref_=adv_next'
            response = requests.get(url)
        except:
            break
        
        if response.status_code != 200:
            break
           
    # Parse of html using BeautifulSoup lib
        doc = BeautifulSoup(response.text, 'html.parser')
        titles = get_movie_titles(doc)
        years = get_movie_years(doc)
        runtimes = get_movie_runtime(doc)
        # ratings = get_movie_ratings(doc)
        imdb_ratings = get_movie_imdb_ratings(doc)
        genres = get_movie_genres(doc)
        # votes = get_movie_votes(doc)
        # gross = get_movie_gross(doc)
        # director = get_movie_director(doc)
        # stars = get_movie_stars(doc)
        
    # Adding every movie data to dictionary
        for i in range(len(titles)):
            movies_dict['titles'].append(titles[i])
            movies_dict['years'].append(years[i])
            movies_dict['runtimes'].append(runtimes[i])
            # movies_dict['ratings'].append(ratings[i])
            movies_dict['imdb_ratings'].append(imdb_ratings[i])
            movies_dict['genres'].append(genres[i])
            # movies_dict['votes'].append(votes[i])
            # movies_dict['gross'].append(gross[i])
            # movies_dict['director'].append(director[i])
            # movies_dict['stars'].append(stars[i])
            
    # Convert dictionary to a Pandas DataFrame
    return pd.DataFrame(movies_dict)

imdb_movies = full_pages_imdb_movies()

df = pd.DataFrame(imdb_movies)

df.head()

df

df.to_csv('imdb_movies.csv',index=None)

