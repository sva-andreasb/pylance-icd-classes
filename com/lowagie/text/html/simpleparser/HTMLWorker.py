tagsSupportedString = "String  \"ol ul li a pre font span br p div body table td th tr i b u sub sup em strong h1 h2 h3 h4 h5 h6\""
def ():
    '''returns HTMLWorker\n\n
    (final DocListener document)\n
    '''
def setStyleSheet():
    '''returns None\n\n
    setStyleSheet(final StyleSheet style)\n
    '''
def parse():
    '''returns None\n\n
    parse(final Reader reader)\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument()\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument()\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String tag, final HashMap h)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String tag)\n
    '''
def text():
    '''returns None\n\n
    text(final String str)\n
    '''
def add():
    '''returns boolean\n\n
    add(final Element element)\n
    add(final Watermark watermark)\n
    '''
def clearTextWrap():
    '''returns None\n\n
    clearTextWrap()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def newPage():
    '''returns boolean\n\n
    newPage()\n
    '''
def open():
    '''returns None\n\n
    open()\n
    '''
def removeWatermark():
    '''returns None\n\n
    removeWatermark()\n
    '''
def resetFooter():
    '''returns None\n\n
    resetFooter()\n
    '''
def resetHeader():
    '''returns None\n\n
    resetHeader()\n
    '''
def resetPageCount():
    '''returns None\n\n
    resetPageCount()\n
    '''
def setFooter():
    '''returns None\n\n
    setFooter(final HeaderFooter footer)\n
    '''
def setHeader():
    '''returns None\n\n
    setHeader(final HeaderFooter header)\n
    '''
def setMarginMirroring():
    '''returns boolean\n\n
    setMarginMirroring(final boolean marginMirroring)\n
    '''
def setMargins():
    '''returns boolean\n\n
    setMargins(final float marginLeft, final float marginRight, final float marginTop, final float marginBottom)\n
    '''
def setPageCount():
    '''returns None\n\n
    setPageCount(final int pageN)\n
    '''
def setPageSize():
    '''returns boolean\n\n
    setPageSize(final Rectangle pageSize)\n
    '''
