STATUS_OK_AS_IS = "int  0"
STATUS_OK_AFTER_COMMA = "int  1"
STATUS_OK_AFTER_COLON = "int  2"
STATUS_OK_AFTER_SPACE = "int  3"
STATUS_EXPECT_VALUE = "int  4"
STATUS_EXPECT_NAME = "int  5"
def withDupDetector():
    '''returns JsonWriteContext\n\n
    withDupDetector(final DupDetector dups)\n
    '''
def getCurrentValue():
    '''returns Object\n\n
    getCurrentValue()\n
    '''
def setCurrentValue():
    '''returns None\n\n
    setCurrentValue(final Object v)\n
    '''
def createChildArrayContext():
    '''returns JsonWriteContext\n\n
    createChildArrayContext()\n
    '''
def createChildObjectContext():
    '''returns JsonWriteContext\n\n
    createChildObjectContext()\n
    '''
def hasCurrentName():
    '''returns boolean\n\n
    hasCurrentName()\n
    '''
def clearAndGetParent():
    '''returns JsonWriteContext\n\n
    clearAndGetParent()\n
    '''
def getDupDetector():
    '''returns DupDetector\n\n
    getDupDetector()\n
    '''
def writeFieldName():
    '''returns int\n\n
    writeFieldName(final String name)\n
    '''
def writeValue():
    '''returns int\n\n
    writeValue()\n
    '''
