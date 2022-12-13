BASECANVAS = "int  0"
BACKGROUNDCANVAS = "int  1"
LINECANVAS = "int  2"
TEXTCANVAS = "int  3"
def PdfPTable():
    '''    public PdfPTable(final float[] relativeWidths)
    public PdfPTable(final int numColumns)
    public PdfPTable(final PdfPTable table)
    '''
def shallowCopy():
    '''    public static PdfPTable shallowCopy(final PdfPTable table)
    '''
def setWidths():
    '''    public void setWidths(final float[] relativeWidths)
    public void setWidths(final int[] relativeWidths)
    '''
def setTotalWidth():
    '''    public void setTotalWidth(final float totalWidth)
    public void setTotalWidth(final float[] columnWidth)
    '''
def setWidthPercentage():
    '''    public void setWidthPercentage(final float[] columnWidth, final Rectangle pageSize)
    public void setWidthPercentage(final float widthPercentage)
    '''
def getTotalWidth():
    '''    public float getTotalWidth()
    '''
def calculateHeightsFast():
    '''    public void calculateHeightsFast()
    '''
def getDefaultCell():
    '''    public PdfPCell getDefaultCell()
    '''
def addCell():
    '''    public void addCell(final PdfPCell cell)
    public void addCell(final String text)
    public void addCell(final PdfPTable table)
    public void addCell(final Image image)
    public void addCell(final Phrase phrase)
    '''
def writeSelectedRows():
    '''    public float writeSelectedRows(final int rowStart, final int rowEnd, final float xPos, final float yPos, final PdfContentByte[] canvases)
    public float writeSelectedRows(int colStart, int colEnd, int rowStart, int rowEnd, final float xPos, float yPos, final PdfContentByte[] canvases)
    public float writeSelectedRows(final int rowStart, final int rowEnd, final float xPos, final float yPos, final PdfContentByte canvas)
    public float writeSelectedRows(int colStart, int colEnd, final int rowStart, final int rowEnd, final float xPos, final float yPos, final PdfContentByte canvas)
    '''
def beginWritingRows():
    '''    public static PdfContentByte[] beginWritingRows(final PdfContentByte canvas)
    '''
def endWritingRows():
    '''    public static void endWritingRows(final PdfContentByte[] canvases)
    '''
def size():
    '''    public int size()
    '''
def getTotalHeight():
    '''    public float getTotalHeight()
    '''
def getRowHeight():
    '''    public float getRowHeight(final int idx)
    '''
def getHeaderHeight():
    '''    public float getHeaderHeight()
    '''
def deleteRow():
    '''    public boolean deleteRow(final int rowNumber)
    '''
def deleteLastRow():
    '''    public boolean deleteLastRow()
    '''
def deleteBodyRows():
    '''    public void deleteBodyRows()
    '''
def getHeaderRows():
    '''    public int getHeaderRows()
    '''
def setHeaderRows():
    '''    public void setHeaderRows(int headerRows)
    '''
def getChunks():
    '''    public ArrayList getChunks()
    '''
def type():
    '''    public int type()
    '''
def process():
    '''    public boolean process(final ElementListener listener)
    '''
def getWidthPercentage():
    '''    public float getWidthPercentage()
    '''
def getHorizontalAlignment():
    '''    public int getHorizontalAlignment()
    '''
def setHorizontalAlignment():
    '''    public void setHorizontalAlignment(final int horizontalAlignment)
    '''
def getRow():
    '''    public PdfPRow getRow(final int idx)
    '''
def getRows():
    '''    public ArrayList getRows()
    '''
def setTableEvent():
    '''    public void setTableEvent(final PdfPTableEvent event)
    '''
def getTableEvent():
    '''    public PdfPTableEvent getTableEvent()
    '''
def getAbsoluteWidths():
    '''    public float[] getAbsoluteWidths()
    '''
def isSkipFirstHeader():
    '''    public boolean isSkipFirstHeader()
    '''
def setSkipFirstHeader():
    '''    public void setSkipFirstHeader(final boolean skipFirstHeader)
    '''
def setRunDirection():
    '''    public void setRunDirection(final int runDirection)
    '''
def getRunDirection():
    '''    public int getRunDirection()
    '''
def isLockedWidth():
    '''    public boolean isLockedWidth()
    '''
def setLockedWidth():
    '''    public void setLockedWidth(final boolean lockedWidth)
    '''
def isSplitRows():
    '''    public boolean isSplitRows()
    '''
def setSplitRows():
    '''    public void setSplitRows(final boolean splitRows)
    '''
def setSpacingBefore():
    '''    public void setSpacingBefore(final float spacing)
    '''
def setSpacingAfter():
    '''    public void setSpacingAfter(final float spacing)
    '''
def spacingBefore():
    '''    public float spacingBefore()
    '''
def spacingAfter():
    '''    public float spacingAfter()
    '''
def isExtendLastRow():
    '''    public boolean isExtendLastRow()
    '''
def setExtendLastRow():
    '''    public void setExtendLastRow(final boolean extendLastRow)
    '''
def isHeadersInEvent():
    '''    public boolean isHeadersInEvent()
    '''
def setHeadersInEvent():
    '''    public void setHeadersInEvent(final boolean headersInEvent)
    '''
def isSplitLate():
    '''    public boolean isSplitLate()
    '''
def setSplitLate():
    '''    public void setSplitLate(final boolean splitLate)
    '''
