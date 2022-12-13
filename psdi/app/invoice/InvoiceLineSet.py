def InvoiceLineSet():
    '''    public InvoiceLineSet(final MboServerInterface ms)
    '''
def addInvoiceLineWithKey():
    '''    public InvoiceLineRemote addInvoiceLineWithKey(final String key)
    '''
def createInvoiceLine():
    '''    public void createInvoiceLine(final MboRemote receiptOrPOLine, final double qty, final double cost)
    '''
def clearAllocatedLines():
    '''    public void clearAllocatedLines()
    '''
def allocateServices():
    '''    public void allocateServices()
    public void allocateServices(final InvoiceLineSetRemote acceptingLines)
    '''
def hasAllocatedLines():
    '''    public boolean hasAllocatedLines()
    '''
def canAdd():
    '''    public void canAdd()
    '''
def getInvoiceForQueryOnly():
    '''    public MboRemote getInvoiceForQueryOnly(final String invoicenum, final String siteid)
    '''
def setInvoiceforQueryOnly():
    '''    public void setInvoiceforQueryOnly(final MboRemote invoice)
    '''
def getPOForQueryOnly():
    '''    public MboRemote getPOForQueryOnly(final String ponum, final String positeid, final String porevisionnum)
    '''
def setPOforQueryOnly():
    '''    public void setPOforQueryOnly(final MboRemote po)
    '''
def getCompaniesForQueryOnly():
    '''    public MboRemote getCompaniesForQueryOnly(final String vendor, final String orgid)
    '''
def setCompaniesforQueryOnly():
    '''    public void setCompaniesforQueryOnly(final MboRemote company)
    '''
def getTaxTypeForQueryOnly():
    '''    public MboRemote getTaxTypeForQueryOnly(final String typeCode, final String orgid)
    '''
def setTaxTypeforQueryOnly():
    '''    public void setTaxTypeforQueryOnly(final MboRemote taxType)
    '''
def getTaxRateForQueryOnly():
    '''    public Double getTaxRateForQueryOnly(final String typeCode, final String taxCode, final String orgID, final String currentDate)
    '''
def setTaxRateforQueryOnly():
    '''    public void setTaxRateforQueryOnly(final String typeCode, final String taxCode, final String orgID, final String currentDate, final double rate)
    '''
def getTaxForQueryOnly():
    '''    public MboRemote getTaxForQueryOnly(final String typeCode, final String taxCode, final String orgid)
    '''
def setTaxforQueryOnly():
    '''    public void setTaxforQueryOnly(final MboRemote tax)
    '''
