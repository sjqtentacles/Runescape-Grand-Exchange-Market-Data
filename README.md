# Runescape-Grand-Exchange-Market-Data
Years of Runescape Grand Exchange data collected from grandexchangewatch.com. Cleaned, pruned for duplicates, and some analysis. 

Runescape has a terrible API. Just terrible. 

I spent at least 20 hours hammering the grandexchangewatch.com website for the data using BeautifulSoup and Requests. The cleaning was a nightmare, but in the end all was eventually handled.

The data is in the zip file which expands into a 300MB CSV file.

Note: In the analysis notebook, there exists code for encoding the labels (e.g. the item name) as numeric values, but the data file is left 'as is' for your analysis. 

All of the 'analysis' is incredibly crude. This was more of a data-scraping-and-cleaning project than a predictive modeling one.

Here's a pretty picture!

<img src='adamant_longsword.png'>

The analysis pulls the data from my local MongoDB storage, so you should rewrite that to just pull from the CSV that you can get from the data (zip) file.

i.e. load a csv into pandas for your analysis. 

Enjoy.
