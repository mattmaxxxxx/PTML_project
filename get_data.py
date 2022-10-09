import wget
from zipfile import ZipFile
import pandas as pd
import os

def get_data():
    url = 'https://files.grouplens.org/datasets/movielens/ml-25m.zip'

    if not os.path.exists(os.path.abspath(os.getcwd()) + '\ml-25m.zip'):
        print('Downloading from %s, this may take a while...' % url)
        wget.download(url)

    # pass in the specific file name 
    # to the open method
    with ZipFile("ml-25m.zip") as myzip:
        movies_data = myzip.open("ml-25m/movies.csv")
        links_data = myzip.open("ml-25m/links.csv")
        ratings_data = myzip.open("ml-25m/ratings.csv")
        tags_data = myzip.open("ml-25m/tags.csv")
        genomesScores_data = myzip.open("ml-25m/genome-scores.csv")
        genomesTags_data = myzip.open("ml-25m/genome-tags.csv")
    

    # Now, we can read in the data
    movies_df = pd.read_csv(movies_data)
    links_df = pd.read_csv(links_data)
    ratings_df = pd.read_csv(ratings_data)
    tags_df = pd.read_csv(tags_data)
    genomesScores_df = pd.read_csv(genomesScores_data)
    genomesTags_df = pd.read_csv(genomesTags_data)

    return movies_df, links_df, ratings_df, tags_df, genomesScores_df, genomesTags_df