TA_NOUPDATECP = "int  0"
TA_UPDATECP = "int  1"
TA_LEFT = "int  0"
TA_RIGHT = "int  2"
TA_CENTER = "int  6"
TA_TOP = "int  0"
TA_BOTTOM = "int  8"
TA_BASELINE = "int  24"
TRANSPARENT = "int  1"
OPAQUE = "int  2"
ALTERNATE = "int  1"
WINDING = "int  2"
def ():
    '''returns MetaState\n\n
    ()\n
    (final MetaState state)\n
    '''
def setMetaState():
    '''returns None\n\n
    setMetaState(final MetaState state)\n
    '''
def addMetaObject():
    '''returns None\n\n
    addMetaObject(final MetaObject object)\n
    '''
def selectMetaObject():
    '''returns None\n\n
    selectMetaObject(final int index, final PdfContentByte cb)\n
    '''
def deleteMetaObject():
    '''returns None\n\n
    deleteMetaObject(final int index)\n
    '''
def saveState():
    '''returns None\n\n
    saveState(final PdfContentByte cb)\n
    '''
def restoreState():
    '''returns None\n\n
    restoreState(final int index, final PdfContentByte cb)\n
    '''
def transformX():
    '''returns float\n\n
    transformX(final int x)\n
    '''
def transformY():
    '''returns float\n\n
    transformY(final int y)\n
    '''
def setScalingX():
    '''returns None\n\n
    setScalingX(final float scalingX)\n
    '''
def setScalingY():
    '''returns None\n\n
    setScalingY(final float scalingY)\n
    '''
def setOffsetWx():
    '''returns None\n\n
    setOffsetWx(final int offsetWx)\n
    '''
def setOffsetWy():
    '''returns None\n\n
    setOffsetWy(final int offsetWy)\n
    '''
def setExtentWx():
    '''returns None\n\n
    setExtentWx(final int extentWx)\n
    '''
def setExtentWy():
    '''returns None\n\n
    setExtentWy(final int extentWy)\n
    '''
def transformAngle():
    '''returns float\n\n
    transformAngle(final float angle)\n
    '''
def setCurrentPoint():
    '''returns None\n\n
    setCurrentPoint(final Point p)\n
    '''
def getCurrentPoint():
    '''returns Point\n\n
    getCurrentPoint()\n
    '''
def getCurrentBrush():
    '''returns MetaBrush\n\n
    getCurrentBrush()\n
    '''
def getCurrentPen():
    '''returns MetaPen\n\n
    getCurrentPen()\n
    '''
def getCurrentFont():
    '''returns MetaFont\n\n
    getCurrentFont()\n
    '''
def getCurrentBackgroundColor():
    '''returns Color\n\n
    getCurrentBackgroundColor()\n
    '''
def setCurrentBackgroundColor():
    '''returns None\n\n
    setCurrentBackgroundColor(final Color currentBackgroundColor)\n
    '''
def getCurrentTextColor():
    '''returns Color\n\n
    getCurrentTextColor()\n
    '''
def setCurrentTextColor():
    '''returns None\n\n
    setCurrentTextColor(final Color currentTextColor)\n
    '''
def getBackgroundMode():
    '''returns int\n\n
    getBackgroundMode()\n
    '''
def setBackgroundMode():
    '''returns None\n\n
    setBackgroundMode(final int backgroundMode)\n
    '''
def getTextAlign():
    '''returns int\n\n
    getTextAlign()\n
    '''
def setTextAlign():
    '''returns None\n\n
    setTextAlign(final int textAlign)\n
    '''
def getPolyFillMode():
    '''returns int\n\n
    getPolyFillMode()\n
    '''
def setPolyFillMode():
    '''returns None\n\n
    setPolyFillMode(final int polyFillMode)\n
    '''
def setLineJoinRectangle():
    '''returns None\n\n
    setLineJoinRectangle(final PdfContentByte cb)\n
    '''
def setLineJoinPolygon():
    '''returns None\n\n
    setLineJoinPolygon(final PdfContentByte cb)\n
    '''
def getLineNeutral():
    '''returns boolean\n\n
    getLineNeutral()\n
    '''
