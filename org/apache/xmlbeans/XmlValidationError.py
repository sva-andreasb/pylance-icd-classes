INCORRECT_ELEMENT = "int  1"
ELEMENT_NOT_ALLOWED = "int  2"
ELEMENT_TYPE_INVALID = "int  3"
NIL_ELEMENT = "int  4"
INCORRECT_ATTRIBUTE = "int  1000"
ATTRIBUTE_TYPE_INVALID = "int  1001"
LIST_INVALID = "int  2000"
UNION_INVALID = "int  3000"
UNDEFINED = "int  10000"
def forCursorWithDetails():
    '''public static XmlValidationError forCursorWithDetails(final String message, final String code, final Object[] args, final int severity, final XmlCursor cursor, final QName fieldQName, final QName offendingQname, final SchemaType expectedSchemaType, final List expectedQNames, final int errorType, final SchemaType badSchemaType)
    '''
def forLocationWithDetails():
    '''public static XmlValidationError forLocationWithDetails(final String message, final String code, final Object[] args, final int severity, final Location location, final QName fieldQName, final QName offendingQname, final SchemaType expectedSchemaType, final List expectedQNames, final int errorType, final SchemaType badSchemaType)
    '''
def getMessage():
    '''public String getMessage()
    '''
def getBadSchemaType():
    '''public SchemaType getBadSchemaType()
    '''
def setBadSchemaType():
    '''public void setBadSchemaType(final SchemaType _badSchemaType)
    '''
def getErrorType():
    '''public int getErrorType()
    '''
def setErrorType():
    '''public void setErrorType(final int _errorType)
    '''
def getExpectedQNames():
    '''public List getExpectedQNames()
    '''
def setExpectedQNames():
    '''public void setExpectedQNames(final List _expectedQNames)
    '''
def getFieldQName():
    '''public QName getFieldQName()
    '''
def setFieldQName():
    '''public void setFieldQName(final QName _fieldQName)
    '''
def getOffendingQName():
    '''public QName getOffendingQName()
    '''
def setOffendingQName():
    '''public void setOffendingQName(final QName _offendingQName)
    '''
def getExpectedSchemaType():
    '''public SchemaType getExpectedSchemaType()
    '''
def setExpectedSchemaType():
    '''public void setExpectedSchemaType(final SchemaType _expectedSchemaType)
    '''
