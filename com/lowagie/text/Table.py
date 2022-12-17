def ():
    '''returns Table\n\n
    (final int columns)\n
    (final int columns, final int rows)\n
    (final Properties attributes)\n
    '''
def process():
    '''returns boolean\n\n
    process(final ElementListener listener)\n
    '''
def setDebug():
    '''returns None\n\n
    setDebug(final boolean aDebug)\n
    '''
def setDefaultLayout():
    '''returns None\n\n
    setDefaultLayout(final Cell value)\n
    '''
def setAutoFillEmptyCells():
    '''returns None\n\n
    setAutoFillEmptyCells(final boolean aDoAutoFill)\n
    '''
def setTableFitsPage():
    '''returns None\n\n
    setTableFitsPage(final boolean fitPage)\n
    '''
def setCellsFitPage():
    '''returns None\n\n
    setCellsFitPage(final boolean fitPage)\n
    '''
def hasToFitPageTable():
    '''returns boolean\n\n
    hasToFitPageTable()\n
    '''
def hasToFitPageCells():
    '''returns boolean\n\n
    hasToFitPageCells()\n
    '''
def setOffset():
    '''returns None\n\n
    setOffset(final float offset)\n
    '''
def getOffset():
    '''returns float\n\n
    getOffset()\n
    '''
def type():
    '''returns int\n\n
    type()\n
    '''
def getChunks():
    '''returns ArrayList\n\n
    getChunks()\n
    '''
def addCell():
    '''returns None\n\n
    addCell(final Cell aCell, final int row, final int column)\n
    addCell(final Cell aCell, final Point aLocation)\n
    addCell(final Cell cell)\n
    addCell(final Phrase content)\n
    addCell(final Phrase content, final Point location)\n
    addCell(final String content)\n
    addCell(final String content, final Point location)\n
    '''
def insertTable():
    '''returns None\n\n
    insertTable(final Table aTable)\n
    insertTable(final Table aTable, final int row, final int column)\n
    insertTable(final Table aTable, final Point aLocation)\n
    '''
def complete():
    '''returns None\n\n
    complete()\n
    '''
def setDefaultCellBorder():
    '''returns None\n\n
    setDefaultCellBorder(final int value)\n
    '''
def setDefaultCellBorderWidth():
    '''returns None\n\n
    setDefaultCellBorderWidth(final float value)\n
    '''
def setDefaultCellBorderColor():
    '''returns None\n\n
    setDefaultCellBorderColor(final Color color)\n
    '''
def setDefaultCellBackgroundColor():
    '''returns None\n\n
    setDefaultCellBackgroundColor(final Color color)\n
    '''
def setDefaultCellGrayFill():
    '''returns None\n\n
    setDefaultCellGrayFill(final float value)\n
    '''
def setDefaultHorizontalAlignment():
    '''returns None\n\n
    setDefaultHorizontalAlignment(final int value)\n
    '''
def setDefaultVerticalAlignment():
    '''returns None\n\n
    setDefaultVerticalAlignment(final int value)\n
    '''
def setDefaultRowspan():
    '''returns None\n\n
    setDefaultRowspan(final int value)\n
    '''
def setDefaultColspan():
    '''returns None\n\n
    setDefaultColspan(final int value)\n
    '''
def deleteColumn():
    '''returns None\n\n
    deleteColumn(final int column)\n
    '''
def deleteRow():
    '''returns boolean\n\n
    deleteRow(final int row)\n
    '''
def deleteAllRows():
    '''returns None\n\n
    deleteAllRows()\n
    '''
def deleteLastRow():
    '''returns boolean\n\n
    deleteLastRow()\n
    '''
def endHeaders():
    '''returns int\n\n
    endHeaders()\n
    '''
def setLastHeaderRow():
    '''returns None\n\n
    setLastHeaderRow(final int value)\n
    '''
def setAlignment():
    '''returns None\n\n
    setAlignment(final int value)\n
    setAlignment(final String alignment)\n
    '''
def setSpaceInsideCell():
    '''returns None\n\n
    setSpaceInsideCell(final float value)\n
    '''
def setSpaceBetweenCells():
    '''returns None\n\n
    setSpaceBetweenCells(final float value)\n
    '''
def setPadding():
    '''returns None\n\n
    setPadding(final float value)\n
    '''
def setSpacing():
    '''returns None\n\n
    setSpacing(final float value)\n
    '''
def setCellpadding():
    '''returns None\n\n
    setCellpadding(final float value)\n
    '''
def setCellspacing():
    '''returns None\n\n
    setCellspacing(final float value)\n
    '''
def setWidth():
    '''returns None\n\n
    setWidth(final float width)\n
    '''
def setAbsWidth():
    '''returns None\n\n
    setAbsWidth(final String width)\n
    '''
def setWidths():
    '''returns None\n\n
    setWidths(final float[] widths)\n
    setWidths(final int[] widths)\n
    '''
def columns():
    '''returns int\n\n
    columns()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def getProportionalWidths():
    '''returns float[]\n\n
    getProportionalWidths()\n
    '''
def iterator():
    '''returns Iterator\n\n
    iterator()\n
    '''
def alignment():
    '''returns int\n\n
    alignment()\n
    '''
def cellpadding():
    '''returns float\n\n
    cellpadding()\n
    '''
def cellspacing():
    '''returns float\n\n
    cellspacing()\n
    '''
def widthPercentage():
    '''returns float\n\n
    widthPercentage()\n
    '''
def absWidth():
    '''returns String\n\n
    absWidth()\n
    '''
def firstDataRow():
    '''returns int\n\n
    firstDataRow()\n
    '''
def lastHeaderRow():
    '''returns int\n\n
    lastHeaderRow()\n
    '''
def getDimension():
    '''returns Dimension\n\n
    getDimension()\n
    '''
def getElement():
    '''returns Object\n\n
    getElement(final int row, final int column)\n
    '''
def addColumns():
    '''returns None\n\n
    addColumns(final int aColumns)\n
    '''
def getWidths():
    '''returns float[]\n\n
    getWidths(final float left, float totalWidth)\n
    '''
def setAlternatingRowAttribute():
    '''returns None\n\n
    setAlternatingRowAttribute(final String name, final String value0, final String value1)\n
    '''
def top():
    '''returns float\n\n
    top()\n
    top(final int margin)\n
    '''
def bottom():
    '''returns float\n\n
    bottom()\n
    bottom(final int margin)\n
    '''
def left():
    '''returns float\n\n
    left()\n
    left(final int margin)\n
    '''
def right():
    '''returns float\n\n
    right()\n
    right(final int margin)\n
    '''
def setTop():
    '''returns None\n\n
    setTop(final int value)\n
    '''
def setBottom():
    '''returns None\n\n
    setBottom(final int value)\n
    '''
def setLeft():
    '''returns None\n\n
    setLeft(final int value)\n
    '''
def setRight():
    '''returns None\n\n
    setRight(final int value)\n
    '''
def getNextRow():
    '''returns int\n\n
    getNextRow()\n
    '''
def getNextColumn():
    '''returns int\n\n
    getNextColumn()\n
    '''
