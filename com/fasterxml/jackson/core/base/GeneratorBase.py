SURR1_FIRST = "int  55296"
SURR1_LAST = "int  56319"
SURR2_FIRST = "int  56320"
SURR2_LAST = "int  57343"
def version():
'''public Version version()
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
def isEnabled():
'''public final boolean isEnabled(final Feature f)
'''
pass
def getFeatureMask():
'''public int getFeatureMask()
'''
pass
def enable():
'''public JsonGenerator enable(final Feature f)
'''
pass
def disable():
'''public JsonGenerator disable(final Feature f)
'''
pass
def setFeatureMask():
'''public JsonGenerator setFeatureMask(final int newMask)
'''
pass
def overrideStdFeatures():
'''public JsonGenerator overrideStdFeatures(final int values, final int mask)
'''
pass
def useDefaultPrettyPrinter():
'''public JsonGenerator useDefaultPrettyPrinter()
'''
pass
def setCodec():
'''public JsonGenerator setCodec(final ObjectCodec oc)
'''
pass
def getCodec():
'''public ObjectCodec getCodec()
'''
pass
def getOutputContext():
'''public JsonStreamContext getOutputContext()
'''
pass
def writeStartObject():
'''public void writeStartObject(final Object forValue)
'''
pass
def writeFieldName():
'''public void writeFieldName(final SerializableString name)
'''
pass
def writeString():
'''public void writeString(final SerializableString text)
'''
pass
def writeRawValue():
'''public void writeRawValue(final String text)
public void writeRawValue(final String text, final int offset, final int len)
public void writeRawValue(final char[] text, final int offset, final int len)
public void writeRawValue(final SerializableString text)
'''
pass
def writeBinary():
'''public int writeBinary(final Base64Variant b64variant, final InputStream data, final int dataLength)
'''
pass
def writeObject():
'''public void writeObject(final Object value)
'''
pass
def writeTree():
'''public void writeTree(final TreeNode rootNode)
'''
pass
def close():
'''public void close()
'''
pass
def isClosed():
'''public boolean isClosed()
'''
pass
