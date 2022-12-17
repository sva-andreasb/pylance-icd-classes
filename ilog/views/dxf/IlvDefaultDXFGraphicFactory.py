def ():
    '''returns IlvDefaultDXFGraphicFactory\n\n
    ()\n
    '''
def addObject():
    '''returns None\n\n
    addObject(final IlvGraphic ilvGraphic, final IlvManager ilvManager, final int n)\n
    addObject(final IlvGraphic ilvGraphic, final IlvGraphicBag ilvGraphicBag)\n
    '''
def prepareLayer():
    '''returns IlvManagerLayer\n\n
    prepareLayer(final IlvManager ilvManager, final String s)\n
    '''
def createPoint():
    '''returns IlvGraphic\n\n
    createPoint(final IlvPoint ilvPoint, final float n, final Color foreground)\n
    '''
def createLine():
    '''returns IlvGraphic\n\n
    createLine(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final float lineWidth, final Color foreground)\n
    '''
def createArc():
    '''returns IlvGraphic\n\n
    createArc(final IlvPoint ilvPoint, final float n, float n2, final float n3, final float n4, final Color foreground)\n
    '''
def createCircle():
    '''returns IlvGraphic\n\n
    createCircle(final IlvPoint ilvPoint, final float n, final float n2, final Color foreground)\n
    '''
def createPolyline():
    '''returns IlvGraphic\n\n
    createPolyline(IlvPoint[] array, final boolean b, final boolean b2, final float lineWidth, final Color foreground)\n
    '''
def createSpline():
    '''returns IlvGraphic\n\n
    createSpline(final IlvPoint[] array, final boolean b, final float n, final Color foreground)\n
    '''
def createTrace():
    '''returns IlvGraphic\n\n
    createTrace(final IlvPoint[] array, final float n, final Color color)\n
    '''
def createSolid():
    '''returns IlvGraphic\n\n
    createSolid(final IlvPoint[] array, final float n, final Color color)\n
    '''
def create3DFace():
    '''returns IlvGraphic\n\n
    create3DFace(final IlvPoint[] array, final Color color)\n
    '''
def createText():
    '''returns IlvGraphic\n\n
    createText(final IlvPoint ilvPoint, final String s, final boolean b, final boolean antialiasing, final Font font, final Color foreground)\n
    '''
def createDimension():
    '''returns IlvGraphic\n\n
    createDimension(final String s, final short n, final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvPoint ilvPoint3, final IlvPoint ilvPoint4, final IlvPoint ilvPoint5, final IlvPoint ilvPoint6, final IlvPoint ilvPoint7)\n
    '''
def createInsert():
    '''returns IlvGraphic\n\n
    createInsert(final IlvGraphicVector ilvGraphicVector, final String s, final Color foreground)\n
    '''
