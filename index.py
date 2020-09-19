from flask import Flask, render_template, request, redirect
# from flask_restful import Resource, Api
# import uuid, hashlib, string, random
import requests,json, os

app = Flask(__name__)
# api = Api(app)
#
# base_domain = 'https://tinyurl.test.com'
# long_url = 'https://www.baidu.com/s?wd=python&rsv_spt=1&rsv_iqid=0xd87989a1001c63cb&issp=1&f=8&rsv_bp=1&' \
#            'rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=11&rsv_sug1=1&rsv_sug7=100&' \
#            'rsv_sug2=0&rsv_btype=i&prefixsug=python&rsp=5&inputT=5276&rsv_sug4=8105'
# uid3 = uuid.uuid3(uuid.NAMESPACE_DNS, long_url)
# source_str = string.ascii_letters + string.digits
# final_key = ''.join(random.choice(source_str) for i in range(8))
#
#
# class GenerateURL(Resource):
#     def get(self):
#         return {'uuid': str(uid3), 'short_url': final_key, 'long_url': long_url}
#         # , 301, {'Location': long_url}

# api.add_resource(GenerateURL, '/api/v1/generate_url')


@app.route('/<resource_id>')
def redirect_long_url(resource_id):
    domain = 'tiny.default.com'
    port = int(os.environ.get('PORT', 5000))
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
    # domain = request.host_url.split('/')[2].split(':')[0]
    domain = 'tiny.default.com'
    response = requests.post(api_url, json={"domain": domain, "url": url})
    if response.status_code in [200, 409]:
        return response.json()['body']
    else:
        return {"short_url": "None"}


if __name__ == '__main__':
    app.run(debug=True)

    # hash_value = hashlib.md5(long_url.encode())
    # print(hash_value.hexdigest())
    #
    # print(uid3)
    #
    # print(final_key)
