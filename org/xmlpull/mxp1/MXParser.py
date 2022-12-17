def ():
    '''returns MXParser\n\n
    ()\n
    '''
def setFeature():
    '''returns None\n\n
    setFeature(final String name, final boolean state)\n
    '''
def getFeature():
    '''returns boolean\n\n
    getFeature(final String name)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String name, final Object value)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String name)\n
    '''
def setInput():
    '''returns None\n\n
    setInput(final Reader in)\n
    setInput(final InputStream inputStream, final String inputEncoding)\n
    '''
def getInputEncoding():
    '''returns String\n\n
    getInputEncoding()\n
    '''
def defineEntityReplacementText():
    '''returns None\n\n
    defineEntityReplacementText(final String entityName, final String replacementText)\n
    '''
def getNamespaceCount():
    '''returns int\n\n
    getNamespaceCount(final int depth)\n
    '''
def getNamespacePrefix():
    '''returns String\n\n
    getNamespacePrefix(final int pos)\n
    '''
def getNamespaceUri():
    '''returns String\n\n
    getNamespaceUri(final int pos)\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace(final String prefix)\n
    getNamespace()\n
    '''
def getDepth():
    '''returns int\n\n
    getDepth()\n
    '''
def getPositionDescription():
    '''returns String\n\n
    getPositionDescription()\n
    '''
def getLineNumber():
    '''returns int\n\n
    getLineNumber()\n
    '''
def getColumnNumber():
    '''returns int\n\n
    getColumnNumber()\n
    '''
def isWhitespace():
    '''returns boolean\n\n
    isWhitespace()\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
    '''
def getTextCharacters():
    '''returns char[]\n\n
    getTextCharacters(final int[] holderForStartAndLength)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix()\n
    '''
def isEmptyElementTag():
    '''returns boolean\n\n
    isEmptyElementTag()\n
    '''
def getAttributeCount():
    '''returns int\n\n
    getAttributeCount()\n
    '''
def getAttributeNamespace():
    '''returns String\n\n
    getAttributeNamespace(final int index)\n
    '''
def getAttributeName():
    '''returns String\n\n
    getAttributeName(final int index)\n
    '''
def getAttributePrefix():
    '''returns String\n\n
    getAttributePrefix(final int index)\n
    '''
def getAttributeType():
    '''returns String\n\n
    getAttributeType(final int index)\n
    '''
def isAttributeDefault():
    '''returns boolean\n\n
    isAttributeDefault(final int index)\n
    '''
def getAttributeValue():
    '''returns String\n\n
    getAttributeValue(final int index)\n
    getAttributeValue(String namespace, final String name)\n
    '''
def getEventType():
    '''returns int\n\n
    getEventType()\n
    '''
def require():
    '''returns None\n\n
    require(final int type, final String namespace, final String name)\n
    '''
def skipSubTree():
    '''returns None\n\n
    skipSubTree()\n
    '''
def nextText():
    '''returns String\n\n
    nextText()\n
    '''
def nextTag():
    '''returns int\n\n
    nextTag()\n
    '''
def next():
    '''returns int\n\n
    next()\n
    '''
def nextToken():
    '''returns int\n\n
    nextToken()\n
    '''
def parseEndTag():
    '''returns int\n\n
    parseEndTag()\n
    '''
def parseStartTag():
    '''returns int\n\n
    parseStartTag()\n
    '''
