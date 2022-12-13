STATUS_OK_AS_IS = "int  0"
STATUS_OK_AFTER_COMMA = "int  1"
STATUS_OK_AFTER_COLON = "int  2"
STATUS_OK_AFTER_SPACE = "int  3"
STATUS_EXPECT_VALUE = "int  4"
STATUS_EXPECT_NAME = "int  5"
def withDupDetector():
    '''    public JsonWriteContext withDupDetector(final DupDetector dups)
    '''
def getCurrentValue():
    '''    public Object getCurrentValue()
    '''
def setCurrentValue():
    '''    public void setCurrentValue(final Object v)
    '''
def createRootContext():
    '''    public static JsonWriteContext createRootContext()
    public static JsonWriteContext createRootContext(final DupDetector dd)
    '''
def createChildArrayContext():
    '''    public JsonWriteContext createChildArrayContext()
    '''
def createChildObjectContext():
    '''    public JsonWriteContext createChildObjectContext()
    '''
def getParent():
    '''    public final JsonWriteContext getParent()
    '''
def getCurrentName():
    '''    public final String getCurrentName()
    '''
def hasCurrentName():
    '''    public boolean hasCurrentName()
    '''
def clearAndGetParent():
    '''    public JsonWriteContext clearAndGetParent()
    '''
def getDupDetector():
    '''    public DupDetector getDupDetector()
    '''
def writeFieldName():
    '''    public int writeFieldName(final String name)
    '''
def writeValue():
    '''    public int writeValue()
    '''
