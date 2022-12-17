def ():
    '''returns XPointerHandler\n\n
    ()\n
    (final SymbolTable fSymbolTable, final XMLErrorHandler fErrorHandler, final XMLErrorReporter fxPointerErrorReporter)\n
    '''
def setDocumentHandler():
    '''returns None\n\n
    setDocumentHandler(final XMLDocumentHandler fDocumentHandler)\n
    '''
def parseXPointer():
    '''returns None\n\n
    parseXPointer(final String s)\n
    '''
def resolveXPointer():
    '''returns boolean\n\n
    resolveXPointer(final QName qName, final XMLAttributes xmlAttributes, final Augmentations augmentations, final int n)\n
    '''
def isFragmentResolved():
    '''returns boolean\n\n
    isFragmentResolved()\n
    '''
def isChildFragmentResolved():
    '''returns boolean\n\n
    isChildFragmentResolved()\n
    '''
def isXPointerResolved():
    '''returns boolean\n\n
    isXPointerResolved()\n
    '''
def getXPointerPart():
    '''returns XPointerPart\n\n
    getXPointerPart()\n
    '''
def getPointerParts():
    '''returns ArrayList\n\n
    getPointerParts()\n
    '''
def comment():
    '''returns None\n\n
    comment(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String s, final XMLString xmlString, final Augmentations augmentations)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final QName qName, final XMLAttributes xmlAttributes, final Augmentations augmentations)\n
    '''
def emptyElement():
    '''returns None\n\n
    emptyElement(final QName qName, final XMLAttributes xmlAttributes, final Augmentations augmentations)\n
    '''
def characters():
    '''returns None\n\n
    characters(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final QName qName, final Augmentations augmentations)\n
    '''
def startCDATA():
    '''returns None\n\n
    startCDATA(final Augmentations augmentations)\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA(final Augmentations augmentations)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String s, final Object o)\n
    '''
