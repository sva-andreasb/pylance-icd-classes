def version():
    '''    public Version version()
    '''
def enable():
    '''    public JsonGenerator enable(final Feature f)
    '''
def disable():
    '''    public JsonGenerator disable(final Feature f)
    '''
def isEnabled():
    '''    public final boolean isEnabled(final Feature f)
    '''
def useDefaultPrettyPrinter():
    '''    public JsonGenerator useDefaultPrettyPrinter()
    '''
def setCodec():
    '''    public JsonGenerator setCodec(final ObjectCodec oc)
    '''
def getCodec():
    '''    public final ObjectCodec getCodec()
    '''
def getOutputContext():
    '''    public final JsonWriteContext getOutputContext()
    '''
def writeStartArray():
    '''    public void writeStartArray()
    '''
def writeEndArray():
    '''    public void writeEndArray()
    '''
def writeStartObject():
    '''    public void writeStartObject()
    '''
def writeEndObject():
    '''    public void writeEndObject()
    '''
def writeRawValue():
    '''    public void writeRawValue(final String text)
    public void writeRawValue(final String text, final int offset, final int len)
    public void writeRawValue(final char[] text, final int offset, final int len)
    '''
def writeObject():
    '''    public void writeObject(final Object value)
    '''
def writeTree():
    '''    public void writeTree(final JsonNode rootNode)
    '''
def close():
    '''    public void close()
    '''
def isClosed():
    '''    public boolean isClosed()
    '''
def copyCurrentEvent():
    '''    public final void copyCurrentEvent(final JsonParser jp)
    '''
def copyCurrentStructure():
    '''    public final void copyCurrentStructure(final JsonParser jp)
    '''
