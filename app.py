from flask import Flask, render_template, request, redirect, url_for
from scrapt import Scrapt

app = Flask(__name__)
url = 'https://luminarynovels.com/novel/is-it-funny-that-the-dragon-slayer-failed-and-became-the-dragon-princess/volume-1-chapter-1/'
sc = Scrapt(url)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', title=sc.getTitle(), content=sc.getText(), prev=sc.getPrev(), next=sc.getNext())

@app.route("/change")
def change():
    recv_url = request.args.get('recv_url')
    print('contiene: ', recv_url)
    if recv_url:
        print(recv_url)
        sc.change_url(recv_url)
        
    else:
        return redirect(url_for('index'))

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=False)
