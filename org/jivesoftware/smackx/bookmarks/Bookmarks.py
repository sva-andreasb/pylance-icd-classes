NAMESPACE = "String  \"storage:bookmarks\""
ELEMENT = "String  \"storage\""
def ():
    '''returns Bookmarks\n\n
    ()\n
    '''
def addBookmarkedURL():
    '''returns None\n\n
    addBookmarkedURL(final BookmarkedURL bookmarkedURL)\n
    '''
def removeBookmarkedURL():
    '''returns None\n\n
    removeBookmarkedURL(final BookmarkedURL bookmarkedURL)\n
    '''
def clearBookmarkedURLS():
    '''returns None\n\n
    clearBookmarkedURLS()\n
    '''
def addBookmarkedConference():
    '''returns None\n\n
    addBookmarkedConference(final BookmarkedConference bookmarkedConference)\n
    '''
def removeBookmarkedConference():
    '''returns None\n\n
    removeBookmarkedConference(final BookmarkedConference bookmarkedConference)\n
    '''
def clearBookmarkedConferences():
    '''returns None\n\n
    clearBookmarkedConferences()\n
    '''
def getBookmarkedURLS():
    '''returns List<BookmarkedURL>\n\n
    getBookmarkedURLS()\n
    '''
def getBookmarkedConferences():
    '''returns List<BookmarkedConference>\n\n
    getBookmarkedConferences()\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML()\n
    '''
def parsePrivateData():
    '''returns PrivateData\n\n
    parsePrivateData(final XmlPullParser parser)\n
    '''
