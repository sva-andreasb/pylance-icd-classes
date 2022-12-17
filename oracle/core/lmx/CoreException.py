UNIMPLEMENTED = "byte  1"
UNDERFLOW = "byte  2"
OVERFLOW = "byte  3"
INVALIDORLN = "byte  4"
BADFORMATORLN = "byte  5"
INVALIDORLD = "byte  6"
BADFORMATORLD = "byte  7"
BADYEAR = "byte  8"
BADDAYYEAR = "byte  9"
BADJULIANDATE = "byte  10"
INVALIDINPUTN = "byte  11"
NLSNOTSUPPORTED = "byte  12"
INVALIDINPUT = "byte  13"
CONVERSIONERROR = "byte  14"
def ():
    '''returns CoreException\n\n
    ()\n
    (final String message)\n
    (final byte ecode)\n
    '''
def setErrorCode():
    '''returns None\n\n
    setErrorCode(final byte ecode)\n
    '''
def getErrorCode():
    '''returns byte\n\n
    getErrorCode()\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage()\n
    '''
