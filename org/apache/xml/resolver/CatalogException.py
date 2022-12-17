WRAPPER = "int  1"
INVALID_ENTRY = "int  2"
INVALID_ENTRY_TYPE = "int  3"
NO_XML_PARSER = "int  4"
UNKNOWN_FORMAT = "int  5"
UNPARSEABLE = "int  6"
PARSE_FAILED = "int  7"
UNENDED_COMMENT = "int  8"
def ():
    '''returns CatalogException\n\n
    (final int type, final String message)\n
    (final int type)\n
    (final Exception e)\n
    (final String message, final Exception e)\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage()\n
    '''
def getException():
    '''returns Exception\n\n
    getException()\n
    '''
def getExceptionType():
    '''returns int\n\n
    getExceptionType()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
