BASECANVAS = "int  0"
BACKGROUNDCANVAS = "int  1"
LINECANVAS = "int  2"
TEXTCANVAS = "int  3"
def ():
    '''returns PdfPTable\n\n
    (final float[] relativeWidths)\n
    (final int numColumns)\n
    (final PdfPTable table)\n
    '''
def setWidths():
    '''returns None\n\n
    setWidths(final float[] relativeWidths)\n
    setWidths(final int[] relativeWidths)\n
    '''
def setTotalWidth():
    '''returns None\n\n
    setTotalWidth(final float totalWidth)\n
    setTotalWidth(final float[] columnWidth)\n
    '''
def setWidthPercentage():
    '''returns None\n\n
    setWidthPercentage(final float[] columnWidth, final Rectangle pageSize)\n
    setWidthPercentage(final float widthPercentage)\n
    '''
def getTotalWidth():
    '''returns float\n\n
    getTotalWidth()\n
    '''
def calculateHeightsFast():
    '''returns None\n\n
    calculateHeightsFast()\n
    '''
def getDefaultCell():
    '''returns PdfPCell\n\n
    getDefaultCell()\n
    '''
def addCell():
    '''returns None\n\n
    addCell(final PdfPCell cell)\n
    addCell(final String text)\n
    addCell(final PdfPTable table)\n
    addCell(final Image image)\n
    addCell(final Phrase phrase)\n
    '''
def writeSelectedRows():
    '''returns float\n\n
    writeSelectedRows(final int rowStart, final int rowEnd, final float xPos, final float yPos, final PdfContentByte[] canvases)\n
    writeSelectedRows(int colStart, int colEnd, int rowStart, int rowEnd, final float xPos, float yPos, final PdfContentByte[] canvases)\n
    writeSelectedRows(final int rowStart, final int rowEnd, final float xPos, final float yPos, final PdfContentByte canvas)\n
    writeSelectedRows(int colStart, int colEnd, final int rowStart, final int rowEnd, final float xPos, final float yPos, final PdfContentByte canvas)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def getTotalHeight():
    '''returns float\n\n
    getTotalHeight()\n
    '''
def getRowHeight():
    '''returns float\n\n
    getRowHeight(final int idx)\n
    '''
def getHeaderHeight():
    '''returns float\n\n
    getHeaderHeight()\n
    '''
def deleteRow():
    '''returns boolean\n\n
    deleteRow(final int rowNumber)\n
    '''
def deleteLastRow():
    '''returns boolean\n\n
    deleteLastRow()\n
    '''
def deleteBodyRows():
    '''returns None\n\n
    deleteBodyRows()\n
    '''
def getHeaderRows():
    '''returns int\n\n
    getHeaderRows()\n
    '''
def setHeaderRows():
    '''returns None\n\n
    setHeaderRows(int headerRows)\n
    '''
def getChunks():
    '''returns ArrayList\n\n
    getChunks()\n
    '''
def type():
    '''returns int\n\n
    type()\n
    '''
def process():
    '''returns boolean\n\n
    process(final ElementListener listener)\n
    '''
def getWidthPercentage():
    '''returns float\n\n
    getWidthPercentage()\n
    '''
def getHorizontalAlignment():
    '''returns int\n\n
    getHorizontalAlignment()\n
    '''
def setHorizontalAlignment():
    '''returns None\n\n
    setHorizontalAlignment(final int horizontalAlignment)\n
    '''
def getRow():
    '''returns PdfPRow\n\n
    getRow(final int idx)\n
    '''
def getRows():
    '''returns ArrayList\n\n
    getRows()\n
    '''
def setTableEvent():
    '''returns None\n\n
    setTableEvent(final PdfPTableEvent event)\n
    '''
def getTableEvent():
    '''returns PdfPTableEvent\n\n
    getTableEvent()\n
    '''
def getAbsoluteWidths():
    '''returns float[]\n\n
    getAbsoluteWidths()\n
    '''
def isSkipFirstHeader():
    '''returns boolean\n\n
    isSkipFirstHeader()\n
    '''
def setSkipFirstHeader():
    '''returns None\n\n
    setSkipFirstHeader(final boolean skipFirstHeader)\n
    '''
def setRunDirection():
    '''returns None\n\n
    setRunDirection(final int runDirection)\n
    '''
def getRunDirection():
    '''returns int\n\n
    getRunDirection()\n
    '''
def isLockedWidth():
    '''returns boolean\n\n
    isLockedWidth()\n
    '''
def setLockedWidth():
    '''returns None\n\n
    setLockedWidth(final boolean lockedWidth)\n
    '''
def isSplitRows():
    '''returns boolean\n\n
    isSplitRows()\n
    '''
def setSplitRows():
    '''returns None\n\n
    setSplitRows(final boolean splitRows)\n
    '''
def setSpacingBefore():
    '''returns None\n\n
    setSpacingBefore(final float spacing)\n
    '''
def setSpacingAfter():
    '''returns None\n\n
    setSpacingAfter(final float spacing)\n
    '''
def spacingBefore():
    '''returns float\n\n
    spacingBefore()\n
    '''
def spacingAfter():
    '''returns float\n\n
    spacingAfter()\n
    '''
def isExtendLastRow():
    '''returns boolean\n\n
    isExtendLastRow()\n
    '''
def setExtendLastRow():
    '''returns None\n\n
    setExtendLastRow(final boolean extendLastRow)\n
    '''
def isHeadersInEvent():
    '''returns boolean\n\n
    isHeadersInEvent()\n
    '''
def setHeadersInEvent():
    '''returns None\n\n
    setHeadersInEvent(final boolean headersInEvent)\n
    '''
def isSplitLate():
    '''returns boolean\n\n
    isSplitLate()\n
    '''
def setSplitLate():
    '''returns None\n\n
    setSplitLate(final boolean splitLate)\n
    '''
