DEFAULT = "String  \"DEFAULT\""
OPTIMIZE_ALL_REIFICATIONS_AND_HIDE_NOTHING = "int  1"
OPTIMIZE_AND_HIDE_FULL_AND_PARTIAL_REIFICATIONS = "int  2"
OPTIMIZE_AND_HIDE_ONLY_FULL_REIFICATIONS = "int  3"
def ():
    '''returns GraphRDB\n\n
    (final IDBConnection con, String graphID, final Graph requestedProperties, final int reificationBehaviour, final boolean isNew)\n
    '''
def getCapabilities():
    '''returns Capabilities\n\n
    getCapabilities()\n
    '''
def handlesLiteralTyping():
    '''returns boolean\n\n
    handlesLiteralTyping()\n
    '''
def getNode():
    '''returns Node\n\n
    getNode()\n
    '''
def getPropertyTriples():
    '''returns ExtendedIterator<Triple>\n\n
    getPropertyTriples()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def performAdd():
    '''returns None\n\n
    performAdd(final Triple t)\n
    '''
def add():
    '''returns None\n\n
    add(final List<Triple> triples)\n
    '''
def performDelete():
    '''returns None\n\n
    performDelete(final Triple t)\n
    '''
def delete():
    '''returns None\n\n
    delete(final List<Triple> triples)\n
    '''
def graphBaseSize():
    '''returns int\n\n
    graphBaseSize()\n
    '''
def graphBaseContains():
    '''returns boolean\n\n
    graphBaseContains(final Triple t)\n
    '''
def graphBaseFind():
    '''returns ExtendedIterator<Triple>\n\n
    graphBaseFind(final TripleMatch m)\n
    '''
def reifierTriples():
    '''returns ExtendedIterator<Triple>\n\n
    reifierTriples(final TripleMatch m)\n
    '''
def reifierSize():
    '''returns int\n\n
    reifierSize()\n
    '''
def getBulkUpdateHandler():
    '''returns BulkUpdateHandler\n\n
    getBulkUpdateHandler()\n
    '''
def getReifier():
    '''returns Reifier\n\n
    getReifier()\n
    '''
def getPrefixMapping():
    '''returns PrefixMapping\n\n
    getPrefixMapping()\n
    '''
def getTransactionHandler():
    '''returns TransactionHandler\n\n
    getTransactionHandler()\n
    '''
def getConnection():
    '''returns IDBConnection\n\n
    getConnection()\n
    '''
def reificationBehavior():
    '''returns int\n\n
    reificationBehavior()\n
    '''
def getSpecializedGraphs():
    '''returns Iterator<SpecializedGraph>\n\n
    getSpecializedGraphs()\n
    '''
def queryHandler():
    '''returns QueryHandler\n\n
    queryHandler()\n
    '''
def DBqueryHandler():
    '''returns DBQueryHandler\n\n
    DBqueryHandler()\n
    '''
def getDoDuplicateCheck():
    '''returns boolean\n\n
    getDoDuplicateCheck()\n
    '''
def setDoDuplicateCheck():
    '''returns None\n\n
    setDoDuplicateCheck(final boolean bool)\n
    '''
def setDoFastpath():
    '''returns None\n\n
    setDoFastpath(final boolean val)\n
    '''
def getDoFastpath():
    '''returns boolean\n\n
    getDoFastpath()\n
    '''
def setQueryOnlyAsserted():
    '''returns None\n\n
    setQueryOnlyAsserted(final boolean opt)\n
    '''
def getQueryOnlyAsserted():
    '''returns boolean\n\n
    getQueryOnlyAsserted()\n
    '''
def setQueryOnlyReified():
    '''returns None\n\n
    setQueryOnlyReified(final boolean opt)\n
    '''
def getQueryOnlyReified():
    '''returns boolean\n\n
    getQueryOnlyReified()\n
    '''
def setQueryFullReified():
    '''returns None\n\n
    setQueryFullReified(final boolean opt)\n
    '''
def getQueryFullReified():
    '''returns boolean\n\n
    getQueryFullReified()\n
    '''
def setDoImplicitJoin():
    '''returns None\n\n
    setDoImplicitJoin(final boolean val)\n
    '''
