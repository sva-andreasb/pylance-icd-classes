COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def ():
    '''returns PmChgWOChange\n\n
    (final MboSet ms)\n
    '''
def findAndSetAvailableSchedulerValue():
    '''returns None\n\n
    findAndSetAvailableSchedulerValue()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def detectConflicts():
    '''returns None\n\n
    detectConflicts()\n
    '''
def hasBlackoutConflict():
    '''returns boolean\n\n
    hasBlackoutConflict(final String type)\n
    hasBlackoutConflict()\n
    '''
def hasChangeWindowConflict():
    '''returns boolean\n\n
    hasChangeWindowConflict()\n
    '''
def getChangeWindowConflictRecords():
    '''returns List<PmChgConflictDetectionRemote>\n\n
    getChangeWindowConflictRecords()\n
    '''
def hasCiConflict():
    '''returns boolean\n\n
    hasCiConflict()\n
    '''
def getCiConflictRecords():
    '''returns List<PmChgConflictDetectionRemote>\n\n
    getCiConflictRecords()\n
    '''
def getBlackoutConflictRecords():
    '''returns List<PmChgConflictDetectionRemote>\n\n
    getBlackoutConflictRecords()\n
    '''
def hasConflict():
    '''returns boolean\n\n
    hasConflict()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def hasImpactedCis():
    '''returns boolean\n\n
    hasImpactedCis()\n
    '''
def previewImpactedCIs():
    '''returns MboSetRemote\n\n
    previewImpactedCIs()\n
    '''
def previewHistoricalImpactedAssets():
    '''returns MboSetRemote\n\n
    previewHistoricalImpactedAssets()\n
    '''
def previewHistoricalImpactedCIs():
    '''returns MboSetRemote\n\n
    previewHistoricalImpactedCIs()\n
    '''
def setJobPlanFieldFlag():
    '''returns None\n\n
    setJobPlanFieldFlag()\n
    '''
def calculateImpactedCIs():
    '''returns None\n\n
    calculateImpactedCIs()\n
    '''
def detectHistoricalImpacts():
    '''returns None\n\n
    detectHistoricalImpacts()\n
    '''
def validateReadyForImpactAssessment():
    '''returns None\n\n
    validateReadyForImpactAssessment(final boolean checkAssets)\n
    '''
def isReadyForImpactAssessment():
    '''returns boolean\n\n
    isReadyForImpactAssessment(final boolean checkAssets)\n
    '''
def applyBlackoutApprovers():
    '''returns None\n\n
    applyBlackoutApprovers(final String blackoutType, final String apprlType)\n
    '''
def addScheduleApproversByRole():
    '''returns None\n\n
    addScheduleApproversByRole(final String roleName, final String apprlType)\n
    '''
def deleteScheduleApprovers():
    '''returns None\n\n
    deleteScheduleApprovers()\n
    '''
def calculateOutageImpact():
    '''returns int\n\n
    calculateOutageImpact()\n
    '''
def previewOutageImpact():
    '''returns int\n\n
    previewOutageImpact()\n
    '''
def calculateMaximumAssessedImpact():
    '''returns int\n\n
    calculateMaximumAssessedImpact()\n
    '''
def reportMessage():
    '''returns None\n\n
    reportMessage(final MXApplicationException mae)\n
    '''
def copyWOFieldsToMultiAsset():
    '''returns None\n\n
    copyWOFieldsToMultiAsset(final MultiAssetLocCIRemote multiAssetMbo)\n
    '''
