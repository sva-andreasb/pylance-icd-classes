def IlvTransformer():
'''public IlvTransformer()
public IlvTransformer(final IlvTransformer ilvTransformer)
public IlvTransformer(final double a, final double b, final double c, final double d, final double e, final double f)
public IlvTransformer(final AffineTransform affineTransform)
public IlvTransformer(final IlvPoint ilvPoint, double degreesToRadians)
public IlvTransformer(final double n, final double n2, final IlvPoint ilvPoint)
public IlvTransformer(final IlvPoint ilvPoint)
'''
pass
def setValues():
'''public final void setValues(final double e, final double f)
public void setValues(final double a, final double b, final double c, final double d)
public void setValues(final double a, final double b, final double c, final double d, final double e, final double f)
'''
pass
def setAffineTransform():
'''public void setAffineTransform(final AffineTransform affineTransform)
'''
pass
def getAffineTransform():
'''public AffineTransform getAffineTransform(final AffineTransform affineTransform)
'''
pass
def getx0():
'''public double getx0()
'''
pass
def gety0():
'''public double gety0()
'''
pass
def getx11():
'''public double getx11()
'''
pass
def getx12():
'''public double getx12()
'''
pass
def getx21():
'''public double getx21()
'''
pass
def getx22():
'''public double getx22()
'''
pass
def isIdentity():
'''public boolean isIdentity()
'''
pass
def isTranslation():
'''public boolean isTranslation()
'''
pass
def isScale():
'''public boolean isScale()
'''
pass
def isBad():
'''public boolean isBad()
'''
pass
def getDeterminant():
'''public double getDeterminant()
'''
pass
def apply():
'''public void apply(final IlvPoint ilvPoint)
public void apply(final IlvRect ilvRect)
'''
pass
def applyFloor():
'''public void applyFloor(final IlvPoint ilvPoint)
public void applyFloor(final IlvRect ilvRect)
'''
pass
def boundingBox():
'''public void boundingBox(final IlvRect ilvRect, final boolean b)
'''
pass
def deltaApply():
'''public void deltaApply(final IlvPoint ilvPoint)
'''
pass
def inverse():
'''public boolean inverse(final IlvPoint ilvPoint)
public boolean inverse(final IlvRect ilvRect)
'''
pass
def compose():
'''public void compose(final IlvTransformer ilvTransformer)
'''
pass
def postCompose():
'''public void postCompose(final IlvTransformer ilvTransformer)
'''
pass
def computeInverse():
'''public boolean computeInverse(final IlvTransformer ilvTransformer)
'''
pass
def translate():
'''public void translate(final double n, final double n2)
'''
pass
def scale():
'''public void scale(final double n, final double n2, final double n3, final double n4)
'''
pass
def rotate():
'''public void rotate(final double n, final double n2, double degreesToRadians)
'''
pass
def computeTransformer():
'''public static IlvTransformer computeTransformer(final IlvRect ilvRect, final IlvRect ilvRect2, IlvTransformer ilvTransformer)
'''
pass
def zoomFactor():
'''public double zoomFactor()
'''
pass
def zoomXFactor():
'''public double zoomXFactor()
'''
pass
def zoomYFactor():
'''public double zoomYFactor()
'''
pass
def clone():
'''public Object clone()
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def toString():
'''public String toString()
'''
pass