sid = "short  49"
SS_NONE = "short  0"
SS_SUPER = "short  1"
SS_SUB = "short  2"
U_NONE = "byte  0"
U_SINGLE = "byte  1"
U_DOUBLE = "byte  2"
U_SINGLE_ACCOUNTING = "byte  33"
U_DOUBLE_ACCOUNTING = "byte  34"
def FontRecord():
    '''public FontRecord()
    public FontRecord(final RecordInputStream in)
    '''
def setFontHeight():
    '''public void setFontHeight(final short height)
    '''
def setAttributes():
    '''public void setAttributes(final short attributes)
    '''
def setItalic():
    '''public void setItalic(final boolean italics)
    '''
def setStrikeout():
    '''public void setStrikeout(final boolean strike)
    '''
def setMacoutline():
    '''public void setMacoutline(final boolean mac)
    '''
def setMacshadow():
    '''public void setMacshadow(final boolean mac)
    '''
def setColorPaletteIndex():
    '''public void setColorPaletteIndex(final short cpi)
    '''
def setBoldWeight():
    '''public void setBoldWeight(final short bw)
    '''
def setSuperSubScript():
    '''public void setSuperSubScript(final short sss)
    '''
def setUnderline():
    '''public void setUnderline(final byte u)
    '''
def setFamily():
    '''public void setFamily(final byte f)
    '''
def setCharset():
    '''public void setCharset(final byte charset)
    '''
def setFontName():
    '''public void setFontName(final String fn)
    '''
def getFontHeight():
    '''public short getFontHeight()
    '''
def getAttributes():
    '''public short getAttributes()
    '''
def isItalic():
    '''public boolean isItalic()
    '''
def isStruckout():
    '''public boolean isStruckout()
    '''
def isMacoutlined():
    '''public boolean isMacoutlined()
    '''
def isMacshadowed():
    '''public boolean isMacshadowed()
    '''
def getColorPaletteIndex():
    '''public short getColorPaletteIndex()
    '''
def getBoldWeight():
    '''public short getBoldWeight()
    '''
def getSuperSubScript():
    '''public short getSuperSubScript()
    '''
def getUnderline():
    '''public byte getUnderline()
    '''
def getFamily():
    '''public byte getFamily()
    '''
def getCharset():
    '''public byte getCharset()
    '''
def getFontName():
    '''public String getFontName()
    '''
def toString():
    '''public String toString()
    '''
def serialize():
    '''public void serialize(final LittleEndianOutput out)
    '''
def getSid():
    '''public short getSid()
    '''
def cloneStyleFrom():
    '''public void cloneStyleFrom(final FontRecord source)
    '''
def hashCode():
    '''public int hashCode()
    '''
def sameProperties():
    '''public boolean sameProperties(final FontRecord other)
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
