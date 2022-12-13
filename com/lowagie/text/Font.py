COURIER = "int  0"
HELVETICA = "int  1"
TIMES_ROMAN = "int  2"
SYMBOL = "int  3"
ZAPFDINGBATS = "int  4"
NORMAL = "int  0"
BOLD = "int  1"
ITALIC = "int  2"
UNDERLINE = "int  4"
STRIKETHRU = "int  8"
BOLDITALIC = "int  3"
UNDEFINED = "int  -1"
DEFAULTSIZE = "int  12"
def Font():
    '''    public Font(final Font other)
    public Font(final int family, final float size, final int style, final Color color)
    public Font(final BaseFont bf, final float size, final int style, final Color color)
    public Font(final BaseFont bf, final float size, final int style)
    public Font(final BaseFont bf, final float size)
    public Font(final BaseFont bf)
    public Font(final int family, final float size, final int style)
    public Font(final int family, final float size)
    public Font(final int family)
    public Font()
    '''
def compareTo():
    '''    public int compareTo(final Object object)
    '''
def setFamily():
    '''    public void setFamily(final String family)
    '''
def getFamilyIndex():
    '''    public static int getFamilyIndex(final String family)
    '''
def getFamilyname():
    '''    public String getFamilyname()
    '''
def setSize():
    '''    public void setSize(final float size)
    '''
def setStyle():
    '''    public void setStyle(final String style)
    public void setStyle(final int style)
    '''
def getStyleValue():
    '''    public static int getStyleValue(final String style)
    '''
def setColor():
    '''    public void setColor(final Color color)
    public void setColor(final int red, final int green, final int blue)
    '''
def leading():
    '''    public float leading(final float linespacing)
    '''
def isStandardFont():
    '''    public boolean isStandardFont()
    '''
def difference():
    '''    public Font difference(final Font font)
    '''
def family():
    '''    public int family()
    '''
def size():
    '''    public float size()
    '''
def style():
    '''    public int style()
    '''
def isBold():
    '''    public boolean isBold()
    '''
def isItalic():
    '''    public boolean isItalic()
    '''
def isUnderlined():
    '''    public boolean isUnderlined()
    '''
def isStrikethru():
    '''    public boolean isStrikethru()
    '''
def color():
    '''    public Color color()
    '''
def getBaseFont():
    '''    public BaseFont getBaseFont()
    '''
def getCalculatedBaseFont():
    '''    public BaseFont getCalculatedBaseFont(final boolean specialEncoding)
    '''
def getCalculatedStyle():
    '''    public int getCalculatedStyle()
    '''
def getCalculatedSize():
    '''    public float getCalculatedSize()
    '''
