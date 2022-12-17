def ():
    '''returns ToXMLStream\n\n
    ()\n
    '''
def CopyFrom():
    '''returns None\n\n
    CopyFrom(final ToXMLStream xmlListener)\n
    '''
def startDocumentInternal():
    '''returns None\n\n
    startDocumentInternal()\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument()\n
    '''
def startPreserving():
    '''returns None\n\n
    startPreserving()\n
    '''
def endPreserving():
    '''returns None\n\n
    endPreserving()\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String target, final String data)\n
    '''
def entityReference():
    '''returns None\n\n
    entityReference(final String name)\n
    '''
def addUniqueAttribute():
    '''returns None\n\n
    addUniqueAttribute(final String name, final String value, final int flags)\n
    '''
def addAttribute():
    '''returns None\n\n
    addAttribute(final String uri, final String localName, String rawName, final String type, final String value, final boolean xslAttribute)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String elemName)\n
    '''
def namespaceAfterStartElement():
    '''returns None\n\n
    namespaceAfterStartElement(final String prefix, final String uri)\n
    '''
def reset():
    '''returns boolean\n\n
    reset()\n
    '''
