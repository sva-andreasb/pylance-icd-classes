TK_NUMBER = "int  1"
TK_STRING = "int  2"
TK_NAME = "int  3"
TK_COMMENT = "int  4"
TK_START_ARRAY = "int  5"
TK_END_ARRAY = "int  6"
TK_START_DIC = "int  7"
TK_END_DIC = "int  8"
TK_REF = "int  9"
TK_OTHER = "int  10"
def ():
    '''returns PRTokeniser\n\n
    (final String filename)\n
    (final byte[] pdfIn)\n
    (final RandomAccessFileOrArray file)\n
    '''
def seek():
    '''returns None\n\n
    seek(final int pos)\n
    '''
def getFilePointer():
    '''returns int\n\n
    getFilePointer()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def length():
    '''returns int\n\n
    length()\n
    '''
def read():
    '''returns int\n\n
    read()\n
    '''
def getSafeFile():
    '''returns RandomAccessFileOrArray\n\n
    getSafeFile()\n
    '''
def getFile():
    '''returns RandomAccessFileOrArray\n\n
    getFile()\n
    '''
def readString():
    '''returns String\n\n
    readString(int size)\n
    '''
def getTokenType():
    '''returns int\n\n
    getTokenType()\n
    '''
def getStringValue():
    '''returns String\n\n
    getStringValue()\n
    '''
def getReference():
    '''returns int\n\n
    getReference()\n
    '''
def getGeneration():
    '''returns int\n\n
    getGeneration()\n
    '''
def backOnePosition():
    '''returns None\n\n
    backOnePosition(final int ch)\n
    '''
def throwError():
    '''returns None\n\n
    throwError(final String error)\n
    '''
def checkPdfHeader():
    '''returns char\n\n
    checkPdfHeader()\n
    '''
def checkFdfHeader():
    '''returns None\n\n
    checkFdfHeader()\n
    '''
def getStartxref():
    '''returns int\n\n
    getStartxref()\n
    '''
def nextValidToken():
    '''returns None\n\n
    nextValidToken()\n
    '''
def nextToken():
    '''returns boolean\n\n
    nextToken()\n
    '''
def intValue():
    '''returns int\n\n
    intValue()\n
    '''
def readLineSegment():
    '''returns boolean\n\n
    readLineSegment(final byte[] input)\n
    '''
def isHexString():
    '''returns boolean\n\n
    isHexString()\n
    '''
