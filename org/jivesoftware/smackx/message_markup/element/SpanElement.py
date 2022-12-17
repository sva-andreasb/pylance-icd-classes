ELEMENT = "String  \"span\""
emphasis = "String  \"emphasis\""
code = "String  \"code\""
deleted = "String  \"deleted\""
def ():
    '''returns SpanElement\n\n
    (final int start, final int end, final Set<SpanStyle> styles)\n
    '''
def getStart():
    '''returns int\n\n
    getStart()\n
    '''
def getEnd():
    '''returns int\n\n
    getEnd()\n
    '''
def getStyles():
    '''returns Set<SpanStyle>\n\n
    getStyles()\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    '''
