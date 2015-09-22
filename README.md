# CloudFleet Blog

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
