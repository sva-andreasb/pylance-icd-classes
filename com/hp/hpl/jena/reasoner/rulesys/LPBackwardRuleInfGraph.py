def ():
    '''returns LPBackwardRuleInfGraph\n\n
    (final Reasoner reasoner, final LPRuleStore ruleStore, final Graph data, final Graph schema)\n
    '''
def getSchemaGraph():
    '''returns Graph\n\n
    getSchemaGraph()\n
    '''
def prepare():
    '''returns None\n\n
    prepare()\n
    '''
def graphBaseFind():
    '''returns ExtendedIterator<Triple>\n\n
    graphBaseFind(final Node subject, final Node property, final Node object)\n
    '''
def find():
    '''returns ExtendedIterator<Triple>\n\n
    find(final TriplePattern pattern)\n
    '''
def setTabled():
    '''returns None\n\n
    setTabled(final Node predicate)\n
    '''
def setDerivationLogging():
    '''returns None\n\n
    setDerivationLogging(final boolean recordDerivations)\n
    '''
def getDerivation():
    '''returns Iterator<Derivation>\n\n
    getDerivation(final Triple t)\n
    '''
def setTraceOn():
    '''returns None\n\n
    setTraceOn(final boolean state)\n
    '''
def isTraceOn():
    '''returns boolean\n\n
    isTraceOn()\n
    '''
def logDerivation():
    '''returns None\n\n
    logDerivation(final Triple t, final Derivation derivation)\n
    '''
def findDataMatches():
    '''returns ExtendedIterator<Triple>\n\n
    findDataMatches(final TriplePattern pattern)\n
    '''
def processBuiltin():
    '''returns boolean\n\n
    processBuiltin(final ClauseEntry clause, final Rule rule, final BindingEnvironment env)\n
    '''
def silentAdd():
    '''returns None\n\n
    silentAdd(final Triple t)\n
    '''
def getTemp():
    '''returns Node\n\n
    getTemp(final Node instance, final Node prop, final Node pclass)\n
    '''
