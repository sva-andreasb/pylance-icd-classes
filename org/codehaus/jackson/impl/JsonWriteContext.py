STATUS_OK_AS_IS = "int  0"
STATUS_OK_AFTER_COMMA = "int  1"
STATUS_OK_AFTER_COLON = "int  2"
STATUS_OK_AFTER_SPACE = "int  3"
STATUS_EXPECT_VALUE = "int  4"
STATUS_EXPECT_NAME = "int  5"
def createRootContext():
    '''    public static JsonWriteContext createRootContext()
    '''
def createChildArrayContext():
    '''    public final JsonWriteContext createChildArrayContext()
    '''
def createChildObjectContext():
    '''    public final JsonWriteContext createChildObjectContext()
    '''
def getParent():
    '''    public final JsonWriteContext getParent()
    '''
def getCurrentName():
    '''    public final String getCurrentName()
    '''
def writeFieldName():
    '''    public final int writeFieldName(final String name)
    '''
def writeValue():
    '''    public final int writeValue()
    '''
def toString():
    '''    public final String toString()
    '''
