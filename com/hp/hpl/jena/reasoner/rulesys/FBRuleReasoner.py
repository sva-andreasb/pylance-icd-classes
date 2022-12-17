def ():
    '''returns FBRuleReasoner\n\n
    (final List<Rule> rules)\n
    (final ReasonerFactory factory)\n
    (final ReasonerFactory factory, final Resource configuration)\n
    (final List<Rule> rules, final ReasonerFactory factory)\n
    '''
def addRules():
    '''returns FBRuleReasoner\n\n
    addRules(final List<Rule> rules)\n
    '''
def getReasonerCapabilities():
    '''returns Model\n\n
    getReasonerCapabilities()\n
    '''
def getBoundSchema():
    '''returns Graph\n\n
    getBoundSchema()\n
    '''
def addDescription():
    '''returns None\n\n
    addDescription(final Model configSpec, final Resource base)\n
    '''
def supportsProperty():
    '''returns boolean\n\n
    supportsProperty(final Property property)\n
    '''
def bindSchema():
    '''returns Reasoner\n\n
    bindSchema(final Graph tbox)\n
    bindSchema(final Model tbox)\n
    '''
def bind():
    '''returns InfGraph\n\n
    bind(final Graph data)\n
    '''
def setRules():
    '''returns None\n\n
    setRules(final List<Rule> rules)\n
    '''
def getRules():
    '''returns List<Rule>\n\n
    getRules()\n
    '''
def setDerivationLogging():
    '''returns None\n\n
    setDerivationLogging(final boolean logOn)\n
    '''
def setTraceOn():
    '''returns None\n\n
    setTraceOn(final boolean state)\n
    '''
def isTraceOn():
    '''returns boolean\n\n
    isTraceOn()\n
    '''
def setParameter():
    '''returns None\n\n
    setParameter(final Property parameter, final Object value)\n
    '''
def getGraphCapabilities():
    '''returns Capabilities\n\n
    getGraphCapabilities()\n
    '''
