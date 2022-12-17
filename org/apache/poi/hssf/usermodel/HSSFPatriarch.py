def removeShape():
    '''returns boolean\n\n
    removeShape(final HSSFShape shape)\n
    '''
def createGroup():
    '''returns HSSFShapeGroup\n\n
    createGroup(final HSSFClientAnchor anchor)\n
    '''
def createSimpleShape():
    '''returns HSSFSimpleShape\n\n
    createSimpleShape(final HSSFClientAnchor anchor)\n
    '''
def createPicture():
    '''returns HSSFPicture\n\n
    createPicture(final HSSFClientAnchor anchor, final int pictureIndex)\n
    createPicture(final ClientAnchor anchor, final int pictureIndex)\n
    '''
def createObjectData():
    '''returns HSSFObjectData\n\n
    createObjectData(final ClientAnchor anchor, final int storageId, final int pictureIndex)\n
    '''
def createPolygon():
    '''returns HSSFPolygon\n\n
    createPolygon(final HSSFClientAnchor anchor)\n
    '''
def createTextbox():
    '''returns HSSFTextbox\n\n
    createTextbox(final HSSFClientAnchor anchor)\n
    '''
def createComment():
    '''returns HSSFComment\n\n
    createComment(final HSSFAnchor anchor)\n
    '''
def createCellComment():
    '''returns HSSFComment\n\n
    createCellComment(final ClientAnchor anchor)\n
    '''
def getChildren():
    '''returns List<HSSFShape>\n\n
    getChildren()\n
    '''
def addShape():
    '''returns None\n\n
    addShape(final HSSFShape shape)\n
    '''
def countOfAllChildren():
    '''returns int\n\n
    countOfAllChildren()\n
    '''
def setCoordinates():
    '''returns None\n\n
    setCoordinates(final int x1, final int y1, final int x2, final int y2)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def containsChart():
    '''returns boolean\n\n
    containsChart()\n
    '''
def getX1():
    '''returns int\n\n
    getX1()\n
    '''
def getY1():
    '''returns int\n\n
    getY1()\n
    '''
def getX2():
    '''returns int\n\n
    getX2()\n
    '''
def getY2():
    '''returns int\n\n
    getY2()\n
    '''
def getBoundAggregate():
    '''returns EscherAggregate\n\n
    getBoundAggregate()\n
    '''
def createAnchor():
    '''returns HSSFClientAnchor\n\n
    createAnchor(final int dx1, final int dy1, final int dx2, final int dy2, final int col1, final int row1, final int col2, final int row2)\n
    '''
def createChart():
    '''returns Chart\n\n
    createChart(final ClientAnchor anchor)\n
    '''
def iterator():
    '''returns Iterator<HSSFShape>\n\n
    iterator()\n
    '''
