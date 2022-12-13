def setSchema():
    '''public void setSchema(final FormatSchema schema)
    '''
def canUseSchema():
    '''public boolean canUseSchema(final FormatSchema schema)
    '''
def version():
    '''public Version version()
    '''
def getOutputTarget():
    '''public Object getOutputTarget()
    '''
def configure():
    '''public JsonGenerator configure(final Feature f, final boolean state)
    '''
def enableFeature():
    '''public void enableFeature(final Feature f)
    '''
def disableFeature():
    '''public void disableFeature(final Feature f)
    '''
def setFeature():
    '''public void setFeature(final Feature f, final boolean state)
    '''
def isFeatureEnabled():
    '''public boolean isFeatureEnabled(final Feature f)
    '''
def setPrettyPrinter():
    '''public JsonGenerator setPrettyPrinter(final PrettyPrinter pp)
    '''
def setHighestNonEscapedChar():
    '''public JsonGenerator setHighestNonEscapedChar(final int charCode)
    '''
def getHighestEscapedChar():
    '''public int getHighestEscapedChar()
    '''
def getCharacterEscapes():
    '''public CharacterEscapes getCharacterEscapes()
    '''
def setCharacterEscapes():
    '''public JsonGenerator setCharacterEscapes(final CharacterEscapes esc)
    '''
def writeFieldName():
    '''public void writeFieldName(final SerializedString name)
    public void writeFieldName(final SerializableString name)
    '''
def writeString():
    '''public void writeString(final SerializableString text)
    '''
def writeBinary():
    '''public void writeBinary(final byte[] data, final int offset, final int len)
    public void writeBinary(final byte[] data)
    '''
def writeStringField():
    '''public void writeStringField(final String fieldName, final String value)
    '''
def writeBooleanField():
    '''public final void writeBooleanField(final String fieldName, final boolean value)
    '''
def writeNullField():
    '''public final void writeNullField(final String fieldName)
    '''
def writeNumberField():
    '''public final void writeNumberField(final String fieldName, final int value)
    public final void writeNumberField(final String fieldName, final long value)
    public final void writeNumberField(final String fieldName, final double value)
    public final void writeNumberField(final String fieldName, final float value)
    public final void writeNumberField(final String fieldName, final BigDecimal value)
    '''
def writeBinaryField():
    '''public final void writeBinaryField(final String fieldName, final byte[] data)
    '''
def writeArrayFieldStart():
    '''public final void writeArrayFieldStart(final String fieldName)
    '''
def writeObjectFieldStart():
    '''public final void writeObjectFieldStart(final String fieldName)
    '''
def writeObjectField():
    '''public final void writeObjectField(final String fieldName, final Object pojo)
    '''
def collectDefaults():
    '''public static int collectDefaults()
    '''
def enabledByDefault():
    '''public boolean enabledByDefault()
    '''
def getMask():
    '''public int getMask()
    '''
