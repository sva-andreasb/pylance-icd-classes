NO_USERINTERACTIVE = "int  101"
BEFORE = "int  -1"
EQUALS = "int  0"
AFTER = "int  1"
def ():
    '''returns WOStatusHandler\n\n
    (final StatefulMbo sm)\n
    '''
def checkStatusChangeAuthorization():
    '''returns None\n\n
    checkStatusChangeAuthorization(final String desiredStatus)\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String currentStatus, final String desiredStatus, final Date asOfDate, final String memo)\n
    '''
def materialsReceiptsCompleted():
    '''returns boolean\n\n
    materialsReceiptsCompleted()\n
    '''
def postStatusChange():
    '''returns None\n\n
    postStatusChange(final String currentStatus, final String status, final Date asOfDate, final String memo)\n
    '''
def updateMboForStatus():
    '''returns None\n\n
    updateMboForStatus(final String status)\n
    '''
def resetUsingAssetWorkType():
    '''returns None\n\n
    resetUsingAssetWorkType()\n
    '''
def resetUsingLocationWorkType():
    '''returns None\n\n
    resetUsingLocationWorkType()\n
    '''
def validatePlannedLaborCraftRate():
    '''returns None\n\n
    validatePlannedLaborCraftRate()\n
    '''
def validateAssignAMCrew():
    '''returns None\n\n
    validateAssignAMCrew()\n
    '''
def alertPMStatus():
    '''returns boolean\n\n
    alertPMStatus(final String currentStatus, final String desiredStatus)\n
    '''
def canChangePFCStatus():
    '''returns boolean\n\n
    canChangePFCStatus(final String currentStatus, final String desiredStatus, final long accessModifier, final boolean throwExceptions)\n
    '''
def canChangeStatusCal():
    '''returns None\n\n
    canChangeStatusCal(final String currentStatus, final String desiredStatus, final long accessModifier)\n
    '''
def postStatusChangeCal():
    '''returns None\n\n
    postStatusChangeCal(final String currentStatus, final String status, final Date asOfDate, final String memo)\n
    '''
def cancelYesNOMessage():
    '''returns None\n\n
    cancelYesNOMessage(final String message)\n
    '''
def timerIsActive():
    '''returns None\n\n
    timerIsActive()\n
    '''
def toIncludeTaskLabTrans():
    '''returns int\n\n
    toIncludeTaskLabTrans()\n
    '''
