import os
import pandas as pd
import numpy as np
import re
from tqdm.notebook import tqdm
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA

'''
    METHODS FOR RECOMMENDATION ASPECT OF THE SYSTEM
'''

def recommend(title):
    ddump = pd.read_csv("data/ddump_soup.csv")

    # Format for textual analysis
    text_data = ddump[[
        'Series_Title','Genre','Overview','Director',
        'Star1', 'Star2', 'Star3', 'Star4','Soup'
    ]].astype(str)
    text_data = np.array(text_data)
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(text_data)

    # Semantic analysis output into numpy array
    text_data = np.array(embeddings)
    pca = PCA(n_components=5)
    pca.fit(text_data)
    pca_data = pd.DataFrame(pca.transform(text_data))

    # Cosine Similarity Measure
    cos_sim_data = pd.DataFrame(cosine_similarity(text_data))

    # Figire out [index] -> relevant title?    
    data = ddump.dropna()
    index = data.loc[ddump['Series_Title']==title].index

    # Select column of values -> sort by value -> record indexes of [1:6]
    index_recomm = cos_sim_data[index]

    index_recomm = index_recomm.sort_values(by=index_recomm.columns[0], ascending=False).index.tolist()[1:6]

    movies_recomm = []
    for value in index_recomm:
        try:
            movies_recomm.append(data['Series_Title'].loc[value])
        except(KeyError):
            continue

    result = {'Movies':movies_recomm,'Index':index_recomm}
    return movies_recomm