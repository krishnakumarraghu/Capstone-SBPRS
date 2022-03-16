import pandas as pd
import numpy as np
import pickle
import compress_pickle as cp
import os

dirname = os.path.dirname(__file__)

UserRecommender_path = os.path.join(dirname, 'models', 'UserRecommendModel.pkl')
fCleandf_path = os.path.join(dirname, 'models', 'fCleandf.pkl')

UserRecommender = cp.load(open(UserRecommender_path, 'rb'),compression='gzip')
fCleandf = pickle.load(file = open(fCleandf_path, 'rb'))


def getRecommendations(username):
    try:
        # limit of 20 added due to memeory issue
        _Top20Recproductdf = pd.DataFrame(UserRecommender.loc[username].sort_values(ascending=False)[0:20].index)
    except KeyError:
        errorMessage = f'OOPS! we weren\'t able to lookup "{username}", so we couldn\'t recommend anything \n\
            ....If you think this is an issue, You can call the Ebuss Help Centre support and get professional help regarding various topics. \n\
            ....You can try again by selecting any of the below username to find their recommendations.'
        print(type(errorMessage))
        return errorMessage, None
    
    _Top5Recproductdf = pd.merge(_Top20Recproductdf,fCleandf,on='id',how='inner').sort_values(['PositivePct'],ascending=False)[:5]

    productNameList = _Top5Recproductdf['name'].tolist()
    posSentimentRateList = _Top5Recproductdf['PositivePct'].tolist()

    return productNameList, posSentimentRateList