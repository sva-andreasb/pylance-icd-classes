TYPE_AUTO = "int  0"
TYPE_INDEXED = "int  1"
TYPE_RGB = "int  2"
TYPE_THEMED = "int  3"
TYPE_UNSET = "int  4"
THEME_DARK_1 = "int  0"
THEME_LIGHT_1 = "int  1"
THEME_DARK_2 = "int  2"
THEME_LIGHT_2 = "int  3"
THEME_ACCENT_1 = "int  4"
THEME_ACCENT_2 = "int  5"
THEME_ACCENT_3 = "int  6"
THEME_ACCENT_4 = "int  7"
THEME_ACCENT_5 = "int  8"
THEME_ACCENT_6 = "int  9"
THEME_HYPERLINK = "int  10"
THEME_FOLLOWED_HYPERLINK = "int  11"
def ():
    '''returns ExtendedColor\n\n
    ()\n
    (final LittleEndianInput in)\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def setType():
    '''returns None\n\n
    setType(final int type)\n
    '''
def getColorIndex():
    '''returns int\n\n
    getColorIndex()\n
    '''
def setColorIndex():
    '''returns None\n\n
    setColorIndex(final int colorIndex)\n
    '''
def getRGBA():
    '''returns byte[]\n\n
    getRGBA()\n
    '''
def setRGBA():
    '''returns None\n\n
    setRGBA(final byte[] rgba)\n
    '''
def getThemeIndex():
    '''returns int\n\n
    getThemeIndex()\n
    '''
def setThemeIndex():
    '''returns None\n\n
    setThemeIndex(final int themeIndex)\n
    '''
def getTint():
    '''returns double\n\n
    getTint()\n
    '''
def setTint():
    '''returns None\n\n
    setTint(final double tint)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def clone():
    '''returns ExtendedColor\n\n
    clone()\n
    '''
def getDataLength():
    '''returns int\n\n
    getDataLength()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final LittleEndianOutput out)\n
    '''
