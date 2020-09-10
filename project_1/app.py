from flask import Flask, render_template, jsonify, request
import xmltodict, json, urllib.request, requests
from bs4 import BeautifulSoup

app = Flask(__name__)

## Access To Each Category
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/blog')
def blog():
    return  render_template('blogSearch.html')
@app.route('/news')
def news():
    return  render_template('newsSearch.html')
@app.route('/image')
def image():
    return  render_template('imageSearch.html')
@app.route('/shopping')
def shopping():
    return  render_template('shoppingSearch.html')
@app.route('/dict')
def dictionary():
    return  render_template('dictionarySearch.html')
@app.route('/expert')
def location():
    return  render_template('expertSearch.html')

## 블로그 검색 API 활용 코드
@app.route('/blog1', methods=['GET'])
def blog_get1():
    search = request.args.get('search')
    client_id = "cjw_pzXf_UoUu4bgETXd"
    client_secret = "zFUL37euWy"
    encText = urllib.parse.quote(search)
    addingSearches = "&display=20"
    url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText + addingSearches
    Request = urllib.request.Request(url)
    Request.add_header("X-Naver-Client-Id", client_id)
    Request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(Request)
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        text = response_body.decode('utf-8')
        dict = xmltodict.parse(text)
        jsonString = json.dumps(dict['rss']['channel']['item'], ensure_ascii=False)
        jsonObj = json.loads(jsonString)
        return jsonify(jsonObj)

## 뉴스 검색 API 활용 코드

@app.route('/news1', methods=['GET'])
def news_get1():
    search = request.args.get('search')
    client_id = "cjw_pzXf_UoUu4bgETXd"
    client_secret = "zFUL37euWy"
    encText = urllib.parse.quote(search)
    addingSearches = "&display=20"
    url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText + addingSearches
    Request = urllib.request.Request(url)
    Request.add_header("X-Naver-Client-Id", client_id)
    Request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(Request)
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        text = response_body.decode('utf-8')
        dict = xmltodict.parse(text)
        jsonString = json.dumps(dict['rss']['channel']['item'], ensure_ascii=False)
        jsonObj = json.loads(jsonString)
        return jsonify(jsonObj)

## 이미지 검색 API 활용 코드

@app.route('/image1', methods=['GET'])
def image_get1():
    search = request.args.get('search')
    client_id = "cjw_pzXf_UoUu4bgETXd"
    client_secret = "zFUL37euWy"
    encText = urllib.parse.quote(search)
    addingSearches = "&display=60"
    url = "https://openapi.naver.com/v1/search/image.xml?query=" + encText + addingSearches
    Request = urllib.request.Request(url)
    Request.add_header("X-Naver-Client-Id", client_id)
    Request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(Request)
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        text = response_body.decode('utf-8')
        dict = xmltodict.parse(text)
        jsonString = json.dumps(dict['rss']['channel']['item'], ensure_ascii=False)
        jsonObj = json.loads(jsonString)
        return jsonify(jsonObj)

## 쇼핑 검색 API 활용 코드

@app.route('/shopping1', methods=['GET'])
def shopping_get1():
    search = request.args.get('search')
    client_id = "cjw_pzXf_UoUu4bgETXd"
    client_secret = "zFUL37euWy"
    encText = urllib.parse.quote(search)
    addingSearches = "&display=40"
    url = "https://openapi.naver.com/v1/search/shop.xml?query=" + encText + addingSearches
    Request = urllib.request.Request(url)
    Request.add_header("X-Naver-Client-Id", client_id)
    Request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(Request)
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        text = response_body.decode('utf-8')
        dict = xmltodict.parse(text)
        jsonString = json.dumps(dict['rss']['channel']['item'], ensure_ascii=False)
        jsonObj = json.loads(jsonString)
        return jsonify(jsonObj)

## 사전 검색 API 활용 코드

@app.route('/dict1', methods=['GET'])
def dict_get1():
    search = request.args.get('search')
    client_id = "cjw_pzXf_UoUu4bgETXd"
    client_secret = "zFUL37euWy"
    encText = urllib.parse.quote(search)
    addingSearches = "&display=20"
    url = "https://openapi.naver.com/v1/search/encyc.xml?query=" + encText + addingSearches
    Request = urllib.request.Request(url)
    Request.add_header("X-Naver-Client-Id", client_id)
    Request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(Request)
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        text = response_body.decode('utf-8')
        dict = xmltodict.parse(text)
        jsonString = json.dumps(dict['rss']['channel']['item'], ensure_ascii=False)
        jsonObj = json.loads(jsonString)
        return jsonify(jsonObj)

## 전문자료 검색 API 활용 코드
@app.route('/expert1', methods=['GET'])
def expert_get1():
    search = request.args.get('search')
    client_id = "cjw_pzXf_UoUu4bgETXd"
    client_secret = "zFUL37euWy"
    encText = urllib.parse.quote(search)
    addingSearches = "&display=40"
    url = "https://openapi.naver.com/v1/search/doc.xml?query=" + encText + addingSearches
    Request = urllib.request.Request(url)
    Request.add_header("X-Naver-Client-Id", client_id)
    Request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(Request)
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        text = response_body.decode('utf-8')
        dict = xmltodict.parse(text)
        jsonString = json.dumps(dict['rss']['channel']['item'], ensure_ascii=False)
        jsonObj = json.loads(jsonString)
        return jsonify(jsonObj)

if __name__ == '__main__':
    app.run('0.0.0.0', port = 5000, debug=True)
