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
pass
def setFontHeight():
'''public void setFontHeight(final short height)
'''
pass
def setAttributes():
'''public void setAttributes(final short attributes)
'''
pass
def setItalic():
'''public void setItalic(final boolean italics)
'''
pass
def setStrikeout():
'''public void setStrikeout(final boolean strike)
'''
pass
def setMacoutline():
'''public void setMacoutline(final boolean mac)
'''
pass
def setMacshadow():
'''public void setMacshadow(final boolean mac)
'''
pass
def setColorPaletteIndex():
'''public void setColorPaletteIndex(final short cpi)
'''
pass
def setBoldWeight():
'''public void setBoldWeight(final short bw)
'''
pass
def setSuperSubScript():
'''public void setSuperSubScript(final short sss)
'''
pass
def setUnderline():
'''public void setUnderline(final byte u)
'''
pass
def setFamily():
'''public void setFamily(final byte f)
'''
pass
def setCharset():
'''public void setCharset(final byte charset)
'''
pass
def setFontName():
'''public void setFontName(final String fn)
'''
pass
def getFontHeight():
'''public short getFontHeight()
'''
pass
def getAttributes():
'''public short getAttributes()
'''
pass
def isItalic():
'''public boolean isItalic()
'''
pass
def isStruckout():
'''public boolean isStruckout()
'''
pass
def isMacoutlined():
'''public boolean isMacoutlined()
'''
pass
def isMacshadowed():
'''public boolean isMacshadowed()
'''
pass
def getColorPaletteIndex():
'''public short getColorPaletteIndex()
'''
pass
def getBoldWeight():
'''public short getBoldWeight()
'''
pass
def getSuperSubScript():
'''public short getSuperSubScript()
'''
pass
def getUnderline():
'''public byte getUnderline()
'''
pass
def getFamily():
'''public byte getFamily()
'''
pass
def getCharset():
'''public byte getCharset()
'''
pass
def getFontName():
'''public String getFontName()
'''
pass
def toString():
'''public String toString()
'''
pass
def serialize():
'''public void serialize(final LittleEndianOutput out)
'''
pass
def getSid():
'''public short getSid()
'''
pass
def cloneStyleFrom():
'''public void cloneStyleFrom(final FontRecord source)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def sameProperties():
'''public boolean sameProperties(final FontRecord other)
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
