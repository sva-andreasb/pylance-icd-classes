sid = "short  6"
STRING = "int  0"
BOOLEAN = "int  1"
ERROR_CODE = "int  2"
EMPTY = "int  3"
def FormulaRecord():
    '''    public FormulaRecord()
    public FormulaRecord(final RecordInputStream ris)
    '''
def setValue():
    '''    public void setValue(final double value)
    '''
def setCachedResultTypeEmptyString():
    '''    public void setCachedResultTypeEmptyString()
    '''
def setCachedResultTypeString():
    '''    public void setCachedResultTypeString()
    '''
def setCachedResultErrorCode():
    '''    public void setCachedResultErrorCode(final int errorCode)
    '''
def setCachedResultBoolean():
    '''    public void setCachedResultBoolean(final boolean value)
    '''
def hasCachedResultString():
    '''    public boolean hasCachedResultString()
    '''
def getCachedResultType():
    '''    public int getCachedResultType()
    '''
def getCachedBooleanValue():
    '''    public boolean getCachedBooleanValue()
    '''
def getCachedErrorValue():
    '''    public int getCachedErrorValue()
    '''
def setOptions():
    '''    public void setOptions(final short options)
    '''
def getValue():
    '''    public double getValue()
    '''
def getOptions():
    '''    public short getOptions()
    '''
def isSharedFormula():
    '''    public boolean isSharedFormula()
    '''
def setSharedFormula():
    '''    public void setSharedFormula(final boolean flag)
    '''
def isAlwaysCalc():
    '''    public boolean isAlwaysCalc()
    '''
def setAlwaysCalc():
    '''    public void setAlwaysCalc(final boolean flag)
    '''
def isCalcOnLoad():
    '''    public boolean isCalcOnLoad()
    '''
def setCalcOnLoad():
    '''    public void setCalcOnLoad(final boolean flag)
    '''
def getParsedExpression():
    '''    public Ptg[] getParsedExpression()
    '''
def getFormula():
    '''    public Formula getFormula()
    '''
def setParsedExpression():
    '''    public void setParsedExpression(final Ptg[] ptgs)
    '''
def getSid():
    '''    public short getSid()
    '''
def clone():
    '''    public FormulaRecord clone()
    '''
def getTypeCode():
    '''    public int getTypeCode()
    '''
def create():
    '''    public static SpecialCachedValue create(final long valueLongBits)
    '''
def serialize():
    '''    public void serialize(final LittleEndianOutput out)
    '''
def formatDebugString():
    '''    public String formatDebugString()
    '''
def createCachedEmptyValue():
    '''    public static SpecialCachedValue createCachedEmptyValue()
    '''
def createForString():
    '''    public static SpecialCachedValue createForString()
    '''
def createCachedBoolean():
    '''    public static SpecialCachedValue createCachedBoolean(final boolean b)
    '''
def createCachedErrorCode():
    '''    public static SpecialCachedValue createCachedErrorCode(final int errorCode)
    '''
def toString():
    '''    public String toString()
    '''
def getValueType():
    '''    public int getValueType()
    '''
def getBooleanValue():
    '''    public boolean getBooleanValue()
    '''
def getErrorValue():
    '''    public int getErrorValue()
    '''
