ARG_NAME_NOT_NUMBER = "int  -1"
ARG_NAME_NOT_VALID = "int  -2"
NO_NUMERIC_VALUE = "double  -1.23456789E8"
def MessagePattern():
    '''    public MessagePattern()
    public MessagePattern(final ApostropheMode mode)
    public MessagePattern(final String pattern)
    '''
def parse():
    '''    public MessagePattern parse(final String pattern)
    '''
def parseChoiceStyle():
    '''    public MessagePattern parseChoiceStyle(final String pattern)
    '''
def parsePluralStyle():
    '''    public MessagePattern parsePluralStyle(final String pattern)
    '''
def parseSelectStyle():
    '''    public MessagePattern parseSelectStyle(final String pattern)
    '''
def clear():
    '''    public void clear()
    '''
def clearPatternAndSetApostropheMode():
    '''    public void clearPatternAndSetApostropheMode(final ApostropheMode mode)
    '''
def equals():
    '''    public boolean equals(final Object other)
    public boolean equals(final Object other)
    '''
def hashCode():
    '''    public int hashCode()
    public int hashCode()
    '''
def getApostropheMode():
    '''    public ApostropheMode getApostropheMode()
    '''
def getPatternString():
    '''    public String getPatternString()
    '''
def hasNamedArguments():
    '''    public boolean hasNamedArguments()
    '''
def hasNumberedArguments():
    '''    public boolean hasNumberedArguments()
    '''
def toString():
    '''    public String toString()
    public String toString()
    '''
def validateArgumentName():
    '''    public static int validateArgumentName(final String name)
    '''
def autoQuoteApostropheDeep():
    '''    public String autoQuoteApostropheDeep()
    '''
def countParts():
    '''    public int countParts()
    '''
def getPart():
    '''    public Part getPart(final int i)
    '''
def getPatternIndex():
    '''    public int getPatternIndex(final int partIndex)
    '''
def getSubstring():
    '''    public String getSubstring(final Part part)
    '''
def partSubstringMatches():
    '''    public boolean partSubstringMatches(final Part part, final String s)
    '''
def getNumericValue():
    '''    public double getNumericValue(final Part part)
    '''
def getPluralOffset():
    '''    public double getPluralOffset(final int pluralStart)
    '''
def getLimitPartIndex():
    '''    public int getLimitPartIndex(final int start)
    '''
def clone():
    '''    public Object clone()
    '''
def cloneAsThawed():
    '''    public MessagePattern cloneAsThawed()
    '''
def freeze():
    '''    public MessagePattern freeze()
    '''
def isFrozen():
    '''    public boolean isFrozen()
    '''
def getType():
    '''    public Type getType()
    '''
def getIndex():
    '''    public int getIndex()
    '''
def getLength():
    '''    public int getLength()
    '''
def getLimit():
    '''    public int getLimit()
    '''
def getValue():
    '''    public int getValue()
    '''
def getArgType():
    '''    public ArgType getArgType()
    '''
def hasNumericValue():
    '''    public boolean hasNumericValue()
    '''
def hasPluralStyle():
    '''    public boolean hasPluralStyle()
    '''
