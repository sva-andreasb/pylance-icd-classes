def ():
    '''returns AttributesImpl\n\n
    ()\n
    (final Attributes atts)\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def getURI():
    '''returns String\n\n
    getURI(final int index)\n
    '''
def getLocalName():
    '''returns String\n\n
    getLocalName(final int index)\n
    '''
def getQName():
    '''returns String\n\n
    getQName(final int index)\n
    '''
def getType():
    '''returns String\n\n
    getType(final int index)\n
    getType(final String uri, final String localName)\n
    getType(final String qName)\n
    '''
def getValue():
    '''returns String\n\n
    getValue(final int index)\n
    getValue(final String uri, final String localName)\n
    getValue(final String qName)\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex(final String uri, final String localName)\n
    getIndex(final String qName)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def setAttributes():
    '''returns None\n\n
    setAttributes(final Attributes atts)\n
    '''
def addAttribute():
    '''returns None\n\n
    addAttribute(final String uri, final String localName, final String qName, final String type, final String value)\n
    '''
def setAttribute():
    '''returns None\n\n
    setAttribute(final int index, final String uri, final String localName, final String qName, final String type, final String value)\n
    '''
def removeAttribute():
    '''returns None\n\n
    removeAttribute(final int index)\n
    '''
def setURI():
    '''returns None\n\n
    setURI(final int index, final String uri)\n
    '''
def setLocalName():
    '''returns None\n\n
    setLocalName(final int index, final String localName)\n
    '''
def setQName():
    '''returns None\n\n
    setQName(final int index, final String qName)\n
    '''
def setType():
    '''returns None\n\n
    setType(final int index, final String type)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final int index, final String value)\n
    '''
