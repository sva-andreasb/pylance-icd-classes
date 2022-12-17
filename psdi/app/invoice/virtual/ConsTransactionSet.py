def ():
    '''returns ConsTransactionSet\n\n
    (final MboServerInterface ms)\n
    '''
def setup():
    '''returns MboRemote\n\n
    setup()\n
    '''
def setInventoryNextInvoiceDate():
    '''returns None\n\n
    setInventoryNextInvoiceDate(final MboSetRemote consTransactionSet)\n
    '''
def getConsignmentTransactions():
    '''returns MboSetRemote\n\n
    getConsignmentTransactions(final String invGenType, final String vendor)\n
    '''
def addConsignmentTransactions():
    '''returns MboSetRemote\n\n
    addConsignmentTransactions(final MboRemote transMbo)\n
    '''
def setValuesFromTransactions():
    '''returns MboRemote\n\n
    setValuesFromTransactions(MboRemote consTransRemote, final MboSetRemote transSetRemote, final HashMap<Long, Double> matUseTransMap)\n
    '''
