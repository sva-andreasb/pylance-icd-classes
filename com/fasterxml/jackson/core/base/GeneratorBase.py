SURR1_FIRST = "int  55296"
SURR1_LAST = "int  56319"
SURR2_FIRST = "int  56320"
SURR2_LAST = "int  57343"
def version():
    '''returns Version\n\n
    version()\n
    '''
def getCurrentValue():
    '''returns Object\n\n
    getCurrentValue()\n
    '''
def setCurrentValue():
    '''returns None\n\n
    setCurrentValue(final Object v)\n
    '''
def getFeatureMask():
    '''returns int\n\n
    getFeatureMask()\n
    '''
def enable():
    '''returns JsonGenerator\n\n
    enable(final Feature f)\n
    '''
def disable():
    '''returns JsonGenerator\n\n
    disable(final Feature f)\n
    '''
def setFeatureMask():
    '''returns JsonGenerator\n\n
    setFeatureMask(final int newMask)\n
    '''
def overrideStdFeatures():
    '''returns JsonGenerator\n\n
    overrideStdFeatures(final int values, final int mask)\n
    '''
def useDefaultPrettyPrinter():
    '''returns JsonGenerator\n\n
    useDefaultPrettyPrinter()\n
    '''
def setCodec():
    '''returns JsonGenerator\n\n
    setCodec(final ObjectCodec oc)\n
    '''
def getCodec():
    '''returns ObjectCodec\n\n
    getCodec()\n
    '''
def getOutputContext():
    '''returns JsonStreamContext\n\n
    getOutputContext()\n
    '''
def writeStartObject():
    '''returns None\n\n
    writeStartObject(final Object forValue)\n
    '''
def writeFieldName():
    '''returns None\n\n
    writeFieldName(final SerializableString name)\n
    '''
def writeString():
    '''returns None\n\n
    writeString(final SerializableString text)\n
    '''
def writeRawValue():
    '''returns None\n\n
    writeRawValue(final String text)\n
    writeRawValue(final String text, final int offset, final int len)\n
    writeRawValue(final char[] text, final int offset, final int len)\n
    writeRawValue(final SerializableString text)\n
    '''
def writeBinary():
    '''returns int\n\n
    writeBinary(final Base64Variant b64variant, final InputStream data, final int dataLength)\n
    '''
def writeObject():
    '''returns None\n\n
    writeObject(final Object value)\n
    '''
def writeTree():
    '''returns None\n\n
    writeTree(final TreeNode rootNode)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
