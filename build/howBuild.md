<style>r{color:#ff7777}</style>

# How Build
To assemble an `HTML` file with all external scripts and styles into a single `HTML` file, you will need to download several programs and libraries.  

## Downloading programs and libraries
* <r>html-minifier-next</r> (https://github.com/j9t/html-minifier-next) -- It's the main abbreviation for the `HTML` file. After downloading, be sure to run the command in the folder. `html-minifier-next` `npm i -D html-minifier-next`.  
* <r>python</r> (https://www.python.org) -- It is required to activate the include.py file. This is done so that this file can be run on any operating system.  
You need to download a library for `Python` `BeautifulSoup` - `pip install beautifulsoup4`.  

## Build
To build a single `HTML` page, you first need to perform several tasks:  
* 1. Ensure that the `html-minifier-next` folder has been created within the `build` folder and that the `html-minifier-next` program is installed.  

Once these settings are configured, you can proceed to the location where the local `HTML` pages will be created and assembled.  
The primary location for creating and assembling `HTML` pages is the `posts` folder.  
To build the HTML page, simply run the command `python post.py`.  

In order to be completely sure that the file was compiled correctly, and no errors occurred during the execution of the work, in the `bin` folder there is a `build post.html` file, this is the file that should be obtained in the end.  