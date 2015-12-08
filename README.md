# CloudFleet Blog

## Quick Start for CloudFleeters

To write posts, Add Markdown files to the *content/* folder. The content should
start with some metadata like:

```
Title: Meet our team – Christoph
Date: 2015-12-08 18:25
Category: general
Tags: team, christoph
Slug: meet-our-team-christoph
Author: Laura Gaetano
Author_link: https://cloudfleet.io/#team-tabs
Summary: Introducing the Admiral of the Clouds
Status: published
```

If you just want to add it as a draft, omit the `Status: published` line.

To publish, make sure `Status: published` is added, check that the date is valid
and from [base-builder](https://code.cloudfleet-hq.net/cloudfleet/base-builder/)
run:

    ansible-playbook spire.yml -K --tags=blog


## Installation

    pip install pelican markdown

Clone cloudfleet-pelican-theme in the same folder where blog is.

## Usage

Then from the blog folder call (every time you change sth :( )

    ./build.sh

Start the site

    cd output/
    python -m pelican.server

Go to <http://localhost:8000>

## Hacking the theme

Clone the theme on the same level as blog.

Edit it and rerun this to see changes:

    ./build.sh; (cd ./output; python -m pelican.server)
