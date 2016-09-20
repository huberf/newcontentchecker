# newcontentchecker
Simple library for checking if a site has added new content, for instance checking for new posts, podcasts, etc.

Make sure you have the following libraries installed:
BeautifulSoup (bs4)
requests

Then simple call checkData("example.com", "Episode 50", "h2", 5) and it will return true if the content in the 5th h2 tag is no longer equal to "Episode 50"

All functions:
checkData - Checks if data in an HTML page is different from the data you put
getData - Returns a string containing the data in a given location on a page
getListData - Returns an array with all the values from an HTML list
