from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import pickle
import model

app = Flask(__name__)

@app.route('/')
def index():
    # fetching all username list
    allUsername = model.UserRecommender.index.tolist()
    return render_template('index.html', usernameList = allUsername)

@app.route('/recommend', methods = ['POST'])
def recommend():
    username = str(request.form.get('username'))
    print('username ', username)

    if not username:
        return redirect(url_for('index'))

    productNameList, posSentimentRateList = model.getRecommendations(username)

    if  posSentimentRateList == None or type(productNameList) == 'str':
        allUsername = model.UserRecommender.index.tolist()
        return render_template('index.html', usernameList = allUsername, error = productNameList)

    productList = zip(productNameList, posSentimentRateList)

    return render_template('recommendations.html', username = username, productList = productList)

if __name__ == '__main__':
    print('Sentiment Based Product Recommendation System')
    app.run(debug = False)