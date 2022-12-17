COURIER = "int  0"
HELVETICA = "int  1"
TIMES_ROMAN = "int  2"
SYMBOL = "int  3"
ZAPFDINGBATS = "int  4"
NORMAL = "int  0"
BOLD = "int  1"
ITALIC = "int  2"
UNDERLINE = "int  4"
STRIKETHRU = "int  8"
BOLDITALIC = "int  3"
UNDEFINED = "int  -1"
DEFAULTSIZE = "int  12"
def ():
    '''returns Font\n\n
    (final Font other)\n
    (final int family, final float size, final int style, final Color color)\n
    (final BaseFont bf, final float size, final int style, final Color color)\n
    (final BaseFont bf, final float size, final int style)\n
    (final BaseFont bf, final float size)\n
    (final BaseFont bf)\n
    (final int family, final float size, final int style)\n
    (final int family, final float size)\n
    (final int family)\n
    ()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Object object)\n
    '''
def setFamily():
    '''returns None\n\n
    setFamily(final String family)\n
    '''
def getFamilyname():
    '''returns String\n\n
    getFamilyname()\n
    '''
def setSize():
    '''returns None\n\n
    setSize(final float size)\n
    '''
def setStyle():
    '''returns None\n\n
    setStyle(final String style)\n
    setStyle(final int style)\n
    '''
def setColor():
    '''returns None\n\n
    setColor(final Color color)\n
    setColor(final int red, final int green, final int blue)\n
    '''
def leading():
    '''returns float\n\n
    leading(final float linespacing)\n
    '''
def isStandardFont():
    '''returns boolean\n\n
    isStandardFont()\n
    '''
def difference():
    '''returns Font\n\n
    difference(final Font font)\n
    '''
def family():
    '''returns int\n\n
    family()\n
    '''
def size():
    '''returns float\n\n
    size()\n
    '''
def style():
    '''returns int\n\n
    style()\n
    '''
def isBold():
    '''returns boolean\n\n
    isBold()\n
    '''
def isItalic():
    '''returns boolean\n\n
    isItalic()\n
    '''
def isUnderlined():
    '''returns boolean\n\n
    isUnderlined()\n
    '''
def isStrikethru():
    '''returns boolean\n\n
    isStrikethru()\n
    '''
def color():
    '''returns Color\n\n
    color()\n
    '''
def getBaseFont():
    '''returns BaseFont\n\n
    getBaseFont()\n
    '''
def getCalculatedBaseFont():
    '''returns BaseFont\n\n
    getCalculatedBaseFont(final boolean specialEncoding)\n
    '''
def getCalculatedStyle():
    '''returns int\n\n
    getCalculatedStyle()\n
    '''
def getCalculatedSize():
    '''returns float\n\n
    getCalculatedSize()\n
    '''
