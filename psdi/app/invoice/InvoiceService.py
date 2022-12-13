def InvoiceService():
'''public InvoiceService()
public InvoiceService(final MXServer mxServer)
'''
pass
def getConsignmentTransactions():
'''public MboSetRemote getConsignmentTransactions(final String invGenType, final UserInfo userInfo, final String vendor)
'''
pass
def addConsignmentTransactions():
'''public MboSetRemote addConsignmentTransactions(final MboRemote transMbo, final UserInfo userInfo)
'''
pass
def setInventoryNextInvoiceDate():
'''public void setInventoryNextInvoiceDate(final MboSetRemote consTransactionSet)
'''
pass
def createInvoiceLine():
'''public InvoiceLineRemote createInvoiceLine(final InvoiceRemote invoice, final String linenum)
'''
pass
def changeStatus():
'''public void changeStatus(@WSMboKey("INVOICE") final InvoiceRemote invoice, final String status, final Date date, final String memo)
'''
pass
def createInvoicesForConsignment():
'''public InvoiceSetRemote createInvoicesForConsignment(final UserInfo userInfo, final MboSetRemote transSet, final String invGenType)
'''
pass
