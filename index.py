from flask import Flask, render_template, request, redirect
import requests,json, os

app = Flask(__name__)


@app.route('/<resource_id>')
def redirect_long_url(resource_id):
    domain = request.host_url.split('/')[2].split(':')[0]
    api_url = 'https://uovraoetk3.execute-api.ap-southeast-1.amazonaws.com/dev/shorturl'
    response = requests.get(api_url, json={"domain": domain, "resource_id": resource_id})
    return redirect(response.json()['result'], code=301)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api', methods=['POST'])
def test():
    api_url = 'https://uovraoetk3.execute-api.ap-southeast-1.amazonaws.com/dev/shorturl'
    url = request.form['long_url']
    domain = request.host_url.split('/')[2].split(':')[0]
    response = requests.post(api_url, json={"domain": domain, "url": url})
    if response.status_code in [200, 409]:
        return response.json()['body']
    else:
        return {"short_url": "None"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
