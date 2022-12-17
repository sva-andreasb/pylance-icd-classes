def setSchema():
    '''returns None\n\n
    setSchema(final FormatSchema schema)\n
    '''
def canUseSchema():
    '''returns boolean\n\n
    canUseSchema(final FormatSchema schema)\n
    '''
def version():
    '''returns Version\n\n
    version()\n
    '''
def getOutputTarget():
    '''returns Object\n\n
    getOutputTarget()\n
    '''
def configure():
    '''returns JsonGenerator\n\n
    configure(final Feature f, final boolean state)\n
    '''
def enableFeature():
    '''returns None\n\n
    enableFeature(final Feature f)\n
    '''
def disableFeature():
    '''returns None\n\n
    disableFeature(final Feature f)\n
    '''
def setFeature():
    '''returns None\n\n
    setFeature(final Feature f, final boolean state)\n
    '''
def isFeatureEnabled():
    '''returns boolean\n\n
    isFeatureEnabled(final Feature f)\n
    '''
def setPrettyPrinter():
    '''returns JsonGenerator\n\n
    setPrettyPrinter(final PrettyPrinter pp)\n
    '''
def setHighestNonEscapedChar():
    '''returns JsonGenerator\n\n
    setHighestNonEscapedChar(final int charCode)\n
    '''
def getHighestEscapedChar():
    '''returns int\n\n
    getHighestEscapedChar()\n
    '''
def getCharacterEscapes():
    '''returns CharacterEscapes\n\n
    getCharacterEscapes()\n
    '''
def setCharacterEscapes():
    '''returns JsonGenerator\n\n
    setCharacterEscapes(final CharacterEscapes esc)\n
    '''
def writeFieldName():
    '''returns None\n\n
    writeFieldName(final SerializedString name)\n
    writeFieldName(final SerializableString name)\n
    '''
def writeString():
    '''returns None\n\n
    writeString(final SerializableString text)\n
    '''
def writeBinary():
    '''returns None\n\n
    writeBinary(final byte[] data, final int offset, final int len)\n
    writeBinary(final byte[] data)\n
    '''
def writeStringField():
    '''returns None\n\n
    writeStringField(final String fieldName, final String value)\n
    '''
def enabledByDefault():
    '''returns boolean\n\n
    enabledByDefault()\n
    '''
def getMask():
    '''returns int\n\n
    getMask()\n
    '''
