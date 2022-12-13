def setSchema():
'''public void setSchema(final FormatSchema schema)
'''
pass
def canUseSchema():
'''public boolean canUseSchema(final FormatSchema schema)
'''
pass
def version():
'''public Version version()
'''
pass
def getOutputTarget():
'''public Object getOutputTarget()
'''
pass
def configure():
'''public JsonGenerator configure(final Feature f, final boolean state)
'''
pass
def enableFeature():
'''public void enableFeature(final Feature f)
'''
pass
def disableFeature():
'''public void disableFeature(final Feature f)
'''
pass
def setFeature():
'''public void setFeature(final Feature f, final boolean state)
'''
pass
def isFeatureEnabled():
'''public boolean isFeatureEnabled(final Feature f)
'''
pass
def setPrettyPrinter():
'''public JsonGenerator setPrettyPrinter(final PrettyPrinter pp)
'''
pass
def setHighestNonEscapedChar():
'''public JsonGenerator setHighestNonEscapedChar(final int charCode)
'''
pass
def getHighestEscapedChar():
'''public int getHighestEscapedChar()
'''
pass
def getCharacterEscapes():
'''public CharacterEscapes getCharacterEscapes()
'''
pass
def setCharacterEscapes():
'''public JsonGenerator setCharacterEscapes(final CharacterEscapes esc)
'''
pass
def writeFieldName():
'''public void writeFieldName(final SerializedString name)
public void writeFieldName(final SerializableString name)
'''
pass
def writeString():
'''public void writeString(final SerializableString text)
'''
pass
def writeBinary():
'''public void writeBinary(final byte[] data, final int offset, final int len)
public void writeBinary(final byte[] data)
'''
pass
def writeStringField():
'''public void writeStringField(final String fieldName, final String value)
'''
pass
def writeBooleanField():
'''public final void writeBooleanField(final String fieldName, final boolean value)
'''
pass
def writeNullField():
'''public final void writeNullField(final String fieldName)
'''
pass
def writeNumberField():
'''public final void writeNumberField(final String fieldName, final int value)
public final void writeNumberField(final String fieldName, final long value)
public final void writeNumberField(final String fieldName, final double value)
public final void writeNumberField(final String fieldName, final float value)
public final void writeNumberField(final String fieldName, final BigDecimal value)
'''
pass
def writeBinaryField():
'''public final void writeBinaryField(final String fieldName, final byte[] data)
'''
pass
def writeArrayFieldStart():
'''public final void writeArrayFieldStart(final String fieldName)
'''
pass
def writeObjectFieldStart():
'''public final void writeObjectFieldStart(final String fieldName)
'''
pass
def writeObjectField():
'''public final void writeObjectField(final String fieldName, final Object pojo)
'''
pass
def collectDefaults():
'''public static int collectDefaults()
'''
pass
def enabledByDefault():
'''public boolean enabledByDefault()
'''
pass
def getMask():
'''public int getMask()
'''
pass
