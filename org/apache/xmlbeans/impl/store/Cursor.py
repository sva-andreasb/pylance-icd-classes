def dump():
    '''returns None\n\n
    dump(final PrintStream o)\n
    dump()\n
    '''
def _dispose():
    '''returns None\n\n
    _dispose()\n
    '''
def _newCursor():
    '''returns XmlCursor\n\n
    _newCursor()\n
    '''
def _getName():
    '''returns QName\n\n
    _getName()\n
    '''
def _setName():
    '''returns None\n\n
    _setName(final QName name)\n
    '''
def _currentTokenType():
    '''returns TokenType\n\n
    _currentTokenType()\n
    '''
def _isStartdoc():
    '''returns boolean\n\n
    _isStartdoc()\n
    '''
def _isEnddoc():
    '''returns boolean\n\n
    _isEnddoc()\n
    '''
def _isStart():
    '''returns boolean\n\n
    _isStart()\n
    '''
def _isEnd():
    '''returns boolean\n\n
    _isEnd()\n
    '''
def _isText():
    '''returns boolean\n\n
    _isText()\n
    '''
def _isAttr():
    '''returns boolean\n\n
    _isAttr()\n
    '''
def _isNamespace():
    '''returns boolean\n\n
    _isNamespace()\n
    '''
def _isComment():
    '''returns boolean\n\n
    _isComment()\n
    '''
def _isProcinst():
    '''returns boolean\n\n
    _isProcinst()\n
    '''
def _isContainer():
    '''returns boolean\n\n
    _isContainer()\n
    '''
def _isFinish():
    '''returns boolean\n\n
    _isFinish()\n
    '''
def _isAnyAttr():
    '''returns boolean\n\n
    _isAnyAttr()\n
    '''
def _toNextToken():
    '''returns TokenType\n\n
    _toNextToken()\n
    '''
def _toPrevToken():
    '''returns TokenType\n\n
    _toPrevToken()\n
    '''
def _monitor():
    '''returns Object\n\n
    _monitor()\n
    '''
def _toParent():
    '''returns boolean\n\n
    _toParent()\n
    '''
def _getDocChangeStamp():
    '''returns ChangeStamp\n\n
    _getDocChangeStamp()\n
    '''
def _newXMLInputStream():
    '''returns XMLInputStream\n\n
    _newXMLInputStream()\n
    _newXMLInputStream(final XmlOptions options)\n
    '''
def _newXMLStreamReader():
    '''returns XMLStreamReader\n\n
    _newXMLStreamReader()\n
    _newXMLStreamReader(final XmlOptions options)\n
    '''
def _newDomNode():
    '''returns Node\n\n
    _newDomNode()\n
    _newDomNode(XmlOptions options)\n
    '''
def _newInputStream():
    '''returns InputStream\n\n
    _newInputStream()\n
    _newInputStream(final XmlOptions options)\n
    '''
def _xmlText():
    '''returns String\n\n
    _xmlText()\n
    _xmlText(final XmlOptions options)\n
    '''
def _newReader():
    '''returns Reader\n\n
    _newReader()\n
    _newReader(final XmlOptions options)\n
    '''
def _save():
    '''returns None\n\n
    _save(final File file)\n
    _save(final OutputStream os)\n
    _save(final Writer w)\n
    _save(final ContentHandler ch, final LexicalHandler lh)\n
    _save(final ContentHandler ch, final LexicalHandler lh, final XmlOptions options)\n
    _save(final File file, final XmlOptions options)\n
    _save(final OutputStream os, final XmlOptions options)\n
    _save(final Writer w, final XmlOptions options)\n
    '''
def _documentProperties():
    '''returns XmlDocumentProperties\n\n
    _documentProperties()\n
    '''
def _getDomNode():
    '''returns Node\n\n
    _getDomNode()\n
    '''
def _toCursor():
    '''returns boolean\n\n
    _toCursor(final Cursor other)\n
    '''
def _push():
    '''returns None\n\n
    _push()\n
    '''
def _pop():
    '''returns boolean\n\n
    _pop()\n
    '''
def notifyChange():
    '''returns None\n\n
    notifyChange()\n
    '''
def setNextChangeListener():
    '''returns None\n\n
    setNextChangeListener(final Locale.ChangeListener listener)\n
    '''
def _selectPath():
    '''returns None\n\n
    _selectPath(final String path)\n
    _selectPath(final String pathExpr, final XmlOptions options)\n
    '''
def _hasNextSelection():
    '''returns boolean\n\n
    _hasNextSelection()\n
    '''
def _toNextSelection():
    '''returns boolean\n\n
    _toNextSelection()\n
    '''
def _toSelection():
    '''returns boolean\n\n
    _toSelection(final int i)\n
    '''
def _getSelectionCount():
    '''returns int\n\n
    _getSelectionCount()\n
    '''
def _addToSelection():
    '''returns None\n\n
    _addToSelection()\n
    '''
def _clearSelections():
    '''returns None\n\n
    _clearSelections()\n
    '''
def _namespaceForPrefix():
    '''returns String\n\n
    _namespaceForPrefix(final String prefix)\n
    '''
def _prefixForNamespace():
    '''returns String\n\n
    _prefixForNamespace(final String ns)\n
    '''
def _getAllNamespaces():
    '''returns None\n\n
    _getAllNamespaces(final Map addToThis)\n
    '''
def _getObject():
    '''returns XmlObject\n\n
    _getObject()\n
    '''
def _prevTokenType():
    '''returns TokenType\n\n
    _prevTokenType()\n
    '''
def _hasNextToken():
    '''returns boolean\n\n
    _hasNextToken()\n
    '''
def _hasPrevToken():
    '''returns boolean\n\n
    _hasPrevToken()\n
    '''
def _toFirstContentToken():
    '''returns TokenType\n\n
    _toFirstContentToken()\n
    '''
def _toEndToken():
    '''returns TokenType\n\n
    _toEndToken()\n
    '''
def _toChild():
    '''returns boolean\n\n
    _toChild(final String local)\n
    _toChild(final QName name)\n
    _toChild(final int index)\n
    _toChild(final String uri, final String local)\n
    _toChild(final QName name, final int index)\n
    '''
def _toNextChar():
    '''returns int\n\n
    _toNextChar(final int maxCharacterCount)\n
    '''
def _toPrevChar():
    '''returns int\n\n
    _toPrevChar(final int maxCharacterCount)\n
    '''
def _toPrevSibling():
    '''returns boolean\n\n
    _toPrevSibling()\n
    '''
def _toLastChild():
    '''returns boolean\n\n
    _toLastChild()\n
    '''
def _toFirstChild():
    '''returns boolean\n\n
    _toFirstChild()\n
    '''
def _toNextSibling():
    '''returns boolean\n\n
    _toNextSibling(final String name)\n
    _toNextSibling(final String uri, final String local)\n
    _toNextSibling(final QName name)\n
    '''
def _toFirstAttribute():
    '''returns boolean\n\n
    _toFirstAttribute()\n
    '''
def _toLastAttribute():
    '''returns boolean\n\n
    _toLastAttribute()\n
    '''
def _toNextAttribute():
    '''returns boolean\n\n
    _toNextAttribute()\n
    '''
def _toPrevAttribute():
    '''returns boolean\n\n
    _toPrevAttribute()\n
    '''
def _getAttributeText():
    '''returns String\n\n
    _getAttributeText(final QName attrName)\n
    '''
def _setAttributeText():
    '''returns boolean\n\n
    _setAttributeText(final QName attrName, final String value)\n
    '''
def _removeAttribute():
    '''returns boolean\n\n
    _removeAttribute(final QName attrName)\n
    '''
def _getTextValue():
    '''returns int\n\n
    _getTextValue()\n
    _getTextValue(final char[] chars, final int offset, int max)\n
    '''
def _setTextValue():
    '''returns None\n\n
    _setTextValue(String text)\n
    _setTextValue(final char[] sourceChars, final int offset, int length)\n
    '''
def _getChars():
    '''returns int\n\n
    _getChars()\n
    _getChars(final char[] buf, final int off, int cch)\n
    '''
def _toStartDoc():
    '''returns None\n\n
    _toStartDoc()\n
    '''
def _toEndDoc():
    '''returns None\n\n
    _toEndDoc()\n
    '''
def _comparePosition():
    '''returns int\n\n
    _comparePosition(final Cursor other)\n
    '''
def _isLeftOf():
    '''returns boolean\n\n
    _isLeftOf(final Cursor other)\n
    '''
def _isAtSamePositionAs():
    '''returns boolean\n\n
    _isAtSamePositionAs(final Cursor other)\n
    '''
def _isRightOf():
    '''returns boolean\n\n
    _isRightOf(final Cursor other)\n
    '''
def _execQuery():
    '''returns XmlCursor\n\n
    _execQuery(final String query)\n
    _execQuery(final String query, final XmlOptions options)\n
    '''
def _toBookmark():
    '''returns boolean\n\n
    _toBookmark(final XmlBookmark bookmark)\n
    '''
def _toNextBookmark():
    '''returns XmlBookmark\n\n
    _toNextBookmark(final Object key)\n
    '''
def _toPrevBookmark():
    '''returns XmlBookmark\n\n
    _toPrevBookmark(final Object key)\n
    '''
def _setBookmark():
    '''returns None\n\n
    _setBookmark(final XmlBookmark bookmark)\n
    '''
def _getBookmark():
    '''returns XmlBookmark\n\n
    _getBookmark(final Object key)\n
    '''
def _clearBookmark():
    '''returns None\n\n
    _clearBookmark(final Object key)\n
    '''
def _getAllBookmarkRefs():
    '''returns None\n\n
    _getAllBookmarkRefs(final Collection listToFill)\n
    '''
def _removeXml():
    '''returns boolean\n\n
    _removeXml()\n
    '''
def _moveXml():
    '''returns boolean\n\n
    _moveXml(final Cursor to)\n
    '''
def _copyXml():
    '''returns boolean\n\n
    _copyXml(final Cursor to)\n
    '''
def _removeXmlContents():
    '''returns boolean\n\n
    _removeXmlContents()\n
    '''
def _moveXmlContents():
    '''returns boolean\n\n
    _moveXmlContents(final Cursor to)\n
    '''
def _copyXmlContents():
    '''returns boolean\n\n
    _copyXmlContents(final Cursor to)\n
    '''
def _removeChars():
    '''returns int\n\n
    _removeChars(int cch)\n
    '''
def _moveChars():
    '''returns int\n\n
    _moveChars(int cch, final Cursor to)\n
    '''
def _copyChars():
    '''returns int\n\n
    _copyChars(int cch, final Cursor to)\n
    '''
def _insertChars():
    '''returns None\n\n
    _insertChars(final String text)\n
    '''
def _beginElement():
    '''returns None\n\n
    _beginElement(final String localName)\n
    _beginElement(final String localName, final String uri)\n
    _beginElement(final QName name)\n
    '''
def _insertElement():
    '''returns None\n\n
    _insertElement(final String localName)\n
    _insertElement(final String localName, final String uri)\n
    _insertElement(final QName name)\n
    '''
def _insertElementWithText():
    '''returns None\n\n
    _insertElementWithText(final String localName, final String text)\n
    _insertElementWithText(final String localName, final String uri, final String text)\n
    _insertElementWithText(final QName name, final String text)\n
    '''
def _insertAttribute():
    '''returns None\n\n
    _insertAttribute(final String localName)\n
    _insertAttribute(final String localName, final String uri)\n
    _insertAttribute(final QName name)\n
    '''
def _insertAttributeWithValue():
    '''returns None\n\n
    _insertAttributeWithValue(final String localName, final String value)\n
    _insertAttributeWithValue(final String localName, final String uri, final String value)\n
    _insertAttributeWithValue(final QName name, final String text)\n
    '''
def _insertNamespace():
    '''returns None\n\n
    _insertNamespace(final String prefix, final String namespace)\n
    '''
def _insertComment():
    '''returns None\n\n
    _insertComment(final String text)\n
    '''
def _insertProcInst():
    '''returns None\n\n
    _insertProcInst(final String target, final String text)\n
    '''
def _dump():
    '''returns None\n\n
    _dump()\n
    '''
def moveXml():
    '''returns boolean\n\n
    moveXml(final XmlCursor xTo)\n
    '''
def copyXml():
    '''returns boolean\n\n
    copyXml(final XmlCursor xTo)\n
    '''
def moveXmlContents():
    '''returns boolean\n\n
    moveXmlContents(final XmlCursor xTo)\n
    '''
def copyXmlContents():
    '''returns boolean\n\n
    copyXmlContents(final XmlCursor xTo)\n
    '''
def moveChars():
    '''returns int\n\n
    moveChars(final int cch, final XmlCursor xTo)\n
    '''
def copyChars():
    '''returns int\n\n
    copyChars(final int cch, final XmlCursor xTo)\n
    '''
def toCursor():
    '''returns boolean\n\n
    toCursor(final XmlCursor xOther)\n
    '''
def isInSameDocument():
    '''returns boolean\n\n
    isInSameDocument(final XmlCursor xOther)\n
    '''
def comparePosition():
    '''returns int\n\n
    comparePosition(final XmlCursor xOther)\n
    '''
def isLeftOf():
    '''returns boolean\n\n
    isLeftOf(final XmlCursor xOther)\n
    '''
def isAtSamePositionAs():
    '''returns boolean\n\n
    isAtSamePositionAs(final XmlCursor xOther)\n
    '''
def isRightOf():
    '''returns boolean\n\n
    isRightOf(final XmlCursor xOther)\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def monitor():
    '''returns Object\n\n
    monitor()\n
    '''
def documentProperties():
    '''returns XmlDocumentProperties\n\n
    documentProperties()\n
    '''
def newCursor():
    '''returns XmlCursor\n\n
    newCursor()\n
    '''
def newXMLStreamReader():
    '''returns XMLStreamReader\n\n
    newXMLStreamReader()\n
    newXMLStreamReader(final XmlOptions options)\n
    '''
def newXMLInputStream():
    '''returns XMLInputStream\n\n
    newXMLInputStream()\n
    newXMLInputStream(final XmlOptions options)\n
    '''
def xmlText():
    '''returns String\n\n
    xmlText()\n
    xmlText(final XmlOptions options)\n
    '''
def newInputStream():
    '''returns InputStream\n\n
    newInputStream()\n
    newInputStream(final XmlOptions options)\n
    '''
def newReader():
    '''returns Reader\n\n
    newReader()\n
    newReader(final XmlOptions options)\n
    '''
def newDomNode():
    '''returns Node\n\n
    newDomNode()\n
    newDomNode(final XmlOptions options)\n
    '''
def getDomNode():
    '''returns Node\n\n
    getDomNode()\n
    '''
def save():
    '''returns None\n\n
    save(final ContentHandler ch, final LexicalHandler lh)\n
    save(final File file)\n
    save(final OutputStream os)\n
    save(final Writer w)\n
    save(final ContentHandler ch, final LexicalHandler lh, final XmlOptions options)\n
    save(final File file, final XmlOptions options)\n
    save(final OutputStream os, final XmlOptions options)\n
    save(final Writer w, final XmlOptions options)\n
    '''
def push():
    '''returns None\n\n
    push()\n
    '''
def pop():
    '''returns boolean\n\n
    pop()\n
    '''
def selectPath():
    '''returns None\n\n
    selectPath(final String path)\n
    selectPath(final String path, final XmlOptions options)\n
    '''
def hasNextSelection():
    '''returns boolean\n\n
    hasNextSelection()\n
    '''
def toNextSelection():
    '''returns boolean\n\n
    toNextSelection()\n
    '''
def toSelection():
    '''returns boolean\n\n
    toSelection(final int i)\n
    '''
def getSelectionCount():
    '''returns int\n\n
    getSelectionCount()\n
    '''
def addToSelection():
    '''returns None\n\n
    addToSelection()\n
    '''
def clearSelections():
    '''returns None\n\n
    clearSelections()\n
    '''
def toBookmark():
    '''returns boolean\n\n
    toBookmark(final XmlBookmark bookmark)\n
    '''
def toNextBookmark():
    '''returns XmlBookmark\n\n
    toNextBookmark(final Object key)\n
    '''
def toPrevBookmark():
    '''returns XmlBookmark\n\n
    toPrevBookmark(final Object key)\n
    '''
def getName():
    '''returns QName\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final QName name)\n
    '''
def namespaceForPrefix():
    '''returns String\n\n
    namespaceForPrefix(final String prefix)\n
    '''
def prefixForNamespace():
    '''returns String\n\n
    prefixForNamespace(final String namespaceURI)\n
    '''
def getAllNamespaces():
    '''returns None\n\n
    getAllNamespaces(final Map addToThis)\n
    '''
def getObject():
    '''returns XmlObject\n\n
    getObject()\n
    '''
def currentTokenType():
    '''returns TokenType\n\n
    currentTokenType()\n
    '''
def isStartdoc():
    '''returns boolean\n\n
    isStartdoc()\n
    '''
def isEnddoc():
    '''returns boolean\n\n
    isEnddoc()\n
    '''
def isStart():
    '''returns boolean\n\n
    isStart()\n
    '''
def isEnd():
    '''returns boolean\n\n
    isEnd()\n
    '''
def isText():
    '''returns boolean\n\n
    isText()\n
    '''
def isAttr():
    '''returns boolean\n\n
    isAttr()\n
    '''
def isNamespace():
    '''returns boolean\n\n
    isNamespace()\n
    '''
def isComment():
    '''returns boolean\n\n
    isComment()\n
    '''
def isProcinst():
    '''returns boolean\n\n
    isProcinst()\n
    '''
def isContainer():
    '''returns boolean\n\n
    isContainer()\n
    '''
def isFinish():
    '''returns boolean\n\n
    isFinish()\n
    '''
def isAnyAttr():
    '''returns boolean\n\n
    isAnyAttr()\n
    '''
def prevTokenType():
    '''returns TokenType\n\n
    prevTokenType()\n
    '''
def hasNextToken():
    '''returns boolean\n\n
    hasNextToken()\n
    '''
def hasPrevToken():
    '''returns boolean\n\n
    hasPrevToken()\n
    '''
def toNextToken():
    '''returns TokenType\n\n
    toNextToken()\n
    '''
def toPrevToken():
    '''returns TokenType\n\n
    toPrevToken()\n
    '''
def toFirstContentToken():
    '''returns TokenType\n\n
    toFirstContentToken()\n
    '''
def toEndToken():
    '''returns TokenType\n\n
    toEndToken()\n
    '''
def toNextChar():
    '''returns int\n\n
    toNextChar(final int cch)\n
    '''
def toPrevChar():
    '''returns int\n\n
    toPrevChar(final int cch)\n
    '''
def ___toNextSibling():
    '''returns boolean\n\n
    ___toNextSibling()\n
    '''
def toNextSibling():
    '''returns boolean\n\n
    toNextSibling()\n
    toNextSibling(final String name)\n
    toNextSibling(final String namespace, final String name)\n
    toNextSibling(final QName name)\n
    '''
def toPrevSibling():
    '''returns boolean\n\n
    toPrevSibling()\n
    '''
def toParent():
    '''returns boolean\n\n
    toParent()\n
    '''
def toFirstChild():
    '''returns boolean\n\n
    toFirstChild()\n
    '''
def toLastChild():
    '''returns boolean\n\n
    toLastChild()\n
    '''
def toChild():
    '''returns boolean\n\n
    toChild(final String name)\n
    toChild(final String namespace, final String name)\n
    toChild(final QName name)\n
    toChild(final int index)\n
    toChild(final QName name, final int index)\n
    '''
def toFirstAttribute():
    '''returns boolean\n\n
    toFirstAttribute()\n
    '''
def toLastAttribute():
    '''returns boolean\n\n
    toLastAttribute()\n
    '''
def toNextAttribute():
    '''returns boolean\n\n
    toNextAttribute()\n
    '''
def toPrevAttribute():
    '''returns boolean\n\n
    toPrevAttribute()\n
    '''
def getAttributeText():
    '''returns String\n\n
    getAttributeText(final QName attrName)\n
    '''
def setAttributeText():
    '''returns boolean\n\n
    setAttributeText(final QName attrName, final String value)\n
    '''
def removeAttribute():
    '''returns boolean\n\n
    removeAttribute(final QName attrName)\n
    '''
def getTextValue():
    '''returns int\n\n
    getTextValue()\n
    getTextValue(final char[] chars, final int offset, final int cch)\n
    '''
def setTextValue():
    '''returns None\n\n
    setTextValue(final String text)\n
    setTextValue(final char[] sourceChars, final int offset, final int length)\n
    '''
def getChars():
    '''returns int\n\n
    getChars()\n
    getChars(final char[] chars, final int offset, final int cch)\n
    '''
def toStartDoc():
    '''returns None\n\n
    toStartDoc()\n
    '''
def toEndDoc():
    '''returns None\n\n
    toEndDoc()\n
    '''
def execQuery():
    '''returns XmlCursor\n\n
    execQuery(final String query)\n
    execQuery(final String query, final XmlOptions options)\n
    '''
def getDocChangeStamp():
    '''returns ChangeStamp\n\n
    getDocChangeStamp()\n
    '''
def setBookmark():
    '''returns None\n\n
    setBookmark(final XmlBookmark bookmark)\n
    '''
def getBookmark():
    '''returns XmlBookmark\n\n
    getBookmark(final Object key)\n
    '''
def clearBookmark():
    '''returns None\n\n
    clearBookmark(final Object key)\n
    '''
def getAllBookmarkRefs():
    '''returns None\n\n
    getAllBookmarkRefs(final Collection listToFill)\n
    '''
def removeXml():
    '''returns boolean\n\n
    removeXml()\n
    '''
def removeXmlContents():
    '''returns boolean\n\n
    removeXmlContents()\n
    '''
def removeChars():
    '''returns int\n\n
    removeChars(final int cch)\n
    '''
def insertChars():
    '''returns None\n\n
    insertChars(final String text)\n
    '''
def insertElement():
    '''returns None\n\n
    insertElement(final QName name)\n
    insertElement(final String localName)\n
    insertElement(final String localName, final String uri)\n
    '''
def beginElement():
    '''returns None\n\n
    beginElement(final QName name)\n
    beginElement(final String localName)\n
    beginElement(final String localName, final String uri)\n
    '''
def insertElementWithText():
    '''returns None\n\n
    insertElementWithText(final QName name, final String text)\n
    insertElementWithText(final String localName, final String text)\n
    insertElementWithText(final String localName, final String uri, final String text)\n
    '''
def insertAttribute():
    '''returns None\n\n
    insertAttribute(final String localName)\n
    insertAttribute(final String localName, final String uri)\n
    insertAttribute(final QName name)\n
    '''
def insertAttributeWithValue():
    '''returns None\n\n
    insertAttributeWithValue(final String Name, final String value)\n
    insertAttributeWithValue(final String name, final String uri, final String value)\n
    insertAttributeWithValue(final QName name, final String value)\n
    '''
def insertNamespace():
    '''returns None\n\n
    insertNamespace(final String prefix, final String namespace)\n
    '''
def insertComment():
    '''returns None\n\n
    insertComment(final String text)\n
    '''
def insertProcInst():
    '''returns None\n\n
    insertProcInst(final String target, final String text)\n
    '''
def hasChanged():
    '''returns boolean\n\n
    hasChanged()\n
    '''
