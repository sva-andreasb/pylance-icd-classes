def ():
    '''returns IlvCompositeLink\n\n
    ()\n
    (final IlvGraphic ilvGraphic, final IlvGraphic ilvGraphic2, final boolean b, final IlvPoint[] array)\n
    (final IlvGraphic ilvGraphic, final IlvGraphic ilvGraphic2, final boolean b)\n
    (final IlvGraphic ilvGraphic, final IlvGraphic ilvGraphic2, final boolean b, final IlvLinkImage link)\n
    (final IlvInputStream ilvInputStream)\n
    (final IlvCompositeLink ilvCompositeLink)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
def invalidate():
    '''returns None\n\n
    invalidate()\n
    '''
def addObject():
    '''returns None\n\n
    addObject(final IlvGraphic ilvGraphic, final boolean b)\n
    '''
def removeObject():
    '''returns None\n\n
    removeObject(final IlvGraphic ilvGraphic, final boolean b)\n
    '''
def getObjects():
    '''returns IlvGraphicEnumeration\n\n
    getObjects()\n
    '''
def reDrawObj():
    '''returns None\n\n
    reDrawObj(final IlvGraphic ilvGraphic)\n
    '''
def reDrawRegion():
    '''returns None\n\n
    reDrawRegion(final IlvRegion ilvRegion)\n
    '''
def reshapeObject():
    '''returns None\n\n
    reshapeObject(final IlvGraphic ilvGraphic, final IlvRect ilvRect, final boolean b)\n
    '''
def moveObject():
    '''returns None\n\n
    moveObject(final IlvGraphic ilvGraphic, final float n, final float n2, final boolean b)\n
    '''
def applyToObject():
    '''returns None\n\n
    applyToObject(final IlvGraphic ilvGraphic, final IlvApplyObject ilvApplyObject, final Object o, final boolean b)\n
    '''
def setObjectName():
    '''returns boolean\n\n
    setObjectName(final IlvGraphic ilvGraphic, final String s)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def getBaseBoundingBox():
    '''returns IlvRect\n\n
    getBaseBoundingBox(final IlvTransformer ilvTransformer)\n
    '''
def doLayout():
    '''returns None\n\n
    doLayout()\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def getToolTipText():
    '''returns String\n\n
    getToolTipText(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer)\n
    '''
def setToolTipText():
    '''returns None\n\n
    setToolTipText(final String s)\n
    '''
def setChildren():
    '''returns None\n\n
    setChildren(final IlvGraphic[] children)\n
    setChildren(final int n, final IlvGraphic ilvGraphic)\n
    '''
def getChildren():
    '''returns IlvGraphic\n\n
    getChildren()\n
    getChildren(final int n)\n
    '''
def setConstraints():
    '''returns None\n\n
    setConstraints(final Object[] constraints)\n
    setConstraints(final int n, final Object o)\n
    '''
def getConstraints():
    '''returns Object\n\n
    getConstraints()\n
    getConstraints(final int n)\n
    '''
def setLink():
    '''returns None\n\n
    setLink(final IlvLinkImage b)\n
    '''
def getLink():
    '''returns IlvLinkImage\n\n
    getLink()\n
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
    '''
def setLineWidth():
    '''returns None\n\n
    setLineWidth(final float n)\n
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
def getEventMaps():
    '''returns IlvEventMap[]\n\n
    getEventMaps()\n
    '''
def getAction():
    '''returns Action\n\n
    getAction(final int n, final IlvMouseGesture ilvMouseGesture)\n
    '''
def getParent():
    '''returns IlvComposite\n\n
    getParent()\n
    '''
def getRoot():
    '''returns IlvComposite\n\n
    getRoot()\n
    '''
def getObject():
    '''returns IlvGraphic\n\n
    getObject(final String s)\n
    '''
def setGraphicBag():
    '''returns None\n\n
    setGraphicBag(final IlvGraphicBag graphicBag)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def setVisibilityThresholds():
    '''returns None\n\n
    setVisibilityThresholds(final double[] visibilityThresholds)\n
    setVisibilityThresholds(final int n, final double n2)\n
    '''
def getVisibilityThresholds():
    '''returns double\n\n
    getVisibilityThresholds()\n
    getVisibilityThresholds(final int n)\n
    '''
def getAttachableGraphic():
    '''returns IlvAttachableGraphic\n\n
    getAttachableGraphic(final IlvGraphic ilvGraphic)\n
    '''
def setLabel():
    '''returns None\n\n
    setLabel(final String label)\n
    '''
def getLabel():
    '''returns String\n\n
    getLabel()\n
    '''
def supportMultiline():
    '''returns boolean\n\n
    supportMultiline()\n
    '''
def getLabelBBox():
    '''returns IlvRect\n\n
    getLabelBBox(final IlvTransformer ilvTransformer)\n
    '''
def hasActions():
    '''returns boolean\n\n
    hasActions(final int n)\n
    '''
def setSensitive():
    '''returns None\n\n
    setSensitive(final boolean b)\n
    '''
def isSensitive():
    '''returns boolean\n\n
    isSensitive()\n
    '''
def isSpline():
    '''returns boolean\n\n
    isSpline()\n
    '''
def setAlpha():
    '''returns None\n\n
    setAlpha(final float g)\n
    '''
def getAlpha():
    '''returns float\n\n
    getAlpha()\n
    '''
def setBaseTextDirection():
    '''returns None\n\n
    setBaseTextDirection(final int baseTextDirection)\n
    '''
def getBaseTextDirection():
    '''returns int\n\n
    getBaseTextDirection()\n
    '''
def isBaseTextDirectionSensitive():
    '''returns boolean\n\n
    isBaseTextDirectionSensitive()\n
    '''
def baseTextDirectionChanged():
    '''returns None\n\n
    baseTextDirectionChanged(final int n, final int n2)\n
    '''
def componentOrientationChanged():
    '''returns None\n\n
    componentOrientationChanged(final ComponentOrientation componentOrientation, final ComponentOrientation componentOrientation2)\n
    '''
def localeChanged():
    '''returns None\n\n
    localeChanged(final ULocale uLocale, final ULocale uLocale2)\n
    '''
