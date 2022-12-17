def version():
    '''returns Version\n\n
    version()\n
    '''
def enable():
    '''returns JsonGenerator\n\n
    enable(final Feature f)\n
    '''
def disable():
    '''returns JsonGenerator\n\n
    disable(final Feature f)\n
    '''
def useDefaultPrettyPrinter():
    '''returns JsonGenerator\n\n
    useDefaultPrettyPrinter()\n
    '''
def setCodec():
    '''returns JsonGenerator\n\n
    setCodec(final ObjectCodec oc)\n
    '''
def writeStartArray():
    '''returns None\n\n
    writeStartArray()\n
    '''
def writeEndArray():
    '''returns None\n\n
    writeEndArray()\n
    '''
def writeStartObject():
    '''returns None\n\n
    writeStartObject()\n
    '''
def writeEndObject():
    '''returns None\n\n
    writeEndObject()\n
    '''
def writeRawValue():
    '''returns None\n\n
    writeRawValue(final String text)\n
    writeRawValue(final String text, final int offset, final int len)\n
    writeRawValue(final char[] text, final int offset, final int len)\n
    '''
def writeObject():
    '''returns None\n\n
    writeObject(final Object value)\n
    '''
def writeTree():
    '''returns None\n\n
    writeTree(final JsonNode rootNode)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
