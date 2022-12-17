sid = "short  49"
SS_NONE = "short  0"
SS_SUPER = "short  1"
SS_SUB = "short  2"
U_NONE = "byte  0"
U_SINGLE = "byte  1"
U_DOUBLE = "byte  2"
U_SINGLE_ACCOUNTING = "byte  33"
U_DOUBLE_ACCOUNTING = "byte  34"
def ():
    '''returns FontRecord\n\n
    ()\n
    (final RecordInputStream in)\n
    '''
def setFontHeight():
    '''returns None\n\n
    setFontHeight(final short height)\n
    '''
def setAttributes():
    '''returns None\n\n
    setAttributes(final short attributes)\n
    '''
def setItalic():
    '''returns None\n\n
    setItalic(final boolean italics)\n
    '''
def setStrikeout():
    '''returns None\n\n
    setStrikeout(final boolean strike)\n
    '''
def setMacoutline():
    '''returns None\n\n
    setMacoutline(final boolean mac)\n
    '''
def setMacshadow():
    '''returns None\n\n
    setMacshadow(final boolean mac)\n
    '''
def setColorPaletteIndex():
    '''returns None\n\n
    setColorPaletteIndex(final short cpi)\n
    '''
def setBoldWeight():
    '''returns None\n\n
    setBoldWeight(final short bw)\n
    '''
def setSuperSubScript():
    '''returns None\n\n
    setSuperSubScript(final short sss)\n
    '''
def setUnderline():
    '''returns None\n\n
    setUnderline(final byte u)\n
    '''
def setFamily():
    '''returns None\n\n
    setFamily(final byte f)\n
    '''
def setCharset():
    '''returns None\n\n
    setCharset(final byte charset)\n
    '''
def setFontName():
    '''returns None\n\n
    setFontName(final String fn)\n
    '''
def getFontHeight():
    '''returns short\n\n
    getFontHeight()\n
    '''
def getAttributes():
    '''returns short\n\n
    getAttributes()\n
    '''
def isItalic():
    '''returns boolean\n\n
    isItalic()\n
    '''
def isStruckout():
    '''returns boolean\n\n
    isStruckout()\n
    '''
def isMacoutlined():
    '''returns boolean\n\n
    isMacoutlined()\n
    '''
def isMacshadowed():
    '''returns boolean\n\n
    isMacshadowed()\n
    '''
def getColorPaletteIndex():
    '''returns short\n\n
    getColorPaletteIndex()\n
    '''
def getBoldWeight():
    '''returns short\n\n
    getBoldWeight()\n
    '''
def getSuperSubScript():
    '''returns short\n\n
    getSuperSubScript()\n
    '''
def getUnderline():
    '''returns byte\n\n
    getUnderline()\n
    '''
def getFamily():
    '''returns byte\n\n
    getFamily()\n
    '''
def getCharset():
    '''returns byte\n\n
    getCharset()\n
    '''
def getFontName():
    '''returns String\n\n
    getFontName()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final LittleEndianOutput out)\n
    '''
def getSid():
    '''returns short\n\n
    getSid()\n
    '''
def cloneStyleFrom():
    '''returns None\n\n
    cloneStyleFrom(final FontRecord source)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def sameProperties():
    '''returns boolean\n\n
    sameProperties(final FontRecord other)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
