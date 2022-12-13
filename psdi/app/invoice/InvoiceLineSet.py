def InvoiceLineSet():
'''public InvoiceLineSet(final MboServerInterface ms)
'''
pass
def addInvoiceLineWithKey():
'''public InvoiceLineRemote addInvoiceLineWithKey(final String key)
'''
pass
def createInvoiceLine():
'''public void createInvoiceLine(final MboRemote receiptOrPOLine, final double qty, final double cost)
'''
pass
def clearAllocatedLines():
'''public void clearAllocatedLines()
'''
pass
def allocateServices():
'''public void allocateServices()
public void allocateServices(final InvoiceLineSetRemote acceptingLines)
'''
pass
def hasAllocatedLines():
'''public boolean hasAllocatedLines()
'''
pass
def canAdd():
'''public void canAdd()
'''
pass
def getInvoiceForQueryOnly():
'''public MboRemote getInvoiceForQueryOnly(final String invoicenum, final String siteid)
'''
pass
def setInvoiceforQueryOnly():
'''public void setInvoiceforQueryOnly(final MboRemote invoice)
'''
pass
def getPOForQueryOnly():
'''public MboRemote getPOForQueryOnly(final String ponum, final String positeid, final String porevisionnum)
'''
pass
def setPOforQueryOnly():
'''public void setPOforQueryOnly(final MboRemote po)
'''
pass
def getCompaniesForQueryOnly():
'''public MboRemote getCompaniesForQueryOnly(final String vendor, final String orgid)
'''
pass
def setCompaniesforQueryOnly():
'''public void setCompaniesforQueryOnly(final MboRemote company)
'''
pass
def getTaxTypeForQueryOnly():
'''public MboRemote getTaxTypeForQueryOnly(final String typeCode, final String orgid)
'''
pass
def setTaxTypeforQueryOnly():
'''public void setTaxTypeforQueryOnly(final MboRemote taxType)
'''
pass
def getTaxRateForQueryOnly():
'''public Double getTaxRateForQueryOnly(final String typeCode, final String taxCode, final String orgID, final String currentDate)
'''
pass
def setTaxRateforQueryOnly():
'''public void setTaxRateforQueryOnly(final String typeCode, final String taxCode, final String orgID, final String currentDate, final double rate)
'''
pass
def getTaxForQueryOnly():
'''public MboRemote getTaxForQueryOnly(final String typeCode, final String taxCode, final String orgid)
'''
pass
def setTaxforQueryOnly():
'''public void setTaxforQueryOnly(final MboRemote tax)
'''
pass
