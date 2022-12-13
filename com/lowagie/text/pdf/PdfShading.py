def throwColorSpaceError():
    '''    public static void throwColorSpaceError()
    '''
def checkCompatibleColors():
    '''    public static void checkCompatibleColors(final Color c1, final Color c2)
    '''
def getColorArray():
    '''    public static float[] getColorArray(final Color color)
    '''
def type1():
    '''    public static PdfShading type1(final PdfWriter writer, final Color colorSpace, final float[] domain, final float[] tMatrix, final PdfFunction function)
    '''
def type2():
    '''    public static PdfShading type2(final PdfWriter writer, final Color colorSpace, final float[] coords, final float[] domain, final PdfFunction function, final boolean[] extend)
    '''
def type3():
    '''    public static PdfShading type3(final PdfWriter writer, final Color colorSpace, final float[] coords, final float[] domain, final PdfFunction function, final boolean[] extend)
    '''
def simpleAxial():
    '''    public static PdfShading simpleAxial(final PdfWriter writer, final float x0, final float y0, final float x1, final float y1, final Color startColor, final Color endColor, final boolean extendStart, final boolean extendEnd)
    public static PdfShading simpleAxial(final PdfWriter writer, final float x0, final float y0, final float x1, final float y1, final Color startColor, final Color endColor)
    '''
def simpleRadial():
    '''    public static PdfShading simpleRadial(final PdfWriter writer, final float x0, final float y0, final float r0, final float x1, final float y1, final float r1, final Color startColor, final Color endColor, final boolean extendStart, final boolean extendEnd)
    public static PdfShading simpleRadial(final PdfWriter writer, final float x0, final float y0, final float r0, final float x1, final float y1, final float r1, final Color startColor, final Color endColor)
    '''
def getBBox():
    '''    public float[] getBBox()
    '''
def setBBox():
    '''    public void setBBox(final float[] bBox)
    '''
def isAntiAlias():
    '''    public boolean isAntiAlias()
    '''
def setAntiAlias():
    '''    public void setAntiAlias(final boolean antiAlias)
    '''
