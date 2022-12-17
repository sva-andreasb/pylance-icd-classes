def ():
    '''returns SLA\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def defineEscalation():
    '''returns None\n\n
    defineEscalation(final int row)\n
    '''
def statusValidate():
    '''returns None\n\n
    statusValidate(final String newStatus)\n
    '''
def validateCriteria():
    '''returns None\n\n
    validateCriteria()\n
    '''
def validateEscalation():
    '''returns None\n\n
    validateEscalation()\n
    '''
def deleteEscalation():
    '''returns None\n\n
    deleteEscalation()\n
    '''
def actDeactEscalation():
    '''returns None\n\n
    actDeactEscalation()\n
    '''
def checkRelatedSLAs():
    '''returns boolean\n\n
    checkRelatedSLAs(final MboRemote commitment)\n
    '''
def validateRelatedSLAs():
    '''returns boolean\n\n
    validateRelatedSLAs()\n
    '''
def validateRelatedSLA():
    '''returns boolean\n\n
    validateRelatedSLA(final MboRemote sla, final boolean isParent)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final boolean deactivateEscalation)\n
    '''
def addRelatedSLA():
    '''returns None\n\n
    addRelatedSLA(final MboSetRemote slaSet, final boolean isParent)\n
    '''
def addAsscoiatedContracts():
    '''returns None\n\n
    addAsscoiatedContracts(final MboSetRemote contractSet)\n
    '''
def addKPIs():
    '''returns None\n\n
    addKPIs(final MboSetRemote kpiSet)\n
    '''
def addAssets():
    '''returns None\n\n
    addAssets(final MboSetRemote assetSet)\n
    '''
def addLocations():
    '''returns None\n\n
    addLocations(final MboSetRemote locationSet)\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def calculateMeasurements():
    '''returns None\n\n
    calculateMeasurements()\n
    '''
def isActive():
    '''returns boolean\n\n
    isActive()\n
    '''
def isInactive():
    '''returns boolean\n\n
    isInactive()\n
    '''
def isVendorSLA():
    '''returns boolean\n\n
    isVendorSLA()\n
    '''
def enableFields():
    '''returns None\n\n
    enableFields(final String prevStatus)\n
    '''
def enableCalendarFields():
    '''returns None\n\n
    enableCalendarFields(final boolean setCalcOrg)\n
    '''
def resetCalendarFields():
    '''returns None\n\n
    resetCalendarFields(final String whichOrg)\n
    '''
def getCalendarFields():
    '''returns Vector\n\n
    getCalendarFields(final boolean includeOrg)\n
    '''
def getSlaCalendarFields():
    '''returns Vector\n\n
    getSlaCalendarFields(final boolean includeOrg)\n
    '''
def getCalcCalendarFields():
    '''returns Vector\n\n
    getCalcCalendarFields(final boolean includeOrg)\n
    '''
def setOrgID():
    '''returns None\n\n
    setOrgID()\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(final String name)\n
    '''
def getsitesByOrg():
    '''returns MboSetRemote\n\n
    getsitesByOrg()\n
    '''
def validateCompanyOrg():
    '''returns boolean\n\n
    validateCompanyOrg(final String company, final String orgid)\n
    '''
def getKPISelect():
    '''returns String\n\n
    getKPISelect()\n
    '''
def getKPIWhere():
    '''returns String\n\n
    getKPIWhere()\n
    '''
def setKPIId():
    '''returns None\n\n
    setKPIId(final long newID)\n
    '''
def clearClassification():
    '''returns None\n\n
    clearClassification()\n
    '''
