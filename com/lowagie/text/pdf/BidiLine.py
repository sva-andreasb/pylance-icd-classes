def ():
    '''returns BidiLine\n\n
    ()\n
    (final BidiLine org)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def clearChunks():
    '''returns None\n\n
    clearChunks()\n
    '''
def getParagraph():
    '''returns boolean\n\n
    getParagraph(final int runDirection)\n
    '''
def addChunk():
    '''returns None\n\n
    addChunk(final PdfChunk chunk)\n
    '''
def addChunks():
    '''returns None\n\n
    addChunks(final ArrayList chunks)\n
    '''
def addPiece():
    '''returns None\n\n
    addPiece(final char c, final PdfChunk chunk)\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def restore():
    '''returns None\n\n
    restore()\n
    '''
def mirrorGlyphs():
    '''returns None\n\n
    mirrorGlyphs()\n
    '''
def doArabicShapping():
    '''returns None\n\n
    doArabicShapping()\n
    '''
def processLine():
    '''returns PdfLine\n\n
    processLine(float width, final int alignment, final int runDirection, final int arabicOptions)\n
    '''
def getWidth():
    '''returns float\n\n
    getWidth(int startIdx, final int lastIdx)\n
    '''
def createArrayOfPdfChunks():
    '''returns ArrayList\n\n
    createArrayOfPdfChunks(final int startIdx, final int endIdx)\n
    createArrayOfPdfChunks(int startIdx, final int endIdx, final PdfChunk extraPdfChunk)\n
    '''
def getWord():
    '''returns int[]\n\n
    getWord(final int startIdx, final int idx)\n
    '''
def trimRight():
    '''returns int\n\n
    trimRight(final int startIdx, final int endIdx)\n
    '''
def trimLeft():
    '''returns int\n\n
    trimLeft(final int startIdx, final int endIdx)\n
    '''
def trimRightEx():
    '''returns int\n\n
    trimRightEx(final int startIdx, final int endIdx)\n
    '''
def trimLeftEx():
    '''returns int\n\n
    trimLeftEx(final int startIdx, final int endIdx)\n
    '''
def reorder():
    '''returns None\n\n
    reorder(final int start, final int end)\n
    '''
def flip():
    '''returns None\n\n
    flip(int start, int end)\n
    '''
