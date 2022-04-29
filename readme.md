# py-ytdl

A simply server to show the video url

## Running serve

```
export FLASK_APP=main.py
export FLASK_ENV=development
flask run
```

## Endpoint
### Path: / (root)
```{host}/```

Shows the url from the sample link ```https://www.youtube.com/watch?v=vsGWMmNtWQY```

### Path: /d (download)
```{host}/d?link=https://www.youtube.com/watch?v=KwM4yOwMls4```

Expects a link query param. Show the respective url.