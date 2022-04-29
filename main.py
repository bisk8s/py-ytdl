from flask import Flask, request
from youtube_dl import YoutubeDL 

PORT = 8080
app = Flask(__name__)
url = 'https://www.youtube.com/watch?v=vsGWMmNtWQY'

youtube_dl_opts=dict(forceurl=True)

@app.route('/')
def home():
    with YoutubeDL(youtube_dl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        media_url = info_dict['formats'][-1]['url']
        return f'media_url: {media_url}'


@app.route('/d')
def download():
    link = request.args.get('link', '')
    with YoutubeDL(youtube_dl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=False)
        media_url = info_dict['formats'][-1]['url']
        return f'media_url: {media_url}'

if __name__ == '__main__':
    print(f'serving at port http://127.0.0.1:{PORT}')
    app.run(port=PORT)