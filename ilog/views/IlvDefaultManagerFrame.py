LEFT = "int  1"
CENTER = "int  16"
RIGHT = "int  2"
TOP = "int  4"
BOTTOM = "int  8"
WRAPPED = "int  128"
def ():
    '''returns IlvDefaultManagerFrame\n\n
    ()\n
    (final IlvDefaultManagerFrame ilvDefaultManagerFrame)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def copy():
    '''returns IlvManagerFrame\n\n
    copy()\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def setExpandCollapseIcon():
    '''returns None\n\n
    setExpandCollapseIcon(final IlvGraphic ah)\n
    '''
def getExpandCollapseIcon():
    '''returns IlvGraphic\n\n
    getExpandCollapseIcon()\n
    '''
def isShowingExpandCollapseIcon():
    '''returns boolean\n\n
    isShowingExpandCollapseIcon()\n
    '''
def setShowingExpandCollapseIcon():
    '''returns None\n\n
    setShowingExpandCollapseIcon(final boolean b)\n
    '''
def setExpandCollapseIconPosition():
    '''returns None\n\n
    setExpandCollapseIconPosition(final float n, final float n2, final float n3, final float n4)\n
    '''
def setRelativeExpandCollapseIconPosition():
    '''returns None\n\n
    setRelativeExpandCollapseIconPosition(final IlvPoint ilvPoint)\n
    '''
def setAbsoluteExpandCollapseIconPosition():
    '''returns None\n\n
    setAbsoluteExpandCollapseIconPosition(final IlvPoint ilvPoint)\n
    '''
def getTopMargin():
    '''returns float\n\n
    getTopMargin(final IlvManager ilvManager, final IlvTransformer ilvTransformer)\n
    getTopMargin()\n
    '''
def moveResize():
    '''returns boolean\n\n
    moveResize(final IlvManager ilvManager, final IlvRect ilvRect)\n
    '''
def managerChanged():
    '''returns None\n\n
    managerChanged(final IlvManager ilvManager)\n
    '''
def getTitleHeight():
    '''returns float\n\n
    getTitleHeight(final IlvManager al, final IlvTransformer ilvTransformer)\n
    '''
def setTopMargin():
    '''returns None\n\n
    setTopMargin(final float q)\n
    '''
def getBottomMargin():
    '''returns float\n\n
    getBottomMargin(final IlvManager ilvManager, final IlvTransformer ilvTransformer)\n
    getBottomMargin()\n
    '''
def setBottomMargin():
    '''returns None\n\n
    setBottomMargin(final float r)\n
    '''
def getRightMargin():
    '''returns float\n\n
    getRightMargin(final IlvManager ilvManager, final IlvTransformer ilvTransformer)\n
    getRightMargin()\n
    '''
def setRightMargin():
    '''returns None\n\n
    setRightMargin(final float t)\n
    '''
def getLeftMargin():
    '''returns float\n\n
    getLeftMargin(final IlvManager ilvManager, final IlvTransformer ilvTransformer)\n
    getLeftMargin()\n
    '''
def setLeftMargin():
    '''returns None\n\n
    setLeftMargin(final float s)\n
    '''
def isOpaque():
    '''returns boolean\n\n
    isOpaque(final IlvManager ilvManager)\n
    isOpaque()\n
    '''
def setOpaque():
    '''returns None\n\n
    setOpaque(final boolean u)\n
    '''
def getTitleColor():
    '''returns Color\n\n
    getTitleColor()\n
    '''
def setTitleColor():
    '''returns None\n\n
    setTitleColor(final Color ac)\n
    '''
def getFont():
    '''returns Font\n\n
    getFont()\n
    '''
def setFont():
    '''returns None\n\n
    setFont(final Font ab)\n
    '''
def getBackground():
    '''returns Paint\n\n
    getBackground()\n
    '''
def setBackground():
    '''returns None\n\n
    setBackground(final Paint w)\n
    '''
def getForeground():
    '''returns Color\n\n
    getForeground()\n
    '''
def setForeground():
    '''returns None\n\n
    setForeground(final Color v)\n
    '''
def isShowingTitle():
    '''returns boolean\n\n
    isShowingTitle()\n
    '''
def setShowingTitle():
    '''returns None\n\n
    setShowingTitle(final boolean aa)\n
    '''
def setTitleJustification():
    '''returns None\n\n
    setTitleJustification(final int ad)\n
    '''
def getTitleJustification():
    '''returns int\n\n
    getTitleJustification()\n
    '''
def setBaseTextDirection():
    '''returns None\n\n
    setBaseTextDirection(final int n)\n
    setBaseTextDirection(final IlvManager ilvManager, final int ai)\n
    '''
def getBaseTextDirection():
    '''returns int\n\n
    getBaseTextDirection()\n
    '''
def getResolvedBaseTextDirection():
    '''returns int\n\n
    getResolvedBaseTextDirection()\n
    getResolvedBaseTextDirection(final IlvManager ilvManager)\n
    '''
def baseTextDirectionChanged():
    '''returns None\n\n
    baseTextDirectionChanged(final IlvManager ilvManager, final int n, final int n2)\n
    '''
def componentOrientationChanged():
    '''returns None\n\n
    componentOrientationChanged(final IlvManager ilvManager, final ComponentOrientation componentOrientation, final ComponentOrientation componentOrientation2)\n
    '''
def localeChanged():
    '''returns None\n\n
    localeChanged(final IlvManager ilvManager, final ULocale uLocale, final ULocale uLocale2)\n
    '''
def draw():
    '''returns None\n\n
    draw(final IlvManager ilvManager, IlvRect a, final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def drawExpandCollapseIcon():
    '''returns None\n\n
    drawExpandCollapseIcon(final IlvManager ilvManager, final IlvRect ilvRect, final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def boundingBoxExpandCollapseIcon():
    '''returns IlvRect\n\n
    boundingBoxExpandCollapseIcon(final IlvManager ilvManager, final IlvRect ilvRect, final IlvTransformer ilvTransformer)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvManager ilvManager, final IlvPoint ilvPoint, final IlvPoint p4, final IlvTransformer ilvTransformer)\n
    '''
def setTitle():
    '''returns None\n\n
    setTitle(final String ag)\n
    '''
def getTitle():
    '''returns String\n\n
    getTitle()\n
    '''
def getMinTitleZoomFactor():
    '''returns double\n\n
    getMinTitleZoomFactor()\n
    '''
def setMinTitleZoomFactor():
    '''returns None\n\n
    setMinTitleZoomFactor(final double ae)\n
    '''
def getMaxTitleZoomFactor():
    '''returns double\n\n
    getMaxTitleZoomFactor()\n
    '''
def setMaxTitleZoomFactor():
    '''returns None\n\n
    setMaxTitleZoomFactor(final double af)\n
    '''
def getShadowThickness():
    '''returns float\n\n
    getShadowThickness()\n
    '''
def setShadowThickness():
    '''returns None\n\n
    setShadowThickness(final float y)\n
    '''
def getShadowPosition():
    '''returns int\n\n
    getShadowPosition()\n
    '''
def setShadowPosition():
    '''returns None\n\n
    setShadowPosition(final int z)\n
    '''
def getShadowPaint():
    '''returns Paint\n\n
    getShadowPaint()\n
    '''
def setShadowPaint():
    '''returns None\n\n
    setShadowPaint(Paint m)\n
    '''
