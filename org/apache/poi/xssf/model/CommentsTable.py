DEFAULT_AUTHOR = "String  \"\""
DEFAULT_AUTHOR_ID = "int  0"
def CommentsTable():
    '''public CommentsTable()
    public CommentsTable(final PackagePart part)
    '''
def readFrom():
    '''public void readFrom(final InputStream is)
    '''
def writeTo():
    '''public void writeTo(final OutputStream out)
    '''
def referenceUpdated():
    '''public void referenceUpdated(final CellAddress oldReference, final CTComment comment)
    '''
def getNumberOfComments():
    '''public int getNumberOfComments()
    '''
def getNumberOfAuthors():
    '''public int getNumberOfAuthors()
    '''
def getAuthor():
    '''public String getAuthor(final long authorId)
    '''
def findAuthor():
    '''public int findAuthor(final String author)
    '''
def findCellComment():
    '''public XSSFComment findCellComment(final CellAddress cellAddress)
    '''
def getCTComment():
    '''public CTComment getCTComment(final CellAddress cellRef)
    '''
def getCellComments():
    '''public Map<CellAddress, XSSFComment> getCellComments()
    '''
def newComment():
    '''public CTComment newComment(final CellAddress ref)
    '''
def removeComment():
    '''public boolean removeComment(final CellAddress cellRef)
    '''
def getCTComments():
    '''public CTComments getCTComments()
    '''
