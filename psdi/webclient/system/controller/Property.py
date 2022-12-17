TRANSLATE_FLAG = "int  1"
GLOBAL_FLAG = "int  2"
FORMAT_FLAG = "int  16"
FINAL = "int  32"
SYSTEM = "int  64"
NONCONDITIONAL = "int  128"
RENDERID = "int  256"
LABEL_SOURCE_ID = "String  \"id\""
def ():
    '''returns Property\n\n
    (final String name)\n
    (final String name, final String value)\n
    (final Property prop)\n
    '''
def setFlag():
    '''returns None\n\n
    setFlag(final long index)\n
    '''
def setFlags():
    '''returns None\n\n
    setFlags(final long flags)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final String value)\n
    '''
def getValue():
    '''returns String\n\n
    getValue()\n
    getValue(final List<String> paramValues)\n
    '''
def setDetaultValue():
    '''returns None\n\n
    setDetaultValue(final String val)\n
    '''
def getDefaultValue():
    '''returns String\n\n
    getDefaultValue()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def clearFlags():
    '''returns None\n\n
    clearFlags()\n
    '''
def clearFlag():
    '''returns None\n\n
    clearFlag(final long index)\n
    '''
def getFlag():
    '''returns boolean\n\n
    getFlag(final long index)\n
    '''
def getFlags():
    '''returns long\n\n
    getFlags()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def setFlagsFromString():
    '''returns None\n\n
    setFlagsFromString(final String flags)\n
    '''
def setFlagFromString():
    '''returns None\n\n
    setFlagFromString(final String flag)\n
    '''
def isParameterized():
    '''returns boolean\n\n
    isParameterized()\n
    '''
def getParameterList():
    '''returns List<String>\n\n
    getParameterList()\n
    '''
def setRegexPattern():
    '''returns None\n\n
    setRegexPattern(final String regex)\n
    '''
def getTranslatable():
    '''returns String\n\n
    getTranslatable(final WebClientSession sc, final String controlId, final String property)\n
    getTranslatable(final WebClientSession sc, final String controlId, final String property, final String defaultValue)\n
    '''
def getString():
    '''returns String\n\n
    getString(final String property)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
