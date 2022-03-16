import pandas as pd
import numpy as np
import pickle
import os

dirname = os.path.dirname(__file__)

UserRecommender_path = os.path.join(dirname, 'models', 'UserRecommender.pkl')
fCleandf_path = os.path.join(dirname, 'models', 'fCleandf.pkl')

UserRecommender = pickle.load(file = open(UserRecommender_path, 'rb'))
fCleandf = pickle.load(file = open(fCleandf_path, 'rb'))


def getRecommendations(username):
    try:
        # limit of 20 added due to memeory issue
        _Top20Recproductdf = pd.DataFrame(UserRecommender.loc[username].sort_values(ascending=False)[0:20].index)
    except KeyError:
        errorMessage = f'Hey Mate! we tried hard but couldn\'t find the user "{username}", so we couldn\'t recommend anything \n\
         for "{username}", you can try again by select any of the below username to find their recommendations.'
        print(type(errorMessage))
        return errorMessage, None
    
    _Top5Recproductdf = pd.merge(_Top20Recproductdf,fCleandf,on='id',how='inner').sort_values(['PositivePct'],ascending=False)[:5]

    productNameList = _Top5Recproductdf['name'].tolist()
    posSentimentRateList = _Top5Recproductdf['PositivePct'].tolist()

    return productNameList, posSentimentRateList
