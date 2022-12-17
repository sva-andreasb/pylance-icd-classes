def ():
    '''returns BasicForwardRuleInfGraph\n\n
    (final Reasoner reasoner, final Graph schema)\n
    (final Reasoner reasoner, final List<Rule> rules, final Graph schema)\n
    (final Reasoner reasoner, final List<Rule> rules, final Graph schema, final ReificationStyle style)\n
    (final Reasoner reasoner, final List<Rule> rules, final Graph schema, final Graph data)\n
    '''
def setRuleStore():
    '''returns None\n\n
    setRuleStore(final Object ruleStore)\n
    '''
def rebind():
    '''returns None\n\n
    rebind(final Graph data)\n
    rebind()\n
    '''
def getSchemaGraph():
    '''returns Graph\n\n
    getSchemaGraph()\n
    '''
def addDeduction():
    '''returns None\n\n
    addDeduction(final Triple t)\n
    '''
def setFunctorFiltering():
    '''returns None\n\n
    setFunctorFiltering(final boolean param)\n
    '''
def findWithContinuation():
    '''returns ExtendedIterator<Triple>\n\n
    findWithContinuation(final TriplePattern pattern, final Finder continuation)\n
    '''
def graphBaseFind():
    '''returns ExtendedIterator<Triple>\n\n
    graphBaseFind(final Node subject, final Node property, final Node object)\n
    '''
def find():
    '''returns ExtendedIterator<Triple>\n\n
    find(final TriplePattern pattern)\n
    '''
def graphBaseSize():
    '''returns int\n\n
    graphBaseSize()\n
    '''
def performDelete():
    '''returns None\n\n
    performDelete(final Triple t)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def addBRule():
    '''returns None\n\n
    addBRule(final Rule brule)\n
    '''
def deleteBRule():
    '''returns None\n\n
    deleteBRule(final Rule brule)\n
    '''
def getDeductionsGraph():
    '''returns Graph\n\n
    getDeductionsGraph()\n
    '''
def getCurrentDeductionsGraph():
    '''returns Graph\n\n
    getCurrentDeductionsGraph()\n
    '''
def findDataMatches():
    '''returns ExtendedIterator<Triple>\n\n
    findDataMatches(final Node subject, final Node predicate, final Node object)\n
    '''
def logDerivation():
    '''returns None\n\n
    logDerivation(final Triple t, final Derivation derivation)\n
    '''
def silentAdd():
    '''returns None\n\n
    silentAdd(final Triple t)\n
    '''
def setDerivationLogging():
    '''returns None\n\n
    setDerivationLogging(final boolean recordDerivations)\n
    '''
def shouldLogDerivations():
    '''returns boolean\n\n
    shouldLogDerivations()\n
    '''
def getDerivation():
    '''returns Iterator<Derivation>\n\n
    getDerivation(final Triple t)\n
    '''
def setTraceOn():
    '''returns None\n\n
    setTraceOn(final boolean state)\n
    '''
def shouldTrace():
    '''returns boolean\n\n
    shouldTrace()\n
    '''
def getNRulesFired():
    '''returns long\n\n
    getNRulesFired()\n
    '''
def constructReifier():
    '''returns Reifier\n\n
    constructReifier()\n
    '''
def getReifier():
    '''returns Reifier\n\n
    getReifier()\n
    '''
