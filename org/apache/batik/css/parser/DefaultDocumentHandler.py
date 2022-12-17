def startDocument():
    '''returns None\n\n
    startDocument(final InputSource source)\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument(final InputSource source)\n
    '''
def comment():
    '''returns None\n\n
    comment(final String text)\n
    '''
def ignorableAtRule():
    '''returns None\n\n
    ignorableAtRule(final String atRule)\n
    '''
def namespaceDeclaration():
    '''returns None\n\n
    namespaceDeclaration(final String prefix, final String uri)\n
    '''
def importStyle():
    '''returns None\n\n
    importStyle(final String uri, final SACMediaList media, final String defaultNamespaceURI)\n
    '''
def startMedia():
    '''returns None\n\n
    startMedia(final SACMediaList media)\n
    '''
def endMedia():
    '''returns None\n\n
    endMedia(final SACMediaList media)\n
    '''
def startPage():
    '''returns None\n\n
    startPage(final String name, final String pseudo_page)\n
    '''
def endPage():
    '''returns None\n\n
    endPage(final String name, final String pseudo_page)\n
    '''
def startFontFace():
    '''returns None\n\n
    startFontFace()\n
    '''
def endFontFace():
    '''returns None\n\n
    endFontFace()\n
    '''
def startSelector():
    '''returns None\n\n
    startSelector(final SelectorList selectors)\n
    '''
def endSelector():
    '''returns None\n\n
    endSelector(final SelectorList selectors)\n
    '''
def property():
    '''returns None\n\n
    property(final String name, final LexicalUnit value, final boolean important)\n
    '''
