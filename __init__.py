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
      
  def getData(self, url, place, itemOccurence):
    contents = requests.get(url)
    contents = contents.text
    soup = BeautifulSoup(contents, "html.parser")
    return soup(place)[itemOccurence].string
