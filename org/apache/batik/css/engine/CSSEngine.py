def getCSSParentNode():
    '''public static Node getCSSParentNode(final Node n)
    '''
def getParentCSSStylableElement():
    '''public static CSSStylableElement getParentCSSStylableElement(final Element elt)
    '''
def dispose():
    '''public void dispose()
    '''
def getCSSContext():
    '''public CSSContext getCSSContext()
    '''
def getDocument():
    '''public Document getDocument()
    '''
def getFontSizeIndex():
    '''public int getFontSizeIndex()
    '''
def getLineHeightIndex():
    '''public int getLineHeightIndex()
    '''
def getColorIndex():
    '''public int getColorIndex()
    '''
def getNumberOfProperties():
    '''public int getNumberOfProperties()
    '''
def getPropertyIndex():
    '''public int getPropertyIndex(final String name)
    '''
def getShorthandIndex():
    '''public int getShorthandIndex(final String name)
    '''
def getPropertyName():
    '''public String getPropertyName(final int idx)
    '''
def setCSSEngineUserAgent():
    '''public void setCSSEngineUserAgent(final CSSEngineUserAgent userAgent)
    '''
def getCSSEngineUserAgent():
    '''public CSSEngineUserAgent getCSSEngineUserAgent()
    '''
def setUserAgentStyleSheet():
    '''public void setUserAgentStyleSheet(final StyleSheet ss)
    '''
def setUserStyleSheet():
    '''public void setUserStyleSheet(final StyleSheet ss)
    '''
def getValueManagers():
    '''public ValueManager[] getValueManagers()
    '''
def getShorthandManagers():
    '''public ShorthandManager[] getShorthandManagers()
    '''
def getFontFaces():
    '''public List getFontFaces()
    '''
def setMedia():
    '''public void setMedia(final String str)
    '''
def setAlternateStyleSheet():
    '''public void setAlternateStyleSheet(final String str)
    '''
def importCascadedStyleMaps():
    '''public void importCascadedStyleMaps(final Element src, final CSSEngine srceng, final Element dest)
    '''
def getCSSBaseURI():
    '''public ParsedURL getCSSBaseURI()
    '''
def getCascadedStyleMap():
    '''public StyleMap getCascadedStyleMap(final CSSStylableElement elt, final String pseudo)
    '''
def property():
    '''public void property(final String pname, final LexicalUnit lu, final boolean important)
    public void property(final String pname, final LexicalUnit lu, final boolean important)
    public void property(final String name, final LexicalUnit value, final boolean important)
    public void property(final String name, final LexicalUnit value, final boolean important)
    public void property(final String name, final LexicalUnit value, final boolean important)
    public void property(final String name, final LexicalUnit value, final boolean important)
    public void property(final String name, final LexicalUnit value, final boolean important)
    '''
def getComputedStyle():
    '''public Value getComputedStyle(final CSSStylableElement elt, final String pseudo, final int propidx)
    '''
def getStyleSheetNodes():
    '''public List getStyleSheetNodes()
    '''
def setMainProperties():
    '''public void setMainProperties(final CSSStylableElement elt, final MainPropertyReceiver dst, final String pname, final String value, final boolean important)
    '''
def parsePropertyValue():
    '''public Value parsePropertyValue(final CSSStylableElement elt, final String prop, final String value)
    '''
def parseStyleDeclaration():
    '''public StyleDeclaration parseStyleDeclaration(final CSSStylableElement elt, final String value)
    '''
def parseStyleSheet():
    '''public StyleSheet parseStyleSheet(final ParsedURL uri, final String media)
    public StyleSheet parseStyleSheet(final InputSource is, final ParsedURL uri, final String media)
    public void parseStyleSheet(final StyleSheet ss, final ParsedURL uri)
    public StyleSheet parseStyleSheet(final String rules, final ParsedURL uri, final String media)
    public void parseStyleSheet(final StyleSheet ss, final String rules, final ParsedURL uri)
    '''
def addCSSEngineListener():
    '''public void addCSSEngineListener(final CSSEngineListener l)
    '''
def removeCSSEngineListener():
    '''public void removeCSSEngineListener(final CSSEngineListener l)
    '''
def startDocument():
    '''public void startDocument(final InputSource source)
    public void startDocument(final InputSource source)
    '''
def endDocument():
    '''public void endDocument(final InputSource source)
    public void endDocument(final InputSource source)
    '''
def ignorableAtRule():
    '''public void ignorableAtRule(final String atRule)
    public void ignorableAtRule(final String atRule)
    '''
def importStyle():
    '''public void importStyle(final String uri, final SACMediaList media, final String defaultNamespaceURI)
    public void importStyle(final String uri, final SACMediaList media, final String defaultNamespaceURI)
    '''
def startMedia():
    '''public void startMedia(final SACMediaList media)
    public void startMedia(final SACMediaList media)
    '''
def endMedia():
    '''public void endMedia(final SACMediaList media)
    public void endMedia(final SACMediaList media)
    '''
def startPage():
    '''public void startPage(final String name, final String pseudo_page)
    public void startPage(final String name, final String pseudo_page)
    '''
def endPage():
    '''public void endPage(final String name, final String pseudo_page)
    public void endPage(final String name, final String pseudo_page)
    '''
def startFontFace():
    '''public void startFontFace()
    public void startFontFace()
    '''
def endFontFace():
    '''public void endFontFace()
    public void endFontFace()
    '''
def startSelector():
    '''public void startSelector(final SelectorList selectors)
    public void startSelector(final SelectorList selectors)
    '''
def endSelector():
    '''public void endSelector(final SelectorList selectors)
    public void endSelector(final SelectorList selectors)
    '''
def comment():
    '''public void comment(final String text)
    '''
def namespaceDeclaration():
    '''public void namespaceDeclaration(final String prefix, final String uri)
    '''
def nodeInserted():
    '''public void nodeInserted(final Node newNode)
    '''
def nodeToBeRemoved():
    '''public void nodeToBeRemoved(final Node oldNode)
    '''
def subtreeModified():
    '''public void subtreeModified(final Node rootOfModifications)
    '''
def characterDataModified():
    '''public void characterDataModified(final Node text)
    '''
def attrModified():
    '''public void attrModified(final Element e, final Attr attr, final short attrChange, final String prevValue, final String newValue)
    '''
def overrideStyleTextChanged():
    '''public void overrideStyleTextChanged(final CSSStylableElement elt, final String text)
    '''
def overrideStylePropertyRemoved():
    '''public void overrideStylePropertyRemoved(final CSSStylableElement elt, final String name)
    '''
def overrideStylePropertyChanged():
    '''public void overrideStylePropertyChanged(final CSSStylableElement elt, final String name, final String val, final String prio)
    '''
def setMainProperty():
    '''public void setMainProperty(final String name, final Value v, final boolean important)
    '''
def handleEvent():
    '''public void handleEvent(final Event evt)
    public void handleEvent(final Event evt)
    public void handleEvent(final Event evt)
    public void handleEvent(final Event evt)
    public void handleEvent(final Event evt)
    '''
