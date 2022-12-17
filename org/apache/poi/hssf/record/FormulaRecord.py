sid = "short  6"
STRING = "int  0"
BOOLEAN = "int  1"
ERROR_CODE = "int  2"
EMPTY = "int  3"
def ():
    '''returns FormulaRecord\n\n
    ()\n
    (final RecordInputStream ris)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final double value)\n
    '''
def setCachedResultTypeEmptyString():
    '''returns None\n\n
    setCachedResultTypeEmptyString()\n
    '''
def setCachedResultTypeString():
    '''returns None\n\n
    setCachedResultTypeString()\n
    '''
def setCachedResultErrorCode():
    '''returns None\n\n
    setCachedResultErrorCode(final int errorCode)\n
    '''
def setCachedResultBoolean():
    '''returns None\n\n
    setCachedResultBoolean(final boolean value)\n
    '''
def hasCachedResultString():
    '''returns boolean\n\n
    hasCachedResultString()\n
    '''
def getCachedResultType():
    '''returns int\n\n
    getCachedResultType()\n
    '''
def getCachedBooleanValue():
    '''returns boolean\n\n
    getCachedBooleanValue()\n
    '''
def getCachedErrorValue():
    '''returns int\n\n
    getCachedErrorValue()\n
    '''
def setOptions():
    '''returns None\n\n
    setOptions(final short options)\n
    '''
def getValue():
    '''returns double\n\n
    getValue()\n
    '''
def getOptions():
    '''returns short\n\n
    getOptions()\n
    '''
def isSharedFormula():
    '''returns boolean\n\n
    isSharedFormula()\n
    '''
def setSharedFormula():
    '''returns None\n\n
    setSharedFormula(final boolean flag)\n
    '''
def isAlwaysCalc():
    '''returns boolean\n\n
    isAlwaysCalc()\n
    '''
def setAlwaysCalc():
    '''returns None\n\n
    setAlwaysCalc(final boolean flag)\n
    '''
def isCalcOnLoad():
    '''returns boolean\n\n
    isCalcOnLoad()\n
    '''
def setCalcOnLoad():
    '''returns None\n\n
    setCalcOnLoad(final boolean flag)\n
    '''
def getParsedExpression():
    '''returns Ptg[]\n\n
    getParsedExpression()\n
    '''
def getFormula():
    '''returns Formula\n\n
    getFormula()\n
    '''
def setParsedExpression():
    '''returns None\n\n
    setParsedExpression(final Ptg[] ptgs)\n
    '''
def getSid():
    '''returns short\n\n
    getSid()\n
    '''
def clone():
    '''returns FormulaRecord\n\n
    clone()\n
    '''
def getTypeCode():
    '''returns int\n\n
    getTypeCode()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final LittleEndianOutput out)\n
    '''
def formatDebugString():
    '''returns String\n\n
    formatDebugString()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getValueType():
    '''returns int\n\n
    getValueType()\n
    '''
def getBooleanValue():
    '''returns boolean\n\n
    getBooleanValue()\n
    '''
def getErrorValue():
    '''returns int\n\n
    getErrorValue()\n
    '''
