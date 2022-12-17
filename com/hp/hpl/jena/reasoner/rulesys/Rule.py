def ():
    '''returns ParserException\n\n
    (final List<ClauseEntry> head, final List<ClauseEntry> body)\n
    (final String name, final List<ClauseEntry> head, final List<ClauseEntry> body)\n
    (final String name, final ClauseEntry[] head, final ClauseEntry[] body)\n
    (final String message, final Parser parser)\n
    '''
def bodyLength():
    '''returns int\n\n
    bodyLength()\n
    '''
def getBodyElement():
    '''returns ClauseEntry\n\n
    getBodyElement(final int n)\n
    '''
def getBody():
    '''returns ClauseEntry[]\n\n
    getBody()\n
    '''
def headLength():
    '''returns int\n\n
    headLength()\n
    '''
def getHeadElement():
    '''returns ClauseEntry\n\n
    getHeadElement(final int n)\n
    '''
def getHead():
    '''returns ClauseEntry[]\n\n
    getHead()\n
    '''
def isBackward():
    '''returns boolean\n\n
    isBackward()\n
    '''
def setBackward():
    '''returns None\n\n
    setBackward(final boolean flag)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setNumVars():
    '''returns None\n\n
    setNumVars(final int n)\n
    '''
def getNumVars():
    '''returns int\n\n
    getNumVars()\n
    '''
def instantiate():
    '''returns Rule\n\n
    instantiate(final BindingEnvironment env)\n
    '''
def cloneRule():
    '''returns Rule\n\n
    cloneRule()\n
    '''
def isMonotonic():
    '''returns boolean\n\n
    isMonotonic()\n
    '''
def isAxiom():
    '''returns boolean\n\n
    isAxiom()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def toShortString():
    '''returns String\n\n
    toShortString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def sameAs():
    '''returns boolean\n\n
    sameAs(final Object o)\n
    '''
def registerPrefix():
    '''returns None\n\n
    registerPrefix(final String prefix, final String namespace)\n
    '''
def registerPrefixMap():
    '''returns None\n\n
    registerPrefixMap(final Map<String, String> map)\n
    '''
def getRulesPreload():
    '''returns List<Rule>\n\n
    getRulesPreload()\n
    '''
def recentTokens():
    '''returns String\n\n
    recentTokens()\n
    '''
def parseRule():
    '''returns Rule\n\n
    parseRule()\n
    '''
