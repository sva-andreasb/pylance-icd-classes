def getPrefixMapping():
    '''returns PrefixMapping\n\n
    getPrefixMapping()\n
    '''
def constructReifier():
    '''returns Reifier\n\n
    constructReifier()\n
    '''
def ():
    '''returns InfTransactionHandler\n\n
    (final Graph data, final Reasoner reasoner)\n
    (final Graph data, final Reasoner reasoner, final ReificationStyle style)\n
    (final BaseInfGraph graph)\n
    (final BaseInfGraph base)\n
    '''
def getCapabilities():
    '''returns Capabilities\n\n
    getCapabilities()\n
    '''
def getBulkUpdateHandler():
    '''returns BulkUpdateHandler\n\n
    getBulkUpdateHandler()\n
    '''
def getTransactionHandler():
    '''returns TransactionHandler\n\n
    getTransactionHandler()\n
    '''
def getRawGraph():
    '''returns Graph\n\n
    getRawGraph()\n
    '''
def getReasoner():
    '''returns Reasoner\n\n
    getReasoner()\n
    '''
def rebind():
    '''returns None\n\n
    rebind(final Graph data)\n
    rebind()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def prepare():
    '''returns None\n\n
    prepare()\n
    '''
def getDeductionsGraph():
    '''returns Graph\n\n
    getDeductionsGraph()\n
    '''
def getGlobalProperty():
    '''returns Node\n\n
    getGlobalProperty(final Node property)\n
    '''
def testGlobalProperty():
    '''returns boolean\n\n
    testGlobalProperty(final Node property)\n
    '''
def validate():
    '''returns ValidityReport\n\n
    validate()\n
    '''
def find():
    '''returns ExtendedIterator<Triple>\n\n
    find(final Node subject, final Node property, final Node object, final Graph param)\n
    find(final TriplePattern pattern)\n
    '''
def graphBaseFind():
    '''returns ExtendedIterator<Triple>\n\n
    graphBaseFind(final TripleMatch m)\n
    graphBaseFind(final Node subject, final Node property, final Node object)\n
    '''
def setDerivationLogging():
    '''returns None\n\n
    setDerivationLogging(final boolean logOn)\n
    '''
def getDerivation():
    '''returns Iterator<Derivation>\n\n
    getDerivation(final Triple triple)\n
    '''
def graphBaseSize():
    '''returns int\n\n
    graphBaseSize()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getVersion():
    '''returns int\n\n
    getVersion()\n
    '''
def performDelete():
    '''returns None\n\n
    performDelete(final Triple t)\n
    '''
def cloneWithPremises():
    '''returns InfGraph\n\n
    cloneWithPremises(final Graph premises)\n
    '''
def isPrepared():
    '''returns boolean\n\n
    isPrepared()\n
    '''
def sizeAccurate():
    '''returns boolean\n\n
    sizeAccurate()\n
    '''
def deleteAllowed():
    '''returns boolean\n\n
    deleteAllowed(final boolean every)\n
    '''
def iteratorRemoveAllowed():
    '''returns boolean\n\n
    iteratorRemoveAllowed()\n
    '''
def findContractSafe():
    '''returns boolean\n\n
    findContractSafe()\n
    findContractSafe()\n
    '''
def remove():
    '''returns None\n\n
    remove(final Node s, final Node p, final Node o)\n
    '''
def removeAll():
    '''returns None\n\n
    removeAll()\n
    '''
def transactionsSupported():
    '''returns boolean\n\n
    transactionsSupported()\n
    '''
def begin():
    '''returns None\n\n
    begin()\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
    '''
def commit():
    '''returns None\n\n
    commit()\n
    '''
