FORMAT_DOT = "int  1"
FORMAT_DASH_SPACE = "int  2"
ALL_LEVELS = "int  Integer.MAX_VALUE"
ASTM_Z_NOT_SUPPORTED = "String  \"Z\""
def ():
    '''returns UniFormatNumber\n\n
    (String value, final int level)\n
    (final int level, final HashMap<Integer, String> wbs)\n
    '''
def getLevel():
    '''returns int\n\n
    getLevel()\n
    '''
def getTitle():
    '''returns String\n\n
    getTitle()\n
    '''
def setTitle():
    '''returns None\n\n
    setTitle(final String title)\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
def format():
    '''returns String\n\n
    format()\n
    format(final int format, final boolean zeroPad)\n
    format(final int format, final boolean zeroPad, final int numberOfLevels)\n
    '''
