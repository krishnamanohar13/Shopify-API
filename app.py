# Flask starter template
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/requestData', methods=['GET'])
def requestData():
    username = 'fa14698cf08907476b4e16cf8f324646'
    password = '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'
    shop_addr = 'messoldtech-test'
    url = 'https://'+username+':'+password+'@'+shop_addr+'.myshopify.com/admin/api/2020-10/products.json'
    # print(url)
    response = requests.get(url)
    return response.json()

if '__main__' == __name__:
    app.run(debug=True)