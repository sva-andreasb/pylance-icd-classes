def ():
    '''returns UninvoicedReceiptsInfo\n\n
    (final Invoice inv)\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def getRemainingQty():
    '''returns double\n\n
    getRemainingQty(final MboRemote receipt)\n
    '''
def getRemainingCost():
    '''returns double\n\n
    getRemainingCost(final MboRemote receipt)\n
    '''
def getNewlyAllocated():
    '''returns double[]\n\n
    getNewlyAllocated(final String invoiceLineNum, final String receiptID)\n
    '''
def getUninvoicedReceipts():
    '''returns Vector<MboRemote>\n\n
    getUninvoicedReceipts(final String poNum, final String polinenum, final int type, final boolean isCreditInvoice, final String siteID, final boolean isNegativeLine, final String receiptID)\n
    '''
def update():
    '''returns None\n\n
    update(final MboRemote invoiceLine, final MboRemote receipt, final double qty, final double cost)\n
    '''
def getIssueUnitCost():
    '''returns double\n\n
    getIssueUnitCost(final MboRemote receipt, final MboRemote invoiceLine)\n
    '''
