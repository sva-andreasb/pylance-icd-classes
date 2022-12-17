def ():
    '''returns XMLString\n\n
    ()\n
    (final int lineWidth)\n
    (final int lineWidth, final String temporaryFileName)\n
    (final int lineWidth, final String publicId, final String systemId)\n
    (final int lineWidth, final String publicId, final String systemId, final String temporaryFileName)\n
    '''
def setLineWidth():
    '''returns None\n\n
    setLineWidth(final int lineWidth)\n
    '''
def reset():
    '''returns None\n\n
    reset(final String publicId, final String systemId, final int lineWidth, final String temporaryFileName)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String name)\n
    '''
def saveNilElement():
    '''returns None\n\n
    saveNilElement(final String name)\n
    '''
def saveDataValueElement():
    '''returns None\n\n
    saveDataValueElement(final String name, final String content)\n
    '''
def setMixed():
    '''returns None\n\n
    setMixed(final boolean isMixed)\n
    '''
def setUnformatted():
    '''returns None\n\n
    setUnformatted(final boolean isUnformatted)\n
    '''
def addAttribute():
    '''returns None\n\n
    addAttribute(final String name, final String value)\n
    '''
def addAttributeNS():
    '''returns None\n\n
    addAttributeNS(final String prefix, final String localName, final String value)\n
    '''
def startAttribute():
    '''returns None\n\n
    startAttribute(final String name)\n
    '''
def addAttributeContent():
    '''returns None\n\n
    addAttributeContent(final String content)\n
    '''
def endAttribute():
    '''returns None\n\n
    endAttribute()\n
    '''
def endEmptyElement():
    '''returns None\n\n
    endEmptyElement()\n
    '''
def endContentElement():
    '''returns None\n\n
    endContentElement(final String content)\n
    '''
def endElement():
    '''returns None\n\n
    endElement()\n
    '''
def addText():
    '''returns None\n\n
    addText(final String newString)\n
    '''
def addCDATA():
    '''returns None\n\n
    addCDATA(final String newString)\n
    '''
def addComment():
    '''returns None\n\n
    addComment(final String newString)\n
    '''
def add():
    '''returns None\n\n
    add(final String newString)\n
    '''
def addLine():
    '''returns None\n\n
    addLine()\n
    '''
def mark():
    '''returns Object\n\n
    mark()\n
    '''
def resetToMark():
    '''returns None\n\n
    resetToMark(Object mark)\n
    '''
