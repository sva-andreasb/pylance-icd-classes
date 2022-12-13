def IlvLinkImage():
    '''    public IlvLinkImage(final IlvGraphic a, final IlvGraphic b, final boolean c)
    public IlvLinkImage(final IlvLinkImage ilvLinkImage)
    public IlvLinkImage(final IlvInputStream ilvInputStream)
    '''
def copy():
    '''    public IlvGraphic copy()
    '''
def getFrom():
    '''    public final IlvGraphic getFrom()
    '''
def setFrom():
    '''    public void setFrom(final IlvGraphic a)
    '''
def getTo():
    '''    public final IlvGraphic getTo()
    '''
def setTo():
    '''    public void setTo(final IlvGraphic b)
    '''
def getOpposite():
    '''    public final IlvGraphic getOpposite(final IlvGraphic ilvGraphic)
    '''
def getPointsCardinal():
    '''    public int getPointsCardinal()
    '''
def allowsPointInsertion():
    '''    public boolean allowsPointInsertion()
    '''
def allowsPointRemoval():
    '''    public boolean allowsPointRemoval()
    '''
def allowsPointMove():
    '''    public boolean allowsPointMove(final int n)
    '''
def insertPoint():
    '''    public void insertPoint(final int n, final float n2, final float n3, final IlvTransformer ilvTransformer)
    '''
def removePoint():
    '''    public void removePoint(final int n, final IlvTransformer ilvTransformer)
    '''
def getPointAt():
    '''    public IlvPoint getPointAt(final int i, final IlvTransformer ilvTransformer)
    '''
def movePoint():
    '''    public void movePoint(final int n, final float n2, final float n3, final IlvTransformer ilvTransformer)
    '''
def setIntermediateLinkPoints():
    '''    public void setIntermediateLinkPoints(final IlvPoint[] array, final int n, final int n2)
    '''
def pointsInBBox():
    '''    public boolean pointsInBBox()
    '''
def getConnectionReferencePoint():
    '''    public IlvPoint getConnectionReferencePoint(final boolean b, final IlvTransformer ilvTransformer)
    '''
def getConnectionPoints():
    '''    public void getConnectionPoints(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)
    '''
def getLinkConnectorConnectionPoint():
    '''    public final boolean getLinkConnectorConnectionPoint(final boolean b, final IlvPoint ilvPoint, final IlvTransformer ilvTransformer)
    '''
def getToBoundingBox():
    '''    public final IlvRect getToBoundingBox(IlvTransformer a)
    '''
def getFromBoundingBox():
    '''    public final IlvRect getFromBoundingBox(IlvTransformer a)
    '''
def getVisibleFrom():
    '''    public final IlvGraphic getVisibleFrom()
    '''
def getVisibleTo():
    '''    public final IlvGraphic getVisibleTo()
    '''
def getFromTransformer():
    '''    public final IlvTransformer getFromTransformer(final IlvTransformer ilvTransformer)
    '''
def getToTransformer():
    '''    public final IlvTransformer getToTransformer(final IlvTransformer ilvTransformer)
    '''
def getLocalTransformerOf():
    '''    public static IlvTransformer getLocalTransformerOf(final IlvGraphic ilvGraphic, IlvGraphicBag ilvGraphicBag, final IlvTransformer ilvTransformer)
    '''
def isSpline():
    '''    public boolean isSpline()
    '''
def draw():
    '''    public void draw(final Graphics graphics, final IlvTransformer ilvTransformer)
    '''
def boundingBox():
    '''    public IlvRect boundingBox(final IlvTransformer ilvTransformer)
    '''
def applyTransform():
    '''    public void applyTransform(final IlvTransformer ilvTransformer)
    '''
def contains():
    '''    public boolean contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)
    '''
def zoomable():
    '''    public boolean zoomable()
    '''
def isOriented():
    '''    public boolean isOriented()
    '''
def setOriented():
    '''    public void setOriented(final boolean c)
    '''
def setForeground():
    '''    public void setForeground(final Color d)
    '''
def getForeground():
    '''    public Color getForeground()
    '''
def getLineWidth():
    '''    public float getLineWidth()
    public float getLineWidth(final IlvTransformer ilvTransformer)
    '''
def setLineWidth():
    '''    public void setLineWidth(final float f)
    '''
def getEndCap():
    '''    public int getEndCap()
    '''
def setEndCap():
    '''    public void setEndCap(final int n)
    '''
def getLineJoin():
    '''    public int getLineJoin()
    '''
def setLineJoin():
    '''    public void setLineJoin(final int n)
    '''
def getMaximumLineWidth():
    '''    public float getMaximumLineWidth()
    '''
def setMaximumLineWidth():
    '''    public void setMaximumLineWidth(final float f)
    '''
def getLineStyle():
    '''    public float[] getLineStyle()
    '''
def setLineStyle():
    '''    public void setLineStyle(final float[] array)
    '''
def getLinkPoints():
    '''    public IlvPoint[] getLinkPoints(final IlvTransformer ilvTransformer)
    '''
def makeSelection():
    '''    public IlvSelection makeSelection()
    '''
def write():
    '''    public void write(final IlvOutputStream ilvOutputStream)
    '''
def isPersistent():
    '''    public boolean isPersistent()
    '''
