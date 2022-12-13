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
pass
def forLocationWithDetails():
'''public static XmlValidationError forLocationWithDetails(final String message, final String code, final Object[] args, final int severity, final Location location, final QName fieldQName, final QName offendingQname, final SchemaType expectedSchemaType, final List expectedQNames, final int errorType, final SchemaType badSchemaType)
'''
pass
def getMessage():
'''public String getMessage()
'''
pass
def getBadSchemaType():
'''public SchemaType getBadSchemaType()
'''
pass
def setBadSchemaType():
'''public void setBadSchemaType(final SchemaType _badSchemaType)
'''
pass
def getErrorType():
'''public int getErrorType()
'''
pass
def setErrorType():
'''public void setErrorType(final int _errorType)
'''
pass
def getExpectedQNames():
'''public List getExpectedQNames()
'''
pass
def setExpectedQNames():
'''public void setExpectedQNames(final List _expectedQNames)
'''
pass
def getFieldQName():
'''public QName getFieldQName()
'''
pass
def setFieldQName():
'''public void setFieldQName(final QName _fieldQName)
'''
pass
def getOffendingQName():
'''public QName getOffendingQName()
'''
pass
def setOffendingQName():
'''public void setOffendingQName(final QName _offendingQName)
'''
pass
def getExpectedSchemaType():
'''public SchemaType getExpectedSchemaType()
'''
pass
def setExpectedSchemaType():
'''public void setExpectedSchemaType(final SchemaType _expectedSchemaType)
'''
pass
