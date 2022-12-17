MAXPRIORITY = "int  999"
def ():
    '''returns WOService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def restart():
    '''returns None\n\n
    restart()\n
    '''
def calculateWorkPriority():
    '''returns None\n\n
    calculateWorkPriority(final MboRemote forWO, final UserInfo ui)\n
    '''
def calculateResponseDate():
    '''returns None\n\n
    calculateResponseDate(final WO forWO)\n
    '''
def getEditSettings():
    '''returns WoEditSettings\n\n
    getEditSettings(final WO forWO)\n
    '''
def getWorkTypeAttribute():
    '''returns boolean\n\n
    getWorkTypeAttribute(final WO forWO, final String attr)\n
    '''
def updateWoForMovedAsset():
    '''returns None\n\n
    updateWoForMovedAsset(final MboRemote movedAsset)\n
    '''
def initCriteriaList():
    '''returns None\n\n
    initCriteriaList(final Hashtable criteriaTable)\n
    '''
def tagoutsMustBelongToHazards():
    '''returns boolean\n\n
    tagoutsMustBelongToHazards()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(@WSMboKey("WORKORDER") final WORemote wo, final String status, final Date date, final String memo)\n
    '''
def getISCalEditSettings():
    '''returns WoEditSettings\n\n
    getISCalEditSettings(final WO wo)\n
    '''
def getAssingment():
    '''returns Assignment\n\n
    getAssingment(final String assignmentid, final UserInfo userInfo)\n
    '''
def getLaborCode():
    '''returns Labor\n\n
    getLaborCode(final UserInfo userInfo)\n
    '''
def ownership():
    '''returns None\n\n
    ownership(@WSMboKey("WORKORDER") final MboRemote wo)\n
    '''
def removeWorkPlan():
    '''returns boolean\n\n
    removeWorkPlan(@WSMboKey("WORKORDER") final MboRemote wo)\n
    '''
def removeSafetyPlan():
    '''returns None\n\n
    removeSafetyPlan(@WSMboKey("WORKORDER") final MboRemote wo)\n
    '''
def reportDowntime():
    '''returns None\n\n
    reportDowntime(@WSMboKey("WORKORDER") final MboRemote wo, final Date startDate, final Date endDate, final double hoursDown, final String code, final boolean operational)\n
    '''
def startTimer():
    '''returns None\n\n
    startTimer(@WSMboKey("WORKORDER") final MboRemote wo)\n
    '''
def startTimerStartDate():
    '''returns None\n\n
    startTimerStartDate(@WSMboKey("WORKORDER") final MboRemote wo, final Date startDateTime, final Long anywhererefid, final String transtype)\n
    '''
def stopTimer():
    '''returns None\n\n
    stopTimer(@WSMboKey("WORKORDER") final MboRemote wo)\n
    '''
def stopTimerStartFinishDates():
    '''returns None\n\n
    stopTimerStartFinishDates(@WSMboKey("WORKORDER") final MboRemote wo, final Date finishDateTime, final Date startDateTime, final Boolean noStopTimerPopup)\n
    '''
def createFollowUp():
    '''returns MboRemote\n\n
    createFollowUp(@WSMboKey("WORKORDER") final MboRemote wo)\n
    '''
def createChange():
    '''returns MboRemote\n\n
    createChange(@WSMboKey("WORKORDER") final MboRemote wo)\n
    '''
def getQuickReportingWO():
    '''returns MboRemote\n\n
    getQuickReportingWO(final UserInfo userInfo)\n
    '''
def createProblem():
    '''returns MboRemote\n\n
    createProblem(@WSMboKey("WORKORDER") final MboRemote wo)\n
    '''
def createJPFromWO():
    '''returns MboRemote\n\n
    createJPFromWO(@WSMboKey("WORKORDER") final MboRemote wo, String jpnum, final String description, final String longdescription)\n
    '''
def getParentsInChangeStatus():
    '''returns Vector\n\n
    getParentsInChangeStatus()\n
    '''
def clearParentsInChangeStatus():
    '''returns None\n\n
    clearParentsInChangeStatus()\n
    '''
def assignLabor():
    '''returns None\n\n
    assignLabor(@WSMboKey("ASSIGNMENT") final MboRemote assignment, final String laborcode, final String orgid)\n
    '''
def startAssignment():
    '''returns None\n\n
    startAssignment(@WSMboKey("ASSIGNMENT") final MboRemote assignment)\n
    '''
def interruptAssignment():
    '''returns None\n\n
    interruptAssignment(@WSMboKey("ASSIGNMENT") final MboRemote assignment)\n
    '''
def finishAssignment():
    '''returns None\n\n
    finishAssignment(@WSMboKey("ASSIGNMENT") final MboRemote assignment)\n
    '''
def getLaborCraftRateSet():
    '''returns MboSetRemote\n\n
    getLaborCraftRateSet(final MboRemote assignment)\n
    '''
def createAssignmentwithAssignedLabor():
    '''returns None\n\n
    createAssignmentwithAssignedLabor(@WSMboKey("WORKORDER") final MboRemote workorder, final String laborcode, final String orgid, final String laborhrs, final Date starttime)\n
    '''
def getAvailableLabor():
    '''returns MboSetRemote\n\n
    getAvailableLabor(@WSMboKey("WORKORDER") final MboRemote wo, final Date fromdate, final Date todate, final String vendor, final String contractnum, final String location, final Boolean assigned, final String siteid, final String craft, final String skilllevel, final String orgid)\n
    '''
def applyOwner():
    '''returns None\n\n
    applyOwner(@WSMboKey("WORKORDER") final MboRemote wo, final String owner)\n
    '''
def applyOwnerGroup():
    '''returns None\n\n
    applyOwnerGroup(@WSMboKey("WORKORDER") final MboRemote wo, final String ownergroup)\n
    '''
def getWorkLog():
    '''returns MboSetRemote\n\n
    getWorkLog(@WSMboKey("WORKORDER") final MboRemote wo, Boolean viewSR)\n
    '''
def generateWORelRecord():
    '''returns None\n\n
    generateWORelRecord(@WSMboKey("WORKORDER") final MboRemote wo, final String wonum, final String siteId)\n
    '''
def downtimereport():
    '''returns MboRemote\n\n
    downtimereport(@WSMboKey("WORKORDER") final MboRemote wo, final Date statuschangedate, final String statuschangecode, final String operational)\n
    '''
def getJobPlans():
    '''returns MboSetRemote\n\n
    getJobPlans(@WSMboKey("WORKORDER") final WORemote wo, final Boolean jpincludeclassless, final Boolean jpassets)\n
    '''
def changeWOStatus():
    '''returns None\n\n
    changeWOStatus(@WSMboKey("WORKORDER") final WORemote wo, final String status, final Date date, final String memo)\n
    '''
def completeAssignment():
    '''returns None\n\n
    completeAssignment(@WSMboKey("ASSIGNMENT") final MboRemote assignment)\n
    '''
def getAvailableCrew():
    '''returns MboSetRemote\n\n
    getAvailableCrew(@WSMboKey("WORKORDER") final MboRemote wo, final Date fromdate, final Date todate, final String persongroup, final String amcrewtype, final String company, final Boolean assigned, final String siteid, final String orgid)\n
    '''
