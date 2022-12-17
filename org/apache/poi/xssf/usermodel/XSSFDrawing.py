def ():
    '''returns XSSFDrawing\n\n
    (final PackagePart part)\n
    '''
def getCTDrawing():
    '''returns CTDrawing\n\n
    getCTDrawing()\n
    '''
def createAnchor():
    '''returns XSSFClientAnchor\n\n
    createAnchor(final int dx1, final int dy1, final int dx2, final int dy2, final int col1, final int row1, final int col2, final int row2)\n
    '''
def createTextbox():
    '''returns XSSFTextBox\n\n
    createTextbox(final XSSFClientAnchor anchor)\n
    '''
def createPicture():
    '''returns XSSFPicture\n\n
    createPicture(final XSSFClientAnchor anchor, final int pictureIndex)\n
    createPicture(final ClientAnchor anchor, final int pictureIndex)\n
    '''
def createChart():
    '''returns XSSFChart\n\n
    createChart(final XSSFClientAnchor anchor)\n
    createChart(final ClientAnchor anchor)\n
    '''
def createSimpleShape():
    '''returns XSSFSimpleShape\n\n
    createSimpleShape(final XSSFClientAnchor anchor)\n
    '''
def createConnector():
    '''returns XSSFConnector\n\n
    createConnector(final XSSFClientAnchor anchor)\n
    '''
def createGroup():
    '''returns XSSFShapeGroup\n\n
    createGroup(final XSSFClientAnchor anchor)\n
    '''
def createCellComment():
    '''returns XSSFComment\n\n
    createCellComment(final ClientAnchor anchor)\n
    '''
def createObjectData():
    '''returns XSSFObjectData\n\n
    createObjectData(final ClientAnchor anchor, final int storageId, final int pictureIndex)\n
    '''
def getCharts():
    '''returns List<XSSFChart>\n\n
    getCharts()\n
    '''
def getShapes():
    '''returns List<XSSFShape>\n\n
    getShapes()\n
    getShapes(final XSSFShapeGroup groupshape)\n
    '''
def iterator():
    '''returns Iterator<XSSFShape>\n\n
    iterator()\n
    '''
def getSheet():
    '''returns XSSFSheet\n\n
    getSheet()\n
    '''
