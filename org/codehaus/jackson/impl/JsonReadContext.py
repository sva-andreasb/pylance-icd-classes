def JsonReadContext():
    '''    public JsonReadContext(final JsonReadContext parent, final int type, final int lineNr, final int colNr)
    '''
def createRootContext():
    '''    public static JsonReadContext createRootContext(final int lineNr, final int colNr)
    public static JsonReadContext createRootContext()
    '''
def createChildArrayContext():
    '''    public final JsonReadContext createChildArrayContext(final int lineNr, final int colNr)
    '''
def createChildObjectContext():
    '''    public final JsonReadContext createChildObjectContext(final int lineNr, final int colNr)
    '''
def getCurrentName():
    '''    public final String getCurrentName()
    '''
def getParent():
    '''    public final JsonReadContext getParent()
    '''
def getStartLocation():
    '''    public final JsonLocation getStartLocation(final Object srcRef)
    '''
def expectComma():
    '''    public final boolean expectComma()
    '''
def setCurrentName():
    '''    public void setCurrentName(final String name)
    '''
def toString():
    '''    public final String toString()
    '''
