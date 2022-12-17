def ():
    '''returns IlvGraphicHandle\n\n
    (final IlvGraphic ilvGraphic, final boolean b)\n
    (final IlvGraphicHandle ilvGraphicHandle)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def setObject():
    '''returns None\n\n
    setObject(final IlvGraphic a)\n
    '''
def isOwner():
    '''returns boolean\n\n
    isOwner()\n
    '''
def setOwner():
    '''returns None\n\n
    setOwner(final boolean b)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def zoomable():
    '''returns boolean\n\n
    zoomable()\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def intersects():
    '''returns boolean\n\n
    intersects(final IlvRect ilvRect, final IlvRect ilvRect2, final IlvTransformer ilvTransformer)\n
    '''
def inside():
    '''returns boolean\n\n
    inside(final IlvRect ilvRect, final IlvRect ilvRect2, final IlvTransformer ilvTransformer)\n
    '''
def getIntersectionWithOutline():
    '''returns IlvPoint\n\n
    getIntersectionWithOutline(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def move():
    '''returns None\n\n
    move(final float n, final float n2)\n
    move(final IlvPoint ilvPoint)\n
    '''
def moveResize():
    '''returns None\n\n
    moveResize(final IlvRect ilvRect)\n
    '''
def translate():
    '''returns None\n\n
    translate(final float n, final float n2)\n
    '''
def rotate():
    '''returns None\n\n
    rotate(final IlvPoint ilvPoint, final double n)\n
    '''
def scale():
    '''returns None\n\n
    scale(final double n, final double n2)\n
    '''
def resize():
    '''returns None\n\n
    resize(final float n, final float n2)\n
    '''
def setForeground():
    '''returns None\n\n
    setForeground(final Color foreground)\n
    '''
def setBackground():
    '''returns None\n\n
    setBackground(final Color background)\n
    '''
def getToolTipText():
    '''returns String\n\n
    getToolTipText(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer)\n
    '''
def getPopupMenu():
    '''returns JPopupMenu\n\n
    getPopupMenu(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer, final IlvManagerView ilvManagerView, final IlvPopupMenuManager ilvPopupMenuManager)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def isPersistent():
    '''returns boolean\n\n
    isPersistent()\n
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
def usesBidiMarkers():
    '''returns boolean\n\n
    usesBidiMarkers()\n
    '''
def getResolvedBaseTextDirection():
    '''returns int\n\n
    getResolvedBaseTextDirection()\n
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
