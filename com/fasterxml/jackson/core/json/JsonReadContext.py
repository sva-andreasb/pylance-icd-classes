def JsonReadContext():
    '''    public JsonReadContext(final JsonReadContext parent, final DupDetector dups, final int type, final int lineNr, final int colNr)
    '''
def withDupDetector():
    '''    public JsonReadContext withDupDetector(final DupDetector dups)
    '''
def getCurrentValue():
    '''    public Object getCurrentValue()
    '''
def setCurrentValue():
    '''    public void setCurrentValue(final Object v)
    '''
def createRootContext():
    '''    public static JsonReadContext createRootContext(final int lineNr, final int colNr, final DupDetector dups)
    public static JsonReadContext createRootContext(final DupDetector dups)
    '''
def createChildArrayContext():
    '''    public JsonReadContext createChildArrayContext(final int lineNr, final int colNr)
    '''
def createChildObjectContext():
    '''    public JsonReadContext createChildObjectContext(final int lineNr, final int colNr)
    '''
def getCurrentName():
    '''    public String getCurrentName()
    '''
def hasCurrentName():
    '''    public boolean hasCurrentName()
    '''
def getParent():
    '''    public JsonReadContext getParent()
    '''
def getStartLocation():
    '''    public JsonLocation getStartLocation(final Object srcRef)
    '''
def clearAndGetParent():
    '''    public JsonReadContext clearAndGetParent()
    '''
def getDupDetector():
    '''    public DupDetector getDupDetector()
    '''
def expectComma():
    '''    public boolean expectComma()
    '''
def setCurrentName():
    '''    public void setCurrentName(final String name)
    '''
