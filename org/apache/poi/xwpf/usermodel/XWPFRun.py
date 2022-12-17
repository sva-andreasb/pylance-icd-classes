def ():
    '''returns XWPFRun\n\n
    (final CTR r, final IRunBody p)\n
    (final CTR r, final XWPFParagraph p)\n
    '''
def getCTR():
    '''returns CTR\n\n
    getCTR()\n
    '''
def getParent():
    '''returns IRunBody\n\n
    getParent()\n
    '''
def getParagraph():
    '''returns XWPFParagraph\n\n
    getParagraph()\n
    '''
def getDocument():
    '''returns XWPFDocument\n\n
    getDocument()\n
    '''
def isBold():
    '''returns boolean\n\n
    isBold()\n
    '''
def setBold():
    '''returns None\n\n
    setBold(final boolean value)\n
    '''
def getColor():
    '''returns String\n\n
    getColor()\n
    '''
def setColor():
    '''returns None\n\n
    setColor(final String rgbStr)\n
    '''
def getText():
    '''returns String\n\n
    getText(final int pos)\n
    '''
def getPictureText():
    '''returns String\n\n
    getPictureText()\n
    '''
def setText():
    '''returns None\n\n
    setText(final String value)\n
    setText(final String value, final int pos)\n
    '''
def isItalic():
    '''returns boolean\n\n
    isItalic()\n
    '''
def setItalic():
    '''returns None\n\n
    setItalic(final boolean value)\n
    '''
def getUnderline():
    '''returns UnderlinePatterns\n\n
    getUnderline()\n
    '''
def setUnderline():
    '''returns None\n\n
    setUnderline(final UnderlinePatterns value)\n
    '''
def isStrikeThrough():
    '''returns boolean\n\n
    isStrikeThrough()\n
    '''
def setStrikeThrough():
    '''returns None\n\n
    setStrikeThrough(final boolean value)\n
    '''
def isStrike():
    '''returns boolean\n\n
    isStrike()\n
    '''
def setStrike():
    '''returns None\n\n
    setStrike(final boolean value)\n
    '''
def isDoubleStrikeThrough():
    '''returns boolean\n\n
    isDoubleStrikeThrough()\n
    '''
def setDoubleStrikethrough():
    '''returns None\n\n
    setDoubleStrikethrough(final boolean value)\n
    '''
def isSmallCaps():
    '''returns boolean\n\n
    isSmallCaps()\n
    '''
def setSmallCaps():
    '''returns None\n\n
    setSmallCaps(final boolean value)\n
    '''
def isCapitalized():
    '''returns boolean\n\n
    isCapitalized()\n
    '''
def setCapitalized():
    '''returns None\n\n
    setCapitalized(final boolean value)\n
    '''
def isShadowed():
    '''returns boolean\n\n
    isShadowed()\n
    '''
def setShadow():
    '''returns None\n\n
    setShadow(final boolean value)\n
    '''
def isImprinted():
    '''returns boolean\n\n
    isImprinted()\n
    '''
def setImprinted():
    '''returns None\n\n
    setImprinted(final boolean value)\n
    '''
def isEmbossed():
    '''returns boolean\n\n
    isEmbossed()\n
    '''
def setEmbossed():
    '''returns None\n\n
    setEmbossed(final boolean value)\n
    '''
def getSubscript():
    '''returns VerticalAlign\n\n
    getSubscript()\n
    '''
def setSubscript():
    '''returns None\n\n
    setSubscript(final VerticalAlign valign)\n
    '''
def getKerning():
    '''returns int\n\n
    getKerning()\n
    '''
def setKerning():
    '''returns None\n\n
    setKerning(final int kern)\n
    '''
def isHighlighted():
    '''returns boolean\n\n
    isHighlighted()\n
    '''
def getCharacterSpacing():
    '''returns int\n\n
    getCharacterSpacing()\n
    '''
def setCharacterSpacing():
    '''returns None\n\n
    setCharacterSpacing(final int twips)\n
    '''
def getFontFamily():
    '''returns String\n\n
    getFontFamily()\n
    getFontFamily(final FontCharRange fcr)\n
    '''
def setFontFamily():
    '''returns None\n\n
    setFontFamily(final String fontFamily)\n
    setFontFamily(final String fontFamily, final FontCharRange fcr)\n
    '''
def getFontName():
    '''returns String\n\n
    getFontName()\n
    '''
def getFontSize():
    '''returns int\n\n
    getFontSize()\n
    '''
def setFontSize():
    '''returns None\n\n
    setFontSize(final int size)\n
    '''
def getTextPosition():
    '''returns int\n\n
    getTextPosition()\n
    '''
def setTextPosition():
    '''returns None\n\n
    setTextPosition(final int val)\n
    '''
def removeBreak():
    '''returns None\n\n
    removeBreak()\n
    '''
def addBreak():
    '''returns None\n\n
    addBreak()\n
    addBreak(final BreakType type)\n
    addBreak(final BreakClear clear)\n
    '''
def addTab():
    '''returns None\n\n
    addTab()\n
    '''
def removeTab():
    '''returns None\n\n
    removeTab()\n
    '''
def addCarriageReturn():
    '''returns None\n\n
    addCarriageReturn()\n
    '''
def removeCarriageReturn():
    '''returns None\n\n
    removeCarriageReturn()\n
    '''
def addPicture():
    '''returns XWPFPicture\n\n
    addPicture(final InputStream pictureData, final int pictureType, final String filename, final int width, final int height)\n
    '''
def getEmbeddedPictures():
    '''returns List<XWPFPicture>\n\n
    getEmbeddedPictures()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def text():
    '''returns String\n\n
    text()\n
    '''
def getPhonetic():
    '''returns String\n\n
    getPhonetic()\n
    '''
