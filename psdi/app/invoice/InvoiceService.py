def InvoiceService():
    '''public InvoiceService()
    public InvoiceService(final MXServer mxServer)
    '''
def getConsignmentTransactions():
    '''public MboSetRemote getConsignmentTransactions(final String invGenType, final UserInfo userInfo, final String vendor)
    '''
def addConsignmentTransactions():
    '''public MboSetRemote addConsignmentTransactions(final MboRemote transMbo, final UserInfo userInfo)
    '''
def setInventoryNextInvoiceDate():
    '''public void setInventoryNextInvoiceDate(final MboSetRemote consTransactionSet)
    '''
def createInvoiceLine():
    '''public InvoiceLineRemote createInvoiceLine(final InvoiceRemote invoice, final String linenum)
    '''
def changeStatus():
    '''public void changeStatus(@WSMboKey("INVOICE") final InvoiceRemote invoice, final String status, final Date date, final String memo)
    '''
def createInvoicesForConsignment():
    '''public InvoiceSetRemote createInvoicesForConsignment(final UserInfo userInfo, final MboSetRemote transSet, final String invGenType)
    '''
