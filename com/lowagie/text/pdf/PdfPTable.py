BASECANVAS = "int  0"
BACKGROUNDCANVAS = "int  1"
LINECANVAS = "int  2"
TEXTCANVAS = "int  3"
def PdfPTable():
'''public PdfPTable(final float[] relativeWidths)
public PdfPTable(final int numColumns)
public PdfPTable(final PdfPTable table)
'''
pass
def shallowCopy():
'''public static PdfPTable shallowCopy(final PdfPTable table)
'''
pass
def setWidths():
'''public void setWidths(final float[] relativeWidths)
public void setWidths(final int[] relativeWidths)
'''
pass
def setTotalWidth():
'''public void setTotalWidth(final float totalWidth)
public void setTotalWidth(final float[] columnWidth)
'''
pass
def setWidthPercentage():
'''public void setWidthPercentage(final float[] columnWidth, final Rectangle pageSize)
public void setWidthPercentage(final float widthPercentage)
'''
pass
def getTotalWidth():
'''public float getTotalWidth()
'''
pass
def calculateHeightsFast():
'''public void calculateHeightsFast()
'''
pass
def getDefaultCell():
'''public PdfPCell getDefaultCell()
'''
pass
def addCell():
'''public void addCell(final PdfPCell cell)
public void addCell(final String text)
public void addCell(final PdfPTable table)
public void addCell(final Image image)
public void addCell(final Phrase phrase)
'''
pass
def writeSelectedRows():
'''public float writeSelectedRows(final int rowStart, final int rowEnd, final float xPos, final float yPos, final PdfContentByte[] canvases)
public float writeSelectedRows(int colStart, int colEnd, int rowStart, int rowEnd, final float xPos, float yPos, final PdfContentByte[] canvases)
public float writeSelectedRows(final int rowStart, final int rowEnd, final float xPos, final float yPos, final PdfContentByte canvas)
public float writeSelectedRows(int colStart, int colEnd, final int rowStart, final int rowEnd, final float xPos, final float yPos, final PdfContentByte canvas)
'''
pass
def beginWritingRows():
'''public static PdfContentByte[] beginWritingRows(final PdfContentByte canvas)
'''
pass
def endWritingRows():
'''public static void endWritingRows(final PdfContentByte[] canvases)
'''
pass
def size():
'''public int size()
'''
pass
def getTotalHeight():
'''public float getTotalHeight()
'''
pass
def getRowHeight():
'''public float getRowHeight(final int idx)
'''
pass
def getHeaderHeight():
'''public float getHeaderHeight()
'''
pass
def deleteRow():
'''public boolean deleteRow(final int rowNumber)
'''
pass
def deleteLastRow():
'''public boolean deleteLastRow()
'''
pass
def deleteBodyRows():
'''public void deleteBodyRows()
'''
pass
def getHeaderRows():
'''public int getHeaderRows()
'''
pass
def setHeaderRows():
'''public void setHeaderRows(int headerRows)
'''
pass
def getChunks():
'''public ArrayList getChunks()
'''
pass
def type():
'''public int type()
'''
pass
def process():
'''public boolean process(final ElementListener listener)
'''
pass
def getWidthPercentage():
'''public float getWidthPercentage()
'''
pass
def getHorizontalAlignment():
'''public int getHorizontalAlignment()
'''
pass
def setHorizontalAlignment():
'''public void setHorizontalAlignment(final int horizontalAlignment)
'''
pass
def getRow():
'''public PdfPRow getRow(final int idx)
'''
pass
def getRows():
'''public ArrayList getRows()
'''
pass
def setTableEvent():
'''public void setTableEvent(final PdfPTableEvent event)
'''
pass
def getTableEvent():
'''public PdfPTableEvent getTableEvent()
'''
pass
def getAbsoluteWidths():
'''public float[] getAbsoluteWidths()
'''
pass
def isSkipFirstHeader():
'''public boolean isSkipFirstHeader()
'''
pass
def setSkipFirstHeader():
'''public void setSkipFirstHeader(final boolean skipFirstHeader)
'''
pass
def setRunDirection():
'''public void setRunDirection(final int runDirection)
'''
pass
def getRunDirection():
'''public int getRunDirection()
'''
pass
def isLockedWidth():
'''public boolean isLockedWidth()
'''
pass
def setLockedWidth():
'''public void setLockedWidth(final boolean lockedWidth)
'''
pass
def isSplitRows():
'''public boolean isSplitRows()
'''
pass
def setSplitRows():
'''public void setSplitRows(final boolean splitRows)
'''
pass
def setSpacingBefore():
'''public void setSpacingBefore(final float spacing)
'''
pass
def setSpacingAfter():
'''public void setSpacingAfter(final float spacing)
'''
pass
def spacingBefore():
'''public float spacingBefore()
'''
pass
def spacingAfter():
'''public float spacingAfter()
'''
pass
def isExtendLastRow():
'''public boolean isExtendLastRow()
'''
pass
def setExtendLastRow():
'''public void setExtendLastRow(final boolean extendLastRow)
'''
pass
def isHeadersInEvent():
'''public boolean isHeadersInEvent()
'''
pass
def setHeadersInEvent():
'''public void setHeadersInEvent(final boolean headersInEvent)
'''
pass
def isSplitLate():
'''public boolean isSplitLate()
'''
pass
def setSplitLate():
'''public void setSplitLate(final boolean splitLate)
'''
pass
