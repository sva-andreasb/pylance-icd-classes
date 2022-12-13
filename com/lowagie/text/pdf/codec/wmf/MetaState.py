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
def MetaState():
    '''    public MetaState()
    public MetaState(final MetaState state)
    '''
def setMetaState():
    '''    public void setMetaState(final MetaState state)
    '''
def addMetaObject():
    '''    public void addMetaObject(final MetaObject object)
    '''
def selectMetaObject():
    '''    public void selectMetaObject(final int index, final PdfContentByte cb)
    '''
def deleteMetaObject():
    '''    public void deleteMetaObject(final int index)
    '''
def saveState():
    '''    public void saveState(final PdfContentByte cb)
    '''
def restoreState():
    '''    public void restoreState(final int index, final PdfContentByte cb)
    '''
def transformX():
    '''    public float transformX(final int x)
    '''
def transformY():
    '''    public float transformY(final int y)
    '''
def setScalingX():
    '''    public void setScalingX(final float scalingX)
    '''
def setScalingY():
    '''    public void setScalingY(final float scalingY)
    '''
def setOffsetWx():
    '''    public void setOffsetWx(final int offsetWx)
    '''
def setOffsetWy():
    '''    public void setOffsetWy(final int offsetWy)
    '''
def setExtentWx():
    '''    public void setExtentWx(final int extentWx)
    '''
def setExtentWy():
    '''    public void setExtentWy(final int extentWy)
    '''
def transformAngle():
    '''    public float transformAngle(final float angle)
    '''
def setCurrentPoint():
    '''    public void setCurrentPoint(final Point p)
    '''
def getCurrentPoint():
    '''    public Point getCurrentPoint()
    '''
def getCurrentBrush():
    '''    public MetaBrush getCurrentBrush()
    '''
def getCurrentPen():
    '''    public MetaPen getCurrentPen()
    '''
def getCurrentFont():
    '''    public MetaFont getCurrentFont()
    '''
def getCurrentBackgroundColor():
    '''    public Color getCurrentBackgroundColor()
    '''
def setCurrentBackgroundColor():
    '''    public void setCurrentBackgroundColor(final Color currentBackgroundColor)
    '''
def getCurrentTextColor():
    '''    public Color getCurrentTextColor()
    '''
def setCurrentTextColor():
    '''    public void setCurrentTextColor(final Color currentTextColor)
    '''
def getBackgroundMode():
    '''    public int getBackgroundMode()
    '''
def setBackgroundMode():
    '''    public void setBackgroundMode(final int backgroundMode)
    '''
def getTextAlign():
    '''    public int getTextAlign()
    '''
def setTextAlign():
    '''    public void setTextAlign(final int textAlign)
    '''
def getPolyFillMode():
    '''    public int getPolyFillMode()
    '''
def setPolyFillMode():
    '''    public void setPolyFillMode(final int polyFillMode)
    '''
def setLineJoinRectangle():
    '''    public void setLineJoinRectangle(final PdfContentByte cb)
    '''
def setLineJoinPolygon():
    '''    public void setLineJoinPolygon(final PdfContentByte cb)
    '''
def getLineNeutral():
    '''    public boolean getLineNeutral()
    '''
