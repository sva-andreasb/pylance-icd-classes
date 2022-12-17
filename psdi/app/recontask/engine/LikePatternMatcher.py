LIKETOKEN_0ORMORE = "int  1"
LIKETOKEN_EXACTLY1 = "int  2"
LIKETOKEN_TEXT = "int  3"
def ():
    '''returns LikeToken\n\n
    (final String pattern)\n
    (final int type, final String text)\n
    '''
def match():
    '''returns boolean\n\n
    match(final String value)\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
    '''
def setText():
    '''returns None\n\n
    setText(final String text)\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def setType():
    '''returns None\n\n
    setType(final int type)\n
    '''
