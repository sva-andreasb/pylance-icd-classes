def ():
    '''returns HSSFShapeGroup\n\n
    (final EscherContainerRecord spgrContainer, final ObjRecord objRecord)\n
    (final HSSFShape parent, final HSSFAnchor anchor)\n
    '''
def createGroup():
    '''returns HSSFShapeGroup\n\n
    createGroup(final HSSFChildAnchor anchor)\n
    '''
def addShape():
    '''returns None\n\n
    addShape(final HSSFShape shape)\n
    '''
def createShape():
    '''returns HSSFSimpleShape\n\n
    createShape(final HSSFChildAnchor anchor)\n
    '''
def createTextbox():
    '''returns HSSFTextbox\n\n
    createTextbox(final HSSFChildAnchor anchor)\n
    '''
def createPolygon():
    '''returns HSSFPolygon\n\n
    createPolygon(final HSSFChildAnchor anchor)\n
    '''
def createPicture():
    '''returns HSSFPicture\n\n
    createPicture(final HSSFChildAnchor anchor, final int pictureIndex)\n
    '''
def getChildren():
    '''returns List<HSSFShape>\n\n
    getChildren()\n
    '''
def setCoordinates():
    '''returns None\n\n
    setCoordinates(final int x1, final int y1, final int x2, final int y2)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
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
def countOfAllChildren():
    '''returns int\n\n
    countOfAllChildren()\n
    '''
def removeShape():
    '''returns boolean\n\n
    removeShape(final HSSFShape shape)\n
    '''
def iterator():
    '''returns Iterator<HSSFShape>\n\n
    iterator()\n
    '''
