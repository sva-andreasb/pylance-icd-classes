def IlvLinkImage():
'''public IlvLinkImage(final IlvGraphic a, final IlvGraphic b, final boolean c)
public IlvLinkImage(final IlvLinkImage ilvLinkImage)
public IlvLinkImage(final IlvInputStream ilvInputStream)
'''
pass
def copy():
'''public IlvGraphic copy()
'''
pass
def getFrom():
'''public final IlvGraphic getFrom()
'''
pass
def setFrom():
'''public void setFrom(final IlvGraphic a)
'''
pass
def getTo():
'''public final IlvGraphic getTo()
'''
pass
def setTo():
'''public void setTo(final IlvGraphic b)
'''
pass
def getOpposite():
'''public final IlvGraphic getOpposite(final IlvGraphic ilvGraphic)
'''
pass
def getPointsCardinal():
'''public int getPointsCardinal()
'''
pass
def allowsPointInsertion():
'''public boolean allowsPointInsertion()
'''
pass
def allowsPointRemoval():
'''public boolean allowsPointRemoval()
'''
pass
def allowsPointMove():
'''public boolean allowsPointMove(final int n)
'''
pass
def insertPoint():
'''public void insertPoint(final int n, final float n2, final float n3, final IlvTransformer ilvTransformer)
'''
pass
def removePoint():
'''public void removePoint(final int n, final IlvTransformer ilvTransformer)
'''
pass
def getPointAt():
'''public IlvPoint getPointAt(final int i, final IlvTransformer ilvTransformer)
'''
pass
def movePoint():
'''public void movePoint(final int n, final float n2, final float n3, final IlvTransformer ilvTransformer)
'''
pass
def setIntermediateLinkPoints():
'''public void setIntermediateLinkPoints(final IlvPoint[] array, final int n, final int n2)
'''
pass
def pointsInBBox():
'''public boolean pointsInBBox()
'''
pass
def getConnectionReferencePoint():
'''public IlvPoint getConnectionReferencePoint(final boolean b, final IlvTransformer ilvTransformer)
'''
pass
def getConnectionPoints():
'''public void getConnectionPoints(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)
'''
pass
def getLinkConnectorConnectionPoint():
'''public final boolean getLinkConnectorConnectionPoint(final boolean b, final IlvPoint ilvPoint, final IlvTransformer ilvTransformer)
'''
pass
def getToBoundingBox():
'''public final IlvRect getToBoundingBox(IlvTransformer a)
'''
pass
def getFromBoundingBox():
'''public final IlvRect getFromBoundingBox(IlvTransformer a)
'''
pass
def getVisibleFrom():
'''public final IlvGraphic getVisibleFrom()
'''
pass
def getVisibleTo():
'''public final IlvGraphic getVisibleTo()
'''
pass
def getFromTransformer():
'''public final IlvTransformer getFromTransformer(final IlvTransformer ilvTransformer)
'''
pass
def getToTransformer():
'''public final IlvTransformer getToTransformer(final IlvTransformer ilvTransformer)
'''
pass
def getLocalTransformerOf():
'''public static IlvTransformer getLocalTransformerOf(final IlvGraphic ilvGraphic, IlvGraphicBag ilvGraphicBag, final IlvTransformer ilvTransformer)
'''
pass
def isSpline():
'''public boolean isSpline()
'''
pass
def draw():
'''public void draw(final Graphics graphics, final IlvTransformer ilvTransformer)
'''
pass
def boundingBox():
'''public IlvRect boundingBox(final IlvTransformer ilvTransformer)
'''
pass
def applyTransform():
'''public void applyTransform(final IlvTransformer ilvTransformer)
'''
pass
def contains():
'''public boolean contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)
'''
pass
def zoomable():
'''public boolean zoomable()
'''
pass
def isOriented():
'''public boolean isOriented()
'''
pass
def setOriented():
'''public void setOriented(final boolean c)
'''
pass
def setForeground():
'''public void setForeground(final Color d)
'''
pass
def getForeground():
'''public Color getForeground()
'''
pass
def getLineWidth():
'''public float getLineWidth()
public float getLineWidth(final IlvTransformer ilvTransformer)
'''
pass
def setLineWidth():
'''public void setLineWidth(final float f)
'''
pass
def getEndCap():
'''public int getEndCap()
'''
pass
def setEndCap():
'''public void setEndCap(final int n)
'''
pass
def getLineJoin():
'''public int getLineJoin()
'''
pass
def setLineJoin():
'''public void setLineJoin(final int n)
'''
pass
def getMaximumLineWidth():
'''public float getMaximumLineWidth()
'''
pass
def setMaximumLineWidth():
'''public void setMaximumLineWidth(final float f)
'''
pass
def getLineStyle():
'''public float[] getLineStyle()
'''
pass
def setLineStyle():
'''public void setLineStyle(final float[] array)
'''
pass
def getLinkPoints():
'''public IlvPoint[] getLinkPoints(final IlvTransformer ilvTransformer)
'''
pass
def makeSelection():
'''public IlvSelection makeSelection()
'''
pass
def write():
'''public void write(final IlvOutputStream ilvOutputStream)
'''
pass
def isPersistent():
'''public boolean isPersistent()
'''
pass
