Movie-Trailer-Website

Quickstart

Install Python 2.7.0

Command Line

Download the three Python files, entertainment_center.py, media.py and fresh_tomatoes.py.
Open the three Python files in IDLE(Python GUI). Click 'File', followed by 'Open' and select the first file 'entertainment_center.py'. Repeat this for the other 2 python files.
Now click on 'Run', followed by 'Run Module'. Run the module for each of the three Python files. A HTML page will run in a browser. The outcome is a website with a list of movie trailers.
The names of the movies as well as their URLs could be changed in entertainment_center.py if you would like to include other movie trailers in the website.

Example

The following lines in entertainment_center.py could be modified if you would like to add a new movie to the website. The words within the first inverted commas states the movie name, the words in the second inverted commas is the description of the movie, the words in the third inverted commas is a wikipedia page about the movie, and the words in the fourth inverted commas is a link to the youtube trailer of the movie.

The_Foreigner = media.Movie("The Foreigner",
                     "An action thriller featuring Jackie Chan",
                     "https://en.wikipedia.org/wiki/The_Foreigner_(2017_film)",
                     "https://www.youtube.com/watch?v=EypTSjHoFsg")

Issues

Python 2.7.0 needs to be installed in order for the html page to work at runtime. In addition, a working browser such as Opera needs to be installed in your PC. 

License

This work is a public domain work. Feel free to do whatever you want with it.
