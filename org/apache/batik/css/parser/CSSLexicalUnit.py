UNIT_TEXT_CENTIMETER = "String  \"cm\""
UNIT_TEXT_DEGREE = "String  \"deg\""
UNIT_TEXT_EM = "String  \"em\""
UNIT_TEXT_EX = "String  \"ex\""
UNIT_TEXT_GRADIAN = "String  \"grad\""
UNIT_TEXT_HERTZ = "String  \"Hz\""
UNIT_TEXT_INCH = "String  \"in\""
UNIT_TEXT_KILOHERTZ = "String  \"kHz\""
UNIT_TEXT_MILLIMETER = "String  \"mm\""
UNIT_TEXT_MILLISECOND = "String  \"ms\""
UNIT_TEXT_PERCENTAGE = "String  \"%\""
UNIT_TEXT_PICA = "String  \"pc\""
UNIT_TEXT_PIXEL = "String  \"px\""
UNIT_TEXT_POINT = "String  \"pt\""
UNIT_TEXT_RADIAN = "String  \"rad\""
UNIT_TEXT_REAL = "String  \"\""
UNIT_TEXT_SECOND = "String  \"s\""
TEXT_RGBCOLOR = "String  \"rgb\""
TEXT_RECT_FUNCTION = "String  \"rect\""
TEXT_COUNTER_FUNCTION = "String  \"counter\""
TEXT_COUNTERS_FUNCTION = "String  \"counters\""
def getLexicalUnitType():
    '''    public short getLexicalUnitType()
    '''
def getNextLexicalUnit():
    '''    public LexicalUnit getNextLexicalUnit()
    '''
def setNextLexicalUnit():
    '''    public void setNextLexicalUnit(final LexicalUnit lu)
    '''
def getPreviousLexicalUnit():
    '''    public LexicalUnit getPreviousLexicalUnit()
    '''
def setPreviousLexicalUnit():
    '''    public void setPreviousLexicalUnit(final LexicalUnit lu)
    '''
def getIntegerValue():
    '''    public int getIntegerValue()
    public int getIntegerValue()
    '''
def getFloatValue():
    '''    public float getFloatValue()
    public float getFloatValue()
    public float getFloatValue()
    '''
def getDimensionUnitText():
    '''    public String getDimensionUnitText()
    public String getDimensionUnitText()
    '''
def getFunctionName():
    '''    public String getFunctionName()
    public String getFunctionName()
    public String getFunctionName()
    '''
def getParameters():
    '''    public LexicalUnit getParameters()
    public LexicalUnit getParameters()
    public LexicalUnit getParameters()
    '''
def getStringValue():
    '''    public String getStringValue()
    public String getStringValue()
    '''
def getSubValues():
    '''    public LexicalUnit getSubValues()
    '''
def createSimple():
    '''    public static CSSLexicalUnit createSimple(final short t, final LexicalUnit prev)
    '''
def createInteger():
    '''    public static CSSLexicalUnit createInteger(final int val, final LexicalUnit prev)
    '''
def createFloat():
    '''    public static CSSLexicalUnit createFloat(final short t, final float val, final LexicalUnit prev)
    '''
def createDimension():
    '''    public static CSSLexicalUnit createDimension(final float val, final String dim, final LexicalUnit prev)
    '''
def createFunction():
    '''    public static CSSLexicalUnit createFunction(final String f, final LexicalUnit params, final LexicalUnit prev)
    '''
def createPredefinedFunction():
    '''    public static CSSLexicalUnit createPredefinedFunction(final short t, final LexicalUnit params, final LexicalUnit prev)
    '''
def createString():
    '''    public static CSSLexicalUnit createString(final short t, final String val, final LexicalUnit prev)
    '''
def SimpleLexicalUnit():
    '''    public SimpleLexicalUnit(final short t, final LexicalUnit prev)
    '''
def IntegerLexicalUnit():
    '''    public IntegerLexicalUnit(final int val, final LexicalUnit prev)
    '''
def FloatLexicalUnit():
    '''    public FloatLexicalUnit(final short t, final float val, final LexicalUnit prev)
    '''
def DimensionLexicalUnit():
    '''    public DimensionLexicalUnit(final float val, final String dim, final LexicalUnit prev)
    '''
def FunctionLexicalUnit():
    '''    public FunctionLexicalUnit(final String f, final LexicalUnit params, final LexicalUnit prev)
    '''
def PredefinedFunctionLexicalUnit():
    '''    public PredefinedFunctionLexicalUnit(final short t, final LexicalUnit params, final LexicalUnit prev)
    '''
def StringLexicalUnit():
    '''    public StringLexicalUnit(final short t, final String val, final LexicalUnit prev)
    '''
