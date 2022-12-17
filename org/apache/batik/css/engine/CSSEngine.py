def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def getCSSContext():
    '''returns CSSContext\n\n
    getCSSContext()\n
    '''
def getDocument():
    '''returns Document\n\n
    getDocument()\n
    '''
def getFontSizeIndex():
    '''returns int\n\n
    getFontSizeIndex()\n
    '''
def getLineHeightIndex():
    '''returns int\n\n
    getLineHeightIndex()\n
    '''
def getColorIndex():
    '''returns int\n\n
    getColorIndex()\n
    '''
def getNumberOfProperties():
    '''returns int\n\n
    getNumberOfProperties()\n
    '''
def getPropertyIndex():
    '''returns int\n\n
    getPropertyIndex(final String name)\n
    '''
def getShorthandIndex():
    '''returns int\n\n
    getShorthandIndex(final String name)\n
    '''
def getPropertyName():
    '''returns String\n\n
    getPropertyName(final int idx)\n
    '''
def setCSSEngineUserAgent():
    '''returns None\n\n
    setCSSEngineUserAgent(final CSSEngineUserAgent userAgent)\n
    '''
def getCSSEngineUserAgent():
    '''returns CSSEngineUserAgent\n\n
    getCSSEngineUserAgent()\n
    '''
def setUserAgentStyleSheet():
    '''returns None\n\n
    setUserAgentStyleSheet(final StyleSheet ss)\n
    '''
def setUserStyleSheet():
    '''returns None\n\n
    setUserStyleSheet(final StyleSheet ss)\n
    '''
def getValueManagers():
    '''returns ValueManager[]\n\n
    getValueManagers()\n
    '''
def getShorthandManagers():
    '''returns ShorthandManager[]\n\n
    getShorthandManagers()\n
    '''
def getFontFaces():
    '''returns List\n\n
    getFontFaces()\n
    '''
def setMedia():
    '''returns None\n\n
    setMedia(final String str)\n
    '''
def setAlternateStyleSheet():
    '''returns None\n\n
    setAlternateStyleSheet(final String str)\n
    '''
def importCascadedStyleMaps():
    '''returns None\n\n
    importCascadedStyleMaps(final Element src, final CSSEngine srceng, final Element dest)\n
    '''
def getCSSBaseURI():
    '''returns ParsedURL\n\n
    getCSSBaseURI()\n
    '''
def getCascadedStyleMap():
    '''returns StyleMap\n\n
    getCascadedStyleMap(final CSSStylableElement elt, final String pseudo)\n
    '''
def property():
    '''returns None\n\n
    property(final String pname, final LexicalUnit lu, final boolean important)\n
    property(final String pname, final LexicalUnit lu, final boolean important)\n
    property(final String name, final LexicalUnit value, final boolean important)\n
    property(final String name, final LexicalUnit value, final boolean important)\n
    property(final String name, final LexicalUnit value, final boolean important)\n
    property(final String name, final LexicalUnit value, final boolean important)\n
    property(final String name, final LexicalUnit value, final boolean important)\n
    '''
def getComputedStyle():
    '''returns Value\n\n
    getComputedStyle(final CSSStylableElement elt, final String pseudo, final int propidx)\n
    '''
def getStyleSheetNodes():
    '''returns List\n\n
    getStyleSheetNodes()\n
    '''
def setMainProperties():
    '''returns None\n\n
    setMainProperties(final CSSStylableElement elt, final MainPropertyReceiver dst, final String pname, final String value, final boolean important)\n
    '''
def parsePropertyValue():
    '''returns Value\n\n
    parsePropertyValue(final CSSStylableElement elt, final String prop, final String value)\n
    '''
def parseStyleDeclaration():
    '''returns StyleDeclaration\n\n
    parseStyleDeclaration(final CSSStylableElement elt, final String value)\n
    '''
def parseStyleSheet():
    '''returns None\n\n
    parseStyleSheet(final ParsedURL uri, final String media)\n
    parseStyleSheet(final InputSource is, final ParsedURL uri, final String media)\n
    parseStyleSheet(final StyleSheet ss, final ParsedURL uri)\n
    parseStyleSheet(final String rules, final ParsedURL uri, final String media)\n
    parseStyleSheet(final StyleSheet ss, final String rules, final ParsedURL uri)\n
    '''
def addCSSEngineListener():
    '''returns None\n\n
    addCSSEngineListener(final CSSEngineListener l)\n
    '''
def removeCSSEngineListener():
    '''returns None\n\n
    removeCSSEngineListener(final CSSEngineListener l)\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument(final InputSource source)\n
    startDocument(final InputSource source)\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument(final InputSource source)\n
    endDocument(final InputSource source)\n
    '''
def ignorableAtRule():
    '''returns None\n\n
    ignorableAtRule(final String atRule)\n
    ignorableAtRule(final String atRule)\n
    '''
def importStyle():
    '''returns None\n\n
    importStyle(final String uri, final SACMediaList media, final String defaultNamespaceURI)\n
    importStyle(final String uri, final SACMediaList media, final String defaultNamespaceURI)\n
    '''
def startMedia():
    '''returns None\n\n
    startMedia(final SACMediaList media)\n
    startMedia(final SACMediaList media)\n
    '''
def endMedia():
    '''returns None\n\n
    endMedia(final SACMediaList media)\n
    endMedia(final SACMediaList media)\n
    '''
def startPage():
    '''returns None\n\n
    startPage(final String name, final String pseudo_page)\n
    startPage(final String name, final String pseudo_page)\n
    '''
def endPage():
    '''returns None\n\n
    endPage(final String name, final String pseudo_page)\n
    endPage(final String name, final String pseudo_page)\n
    '''
def startFontFace():
    '''returns None\n\n
    startFontFace()\n
    startFontFace()\n
    '''
def endFontFace():
    '''returns None\n\n
    endFontFace()\n
    endFontFace()\n
    '''
def startSelector():
    '''returns None\n\n
    startSelector(final SelectorList selectors)\n
    startSelector(final SelectorList selectors)\n
    '''
def endSelector():
    '''returns None\n\n
    endSelector(final SelectorList selectors)\n
    endSelector(final SelectorList selectors)\n
    '''
def comment():
    '''returns None\n\n
    comment(final String text)\n
    '''
def namespaceDeclaration():
    '''returns None\n\n
    namespaceDeclaration(final String prefix, final String uri)\n
    '''
def nodeInserted():
    '''returns None\n\n
    nodeInserted(final Node newNode)\n
    '''
def nodeToBeRemoved():
    '''returns None\n\n
    nodeToBeRemoved(final Node oldNode)\n
    '''
def subtreeModified():
    '''returns None\n\n
    subtreeModified(final Node rootOfModifications)\n
    '''
def characterDataModified():
    '''returns None\n\n
    characterDataModified(final Node text)\n
    '''
def attrModified():
    '''returns None\n\n
    attrModified(final Element e, final Attr attr, final short attrChange, final String prevValue, final String newValue)\n
    '''
def overrideStyleTextChanged():
    '''returns None\n\n
    overrideStyleTextChanged(final CSSStylableElement elt, final String text)\n
    '''
def overrideStylePropertyRemoved():
    '''returns None\n\n
    overrideStylePropertyRemoved(final CSSStylableElement elt, final String name)\n
    '''
def overrideStylePropertyChanged():
    '''returns None\n\n
    overrideStylePropertyChanged(final CSSStylableElement elt, final String name, final String val, final String prio)\n
    '''
def setMainProperty():
    '''returns None\n\n
    setMainProperty(final String name, final Value v, final boolean important)\n
    '''
def handleEvent():
    '''returns None\n\n
    handleEvent(final Event evt)\n
    handleEvent(final Event evt)\n
    handleEvent(final Event evt)\n
    handleEvent(final Event evt)\n
    handleEvent(final Event evt)\n
    '''
