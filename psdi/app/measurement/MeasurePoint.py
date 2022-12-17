GENERATING_WORK = "String  \"MEASUREPOINT.GeneratingWork\""
def ():
    '''returns MeasurePoint\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def initFieldFlagsOnMbo():
    '''returns None\n\n
    initFieldFlagsOnMbo(final String attrName)\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def generateAutoKey():
    '''returns None\n\n
    generateAutoKey()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def getJobPlanOrPMToGenWO():
    '''returns Object\n\n
    getJobPlanOrPMToGenWO()\n
    '''
def getJobPlanOrPMToGenWOForGaugeMeter():
    '''returns Object\n\n
    getJobPlanOrPMToGenWOForGaugeMeter()\n
    '''
def getJobPlanOrPMToGenWOForCharacteristicMeter():
    '''returns Object\n\n
    getJobPlanOrPMToGenWOForCharacteristicMeter()\n
    getJobPlanOrPMToGenWOForCharacteristicMeter(final MboRemote measurement)\n
    '''
def generateWorkOrder():
    '''returns None\n\n
    generateWorkOrder(final Date effectiveDate, final String memo, final boolean actionsAsCriteria)\n
    generateWorkOrder(final Date effectiveDate, final String memo, final boolean actionsAsCriteria, final MboRemote measurement)\n
    '''
def generateWorkOrderForCharacteristicMeter():
    '''returns None\n\n
    generateWorkOrderForCharacteristicMeter(final Date effectiveDate, final String memo, final boolean actionsAsCriteria)\n
    generateWorkOrderForCharacteristicMeter(final Date effectiveDate, final String memo, final boolean actionsAsCriteria, final MboRemote measurement)\n
    '''
def generateWorkOrderForGaugeMeter():
    '''returns None\n\n
    generateWorkOrderForGaugeMeter(final Date effectiveDate, final String memo, final boolean actionsAsCriteria)\n
    generateWorkOrderForGaugeMeter(final Date effectiveDate, final String memo, final boolean actionsAsCriteria, final MboRemote measurement)\n
    '''
def genWOAndPointWOFromPM():
    '''returns None\n\n
    genWOAndPointWOFromPM(final Date effectiveDate, final String memo, final boolean useActionLimitCriteria, final String pmnum, final int priority)\n
    genWOAndPointWOFromPM(final Date effectiveDate, final String memo, final boolean useActionLimitCriteria, final String pmnum, int priority, final MboRemote measurement)\n
    '''
def genWOAndPointWOFromJobPlan():
    '''returns None\n\n
    genWOAndPointWOFromJobPlan(final Date effectiveDate, final String memo, final boolean useActionLimitCriteria, final String jpnum, final int priority)\n
    genWOAndPointWOFromJobPlan(final Date effectiveDate, final String memo, final boolean useActionLimitCriteria, final String jpnum, int priority, final MboRemote measurement)\n
    '''
def getDeployedMeter():
    '''returns MboRemote\n\n
    getDeployedMeter()\n
    '''
def getDeployedMeterForUpdate():
    '''returns MboRemote\n\n
    getDeployedMeterForUpdate()\n
    '''
def updateMeterOnMeasureDeletion():
    '''returns None\n\n
    updateMeterOnMeasureDeletion()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def setMoveAssetFlag():
    '''returns None\n\n
    setMoveAssetFlag(final boolean flag)\n
    '''
def isChangeByUserWhenSetFromLookup():
    '''returns boolean\n\n
    isChangeByUserWhenSetFromLookup(final String lookupAttrName, final String attributeName)\n
    '''
