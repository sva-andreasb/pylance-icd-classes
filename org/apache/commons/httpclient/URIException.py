UNKNOWN = "int  0"
PARSING = "int  1"
UNSUPPORTED_ENCODING = "int  2"
ESCAPING = "int  3"
PUNYCODE = "int  4"
def URIException():
    '''public URIException()
    public URIException(final int reasonCode)
    public URIException(final int reasonCode, final String reason)
    public URIException(final String reason)
    '''
def getReasonCode():
    '''public int getReasonCode()
    '''
def setReasonCode():
    '''public void setReasonCode(final int reasonCode)
    '''
def getReason():
    '''public String getReason()
    '''
def setReason():
    '''public void setReason(final String reason)
    '''
