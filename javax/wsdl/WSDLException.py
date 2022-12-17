serialVersionUID = "long  1L"
INVALID_WSDL = "String  \"INVALID_WSDL\""
PARSER_ERROR = "String  \"PARSER_ERROR\""
OTHER_ERROR = "String  \"OTHER_ERROR\""
CONFIGURATION_ERROR = "String  \"CONFIGURATION_ERROR\""
def ():
    '''returns WSDLException\n\n
    (final String faultCode, final String message, final Throwable targetException)\n
    (final String s, final String s2)\n
    '''
def setFaultCode():
    '''returns None\n\n
    setFaultCode(final String faultCode)\n
    '''
def getFaultCode():
    '''returns String\n\n
    getFaultCode()\n
    '''
def setTargetException():
    '''returns None\n\n
    setTargetException(final Throwable targetThrowable)\n
    '''
def getTargetException():
    '''returns Throwable\n\n
    getTargetException()\n
    '''
def setLocation():
    '''returns None\n\n
    setLocation(final String location)\n
    '''
def getLocation():
    '''returns String\n\n
    getLocation()\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
