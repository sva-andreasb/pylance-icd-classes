sid = "short  6"
STRING = "int  0"
BOOLEAN = "int  1"
ERROR_CODE = "int  2"
EMPTY = "int  3"
def FormulaRecord():
'''public FormulaRecord()
public FormulaRecord(final RecordInputStream ris)
'''
pass
def setValue():
'''public void setValue(final double value)
'''
pass
def setCachedResultTypeEmptyString():
'''public void setCachedResultTypeEmptyString()
'''
pass
def setCachedResultTypeString():
'''public void setCachedResultTypeString()
'''
pass
def setCachedResultErrorCode():
'''public void setCachedResultErrorCode(final int errorCode)
'''
pass
def setCachedResultBoolean():
'''public void setCachedResultBoolean(final boolean value)
'''
pass
def hasCachedResultString():
'''public boolean hasCachedResultString()
'''
pass
def getCachedResultType():
'''public int getCachedResultType()
'''
pass
def getCachedBooleanValue():
'''public boolean getCachedBooleanValue()
'''
pass
def getCachedErrorValue():
'''public int getCachedErrorValue()
'''
pass
def setOptions():
'''public void setOptions(final short options)
'''
pass
def getValue():
'''public double getValue()
'''
pass
def getOptions():
'''public short getOptions()
'''
pass
def isSharedFormula():
'''public boolean isSharedFormula()
'''
pass
def setSharedFormula():
'''public void setSharedFormula(final boolean flag)
'''
pass
def isAlwaysCalc():
'''public boolean isAlwaysCalc()
'''
pass
def setAlwaysCalc():
'''public void setAlwaysCalc(final boolean flag)
'''
pass
def isCalcOnLoad():
'''public boolean isCalcOnLoad()
'''
pass
def setCalcOnLoad():
'''public void setCalcOnLoad(final boolean flag)
'''
pass
def getParsedExpression():
'''public Ptg[] getParsedExpression()
'''
pass
def getFormula():
'''public Formula getFormula()
'''
pass
def setParsedExpression():
'''public void setParsedExpression(final Ptg[] ptgs)
'''
pass
def getSid():
'''public short getSid()
'''
pass
def clone():
'''public FormulaRecord clone()
'''
pass
def getTypeCode():
'''public int getTypeCode()
'''
pass
def create():
'''public static SpecialCachedValue create(final long valueLongBits)
'''
pass
def serialize():
'''public void serialize(final LittleEndianOutput out)
'''
pass
def formatDebugString():
'''public String formatDebugString()
'''
pass
def createCachedEmptyValue():
'''public static SpecialCachedValue createCachedEmptyValue()
'''
pass
def createForString():
'''public static SpecialCachedValue createForString()
'''
pass
def createCachedBoolean():
'''public static SpecialCachedValue createCachedBoolean(final boolean b)
'''
pass
def createCachedErrorCode():
'''public static SpecialCachedValue createCachedErrorCode(final int errorCode)
'''
pass
def toString():
'''public String toString()
'''
pass
def getValueType():
'''public int getValueType()
'''
pass
def getBooleanValue():
'''public boolean getBooleanValue()
'''
pass
def getErrorValue():
'''public int getErrorValue()
'''
pass
