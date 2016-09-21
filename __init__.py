from bs4 import BeautifulSoup
import requests

class Updates:
  def checkData(self, url, data, place, itemOccurence, debug=False):
    contents = requests.get(url)
    contents = contents.text
    soup = BeautifulSoup(contents, "html.parser")
    if debug:
      print soup(place)[itemOccurence].string
    if soup(place)[itemOccurence].string == data:
      return False
    else:
      return True

  def getData(self, url, place, itemOccurence=0):
    contents = requests.get(url)
    contents = contents.text
    soup = BeautifulSoup(contents, "html.parser")
    return soup(place)[itemOccurence].string

  # This is meant to return the data in a web list
  # Outputs an array with the data elements
  def getListData(self, url, place, itemOccurence=0):
    contents = requests.get(url)
    contents = contents.text
    soup = BeautifulSoup(contents, "html.parser")
    results = soup(place)[itemOccurence]
    results = results.findAll("li")
    toReturn = []
    for i in results:
      toReturn.append(i.text)
    return toReturn

  def checkListData(self, url, data, place, itemOccurence=0, debug=False):
    contents = requests.get(url)
    contents = contents.text
    soup = BeautifulSoup(contents, "html.parser")
    results = soup(place)[itemOccurence]
    results = results.findAll("li")
    toReturn = []
    for i in results:
      toReturn.append(i.text)
    if debug:
      print toReturn
    if toReturn == data:
      return False
    else:
      return True
