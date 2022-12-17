TYPE_SOAP = "int  0"
TYPE_HTTP_GET = "int  1"
TYPE_HTTP_POST = "int  2"
TYPE_UNKNOWN = "int  3"
USE_ENCODED = "int  0"
USE_LITERAL = "int  1"
NO_HEADER = "int  0"
IN_HEADER = "int  1"
OUT_HEADER = "int  2"
def ():
    '''returns OperationAttr\n\n
    (final Binding binding, final int bindingType, final Style bindingStyle, final boolean hasLiteral, final HashMap attributes, final Map mimeTypes, final Map headerParts)\n
    (final Binding binding)\n
    (final Use inputBodyType, final Use outputBodyType, final HashMap faultBodyTypeMap)\n
    ()\n
    '''
def getParameters():
    '''returns HashMap\n\n
    getParameters(final Operation operation)\n
    getParameters()\n
    '''
def setParameters():
    '''returns None\n\n
    setParameters(final HashMap parameters)\n
    '''
def getMIMEInfo():
    '''returns MimeInfo\n\n
    getMIMEInfo(final String operationName, final String parameterName)\n
    '''
def getMIMETypes():
    '''returns Map\n\n
    getMIMETypes()\n
    '''
def setMIMEInfo():
    '''returns None\n\n
    setMIMEInfo(final String operationName, final String parameterName, final String type, final String dims)\n
    '''
def setOperationDIME():
    '''returns None\n\n
    setOperationDIME(final String operationName)\n
    '''
def isOperationDIME():
    '''returns boolean\n\n
    isOperationDIME(final String operationName)\n
    '''
def isInHeaderPart():
    '''returns boolean\n\n
    isInHeaderPart(final String operationName, final String partName)\n
    '''
def isOutHeaderPart():
    '''returns boolean\n\n
    isOutHeaderPart(final String operationName, final String partName)\n
    '''
def getHeaderParts():
    '''returns Map\n\n
    getHeaderParts()\n
    '''
def setHeaderPart():
    '''returns None\n\n
    setHeaderPart(final String operationName, final String partName, final int headerFlags)\n
    '''
def getBinding():
    '''returns Binding\n\n
    getBinding()\n
    '''
def getBindingType():
    '''returns int\n\n
    getBindingType()\n
    '''
def getBindingStyle():
    '''returns Style\n\n
    getBindingStyle()\n
    '''
def hasLiteral():
    '''returns boolean\n\n
    hasLiteral()\n
    '''
def getInputBodyType():
    '''returns Use\n\n
    getInputBodyType(final Operation operation)\n
    getInputBodyType()\n
    '''
def getOutputBodyType():
    '''returns Use\n\n
    getOutputBodyType(final Operation operation)\n
    getOutputBodyType()\n
    '''
def getFaultBodyType():
    '''returns Use\n\n
    getFaultBodyType(final Operation operation, final String faultName)\n
    '''
def getFaults():
    '''returns HashMap\n\n
    getFaults()\n
    '''
def setFaults():
    '''returns None\n\n
    setFaults(final HashMap faults)\n
    '''
def getOperations():
    '''returns Set\n\n
    getOperations()\n
    '''
def getFaultBodyTypeMap():
    '''returns HashMap\n\n
    getFaultBodyTypeMap()\n
    '''
