def ():
    '''returns IlvCrossingAwareLinkImage\n\n
    (final IlvGraphic ilvGraphic, final IlvGraphic ilvGraphic2, final boolean b, final IlvPoint[] array)\n
    (final IlvGraphic ilvGraphic, final IlvGraphic ilvGraphic2, final boolean backOriented, final boolean b, final IlvPoint[] array)\n
    (final IlvCrossingAwareLinkImage ilvCrossingAwareLinkImage)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def setCrossingEnabled():
    '''returns None\n\n
    setCrossingEnabled(final boolean m)\n
    '''
def isCrossingEnabled():
    '''returns boolean\n\n
    isCrossingEnabled()\n
    '''
def setGap():
    '''returns None\n\n
    setGap(final float c)\n
    '''
def setGapZoomable():
    '''returns None\n\n
    setGapZoomable(final boolean d)\n
    '''
def zoomable():
    '''returns boolean\n\n
    zoomable()\n
    '''
def setCrossingGraphic():
    '''returns None\n\n
    setCrossingGraphic(final IlvGraphic ilvGraphic)\n
    setCrossingGraphic(final IlvGraphic crossingGraphic, final int layerOfCrossingGraphic)\n
    '''
def apply():
    '''returns boolean\n\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvCrossingGraphic ilvCrossingGraphic, final IlvLinkImage ilvLinkImage, final IlvLinkImage ilvLinkImage2, final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvPoint ilvPoint3, final IlvPoint ilvPoint4, final float n, final float n2, final float n3)\n
    apply(final IlvCrossingGraphic ilvCrossingGraphic, final IlvLinkImage ilvLinkImage, final IlvLinkImage ilvLinkImage2, final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvPoint ilvPoint3, final IlvPoint ilvPoint4, final float n, final float n2, final float n3)\n
    apply(final IlvCrossingGraphic ilvCrossingGraphic, final IlvLinkImage ilvLinkImage, final IlvLinkImage ilvLinkImage2, final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvPoint ilvPoint3, final IlvPoint ilvPoint4, final float n, final float n2, final float n3)\n
    '''
def setLayerOfCrossingGraphic():
    '''returns None\n\n
    setLayerOfCrossingGraphic(final int g)\n
    '''
def setGraphicBag():
    '''returns None\n\n
    setGraphicBag(final IlvGraphicBag graphicBag)\n
    '''
def getCrossingPolicy():
    '''returns IlvCrossingLinkShapePolicy\n\n
    getCrossingPolicy()\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def setBoundingBoxCacheSize():
    '''returns None\n\n
    setBoundingBoxCacheSize(final int size)\n
    '''
def getBoundingBoxCacheSize():
    '''returns int\n\n
    getBoundingBoxCacheSize()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def insertPoint():
    '''returns None\n\n
    insertPoint(final int n, final float n2, final float n3, final IlvTransformer ilvTransformer)\n
    '''
def removePoint():
    '''returns None\n\n
    removePoint(final int n, final IlvTransformer ilvTransformer)\n
    '''
def movePoint():
    '''returns None\n\n
    movePoint(final int n, final float n2, final float n3, final IlvTransformer ilvTransformer)\n
    '''
def setIntermediateLinkPoints():
    '''returns None\n\n
    setIntermediateLinkPoints(final IlvPoint[] array, final int n, final int n2)\n
    '''
def setOriented():
    '''returns None\n\n
    setOriented(final boolean oriented)\n
    '''
def setBackOriented():
    '''returns None\n\n
    setBackOriented(final boolean l)\n
    '''
def isBackOriented():
    '''returns boolean\n\n
    isBackOriented()\n
    '''
def setLineWidth():
    '''returns None\n\n
    setLineWidth(final float lineWidth)\n
    '''
def setMaximumLineWidth():
    '''returns None\n\n
    setMaximumLineWidth(final float maximumLineWidth)\n
    '''
def setEndCap():
    '''returns None\n\n
    setEndCap(final int endCap)\n
    '''
def setLineJoin():
    '''returns None\n\n
    setLineJoin(final int lineJoin)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def viewChanged():
    '''returns None\n\n
    viewChanged(final ManagerViewsChangedEvent managerViewsChangedEvent)\n
    '''
def contentsChanged():
    '''returns None\n\n
    contentsChanged(final ManagerContentChangedEvent managerContentChangedEvent)\n
    '''
