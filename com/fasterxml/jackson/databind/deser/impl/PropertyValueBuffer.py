def ():
    '''returns PropertyValueBuffer\n\n
    (final JsonParser p, final DeserializationContext ctxt, final int paramCount, final ObjectIdReader oir)\n
    '''
def getParameter():
    '''returns Object\n\n
    getParameter(final SettableBeanProperty prop)\n
    '''
def getParameters():
    '''returns Object[]\n\n
    getParameters(final SettableBeanProperty[] props)\n
    '''
def readIdProperty():
    '''returns boolean\n\n
    readIdProperty(final String propName)\n
    '''
def handleIdValue():
    '''returns Object\n\n
    handleIdValue(final DeserializationContext ctxt, final Object bean)\n
    '''
def isComplete():
    '''returns boolean\n\n
    isComplete()\n
    '''
def assignParameter():
    '''returns boolean\n\n
    assignParameter(final SettableBeanProperty prop, final Object value)\n
    '''
def bufferProperty():
    '''returns None\n\n
    bufferProperty(final SettableBeanProperty prop, final Object value)\n
    '''
def bufferAnyProperty():
    '''returns None\n\n
    bufferAnyProperty(final SettableAnyProperty prop, final String propName, final Object value)\n
    '''
def bufferMapProperty():
    '''returns None\n\n
    bufferMapProperty(final Object key, final Object value)\n
    '''
