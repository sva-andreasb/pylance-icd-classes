def clone():
    '''public Object clone()
    '''
def createTranslateElement():
    '''public static TransformStackElement createTranslateElement(final double tx, final double ty)
    '''
def createRotateElement():
    '''public static TransformStackElement createRotateElement(final double theta)
    '''
def createScaleElement():
    '''public static TransformStackElement createScaleElement(final double scaleX, final double scaleY)
    '''
def createShearElement():
    '''public static TransformStackElement createShearElement(final double shearX, final double shearY)
    '''
def createGeneralTransformElement():
    '''public static TransformStackElement createGeneralTransformElement(final AffineTransform txf)
    '''
def isIdentity():
    '''public boolean isIdentity()
    '''
def getTransformParameters():
    '''public double[] getTransformParameters()
    '''
def getType():
    '''public TransformType getType()
    '''
def concatenate():
    '''public boolean concatenate(final TransformStackElement stackElement)
    '''
