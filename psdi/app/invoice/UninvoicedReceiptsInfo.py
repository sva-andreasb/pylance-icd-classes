def UninvoicedReceiptsInfo():
'''public UninvoicedReceiptsInfo(final Invoice inv)
'''
pass
def destroy():
'''public void destroy()
'''
pass
def getRemainingQty():
'''public double getRemainingQty(final MboRemote receipt)
'''
pass
def getRemainingCost():
'''public double getRemainingCost(final MboRemote receipt)
'''
pass
def getNewlyAllocated():
'''public double[] getNewlyAllocated(final String invoiceLineNum, final String receiptID)
'''
pass
def getUninvoicedReceipts():
'''public Vector<MboRemote> getUninvoicedReceipts(final String poNum, final String polinenum, final int type, final boolean isCreditInvoice, final String siteID, final boolean isNegativeLine, final String receiptID)
'''
pass
def update():
'''public void update(final MboRemote invoiceLine, final MboRemote receipt, final double qty, final double cost)
'''
pass
def getIssueUnitCost():
'''public double getIssueUnitCost(final MboRemote receipt, final MboRemote invoiceLine)
'''
pass
