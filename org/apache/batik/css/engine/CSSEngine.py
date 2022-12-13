def getCSSParentNode():
'''public static Node getCSSParentNode(final Node n)
'''
pass
def getParentCSSStylableElement():
'''public static CSSStylableElement getParentCSSStylableElement(final Element elt)
'''
pass
def dispose():
'''public void dispose()
'''
pass
def getCSSContext():
'''public CSSContext getCSSContext()
'''
pass
def getDocument():
'''public Document getDocument()
'''
pass
def getFontSizeIndex():
'''public int getFontSizeIndex()
'''
pass
def getLineHeightIndex():
'''public int getLineHeightIndex()
'''
pass
def getColorIndex():
'''public int getColorIndex()
'''
pass
def getNumberOfProperties():
'''public int getNumberOfProperties()
'''
pass
def getPropertyIndex():
'''public int getPropertyIndex(final String name)
'''
pass
def getShorthandIndex():
'''public int getShorthandIndex(final String name)
'''
pass
def getPropertyName():
'''public String getPropertyName(final int idx)
'''
pass
def setCSSEngineUserAgent():
'''public void setCSSEngineUserAgent(final CSSEngineUserAgent userAgent)
'''
pass
def getCSSEngineUserAgent():
'''public CSSEngineUserAgent getCSSEngineUserAgent()
'''
pass
def setUserAgentStyleSheet():
'''public void setUserAgentStyleSheet(final StyleSheet ss)
'''
pass
def setUserStyleSheet():
'''public void setUserStyleSheet(final StyleSheet ss)
'''
pass
def getValueManagers():
'''public ValueManager[] getValueManagers()
'''
pass
def getShorthandManagers():
'''public ShorthandManager[] getShorthandManagers()
'''
pass
def getFontFaces():
'''public List getFontFaces()
'''
pass
def setMedia():
'''public void setMedia(final String str)
'''
pass
def setAlternateStyleSheet():
'''public void setAlternateStyleSheet(final String str)
'''
pass
def importCascadedStyleMaps():
'''public void importCascadedStyleMaps(final Element src, final CSSEngine srceng, final Element dest)
'''
pass
def getCSSBaseURI():
'''public ParsedURL getCSSBaseURI()
'''
pass
def getCascadedStyleMap():
'''public StyleMap getCascadedStyleMap(final CSSStylableElement elt, final String pseudo)
'''
pass
def property():
'''public void property(final String pname, final LexicalUnit lu, final boolean important)
public void property(final String pname, final LexicalUnit lu, final boolean important)
public void property(final String name, final LexicalUnit value, final boolean important)
public void property(final String name, final LexicalUnit value, final boolean important)
public void property(final String name, final LexicalUnit value, final boolean important)
public void property(final String name, final LexicalUnit value, final boolean important)
public void property(final String name, final LexicalUnit value, final boolean important)
'''
pass
def getComputedStyle():
'''public Value getComputedStyle(final CSSStylableElement elt, final String pseudo, final int propidx)
'''
pass
def getStyleSheetNodes():
'''public List getStyleSheetNodes()
'''
pass
def setMainProperties():
'''public void setMainProperties(final CSSStylableElement elt, final MainPropertyReceiver dst, final String pname, final String value, final boolean important)
'''
pass
def parsePropertyValue():
'''public Value parsePropertyValue(final CSSStylableElement elt, final String prop, final String value)
'''
pass
def parseStyleDeclaration():
'''public StyleDeclaration parseStyleDeclaration(final CSSStylableElement elt, final String value)
'''
pass
def parseStyleSheet():
'''public StyleSheet parseStyleSheet(final ParsedURL uri, final String media)
public StyleSheet parseStyleSheet(final InputSource is, final ParsedURL uri, final String media)
public void parseStyleSheet(final StyleSheet ss, final ParsedURL uri)
public StyleSheet parseStyleSheet(final String rules, final ParsedURL uri, final String media)
public void parseStyleSheet(final StyleSheet ss, final String rules, final ParsedURL uri)
'''
pass
def addCSSEngineListener():
'''public void addCSSEngineListener(final CSSEngineListener l)
'''
pass
def removeCSSEngineListener():
'''public void removeCSSEngineListener(final CSSEngineListener l)
'''
pass
def startDocument():
'''public void startDocument(final InputSource source)
public void startDocument(final InputSource source)
'''
pass
def endDocument():
'''public void endDocument(final InputSource source)
public void endDocument(final InputSource source)
'''
pass
def ignorableAtRule():
'''public void ignorableAtRule(final String atRule)
public void ignorableAtRule(final String atRule)
'''
pass
def importStyle():
'''public void importStyle(final String uri, final SACMediaList media, final String defaultNamespaceURI)
public void importStyle(final String uri, final SACMediaList media, final String defaultNamespaceURI)
'''
pass
def startMedia():
'''public void startMedia(final SACMediaList media)
public void startMedia(final SACMediaList media)
'''
pass
def endMedia():
'''public void endMedia(final SACMediaList media)
public void endMedia(final SACMediaList media)
'''
pass
def startPage():
'''public void startPage(final String name, final String pseudo_page)
public void startPage(final String name, final String pseudo_page)
'''
pass
def endPage():
'''public void endPage(final String name, final String pseudo_page)
public void endPage(final String name, final String pseudo_page)
'''
pass
def startFontFace():
'''public void startFontFace()
public void startFontFace()
'''
pass
def endFontFace():
'''public void endFontFace()
public void endFontFace()
'''
pass
def startSelector():
'''public void startSelector(final SelectorList selectors)
public void startSelector(final SelectorList selectors)
'''
pass
def endSelector():
'''public void endSelector(final SelectorList selectors)
public void endSelector(final SelectorList selectors)
'''
pass
def comment():
'''public void comment(final String text)
'''
pass
def namespaceDeclaration():
'''public void namespaceDeclaration(final String prefix, final String uri)
'''
pass
def nodeInserted():
'''public void nodeInserted(final Node newNode)
'''
pass
def nodeToBeRemoved():
'''public void nodeToBeRemoved(final Node oldNode)
'''
pass
def subtreeModified():
'''public void subtreeModified(final Node rootOfModifications)
'''
pass
def characterDataModified():
'''public void characterDataModified(final Node text)
'''
pass
def attrModified():
'''public void attrModified(final Element e, final Attr attr, final short attrChange, final String prevValue, final String newValue)
'''
pass
def overrideStyleTextChanged():
'''public void overrideStyleTextChanged(final CSSStylableElement elt, final String text)
'''
pass
def overrideStylePropertyRemoved():
'''public void overrideStylePropertyRemoved(final CSSStylableElement elt, final String name)
'''
pass
def overrideStylePropertyChanged():
'''public void overrideStylePropertyChanged(final CSSStylableElement elt, final String name, final String val, final String prio)
'''
pass
def setMainProperty():
'''public void setMainProperty(final String name, final Value v, final boolean important)
'''
pass
def handleEvent():
'''public void handleEvent(final Event evt)
public void handleEvent(final Event evt)
public void handleEvent(final Event evt)
public void handleEvent(final Event evt)
public void handleEvent(final Event evt)
'''
pass
