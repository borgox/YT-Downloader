from flask import Flask, render_template, request, redirect, url_for
from src.download import Downloader
import pytube
import os
from src.colors import Colors, ForegroundColors, BackgroundColors
os.system("cls " if os.name == "nt" else "clear")
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    try:
        x = pytube.YouTube(url)
        x.check_availability()
    except:
        pass
    downloader = Downloader()
    result = downloader.by_url(url, quality='highest')
    if result == "Downloaded.":
        return redirect(url_for('another'))
    else:
        return render_template('failure.html')

@app.route('/another', methods=['GET'])
def another():
    return render_template('another.html')
@app.route('/exit', methods=['POST'])
def exit():
    exit(code="200")


if __name__ == "__main__":
    app.run()

