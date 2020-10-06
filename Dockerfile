FROM python:3-alpine AS builder

WORKDIR /opt/cloudfleet-blog

RUN pip install pelican Markdown

COPY . /opt/cloudfleet-blog
RUN pelican -dt cloudfleet-pelican-theme content

FROM nginx:alpine

COPY --from=builder /opt/cloudfleet-blog/output /usr/share/nginx/html
