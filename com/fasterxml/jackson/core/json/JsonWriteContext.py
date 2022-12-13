STATUS_OK_AS_IS = "int  0"
STATUS_OK_AFTER_COMMA = "int  1"
STATUS_OK_AFTER_COLON = "int  2"
STATUS_OK_AFTER_SPACE = "int  3"
STATUS_EXPECT_VALUE = "int  4"
STATUS_EXPECT_NAME = "int  5"
def withDupDetector():
'''public JsonWriteContext withDupDetector(final DupDetector dups)
'''
pass
def getCurrentValue():
'''public Object getCurrentValue()
'''
pass
def setCurrentValue():
'''public void setCurrentValue(final Object v)
'''
pass
def createRootContext():
'''public static JsonWriteContext createRootContext()
public static JsonWriteContext createRootContext(final DupDetector dd)
'''
pass
def createChildArrayContext():
'''public JsonWriteContext createChildArrayContext()
'''
pass
def createChildObjectContext():
'''public JsonWriteContext createChildObjectContext()
'''
pass
def getParent():
'''public final JsonWriteContext getParent()
'''
pass
def getCurrentName():
'''public final String getCurrentName()
'''
pass
def hasCurrentName():
'''public boolean hasCurrentName()
'''
pass
def clearAndGetParent():
'''public JsonWriteContext clearAndGetParent()
'''
pass
def getDupDetector():
'''public DupDetector getDupDetector()
'''
pass
def writeFieldName():
'''public int writeFieldName(final String name)
'''
pass
def writeValue():
'''public int writeValue()
'''
pass
