def ():
    '''returns XMLTracer\n\n
    (final PrintStream fPrintStream, final SymbolTable fSymbolTable)\n
    '''
def traceStartDocument():
    '''returns None\n\n
    traceStartDocument()\n
    '''
def traceEndDocument():
    '''returns None\n\n
    traceEndDocument()\n
    '''
def traceXMLDecl():
    '''returns None\n\n
    traceXMLDecl(final XMLString xmlString, final XMLString xmlString2, final XMLString xmlString3)\n
    '''
def traceTextDecl():
    '''returns None\n\n
    traceTextDecl(final XMLString xmlString, final XMLString xmlString2)\n
    '''
def traceEmptyElement():
    '''returns None\n\n
    traceEmptyElement(final QName qName, final NSDeclList list, final AttrList list2)\n
    '''
def traceStartElement():
    '''returns None\n\n
    traceStartElement(final QName qName, final NSDeclList list, final AttrList list2)\n
    '''
def traceLeafElement():
    '''returns None\n\n
    traceLeafElement(final QName qName, final NSDeclList list, final AttrList list2)\n
    '''
def traceEndElement():
    '''returns None\n\n
    traceEndElement(final QName qName, final NSDeclList list)\n
    '''
def traceCharacters():
    '''returns None\n\n
    traceCharacters(final XMLString xmlString)\n
    '''
def traceWhitespace():
    '''returns None\n\n
    traceWhitespace(final XMLString xmlString)\n
    '''
def traceCharacter():
    '''returns None\n\n
    traceCharacter(final int n)\n
    '''
def tracePredefinedEntity():
    '''returns None\n\n
    tracePredefinedEntity(final XMLString xmlString, final int n)\n
    '''
def traceProcessingInstruction():
    '''returns None\n\n
    traceProcessingInstruction(final XMLString xmlString, final XMLString xmlString2)\n
    '''
def traceComment():
    '''returns None\n\n
    traceComment(final XMLString xmlString)\n
    '''
def traceStartCDATASection():
    '''returns None\n\n
    traceStartCDATASection()\n
    '''
def traceEndCDATASection():
    '''returns None\n\n
    traceEndCDATASection()\n
    '''
def traceDoctype():
    '''returns None\n\n
    traceDoctype(final XMLString xmlString, final XMLString xmlString2, final XMLString xmlString3, final boolean b)\n
    '''
def traceStartEntity():
    '''returns None\n\n
    traceStartEntity(final XMLString xmlString)\n
    '''
def traceEndEntity():
    '''returns None\n\n
    traceEndEntity(final XMLString xmlString)\n
    '''
def traceEntityReference():
    '''returns None\n\n
    traceEntityReference(final XMLString xmlString)\n
    '''
def traceWarning():
    '''returns None\n\n
    traceWarning(final String s, final int n, final int n2, final XMLString[] array, final long i)\n
    '''
def traceRecoverableError():
    '''returns None\n\n
    traceRecoverableError(final String s, final int n, final int n2, final XMLString[] array, final long i)\n
    '''
def traceFatalError():
    '''returns None\n\n
    traceFatalError(final String s, final int n, final int n2, final XMLString[] array, final long i)\n
    '''
def traceExtension():
    '''returns None\n\n
    traceExtension(final Object o)\n
    '''
