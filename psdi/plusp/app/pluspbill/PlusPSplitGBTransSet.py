def PlusPSplitGBTransSet():
    '''public PlusPSplitGBTransSet(final MboServerInterface ms)
    '''
def init():
    '''public void init()
    '''
def canAdd():
    '''public void canAdd()
    '''
def remove():
    '''public void remove(final MboRemote mbo)
    '''
def validate():
    '''public void validate()
    '''
def fireEventsBeforeDB():
    '''public void fireEventsBeforeDB(final MXTransaction txn)
    '''
def fireEventsAfterDBCommit():
    '''public void fireEventsAfterDBCommit(final MXTransaction txn)
    '''
def getValidRecords():
    '''public Vector<MboRemote> getValidRecords(final MboRemote obj)
    '''
def getNewValidRecords():
    '''public Vector<MboRemote> getNewValidRecords(final MboRemote mboRemote)
    '''
def getCustomersOfSplit():
    '''public HashSet<String> getCustomersOfSplit(final String value)
    '''
def validatePercentageTotals():
    '''public void validatePercentageTotals()
    '''
def validateBillPriceTotals():
    '''public void validateBillPriceTotals()
    '''
def hasIncompatibleSplitType():
    '''public boolean hasIncompatibleSplitType(final String value, final MboRemote mboRemote, final boolean b)
    '''
def allowTotalOnly():
    '''public boolean allowTotalOnly()
    '''
def deleteAndRemoveIncompatibleSplitType():
    '''public void deleteAndRemoveIncompatibleSplitType(final String value, final MboRemote mboRemote)
    '''
def applyAgreements():
    '''public void applyAgreements()
    '''
def createBillTransactions():
    '''public void createBillTransactions()
    '''
def addAllPayersFromActualTransactions():
    '''public void addAllPayersFromActualTransactions()
    '''
def splitForTransactionExists():
    '''public boolean splitForTransactionExists(final MboRemote mboRemote)
    '''
def validatePayerSplitType():
    '''public void validatePayerSplitType(final boolean b)
    '''
