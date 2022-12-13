STATUS_OK_AS_IS = "int  0"
STATUS_OK_AFTER_COMMA = "int  1"
STATUS_OK_AFTER_COLON = "int  2"
STATUS_OK_AFTER_SPACE = "int  3"
STATUS_EXPECT_VALUE = "int  4"
STATUS_EXPECT_NAME = "int  5"
def createRootContext():
'''public static JsonWriteContext createRootContext()
'''
pass
def createChildArrayContext():
'''public final JsonWriteContext createChildArrayContext()
'''
pass
def createChildObjectContext():
'''public final JsonWriteContext createChildObjectContext()
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
def writeFieldName():
'''public final int writeFieldName(final String name)
'''
pass
def writeValue():
'''public final int writeValue()
'''
pass
def toString():
'''public final String toString()
'''
pass
