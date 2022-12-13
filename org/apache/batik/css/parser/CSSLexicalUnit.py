UNIT_TEXT_CENTIMETER = "String  cm""
UNIT_TEXT_DEGREE = "String  deg""
UNIT_TEXT_EM = "String  em""
UNIT_TEXT_EX = "String  ex""
UNIT_TEXT_GRADIAN = "String  grad""
UNIT_TEXT_HERTZ = "String  Hz""
UNIT_TEXT_INCH = "String  in""
UNIT_TEXT_KILOHERTZ = "String  kHz""
UNIT_TEXT_MILLIMETER = "String  mm""
UNIT_TEXT_MILLISECOND = "String  ms""
UNIT_TEXT_PERCENTAGE = "String  %""
UNIT_TEXT_PICA = "String  pc""
UNIT_TEXT_PIXEL = "String  px""
UNIT_TEXT_POINT = "String  pt""
UNIT_TEXT_RADIAN = "String  rad""
UNIT_TEXT_REAL = "String  "
UNIT_TEXT_SECOND = "String  s""
TEXT_RGBCOLOR = "String  rgb""
TEXT_RECT_FUNCTION = "String  rect""
TEXT_COUNTER_FUNCTION = "String  counter""
TEXT_COUNTERS_FUNCTION = "String  counters""
def getLexicalUnitType():
'''public short getLexicalUnitType()
'''
pass
def getNextLexicalUnit():
'''public LexicalUnit getNextLexicalUnit()
'''
pass
def setNextLexicalUnit():
'''public void setNextLexicalUnit(final LexicalUnit lu)
'''
pass
def getPreviousLexicalUnit():
'''public LexicalUnit getPreviousLexicalUnit()
'''
pass
def setPreviousLexicalUnit():
'''public void setPreviousLexicalUnit(final LexicalUnit lu)
'''
pass
def getIntegerValue():
'''public int getIntegerValue()
public int getIntegerValue()
'''
pass
def getFloatValue():
'''public float getFloatValue()
public float getFloatValue()
public float getFloatValue()
'''
pass
def getDimensionUnitText():
'''public String getDimensionUnitText()
public String getDimensionUnitText()
'''
pass
def getFunctionName():
'''public String getFunctionName()
public String getFunctionName()
public String getFunctionName()
'''
pass
def getParameters():
'''public LexicalUnit getParameters()
public LexicalUnit getParameters()
public LexicalUnit getParameters()
'''
pass
def getStringValue():
'''public String getStringValue()
public String getStringValue()
'''
pass
def getSubValues():
'''public LexicalUnit getSubValues()
'''
pass
def createSimple():
'''public static CSSLexicalUnit createSimple(final short t, final LexicalUnit prev)
'''
pass
def createInteger():
'''public static CSSLexicalUnit createInteger(final int val, final LexicalUnit prev)
'''
pass
def createFloat():
'''public static CSSLexicalUnit createFloat(final short t, final float val, final LexicalUnit prev)
'''
pass
def createDimension():
'''public static CSSLexicalUnit createDimension(final float val, final String dim, final LexicalUnit prev)
'''
pass
def createFunction():
'''public static CSSLexicalUnit createFunction(final String f, final LexicalUnit params, final LexicalUnit prev)
'''
pass
def createPredefinedFunction():
'''public static CSSLexicalUnit createPredefinedFunction(final short t, final LexicalUnit params, final LexicalUnit prev)
'''
pass
def createString():
'''public static CSSLexicalUnit createString(final short t, final String val, final LexicalUnit prev)
'''
pass
def SimpleLexicalUnit():
'''public SimpleLexicalUnit(final short t, final LexicalUnit prev)
'''
pass
def IntegerLexicalUnit():
'''public IntegerLexicalUnit(final int val, final LexicalUnit prev)
'''
pass
def FloatLexicalUnit():
'''public FloatLexicalUnit(final short t, final float val, final LexicalUnit prev)
'''
pass
def DimensionLexicalUnit():
'''public DimensionLexicalUnit(final float val, final String dim, final LexicalUnit prev)
'''
pass
def FunctionLexicalUnit():
'''public FunctionLexicalUnit(final String f, final LexicalUnit params, final LexicalUnit prev)
'''
pass
def PredefinedFunctionLexicalUnit():
'''public PredefinedFunctionLexicalUnit(final short t, final LexicalUnit params, final LexicalUnit prev)
'''
pass
def StringLexicalUnit():
'''public StringLexicalUnit(final short t, final String val, final LexicalUnit prev)
'''
pass
