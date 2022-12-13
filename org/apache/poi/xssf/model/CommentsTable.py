DEFAULT_AUTHOR = "String  "
DEFAULT_AUTHOR_ID = "int  0"
def CommentsTable():
'''public CommentsTable()
public CommentsTable(final PackagePart part)
'''
pass
def readFrom():
'''public void readFrom(final InputStream is)
'''
pass
def writeTo():
'''public void writeTo(final OutputStream out)
'''
pass
def referenceUpdated():
'''public void referenceUpdated(final CellAddress oldReference, final CTComment comment)
'''
pass
def getNumberOfComments():
'''public int getNumberOfComments()
'''
pass
def getNumberOfAuthors():
'''public int getNumberOfAuthors()
'''
pass
def getAuthor():
'''public String getAuthor(final long authorId)
'''
pass
def findAuthor():
'''public int findAuthor(final String author)
'''
pass
def findCellComment():
'''public XSSFComment findCellComment(final CellAddress cellAddress)
'''
pass
def getCTComment():
'''public CTComment getCTComment(final CellAddress cellRef)
'''
pass
def getCellComments():
'''public Map<CellAddress, XSSFComment> getCellComments()
'''
pass
def newComment():
'''public CTComment newComment(final CellAddress ref)
'''
pass
def removeComment():
'''public boolean removeComment(final CellAddress cellRef)
'''
pass
def getCTComments():
'''public CTComments getCTComments()
'''
pass
