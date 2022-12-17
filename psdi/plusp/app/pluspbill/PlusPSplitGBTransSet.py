def ():
    '''returns PlusPSplitGBTransSet\n\n
    (final MboServerInterface ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def canAdd():
    '''returns None\n\n
    canAdd()\n
    '''
def remove():
    '''returns None\n\n
    remove(final MboRemote mbo)\n
    '''
def validate():
    '''returns None\n\n
    validate()\n
    '''
def fireEventsBeforeDB():
    '''returns None\n\n
    fireEventsBeforeDB(final MXTransaction txn)\n
    '''
def fireEventsAfterDBCommit():
    '''returns None\n\n
    fireEventsAfterDBCommit(final MXTransaction txn)\n
    '''
def getValidRecords():
    '''returns Vector<MboRemote>\n\n
    getValidRecords(final MboRemote obj)\n
    '''
def getNewValidRecords():
    '''returns Vector<MboRemote>\n\n
    getNewValidRecords(final MboRemote mboRemote)\n
    '''
def getCustomersOfSplit():
    '''returns HashSet<String>\n\n
    getCustomersOfSplit(final String value)\n
    '''
def validatePercentageTotals():
    '''returns None\n\n
    validatePercentageTotals()\n
    '''
def validateBillPriceTotals():
    '''returns None\n\n
    validateBillPriceTotals()\n
    '''
def hasIncompatibleSplitType():
    '''returns boolean\n\n
    hasIncompatibleSplitType(final String value, final MboRemote mboRemote, final boolean b)\n
    '''
def allowTotalOnly():
    '''returns boolean\n\n
    allowTotalOnly()\n
    '''
def deleteAndRemoveIncompatibleSplitType():
    '''returns None\n\n
    deleteAndRemoveIncompatibleSplitType(final String value, final MboRemote mboRemote)\n
    '''
def applyAgreements():
    '''returns None\n\n
    applyAgreements()\n
    '''
def createBillTransactions():
    '''returns None\n\n
    createBillTransactions()\n
    '''
def addAllPayersFromActualTransactions():
    '''returns None\n\n
    addAllPayersFromActualTransactions()\n
    '''
def splitForTransactionExists():
    '''returns boolean\n\n
    splitForTransactionExists(final MboRemote mboRemote)\n
    '''
def validatePayerSplitType():
    '''returns None\n\n
    validatePayerSplitType(final boolean b)\n
    '''
