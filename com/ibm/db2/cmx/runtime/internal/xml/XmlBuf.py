def ():
    '''returns XmlBuf\n\n
    (final int indent_)\n
    '''
def addElement():
    '''returns None\n\n
    addElement(final String str, final String s)\n
    addElement(final String str, final Map<String, String> map, final String s)\n
    addElement(final String s, final Integer obj)\n
    addElement(final String s, final Long obj)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String s)\n
    '''
def addAttrib():
    '''returns None\n\n
    addAttrib(final String str, final String s)\n
    addAttrib(final String s, final Integer obj)\n
    '''
def addText():
    '''returns None\n\n
    addText(final String s)\n
    addText(final Integer obj)\n
    '''
def endElement():
    '''returns None\n\n
    endElement()\n
    '''
def endElementSameLine():
    '''returns None\n\n
    endElementSameLine()\n
    '''
def addBranch():
    '''returns None\n\n
    addBranch(final String str)\n
    addBranch(final XmlExporter xmlExporter)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
