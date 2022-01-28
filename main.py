from sanic import Sanic
from sanic.response import text, html, redirect
from sanic_cors import CORS
import json
import os
import random
import pickle
app = Sanic(__name__)
CORS(app)

# http://localhost:19887/random_pic
@app.route('/random_pic', methods=['GET'])
def func(req):
    with open("pic_list.pkl","rb") as f:
        pic_list = pickle.load(f)
    selected = random.choice(pic_list)
    pic_url = f"https://cdn.jsdelivr.net/gh/you-bowen/random_pics_api/random_pics/{selected}"
    return redirect(f'{pic_url}')


if __name__ == '__main__':
    app.run(debug=True, port=19887, host='127.0.0.1')
