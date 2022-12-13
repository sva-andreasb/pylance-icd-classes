def UninvoicedReceiptsInfo():
    '''public UninvoicedReceiptsInfo(final Invoice inv)
    '''
def destroy():
    '''public void destroy()
    '''
def getRemainingQty():
    '''public double getRemainingQty(final MboRemote receipt)
    '''
def getRemainingCost():
    '''public double getRemainingCost(final MboRemote receipt)
    '''
def getNewlyAllocated():
    '''public double[] getNewlyAllocated(final String invoiceLineNum, final String receiptID)
    '''
def getUninvoicedReceipts():
    '''public Vector<MboRemote> getUninvoicedReceipts(final String poNum, final String polinenum, final int type, final boolean isCreditInvoice, final String siteID, final boolean isNegativeLine, final String receiptID)
    '''
def update():
    '''public void update(final MboRemote invoiceLine, final MboRemote receipt, final double qty, final double cost)
    '''
def getIssueUnitCost():
    '''public double getIssueUnitCost(final MboRemote receipt, final MboRemote invoiceLine)
    '''
