<style>.r{color:#ff7777}</style>

# How Build
To assemble an "html" file with all external scripts and styles into a single "html" file, you will need to download several programs and libraries.

## Downloading programs and libraries
* <span class=r>html-minifier-next</span> (https://github.com/j9t/html-minifier-next) -- It's the main abbreviation for the "html" file. After downloading, be sure to run the command in the folder. `html-minifier-next` `npm i -D html-minifier-next`.
* <span class=r>python</span> (https://www.python.org) -- It is required to activate the include.py file. This is done so that this file can be run on any operating system.
* * You need to download a library for <span class=r>Python</span> `BeautifulSoup` - `pip install beautifulsoup4`.

## Build
This is collected using script activations. `build.py` - `python build.py`.