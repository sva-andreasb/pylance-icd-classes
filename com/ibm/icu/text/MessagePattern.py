ARG_NAME_NOT_NUMBER = "int  -1"
ARG_NAME_NOT_VALID = "int  -2"
NO_NUMERIC_VALUE = "double  -1.23456789E8"
def ():
    '''returns MessagePattern\n\n
    ()\n
    (final ApostropheMode mode)\n
    (final String pattern)\n
    '''
def parse():
    '''returns MessagePattern\n\n
    parse(final String pattern)\n
    '''
def parseChoiceStyle():
    '''returns MessagePattern\n\n
    parseChoiceStyle(final String pattern)\n
    '''
def parsePluralStyle():
    '''returns MessagePattern\n\n
    parsePluralStyle(final String pattern)\n
    '''
def parseSelectStyle():
    '''returns MessagePattern\n\n
    parseSelectStyle(final String pattern)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def clearPatternAndSetApostropheMode():
    '''returns None\n\n
    clearPatternAndSetApostropheMode(final ApostropheMode mode)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    hashCode()\n
    '''
def getApostropheMode():
    '''returns ApostropheMode\n\n
    getApostropheMode()\n
    '''
def getPatternString():
    '''returns String\n\n
    getPatternString()\n
    '''
def hasNamedArguments():
    '''returns boolean\n\n
    hasNamedArguments()\n
    '''
def hasNumberedArguments():
    '''returns boolean\n\n
    hasNumberedArguments()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def autoQuoteApostropheDeep():
    '''returns String\n\n
    autoQuoteApostropheDeep()\n
    '''
def countParts():
    '''returns int\n\n
    countParts()\n
    '''
def getPart():
    '''returns Part\n\n
    getPart(final int i)\n
    '''
def getPatternIndex():
    '''returns int\n\n
    getPatternIndex(final int partIndex)\n
    '''
def getSubstring():
    '''returns String\n\n
    getSubstring(final Part part)\n
    '''
def partSubstringMatches():
    '''returns boolean\n\n
    partSubstringMatches(final Part part, final String s)\n
    '''
def getNumericValue():
    '''returns double\n\n
    getNumericValue(final Part part)\n
    '''
def getPluralOffset():
    '''returns double\n\n
    getPluralOffset(final int pluralStart)\n
    '''
def getLimitPartIndex():
    '''returns int\n\n
    getLimitPartIndex(final int start)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def cloneAsThawed():
    '''returns MessagePattern\n\n
    cloneAsThawed()\n
    '''
def freeze():
    '''returns MessagePattern\n\n
    freeze()\n
    '''
def isFrozen():
    '''returns boolean\n\n
    isFrozen()\n
    '''
def getType():
    '''returns Type\n\n
    getType()\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex()\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def getLimit():
    '''returns int\n\n
    getLimit()\n
    '''
def getValue():
    '''returns int\n\n
    getValue()\n
    '''
def getArgType():
    '''returns ArgType\n\n
    getArgType()\n
    '''
def hasNumericValue():
    '''returns boolean\n\n
    hasNumericValue()\n
    '''
def hasPluralStyle():
    '''returns boolean\n\n
    hasPluralStyle()\n
    '''
