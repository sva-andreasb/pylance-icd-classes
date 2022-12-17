def ():
    '''returns InvoiceLineSet\n\n
    (final MboServerInterface ms)\n
    '''
def addInvoiceLineWithKey():
    '''returns InvoiceLineRemote\n\n
    addInvoiceLineWithKey(final String key)\n
    '''
def createInvoiceLine():
    '''returns None\n\n
    createInvoiceLine(final MboRemote receiptOrPOLine, final double qty, final double cost)\n
    '''
def clearAllocatedLines():
    '''returns None\n\n
    clearAllocatedLines()\n
    '''
def allocateServices():
    '''returns None\n\n
    allocateServices()\n
    allocateServices(final InvoiceLineSetRemote acceptingLines)\n
    '''
def hasAllocatedLines():
    '''returns boolean\n\n
    hasAllocatedLines()\n
    '''
def canAdd():
    '''returns None\n\n
    canAdd()\n
    '''
def getInvoiceForQueryOnly():
    '''returns MboRemote\n\n
    getInvoiceForQueryOnly(final String invoicenum, final String siteid)\n
    '''
def setInvoiceforQueryOnly():
    '''returns None\n\n
    setInvoiceforQueryOnly(final MboRemote invoice)\n
    '''
def getPOForQueryOnly():
    '''returns MboRemote\n\n
    getPOForQueryOnly(final String ponum, final String positeid, final String porevisionnum)\n
    '''
def setPOforQueryOnly():
    '''returns None\n\n
    setPOforQueryOnly(final MboRemote po)\n
    '''
def getCompaniesForQueryOnly():
    '''returns MboRemote\n\n
    getCompaniesForQueryOnly(final String vendor, final String orgid)\n
    '''
def setCompaniesforQueryOnly():
    '''returns None\n\n
    setCompaniesforQueryOnly(final MboRemote company)\n
    '''
def getTaxTypeForQueryOnly():
    '''returns MboRemote\n\n
    getTaxTypeForQueryOnly(final String typeCode, final String orgid)\n
    '''
def setTaxTypeforQueryOnly():
    '''returns None\n\n
    setTaxTypeforQueryOnly(final MboRemote taxType)\n
    '''
def getTaxRateForQueryOnly():
    '''returns Double\n\n
    getTaxRateForQueryOnly(final String typeCode, final String taxCode, final String orgID, final String currentDate)\n
    '''
def setTaxRateforQueryOnly():
    '''returns None\n\n
    setTaxRateforQueryOnly(final String typeCode, final String taxCode, final String orgID, final String currentDate, final double rate)\n
    '''
def getTaxForQueryOnly():
    '''returns MboRemote\n\n
    getTaxForQueryOnly(final String typeCode, final String taxCode, final String orgid)\n
    '''
def setTaxforQueryOnly():
    '''returns None\n\n
    setTaxforQueryOnly(final MboRemote tax)\n
    '''
