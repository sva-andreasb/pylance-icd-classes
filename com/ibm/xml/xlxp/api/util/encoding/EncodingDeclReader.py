UNKNOWN = "int  0"
UTF8N = "int  1"
UTF16BE = "int  2"
UTF16LE = "int  3"
UTF32BE = "int  4"
UTF32LE = "int  5"
LATIN = "int  6"
EBCDIC = "int  7"
UCS2BE = "int  8"
UCS2LE = "int  9"
UCS4BE = "int  10"
UCS4LE = "int  11"
def ():
    '''returns EncodingDeclReader\n\n
    ()\n
    '''
def setSource():
    '''returns None\n\n
    setSource(final RewindableInputStream fSource, final boolean fIsDocumentEntity)\n
    '''
def getEncodingName():
    '''returns String\n\n
    getEncodingName()\n
    '''
def readByte():
    '''returns int\n\n
    readByte()\n
    '''
def detectEncoding():
    '''returns int\n\n
    detectEncoding()\n
    '''
def getEBCDICEncoding():
    '''returns boolean\n\n
    getEBCDICEncoding()\n
    '''
def getLatinEncoding():
    '''returns boolean\n\n
    getLatinEncoding()\n
    '''
def getUCSEncoding():
    '''returns boolean\n\n
    getUCSEncoding(final int fBytesPerChar, final boolean fIsBigEndian)\n
    '''
