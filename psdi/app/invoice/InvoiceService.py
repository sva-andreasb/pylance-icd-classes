def ():
    '''returns InvoiceService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def getConsignmentTransactions():
    '''returns MboSetRemote\n\n
    getConsignmentTransactions(final String invGenType, final UserInfo userInfo, final String vendor)\n
    '''
def addConsignmentTransactions():
    '''returns MboSetRemote\n\n
    addConsignmentTransactions(final MboRemote transMbo, final UserInfo userInfo)\n
    '''
def setInventoryNextInvoiceDate():
    '''returns None\n\n
    setInventoryNextInvoiceDate(final MboSetRemote consTransactionSet)\n
    '''
def createInvoiceLine():
    '''returns InvoiceLineRemote\n\n
    createInvoiceLine(final InvoiceRemote invoice, final String linenum)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(@WSMboKey("INVOICE") final InvoiceRemote invoice, final String status, final Date date, final String memo)\n
    '''
def createInvoicesForConsignment():
    '''returns InvoiceSetRemote\n\n
    createInvoicesForConsignment(final UserInfo userInfo, final MboSetRemote transSet, final String invGenType)\n
    '''
