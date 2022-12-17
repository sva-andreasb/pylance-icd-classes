sid = "short  4103"
LINE_PATTERN_SOLID = "short  0"
LINE_PATTERN_DASH = "short  1"
LINE_PATTERN_DOT = "short  2"
LINE_PATTERN_DASH_DOT = "short  3"
LINE_PATTERN_DASH_DOT_DOT = "short  4"
LINE_PATTERN_NONE = "short  5"
LINE_PATTERN_DARK_GRAY_PATTERN = "short  6"
LINE_PATTERN_MEDIUM_GRAY_PATTERN = "short  7"
LINE_PATTERN_LIGHT_GRAY_PATTERN = "short  8"
WEIGHT_HAIRLINE = "short  -1"
WEIGHT_NARROW = "short  0"
WEIGHT_MEDIUM = "short  1"
WEIGHT_WIDE = "short  2"
def ():
    '''returns LineFormatRecord\n\n
    ()\n
    (final RecordInputStream in)\n
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
def clone():
    '''returns LineFormatRecord\n\n
    clone()\n
    '''
def getLineColor():
    '''returns int\n\n
    getLineColor()\n
    '''
def setLineColor():
    '''returns None\n\n
    setLineColor(final int field_1_lineColor)\n
    '''
def getLinePattern():
    '''returns short\n\n
    getLinePattern()\n
    '''
def setLinePattern():
    '''returns None\n\n
    setLinePattern(final short field_2_linePattern)\n
    '''
def getWeight():
    '''returns short\n\n
    getWeight()\n
    '''
def setWeight():
    '''returns None\n\n
    setWeight(final short field_3_weight)\n
    '''
def getFormat():
    '''returns short\n\n
    getFormat()\n
    '''
def setFormat():
    '''returns None\n\n
    setFormat(final short field_4_format)\n
    '''
def getColourPaletteIndex():
    '''returns short\n\n
    getColourPaletteIndex()\n
    '''
def setColourPaletteIndex():
    '''returns None\n\n
    setColourPaletteIndex(final short field_5_colourPaletteIndex)\n
    '''
def setAuto():
    '''returns None\n\n
    setAuto(final boolean value)\n
    '''
def isAuto():
    '''returns boolean\n\n
    isAuto()\n
    '''
def setDrawTicks():
    '''returns None\n\n
    setDrawTicks(final boolean value)\n
    '''
def isDrawTicks():
    '''returns boolean\n\n
    isDrawTicks()\n
    '''
def setUnknown():
    '''returns None\n\n
    setUnknown(final boolean value)\n
    '''
def isUnknown():
    '''returns boolean\n\n
    isUnknown()\n
    '''
