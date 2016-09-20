'''
VERY simple and TERRIBLY syntactically painful test examples
The URLs used may be local to my stesm and will therefore not work on your setup
out of the box.
'''

import __init__

mine = __init__.Updates()

print mine.getListData("http://localhost:5000/", "ul")
