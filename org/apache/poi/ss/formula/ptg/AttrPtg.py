sid = "byte  25"
SPACE_BEFORE = "int  0"
CR_BEFORE = "int  1"
SPACE_BEFORE_OPEN_PAREN = "int  2"
CR_BEFORE_OPEN_PAREN = "int  3"
SPACE_BEFORE_CLOSE_PAREN = "int  4"
CR_BEFORE_CLOSE_PAREN = "int  5"
SPACE_AFTER_EQUALITY = "int  6"
def ():
    '''returns AttrPtg\n\n
    (final LittleEndianInput in)\n
    '''
def isSemiVolatile():
    '''returns boolean\n\n
    isSemiVolatile()\n
    '''
def isOptimizedIf():
    '''returns boolean\n\n
    isOptimizedIf()\n
    '''
def isOptimizedChoose():
    '''returns boolean\n\n
    isOptimizedChoose()\n
    '''
def isSum():
    '''returns boolean\n\n
    isSum()\n
    '''
def isSkip():
    '''returns boolean\n\n
    isSkip()\n
    '''
def isSpace():
    '''returns boolean\n\n
    isSpace()\n
    '''
def getData():
    '''returns short\n\n
    getData()\n
    '''
def getJumpTable():
    '''returns int[]\n\n
    getJumpTable()\n
    '''
def getChooseFuncOffset():
    '''returns int\n\n
    getChooseFuncOffset()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def write():
    '''returns None\n\n
    write(final LittleEndianOutput out)\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def toFormulaString():
    '''returns String\n\n
    toFormulaString(final String[] operands)\n
    toFormulaString()\n
    '''
def getNumberOfOperands():
    '''returns int\n\n
    getNumberOfOperands()\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
