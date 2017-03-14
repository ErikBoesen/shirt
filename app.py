from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
import json
import random
import string
import re

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/new', methods=['POST'])
def new():
    data = request.json

    if data.get('key') is not None:
        if db.links.find_one({'key': data['key']}) is None:
            key = data['key']
        else:
            # TODO: This can be done more cleanly.
            return jsonify({'error': 409}), 409
    else:
        key = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(0, 4)])

    url = re.sub(r'^https?://(www\.)?', '', data['url'])
    print('Creating link to %s at key %s...' % (url, key), end='')
    db.links.insert({
        'key': key,
        'url': url
    })
    print(' done.')

    return jsonify({'key': key})


@app.route('/<key>')
def link(key):
    url = '//' + db.links.find_one({'key': key})['url']

    return render_template('redir.html', url=url)


if __name__ == '__main__':
    app.run()
