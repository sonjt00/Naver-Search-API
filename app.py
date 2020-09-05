from flask import Flask, render_template, jsonify
from flask import request
import xmltodict
import json
import urllib.request

# 아래 두 코드는, 웹 스크래핑을 위한 코드
import requests 
from bs4 import BeautifulSoup

app = Flask(__name__)


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분

@app.route('/link', methods=['GET'])
def link_get():
    li = request.args.get('link')
    two_li = li.split('//')
    first = two_li[0]
    second = two_li[1]
    link = first + '//m.' +second
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(link, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser') #html파일을 가져와 soup 변수에 넣어주었고
    thumb = soup.select('meta[property="og:image"]')
    thumb_real = thumb[0]
    thumb_url = thumb_real['content']

    title = soup.select('meta[property="og:title"]')
    title_real = title[0]
    title_send = title_real['content']

    descrip = soup.select('meta[property="og:description"]')
    descrip_real = descrip[0]
    descrip_send = descrip_real['content']
    # 필요한 og 고르기
    print(soup)
    # url이 이미지 링크, link가 사이트 모바일 링크, title이 제목, descrip이 설명
    return jsonify({'result': 'success','title':  title_send ,'url': thumb_url, 'link' : link, 'descrip': descrip_send})


@app.route('/test', methods=['GET'])
def test_get():
    dish = request.args.get('dish')
    client_id = "cjw_pzXf_UoUu4bgETXd"
    client_secret = "zFUL37euWy"
    encText = urllib.parse.quote(dish)
    addingSearches = "&display=100"
    url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText  # xml 결과
    url += addingSearches  # 검색 결과를 50개로 늘린 코드
    Request = urllib.request.Request(url)
    Request.add_header("X-Naver-Client-Id", client_id)
    Request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(Request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        text = response_body.decode('utf-8')  # xml 형태의 text
        dict = xmltodict.parse(text)  # xml 형태의 text를 사전형으로 바꾸어 dict 변수에 넣어주고
        jsonString = json.dumps(dict['rss']['channel']['item'], ensure_ascii=False)
        jsonObj = json.loads(jsonString)
    return jsonify(jsonObj)

    # return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)