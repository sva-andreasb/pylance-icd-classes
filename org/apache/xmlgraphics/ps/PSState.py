DEFAULT_DASH = "String  \"[] 0\""
def ():
    '''returns PSState\n\n
    ()\n
    (final PSState org, final boolean copyTransforms)\n
    '''
def getTransform():
    '''returns AffineTransform\n\n
    getTransform()\n
    '''
def checkTransform():
    '''returns boolean\n\n
    checkTransform(final AffineTransform tf)\n
    '''
def concatMatrix():
    '''returns None\n\n
    concatMatrix(final AffineTransform transform)\n
    '''
def useLineCap():
    '''returns boolean\n\n
    useLineCap(final int value)\n
    '''
def useLineJoin():
    '''returns boolean\n\n
    useLineJoin(final int value)\n
    '''
def useMiterLimit():
    '''returns boolean\n\n
    useMiterLimit(final float value)\n
    '''
def useLineWidth():
    '''returns boolean\n\n
    useLineWidth(final double value)\n
    '''
def useDash():
    '''returns boolean\n\n
    useDash(final String pattern)\n
    '''
def useColor():
    '''returns boolean\n\n
    useColor(final Color value)\n
    '''
def useFont():
    '''returns boolean\n\n
    useFont(final String name, final float size)\n
    '''
def reestablish():
    '''returns None\n\n
    reestablish(final PSGenerator gen)\n
    '''
