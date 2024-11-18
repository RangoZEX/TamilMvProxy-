import requests
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    url = request.args.get('url')
    if not url:
        return "Hello world"
    headers = {
        "Referer": "https://www.google.com/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
    }
    response = requests.get(url, headers=headers)
    print(response.text[:5000])
    return response.text

# @app.errorhandler(500)
# def page_not_found(e):
#     # note that we set the 404 status explicitly
#     return render_template('404.html'), 500


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
