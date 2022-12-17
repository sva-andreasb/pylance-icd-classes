def ():
    '''returns PlusPAgreement\n\n
    (final MboSet set)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def isPendingRevision():
    '''returns boolean\n\n
    isPendingRevision()\n
    '''
def canRevise():
    '''returns boolean\n\n
    canRevise()\n
    '''
def apprRevAlreadyExists():
    '''returns boolean\n\n
    apprRevAlreadyExists()\n
    '''
def getValidStatusList():
    '''returns MboSetRemote\n\n
    getValidStatusList()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(String externalAgreeStatus, final Date asOfDate, final String memo, final long accessModifier)\n
    '''
def milestoneBilling():
    '''returns None\n\n
    milestoneBilling()\n
    '''
def reviseAgreement():
    '''returns PlusPAgreementRemote\n\n
    reviseAgreement(final String val, final String val2)\n
    '''
def initRelationship():
    '''returns None\n\n
    initRelationship(final String relationName, final MboSetRemote mboSet)\n
    '''
def isStatusEditable():
    '''returns boolean\n\n
    isStatusEditable()\n
    '''
def fieldAccessForStatus():
    '''returns None\n\n
    fieldAccessForStatus(final String o)\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long n)\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def incrementPreTaxTotal():
    '''returns None\n\n
    incrementPreTaxTotal(final double n)\n
    '''
def incrementRevPreTaxTotal():
    '''returns None\n\n
    incrementRevPreTaxTotal(final double n)\n
    '''
def incrementTaxTotal():
    '''returns None\n\n
    incrementTaxTotal(final double n)\n
    '''
def getNewRevisionNumber():
    '''returns int\n\n
    getNewRevisionNumber()\n
    '''
def canPerformEdit():
    '''returns None\n\n
    canPerformEdit()\n
    '''
def changeChildrenStatus():
    '''returns None\n\n
    changeChildrenStatus(final String s, final Date date, final String s2, final long n)\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def copyRecordToSWItemsTable():
    '''returns None\n\n
    copyRecordToSWItemsTable(final MboSetRemote mboSetRemote)\n
    '''
def copyRecordToSWWorkTable():
    '''returns None\n\n
    copyRecordToSWWorkTable(final MboSetRemote mboSetRemote)\n
    '''
def removeCustomerDependentRecords():
    '''returns None\n\n
    removeCustomerDependentRecords()\n
    '''
def updateScheduleAssetsFromSingleScope():
    '''returns None\n\n
    updateScheduleAssetsFromSingleScope(final MboRemote mboRemote)\n
    '''
def updateScheduleAssetsFromAllScope():
    '''returns None\n\n
    updateScheduleAssetsFromAllScope(final MboRemote mboRemote)\n
    '''
