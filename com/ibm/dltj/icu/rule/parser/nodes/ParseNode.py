setRef = "int  1"
uset = "int  2"
varRef = "int  3"
lookAhead = "int  5"
tag = "int  6"
endMark = "int  7"
opStart = "int  8"
opCat = "int  9"
opOr = "int  10"
opStar = "int  11"
opPlus = "int  12"
opQuestion = "int  13"
opLParen = "int  16"
tagExtTypeName = "int  17"
tagExtFeatureName = "int  18"
tagExtFeatureValue = "int  19"
PREC_NONE = "int  0"
precStart = "int  2"
precLParen = "int  3"
precOpOr = "int  4"
precOpCat = "int  5"
def getPrecedence():
    '''returns int\n\n
    getPrecedence()\n
    '''
def setLeftHandNode():
    '''returns None\n\n
    setLeftHandNode(final ParseNode leftChild)\n
    '''
def getLeftHandNode():
    '''returns ParseNode\n\n
    getLeftHandNode()\n
    '''
def setRightHandNode():
    '''returns None\n\n
    setRightHandNode(final ParseNode rightChild)\n
    '''
def getRightHandNode():
    '''returns ParseNode\n\n
    getRightHandNode()\n
    '''
def setFirstPos():
    '''returns None\n\n
    setFirstPos(final int firstPos)\n
    '''
def getFirstPos():
    '''returns int\n\n
    getFirstPos()\n
    '''
def setLastPos():
    '''returns None\n\n
    setLastPos(final int lastPos)\n
    '''
def setText():
    '''returns None\n\n
    setText(final String text)\n
    '''
def setTextFromPositions():
    '''returns None\n\n
    setTextFromPositions(final String s)\n
    '''
def setTextFromCurrent():
    '''returns None\n\n
    setTextFromCurrent(final RuleCharReader ruleCharReader)\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final int value)\n
    '''
def incValueFromDigit():
    '''returns None\n\n
    incValueFromDigit(final RuleChar ruleChar)\n
    '''
def getValue():
    '''returns int\n\n
    getValue()\n
    '''
