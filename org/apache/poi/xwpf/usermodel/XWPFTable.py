def ():
    '''returns XWPFTable\n\n
    (final CTTbl table, final IBody part, final int row, final int col)\n
    (final CTTbl table, final IBody part)\n
    '''
def getCTTbl():
    '''returns CTTbl\n\n
    getCTTbl()\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
    '''
def addNewRowBetween():
    '''returns None\n\n
    addNewRowBetween(final int start, final int end)\n
    '''
def addNewCol():
    '''returns None\n\n
    addNewCol()\n
    '''
def createRow():
    '''returns XWPFTableRow\n\n
    createRow()\n
    '''
def getRow():
    '''returns XWPFTableRow\n\n
    getRow(final int pos)\n
    getRow(final CTRow row)\n
    '''
def getWidth():
    '''returns int\n\n
    getWidth()\n
    '''
def setWidth():
    '''returns None\n\n
    setWidth(final int width)\n
    '''
def getNumberOfRows():
    '''returns int\n\n
    getNumberOfRows()\n
    '''
def getStyleID():
    '''returns String\n\n
    getStyleID()\n
    '''
def setStyleID():
    '''returns None\n\n
    setStyleID(final String styleName)\n
    '''
def getInsideHBorderType():
    '''returns XWPFBorderType\n\n
    getInsideHBorderType()\n
    '''
def getInsideHBorderSize():
    '''returns int\n\n
    getInsideHBorderSize()\n
    '''
def getInsideHBorderSpace():
    '''returns int\n\n
    getInsideHBorderSpace()\n
    '''
def getInsideHBorderColor():
    '''returns String\n\n
    getInsideHBorderColor()\n
    '''
def getInsideVBorderType():
    '''returns XWPFBorderType\n\n
    getInsideVBorderType()\n
    '''
def getInsideVBorderSize():
    '''returns int\n\n
    getInsideVBorderSize()\n
    '''
def getInsideVBorderSpace():
    '''returns int\n\n
    getInsideVBorderSpace()\n
    '''
def getInsideVBorderColor():
    '''returns String\n\n
    getInsideVBorderColor()\n
    '''
def getRowBandSize():
    '''returns int\n\n
    getRowBandSize()\n
    '''
def setRowBandSize():
    '''returns None\n\n
    setRowBandSize(final int size)\n
    '''
def getColBandSize():
    '''returns int\n\n
    getColBandSize()\n
    '''
def setColBandSize():
    '''returns None\n\n
    setColBandSize(final int size)\n
    '''
def setInsideHBorder():
    '''returns None\n\n
    setInsideHBorder(final XWPFBorderType type, final int size, final int space, final String rgbColor)\n
    '''
def setInsideVBorder():
    '''returns None\n\n
    setInsideVBorder(final XWPFBorderType type, final int size, final int space, final String rgbColor)\n
    '''
def getCellMarginTop():
    '''returns int\n\n
    getCellMarginTop()\n
    '''
def getCellMarginLeft():
    '''returns int\n\n
    getCellMarginLeft()\n
    '''
def getCellMarginBottom():
    '''returns int\n\n
    getCellMarginBottom()\n
    '''
def getCellMarginRight():
    '''returns int\n\n
    getCellMarginRight()\n
    '''
def setCellMargins():
    '''returns None\n\n
    setCellMargins(final int top, final int left, final int bottom, final int right)\n
    '''
def addRow():
    '''returns boolean\n\n
    addRow(final XWPFTableRow row)\n
    addRow(final XWPFTableRow row, final int pos)\n
    '''
def insertNewTableRow():
    '''returns XWPFTableRow\n\n
    insertNewTableRow(final int pos)\n
    '''
def removeRow():
    '''returns boolean\n\n
    removeRow(final int pos)\n
    '''
def getRows():
    '''returns List<XWPFTableRow>\n\n
    getRows()\n
    '''
def getElementType():
    '''returns BodyElementType\n\n
    getElementType()\n
    '''
def getBody():
    '''returns IBody\n\n
    getBody()\n
    '''
def getPart():
    '''returns POIXMLDocumentPart\n\n
    getPart()\n
    '''
def getPartType():
    '''returns BodyType\n\n
    getPartType()\n
    '''
