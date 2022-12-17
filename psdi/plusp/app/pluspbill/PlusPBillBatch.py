def ():
    '''returns PlusPBillBatch\n\n
    (final MboSet ms)\n
    '''
def getLogger():
    '''returns PlusPLog\n\n
    getLogger()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def setFlagsForStatus():
    '''returns None\n\n
    setFlagsForStatus()\n
    '''
def createBillLines():
    '''returns boolean\n\n
    createBillLines()\n
    createBillLines(final String s)\n
    '''
def validateTransaction():
    '''returns boolean\n\n
    validateTransaction(final MboRemote mboRemote, final MboRemote mboRemote2)\n
    '''
def calculateTotals():
    '''returns None\n\n
    calculateTotals()\n
    '''
def getTicketSet():
    '''returns MboSetRemote\n\n
    getTicketSet(final boolean b)\n
    '''
def getWOSet():
    '''returns MboSetRemote\n\n
    getWOSet(final boolean b)\n
    '''
def getSOSet():
    '''returns MboSetRemote\n\n
    getSOSet(final boolean b)\n
    '''
def updateBillBatchTotals():
    '''returns None\n\n
    updateBillBatchTotals(final MboRemote mboRemote, final String s, final String s2)\n
    updateBillBatchTotals()\n
    '''
def getBillableStatusWhereClause():
    '''returns String\n\n
    getBillableStatusWhereClause(final String listName, final String value, final String s)\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def isBilled():
    '''returns boolean\n\n
    isBilled()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String val, final Date asOfDate, final String memo, final long accessModifier)\n
    '''
def setValueCustomerCurrencyTotal():
    '''returns None\n\n
    setValueCustomerCurrencyTotal()\n
    '''
def setRevisionNum():
    '''returns None\n\n
    setRevisionNum()\n
    '''
def canCreateBillLines():
    '''returns None\n\n
    canCreateBillLines()\n
    '''
def hasCopyInProgress():
    '''returns boolean\n\n
    hasCopyInProgress()\n
    '''
def updateCopyHistory():
    '''returns None\n\n
    updateCopyHistory(final String errKey, final String... params)\n
    '''
def getBillBatchCopy():
    '''returns MboRemote\n\n
    getBillBatchCopy()\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String changeToStatus, final long accessModifier)\n
    '''
def setBillBatchFilters():
    '''returns None\n\n
    setBillBatchFilters(final MboRemote e)\n
    '''
def getBillBatchFilters():
    '''returns HashSet<MboRemote>\n\n
    getBillBatchFilters()\n
    '''
