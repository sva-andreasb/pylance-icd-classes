def ():
    '''returns ExtendedParserWrapper\n\n
    (final Parser parser)\n
    '''
def getParserVersion():
    '''returns String\n\n
    getParserVersion()\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
    '''
def setDocumentHandler():
    '''returns None\n\n
    setDocumentHandler(final DocumentHandler handler)\n
    '''
def setSelectorFactory():
    '''returns None\n\n
    setSelectorFactory(final SelectorFactory selectorFactory)\n
    '''
def setConditionFactory():
    '''returns None\n\n
    setConditionFactory(final ConditionFactory conditionFactory)\n
    '''
def setErrorHandler():
    '''returns None\n\n
    setErrorHandler(final ErrorHandler handler)\n
    '''
def parseStyleSheet():
    '''returns None\n\n
    parseStyleSheet(final InputSource source)\n
    parseStyleSheet(final String uri)\n
    '''
def parseStyleDeclaration():
    '''returns None\n\n
    parseStyleDeclaration(final InputSource source)\n
    parseStyleDeclaration(final String source)\n
    '''
def parseRule():
    '''returns None\n\n
    parseRule(final InputSource source)\n
    parseRule(final String source)\n
    '''
def parseSelectors():
    '''returns SelectorList\n\n
    parseSelectors(final InputSource source)\n
    parseSelectors(final String source)\n
    '''
def parsePropertyValue():
    '''returns LexicalUnit\n\n
    parsePropertyValue(final InputSource source)\n
    parsePropertyValue(final String source)\n
    '''
def parsePriority():
    '''returns boolean\n\n
    parsePriority(final InputSource source)\n
    parsePriority(final String source)\n
    '''
def parseMedia():
    '''returns SACMediaList\n\n
    parseMedia(final String mediaText)\n
    '''
