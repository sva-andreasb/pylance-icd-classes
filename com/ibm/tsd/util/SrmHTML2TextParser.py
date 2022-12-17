def ():
    '''returns SrmHTML2TextParser\n\n
    ()\n
    '''
def handleComment():
    '''returns None\n\n
    handleComment(final char[] data, final int pos)\n
    '''
def handleEndOfLineString():
    '''returns None\n\n
    handleEndOfLineString(final String eol)\n
    '''
def handleEndTag():
    '''returns None\n\n
    handleEndTag(final HTML.Tag tag, final int pos)\n
    '''
def handleError():
    '''returns None\n\n
    handleError(final String errorMsg, final int pos)\n
    '''
def handleSimpleTag():
    '''returns None\n\n
    handleSimpleTag(final HTML.Tag tag, final MutableAttributeSet a, final int pos)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def handleStartTag():
    '''returns None\n\n
    handleStartTag(final HTML.Tag tag, final MutableAttributeSet a, final int pos)\n
    '''
def moreRTEConversion():
    '''returns char[]\n\n
    moreRTEConversion(final char[] data)\n
    '''
def handleText():
    '''returns None\n\n
    handleText(char[] data, final int pos)\n
    '''
def getParser():
    '''returns Parser\n\n
    getParser()\n
    '''
