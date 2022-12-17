DEFAULT_AUTHOR = "String  \"\""
DEFAULT_AUTHOR_ID = "int  0"
def ():
    '''returns CommentsTable\n\n
    ()\n
    (final PackagePart part)\n
    '''
def readFrom():
    '''returns None\n\n
    readFrom(final InputStream is)\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final OutputStream out)\n
    '''
def referenceUpdated():
    '''returns None\n\n
    referenceUpdated(final CellAddress oldReference, final CTComment comment)\n
    '''
def getNumberOfComments():
    '''returns int\n\n
    getNumberOfComments()\n
    '''
def getNumberOfAuthors():
    '''returns int\n\n
    getNumberOfAuthors()\n
    '''
def getAuthor():
    '''returns String\n\n
    getAuthor(final long authorId)\n
    '''
def findAuthor():
    '''returns int\n\n
    findAuthor(final String author)\n
    '''
def findCellComment():
    '''returns XSSFComment\n\n
    findCellComment(final CellAddress cellAddress)\n
    '''
def getCTComment():
    '''returns CTComment\n\n
    getCTComment(final CellAddress cellRef)\n
    '''
def newComment():
    '''returns CTComment\n\n
    newComment(final CellAddress ref)\n
    '''
def removeComment():
    '''returns boolean\n\n
    removeComment(final CellAddress cellRef)\n
    '''
def getCTComments():
    '''returns CTComments\n\n
    getCTComments()\n
    '''
