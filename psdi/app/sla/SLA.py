def SLA():
    '''public SLA(final MboSet ms)
    '''
def init():
    '''public void init()
    '''
def add():
    '''public void add()
    '''
def canDelete():
    '''public void canDelete()
    '''
def delete():
    '''public void delete(final long accessModifier)
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def appValidate():
    '''public void appValidate()
    '''
def defineEscalation():
    '''public void defineEscalation(final int row)
    '''
def statusValidate():
    '''public void statusValidate(final String newStatus)
    '''
def validateCriteria():
    '''public void validateCriteria()
    '''
def validateEscalation():
    '''public void validateEscalation()
    '''
def deleteEscalation():
    '''public void deleteEscalation()
    '''
def actDeactEscalation():
    '''public void actDeactEscalation()
    '''
def checkRelatedSLAs():
    '''public boolean checkRelatedSLAs(final MboRemote commitment)
    '''
def validateRelatedSLAs():
    '''public boolean validateRelatedSLAs()
    '''
def validateRelatedSLA():
    '''public boolean validateRelatedSLA(final MboRemote sla, final boolean isParent)
    '''
def changeStatus():
    '''public void changeStatus(final String status, final boolean deactivateEscalation)
    '''
def addRelatedSLA():
    '''public void addRelatedSLA(final MboSetRemote slaSet, final boolean isParent)
    '''
def addAsscoiatedContracts():
    '''public void addAsscoiatedContracts(final MboSetRemote contractSet)
    '''
def addKPIs():
    '''public void addKPIs(final MboSetRemote kpiSet)
    '''
def addAssets():
    '''public void addAssets(final MboSetRemote assetSet)
    '''
def addLocations():
    '''public void addLocations(final MboSetRemote locationSet)
    '''
def getStatusListName():
    '''public String getStatusListName()
    '''
def calculateMeasurements():
    '''public void calculateMeasurements()
    '''
def isActive():
    '''public boolean isActive()
    '''
def isInactive():
    '''public boolean isInactive()
    '''
def isVendorSLA():
    '''public boolean isVendorSLA()
    '''
def enableFields():
    '''public void enableFields(final String prevStatus)
    '''
def enableCalendarFields():
    '''public void enableCalendarFields(final boolean setCalcOrg)
    '''
def resetCalendarFields():
    '''public void resetCalendarFields(final String whichOrg)
    '''
def getCalendarFields():
    '''public Vector getCalendarFields(final boolean includeOrg)
    '''
def getSlaCalendarFields():
    '''public Vector getSlaCalendarFields(final boolean includeOrg)
    '''
def getCalcCalendarFields():
    '''public Vector getCalcCalendarFields(final boolean includeOrg)
    '''
def setOrgID():
    '''public void setOrgID()
    '''
def getMboSet():
    '''public MboSetRemote getMboSet(final String name)
    '''
def getsitesByOrg():
    '''public MboSetRemote getsitesByOrg()
    '''
def validateCompanyOrg():
    '''public boolean validateCompanyOrg(final String company, final String orgid)
    '''
def getKPISelect():
    '''public String getKPISelect()
    '''
def getKPIWhere():
    '''public String getKPIWhere()
    '''
def setKPIId():
    '''public void setKPIId(final long newID)
    '''
def clearClassification():
    '''public void clearClassification()
    '''
