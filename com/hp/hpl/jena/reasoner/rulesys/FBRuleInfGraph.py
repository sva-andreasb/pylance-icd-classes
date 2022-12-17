def ():
    '''returns RuleStore\n\n
    (final Reasoner reasoner, final Graph schema)\n
    (final Reasoner reasoner, final List<Rule> rules, final Graph schema)\n
    (final Reasoner reasoner, final List<Rule> rules, final Graph schema, final ReificationStyle style)\n
    (final Reasoner reasoner, final List<Rule> rules, final Graph schema, final Graph data)\n
    (final List<Rule> rawRules, final Object fRuleStore, final List<Rule> bRules)\n
    '''
def setUseTGCCache():
    '''returns None\n\n
    setUseTGCCache()\n
    '''
def findDataMatches():
    '''returns ExtendedIterator<Triple>\n\n
    findDataMatches(final Node subject, final Node predicate, final Node object)\n
    findDataMatches(final TriplePattern pattern)\n
    '''
def processBuiltin():
    '''returns boolean\n\n
    processBuiltin(final ClauseEntry clause, final Rule rule, final BindingEnvironment env)\n
    '''
def addBRule():
    '''returns None\n\n
    addBRule(final Rule brule)\n
    '''
def deleteBRule():
    '''returns None\n\n
    deleteBRule(final Rule brule)\n
    '''
def addBRules():
    '''returns None\n\n
    addBRules(final List<Rule> rules)\n
    '''
def getBRules():
    '''returns List<Rule>\n\n
    getBRules()\n
    '''
def getRules():
    '''returns List<Rule>\n\n
    getRules()\n
    '''
def setTabled():
    '''returns None\n\n
    setTabled(final Node predicate)\n
    '''
def addDeduction():
    '''returns None\n\n
    addDeduction(final Triple t)\n
    '''
def getTemp():
    '''returns Node\n\n
    getTemp(final Node instance, final Node prop, final Node pclass)\n
    '''
def addRuleDuringPrepare():
    '''returns None\n\n
    addRuleDuringPrepare(final Rule rule)\n
    '''
def addPreprocessingHook():
    '''returns None\n\n
    addPreprocessingHook(final RulePreprocessHook hook)\n
    '''
def rebind():
    '''returns None\n\n
    rebind()\n
    '''
def rebindAll():
    '''returns None\n\n
    rebindAll()\n
    '''
def setTraceOn():
    '''returns None\n\n
    setTraceOn(final boolean state)\n
    '''
def setDerivationLogging():
    '''returns None\n\n
    setDerivationLogging(final boolean recordDerivations)\n
    '''
def getNRulesFired():
    '''returns long\n\n
    getNRulesFired()\n
    '''
def findWithContinuation():
    '''returns ExtendedIterator<Triple>\n\n
    findWithContinuation(final TriplePattern pattern, final Finder continuation)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final Triple o)\n
    accept(final Object tin)\n
    '''
def findFull():
    '''returns ExtendedIterator<Triple>\n\n
    findFull(final TriplePattern pattern)\n
    '''
def graphBaseFind():
    '''returns ExtendedIterator<Triple>\n\n
    graphBaseFind(final Node subject, final Node property, final Node object)\n
    '''
def find():
    '''returns ExtendedIterator<Triple>\n\n
    find(final TriplePattern pattern)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def performDelete():
    '''returns None\n\n
    performDelete(final Triple t)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def validate():
    '''returns ValidityReport\n\n
    validate()\n
    '''
def setDatatypeRangeValidation():
    '''returns None\n\n
    setDatatypeRangeValidation(final boolean on)\n
    '''
def hideNode():
    '''returns None\n\n
    hideNode(final Node n)\n
    '''
def resetLPProfile():
    '''returns None\n\n
    resetLPProfile(final boolean enable)\n
    '''
def printLPProfile():
    '''returns None\n\n
    printLPProfile()\n
    '''
