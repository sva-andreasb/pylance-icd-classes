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
'''public MetaState()
public MetaState(final MetaState state)
'''
pass
def setMetaState():
'''public void setMetaState(final MetaState state)
'''
pass
def addMetaObject():
'''public void addMetaObject(final MetaObject object)
'''
pass
def selectMetaObject():
'''public void selectMetaObject(final int index, final PdfContentByte cb)
'''
pass
def deleteMetaObject():
'''public void deleteMetaObject(final int index)
'''
pass
def saveState():
'''public void saveState(final PdfContentByte cb)
'''
pass
def restoreState():
'''public void restoreState(final int index, final PdfContentByte cb)
'''
pass
def transformX():
'''public float transformX(final int x)
'''
pass
def transformY():
'''public float transformY(final int y)
'''
pass
def setScalingX():
'''public void setScalingX(final float scalingX)
'''
pass
def setScalingY():
'''public void setScalingY(final float scalingY)
'''
pass
def setOffsetWx():
'''public void setOffsetWx(final int offsetWx)
'''
pass
def setOffsetWy():
'''public void setOffsetWy(final int offsetWy)
'''
pass
def setExtentWx():
'''public void setExtentWx(final int extentWx)
'''
pass
def setExtentWy():
'''public void setExtentWy(final int extentWy)
'''
pass
def transformAngle():
'''public float transformAngle(final float angle)
'''
pass
def setCurrentPoint():
'''public void setCurrentPoint(final Point p)
'''
pass
def getCurrentPoint():
'''public Point getCurrentPoint()
'''
pass
def getCurrentBrush():
'''public MetaBrush getCurrentBrush()
'''
pass
def getCurrentPen():
'''public MetaPen getCurrentPen()
'''
pass
def getCurrentFont():
'''public MetaFont getCurrentFont()
'''
pass
def getCurrentBackgroundColor():
'''public Color getCurrentBackgroundColor()
'''
pass
def setCurrentBackgroundColor():
'''public void setCurrentBackgroundColor(final Color currentBackgroundColor)
'''
pass
def getCurrentTextColor():
'''public Color getCurrentTextColor()
'''
pass
def setCurrentTextColor():
'''public void setCurrentTextColor(final Color currentTextColor)
'''
pass
def getBackgroundMode():
'''public int getBackgroundMode()
'''
pass
def setBackgroundMode():
'''public void setBackgroundMode(final int backgroundMode)
'''
pass
def getTextAlign():
'''public int getTextAlign()
'''
pass
def setTextAlign():
'''public void setTextAlign(final int textAlign)
'''
pass
def getPolyFillMode():
'''public int getPolyFillMode()
'''
pass
def setPolyFillMode():
'''public void setPolyFillMode(final int polyFillMode)
'''
pass
def setLineJoinRectangle():
'''public void setLineJoinRectangle(final PdfContentByte cb)
'''
pass
def setLineJoinPolygon():
'''public void setLineJoinPolygon(final PdfContentByte cb)
'''
pass
def getLineNeutral():
'''public boolean getLineNeutral()
'''
pass
