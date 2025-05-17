# Status Site

A simple FastAPI web application.


## Run with Docker

```bash
docker build -t fastapi-app .
docker run -d -p 8000:80 fastapi-app
```


## Deploy with Dokku

```bash
DOKKU_HOST=yourdomain.com dokku apps:create status
git push dokku main
#dokku ps:scale fastapi-app web=1
```
