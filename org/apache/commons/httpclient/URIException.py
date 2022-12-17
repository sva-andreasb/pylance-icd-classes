UNKNOWN = "int  0"
PARSING = "int  1"
UNSUPPORTED_ENCODING = "int  2"
ESCAPING = "int  3"
PUNYCODE = "int  4"
def ():
    '''returns URIException\n\n
    ()\n
    (final int reasonCode)\n
    (final int reasonCode, final String reason)\n
    (final String reason)\n
    '''
def getReasonCode():
    '''returns int\n\n
    getReasonCode()\n
    '''
def setReasonCode():
    '''returns None\n\n
    setReasonCode(final int reasonCode)\n
    '''
def getReason():
    '''returns String\n\n
    getReason()\n
    '''
def setReason():
    '''returns None\n\n
    setReason(final String reason)\n
    '''
