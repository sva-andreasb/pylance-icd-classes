STYLE_NONE = "int  0"
STYLE_ITALIC = "int  1"
STYLE_BOLD = "int  2"
STYLE_UNDERLINE = "int  4"
STYLE_STRIKETHROUGH = "int  8"
def ():
    '''returns RtfFont\n\n
    (final String fontName)\n
    (final String fontName, final float size)\n
    (final String fontName, final float size, final int style)\n
    (final String fontName, final float size, final int style, final Color color)\n
    (final RtfDocument doc, final Font font)\n
    '''
def writeDefinition():
    '''returns byte[]\n\n
    writeDefinition()\n
    '''
def writeBegin():
    '''returns byte[]\n\n
    writeBegin()\n
    '''
def writeEnd():
    '''returns byte[]\n\n
    writeEnd()\n
    '''
def write():
    '''returns byte[]\n\n
    write()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def getFontName():
    '''returns String\n\n
    getFontName()\n
    '''
def getFamilyname():
    '''returns String\n\n
    getFamilyname()\n
    '''
def getFontSize():
    '''returns int\n\n
    getFontSize()\n
    '''
def getFontStyle():
    '''returns int\n\n
    getFontStyle()\n
    '''
def getFontNumber():
    '''returns int\n\n
    getFontNumber()\n
    '''
def setRtfDocument():
    '''returns None\n\n
    setRtfDocument(final RtfDocument doc)\n
    '''
def setInTable():
    '''returns None\n\n
    setInTable(final boolean inTable)\n
    '''
def setInHeader():
    '''returns None\n\n
    setInHeader(final boolean inHeader)\n
    '''
def difference():
    '''returns Font\n\n
    difference(final Font font)\n
    '''
