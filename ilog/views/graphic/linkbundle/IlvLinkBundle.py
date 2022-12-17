def ():
    '''returns IlvLinkBundle\n\n
    ()\n
    (final IlvGraphic ilvGraphic, final IlvGraphic ilvGraphic2, final boolean b)\n
    (final IlvGraphic ilvGraphic, final IlvGraphic ilvGraphic2, final boolean b, final IlvPoint[] array)\n
    (final IlvGraphic ilvGraphic, final IlvGraphic ilvGraphic2, final boolean b, final IlvPoint[] array, final IlvLinkImage overviewLink)\n
    (final IlvInputStream ilvInputStream)\n
    (final IlvLinkBundle ilvLinkBundle)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def setGraphicBag():
    '''returns None\n\n
    setGraphicBag(final IlvGraphicBag graphicBag)\n
    '''
def addObject():
    '''returns None\n\n
    addObject(final IlvGraphic obj, final boolean b)\n
    '''
def apply():
    '''returns None\n\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    '''
def removeObject():
    '''returns None\n\n
    removeObject(final IlvGraphic obj, final boolean b)\n
    '''
def addSublink():
    '''returns None\n\n
    addSublink(final IlvLinkImage ilvLinkImage)\n
    addSublink(final int n, final IlvLinkImage ilvLinkImage)\n
    '''
def removeSublink():
    '''returns None\n\n
    removeSublink(final IlvLinkImage ilvLinkImage)\n
    '''
def getSublink():
    '''returns IlvLinkImage\n\n
    getSublink(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer)\n
    getSublink(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer, final boolean b)\n
    getSublink(final int n)\n
    '''
def getCollapseExpandObject():
    '''returns IlvObjectWithSelection\n\n
    getCollapseExpandObject(final IlvPoint p4, final IlvManagerView ilvManagerView, final IlvTransformer ilvTransformer, final boolean b)\n
    '''
def getSelectableObject():
    '''returns IlvGraphic\n\n
    getSelectableObject(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView, final IlvTransformer ilvTransformer, final boolean b)\n
    '''
def getAllSelectableObjects():
    '''returns IlvGraphicVector\n\n
    getAllSelectableObjects(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView, final IlvTransformer ilvTransformer, final boolean b, final boolean b2)\n
    '''
def getSelection():
    '''returns IlvSelection\n\n
    getSelection(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer)\n
    getSelection(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer, final boolean b)\n
    '''
def getObject():
    '''returns IlvGraphic\n\n
    getObject(final String key)\n
    '''
def setObjectName():
    '''returns boolean\n\n
    setObjectName(final IlvGraphic value, final String s)\n
    '''
def getObjectName():
    '''returns String\n\n
    getObjectName(final IlvGraphic ilvGraphic)\n
    '''
def getPopupMenu():
    '''returns JPopupMenu\n\n
    getPopupMenu(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer, final IlvManagerView ilvManagerView, final IlvPopupMenuManager ilvPopupMenuManager)\n
    '''
def setToolTipText():
    '''returns None\n\n
    setToolTipText(final String s)\n
    '''
def getToolTipText():
    '''returns String\n\n
    getToolTipText()\n
    getToolTipText(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer)\n
    '''
def setSelected():
    '''returns None\n\n
    setSelected(final IlvLinkImage obj, final boolean b)\n
    setSelected(final IlvGraphic ilvGraphic, final boolean b, final boolean b2)\n
    setSelected(final IlvGraphic ilvGraphic, final IlvPoint ilvPoint, final IlvManagerView ilvManagerView)\n
    '''
def selectAll():
    '''returns None\n\n
    selectAll()\n
    selectAll(final boolean b)\n
    selectAll(final boolean b, final boolean b2)\n
    '''
def deSelectAll():
    '''returns None\n\n
    deSelectAll()\n
    deSelectAll(final boolean b)\n
    deSelectAll(final boolean b, final boolean b2)\n
    '''
def getSelectionFactory():
    '''returns IlvSelectionFactory\n\n
    getSelectionFactory()\n
    '''
def setSelectionEventSource():
    '''returns None\n\n
    setSelectionEventSource(final Object source)\n
    '''
def setSelectionAdjusting():
    '''returns None\n\n
    setSelectionAdjusting(final boolean b)\n
    '''
def isSelectionAdjusting():
    '''returns boolean\n\n
    isSelectionAdjusting()\n
    '''
def addLinkBundleSelectionChangedListener():
    '''returns None\n\n
    addLinkBundleSelectionChangedListener(final LinkBundleSelectionChangedListener l)\n
    '''
def removeLinkBundleSelectionChangedListener():
    '''returns None\n\n
    removeLinkBundleSelectionChangedListener(final LinkBundleSelectionChangedListener l)\n
    '''
def isSelected():
    '''returns boolean\n\n
    isSelected(final IlvLinkImage ilvLinkImage)\n
    isSelected(final IlvGraphic ilvGraphic)\n
    '''
def setOffset():
    '''returns None\n\n
    setOffset(final float y)\n
    '''
def getOffset():
    '''returns float\n\n
    getOffset()\n
    '''
def setSingleConnectionPoint():
    '''returns None\n\n
    setSingleConnectionPoint(final boolean aa)\n
    '''
def isSingleConnectionPoint():
    '''returns boolean\n\n
    isSingleConnectionPoint()\n
    '''
def setCollapsed():
    '''returns None\n\n
    setCollapsed(final boolean m)\n
    '''
def isCollapsed():
    '''returns boolean\n\n
    isCollapsed()\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def getFrame():
    '''returns IlvLinkBundleFrame\n\n
    getFrame()\n
    '''
def setFrame():
    '''returns None\n\n
    setFrame(final IlvLinkBundleFrame k)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint p3, final IlvTransformer ilvTransformer)\n
    '''
def containsFrame():
    '''returns boolean\n\n
    containsFrame(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def setSublinks():
    '''returns None\n\n
    setSublinks(final IlvLinkImage[] array)\n
    '''
def setSublink():
    '''returns None\n\n
    setSublink(final int n, final IlvLinkImage ilvLinkImage)\n
    '''
def getPointsCardinal():
    '''returns int\n\n
    getPointsCardinal()\n
    '''
def allowsPointInsertion():
    '''returns boolean\n\n
    allowsPointInsertion()\n
    '''
def allowsPointRemoval():
    '''returns boolean\n\n
    allowsPointRemoval()\n
    '''
def allowsPointMove():
    '''returns boolean\n\n
    allowsPointMove(final int n)\n
    '''
def insertPoint():
    '''returns None\n\n
    insertPoint(final int n, final float n2, final float n3, final IlvTransformer ilvTransformer)\n
    '''
def removePoint():
    '''returns None\n\n
    removePoint(final int n, final IlvTransformer ilvTransformer)\n
    '''
def getPointAt():
    '''returns IlvPoint\n\n
    getPointAt(final int n, final IlvTransformer ilvTransformer)\n
    '''
def movePoint():
    '''returns None\n\n
    movePoint(final int n, final float n2, final float n3, final IlvTransformer ilvTransformer)\n
    '''
def setIntermediateLinkPoints():
    '''returns None\n\n
    setIntermediateLinkPoints(final IlvPoint[] array, final int n, final int n2)\n
    '''
def pointsInBBox():
    '''returns boolean\n\n
    pointsInBBox()\n
    '''
def getConnectionReferencePoint():
    '''returns IlvPoint\n\n
    getConnectionReferencePoint(final boolean b, final IlvTransformer ilvTransformer)\n
    '''
def getConnectionPoints():
    '''returns None\n\n
    getConnectionPoints(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def isOriented():
    '''returns boolean\n\n
    isOriented()\n
    '''
def setOriented():
    '''returns None\n\n
    setOriented(final boolean b)\n
    '''
def setForeground():
    '''returns None\n\n
    setForeground(final Color color)\n
    '''
def getForeground():
    '''returns Color\n\n
    getForeground()\n
    '''
def getLineWidth():
    '''returns float\n\n
    getLineWidth()\n
    getLineWidth(final IlvTransformer ilvTransformer)\n
    getLineWidth(final IlvTransformer ilvTransformer, final boolean b)\n
    '''
def setLineWidth():
    '''returns None\n\n
    setLineWidth(final float n)\n
    '''
def getOverviewLineWidth():
    '''returns float\n\n
    getOverviewLineWidth()\n
    '''
def getEndCap():
    '''returns int\n\n
    getEndCap()\n
    '''
def setEndCap():
    '''returns None\n\n
    setEndCap(final int n)\n
    '''
def getLineJoin():
    '''returns int\n\n
    getLineJoin()\n
    '''
def setLineJoin():
    '''returns None\n\n
    setLineJoin(final int n)\n
    '''
def getMaximumLineWidth():
    '''returns float\n\n
    getMaximumLineWidth()\n
    '''
def setMaximumLineWidth():
    '''returns None\n\n
    setMaximumLineWidth(final float n)\n
    '''
def getLineStyle():
    '''returns float[]\n\n
    getLineStyle()\n
    '''
def setLineStyle():
    '''returns None\n\n
    setLineStyle(final float[] array)\n
    '''
def getLinkPoints():
    '''returns IlvPoint[]\n\n
    getLinkPoints(final IlvTransformer ilvTransformer)\n
    '''
def applyToObject():
    '''returns None\n\n
    applyToObject(final IlvGraphic ilvGraphic, final IlvApplyObject ilvApplyObject, final Object o, final boolean b)\n
    '''
def reshapeObject():
    '''returns None\n\n
    reshapeObject(final IlvGraphic ilvGraphic, final IlvRect ilvRect, final boolean b)\n
    '''
def moveObject():
    '''returns None\n\n
    moveObject(final IlvGraphic ilvGraphic, final float n, final float n2, final boolean b)\n
    '''
def reDrawRegion():
    '''returns None\n\n
    reDrawRegion(final IlvRegion ilvRegion)\n
    '''
def reDrawObj():
    '''returns None\n\n
    reDrawObj(final IlvGraphic ilvGraphic)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def makeSelection():
    '''returns IlvSelection\n\n
    makeSelection()\n
    '''
def zoomable():
    '''returns boolean\n\n
    zoomable()\n
    '''
def ensureClippingLinkConnector():
    '''returns None\n\n
    ensureClippingLinkConnector(final boolean b, final boolean b2)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final IlvGraphic ilvGraphic)\n
    '''
