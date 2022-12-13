def JsonReadContext():
'''public JsonReadContext(final JsonReadContext parent, final DupDetector dups, final int type, final int lineNr, final int colNr)
'''
pass
def withDupDetector():
'''public JsonReadContext withDupDetector(final DupDetector dups)
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
'''public static JsonReadContext createRootContext(final int lineNr, final int colNr, final DupDetector dups)
public static JsonReadContext createRootContext(final DupDetector dups)
'''
pass
def createChildArrayContext():
'''public JsonReadContext createChildArrayContext(final int lineNr, final int colNr)
'''
pass
def createChildObjectContext():
'''public JsonReadContext createChildObjectContext(final int lineNr, final int colNr)
'''
pass
def getCurrentName():
'''public String getCurrentName()
'''
pass
def hasCurrentName():
'''public boolean hasCurrentName()
'''
pass
def getParent():
'''public JsonReadContext getParent()
'''
pass
def getStartLocation():
'''public JsonLocation getStartLocation(final Object srcRef)
'''
pass
def clearAndGetParent():
'''public JsonReadContext clearAndGetParent()
'''
pass
def getDupDetector():
'''public DupDetector getDupDetector()
'''
pass
def expectComma():
'''public boolean expectComma()
'''
pass
def setCurrentName():
'''public void setCurrentName(final String name)
'''
pass
