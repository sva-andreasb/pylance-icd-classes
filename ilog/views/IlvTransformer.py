def IlvTransformer():
    '''    public IlvTransformer()
    public IlvTransformer(final IlvTransformer ilvTransformer)
    public IlvTransformer(final double a, final double b, final double c, final double d, final double e, final double f)
    public IlvTransformer(final AffineTransform affineTransform)
    public IlvTransformer(final IlvPoint ilvPoint, double degreesToRadians)
    public IlvTransformer(final double n, final double n2, final IlvPoint ilvPoint)
    public IlvTransformer(final IlvPoint ilvPoint)
    '''
def setValues():
    '''    public final void setValues(final double e, final double f)
    public void setValues(final double a, final double b, final double c, final double d)
    public void setValues(final double a, final double b, final double c, final double d, final double e, final double f)
    '''
def setAffineTransform():
    '''    public void setAffineTransform(final AffineTransform affineTransform)
    '''
def getAffineTransform():
    '''    public AffineTransform getAffineTransform(final AffineTransform affineTransform)
    '''
def getx0():
    '''    public double getx0()
    '''
def gety0():
    '''    public double gety0()
    '''
def getx11():
    '''    public double getx11()
    '''
def getx12():
    '''    public double getx12()
    '''
def getx21():
    '''    public double getx21()
    '''
def getx22():
    '''    public double getx22()
    '''
def isIdentity():
    '''    public boolean isIdentity()
    '''
def isTranslation():
    '''    public boolean isTranslation()
    '''
def isScale():
    '''    public boolean isScale()
    '''
def isBad():
    '''    public boolean isBad()
    '''
def getDeterminant():
    '''    public double getDeterminant()
    '''
def apply():
    '''    public void apply(final IlvPoint ilvPoint)
    public void apply(final IlvRect ilvRect)
    '''
def applyFloor():
    '''    public void applyFloor(final IlvPoint ilvPoint)
    public void applyFloor(final IlvRect ilvRect)
    '''
def boundingBox():
    '''    public void boundingBox(final IlvRect ilvRect, final boolean b)
    '''
def deltaApply():
    '''    public void deltaApply(final IlvPoint ilvPoint)
    '''
def inverse():
    '''    public boolean inverse(final IlvPoint ilvPoint)
    public boolean inverse(final IlvRect ilvRect)
    '''
def compose():
    '''    public void compose(final IlvTransformer ilvTransformer)
    '''
def postCompose():
    '''    public void postCompose(final IlvTransformer ilvTransformer)
    '''
def computeInverse():
    '''    public boolean computeInverse(final IlvTransformer ilvTransformer)
    '''
def translate():
    '''    public void translate(final double n, final double n2)
    '''
def scale():
    '''    public void scale(final double n, final double n2, final double n3, final double n4)
    '''
def rotate():
    '''    public void rotate(final double n, final double n2, double degreesToRadians)
    '''
def computeTransformer():
    '''    public static IlvTransformer computeTransformer(final IlvRect ilvRect, final IlvRect ilvRect2, IlvTransformer ilvTransformer)
    '''
def zoomFactor():
    '''    public double zoomFactor()
    '''
def zoomXFactor():
    '''    public double zoomXFactor()
    '''
def zoomYFactor():
    '''    public double zoomYFactor()
    '''
def clone():
    '''    public Object clone()
    '''
def equals():
    '''    public boolean equals(final Object o)
    '''
def hashCode():
    '''    public int hashCode()
    '''
def toString():
    '''    public String toString()
    '''
