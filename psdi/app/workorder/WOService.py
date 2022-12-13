MAXPRIORITY = "int  999"
def WOService():
'''public WOService()
public WOService(final MXServer mxServer)
'''
pass
def restart():
'''public void restart()
'''
pass
def calculateWorkPriority():
'''public void calculateWorkPriority(final MboRemote forWO, final UserInfo ui)
'''
pass
def calculateResponseDate():
'''public void calculateResponseDate(final WO forWO)
'''
pass
def getEditSettings():
'''public WoEditSettings getEditSettings(final WO forWO)
'''
pass
def getWorkTypeAttribute():
'''public boolean getWorkTypeAttribute(final WO forWO, final String attr)
'''
pass
def updateWoForMovedAsset():
'''public void updateWoForMovedAsset(final MboRemote movedAsset)
'''
pass
def initCriteriaList():
'''public void initCriteriaList(final Hashtable criteriaTable)
'''
pass
def tagoutsMustBelongToHazards():
'''public boolean tagoutsMustBelongToHazards()
'''
pass
def init():
'''public void init()
'''
pass
def destroy():
'''public void destroy()
'''
pass
def changeStatus():
'''public void changeStatus(@WSMboKey("WORKORDER") final WORemote wo, final String status, final Date date, final String memo)
'''
pass
def getISCalEditSettings():
'''public WoEditSettings getISCalEditSettings(final WO wo)
'''
pass
def getAssingment():
'''public Assignment getAssingment(final String assignmentid, final UserInfo userInfo)
'''
pass
def getLaborCode():
'''public Labor getLaborCode(final UserInfo userInfo)
'''
pass
def ownership():
'''public void ownership(@WSMboKey("WORKORDER") final MboRemote wo)
'''
pass
def removeWorkPlan():
'''public boolean removeWorkPlan(@WSMboKey("WORKORDER") final MboRemote wo)
'''
pass
def removeSafetyPlan():
'''public void removeSafetyPlan(@WSMboKey("WORKORDER") final MboRemote wo)
'''
pass
def reportDowntime():
'''public void reportDowntime(@WSMboKey("WORKORDER") final MboRemote wo, final Date startDate, final Date endDate, final double hoursDown, final String code, final boolean operational)
'''
pass
def startTimer():
'''public void startTimer(@WSMboKey("WORKORDER") final MboRemote wo)
'''
pass
def startTimerStartDate():
'''public void startTimerStartDate(@WSMboKey("WORKORDER") final MboRemote wo, final Date startDateTime, final Long anywhererefid, final String transtype)
'''
pass
def stopTimer():
'''public void stopTimer(@WSMboKey("WORKORDER") final MboRemote wo)
'''
pass
def stopTimerStartFinishDates():
'''public void stopTimerStartFinishDates(@WSMboKey("WORKORDER") final MboRemote wo, final Date finishDateTime, final Date startDateTime, final Boolean noStopTimerPopup)
'''
pass
def createFollowUp():
'''public MboRemote createFollowUp(@WSMboKey("WORKORDER") final MboRemote wo)
'''
pass
def createChange():
'''public MboRemote createChange(@WSMboKey("WORKORDER") final MboRemote wo)
'''
pass
def getQuickReportingWO():
'''public MboRemote getQuickReportingWO(final UserInfo userInfo)
'''
pass
def createProblem():
'''public MboRemote createProblem(@WSMboKey("WORKORDER") final MboRemote wo)
'''
pass
def createJPFromWO():
'''public MboRemote createJPFromWO(@WSMboKey("WORKORDER") final MboRemote wo, String jpnum, final String description, final String longdescription)
'''
pass
def getParentsInChangeStatus():
'''public Vector getParentsInChangeStatus()
'''
pass
def clearParentsInChangeStatus():
'''public void clearParentsInChangeStatus()
'''
pass
def assignLabor():
'''public void assignLabor(@WSMboKey("ASSIGNMENT") final MboRemote assignment, final String laborcode, final String orgid)
'''
pass
def startAssignment():
'''public void startAssignment(@WSMboKey("ASSIGNMENT") final MboRemote assignment)
'''
pass
def interruptAssignment():
'''public void interruptAssignment(@WSMboKey("ASSIGNMENT") final MboRemote assignment)
'''
pass
def finishAssignment():
'''public void finishAssignment(@WSMboKey("ASSIGNMENT") final MboRemote assignment)
'''
pass
def getLaborCraftRateSet():
'''public MboSetRemote getLaborCraftRateSet(final MboRemote assignment)
'''
pass
def createAssignmentwithAssignedLabor():
'''public void createAssignmentwithAssignedLabor(@WSMboKey("WORKORDER") final MboRemote workorder, final String laborcode, final String orgid, final String laborhrs, final Date starttime)
'''
pass
def getAvailableLabor():
'''public MboSetRemote getAvailableLabor(@WSMboKey("WORKORDER") final MboRemote wo, final Date fromdate, final Date todate, final String vendor, final String contractnum, final String location, final Boolean assigned, final String siteid, final String craft, final String skilllevel, final String orgid)
'''
pass
def applyOwner():
'''public void applyOwner(@WSMboKey("WORKORDER") final MboRemote wo, final String owner)
'''
pass
def applyOwnerGroup():
'''public void applyOwnerGroup(@WSMboKey("WORKORDER") final MboRemote wo, final String ownergroup)
'''
pass
def getWorkLog():
'''public MboSetRemote getWorkLog(@WSMboKey("WORKORDER") final MboRemote wo, Boolean viewSR)
'''
pass
def generateWORelRecord():
'''public void generateWORelRecord(@WSMboKey("WORKORDER") final MboRemote wo, final String wonum, final String siteId)
'''
pass
def downtimereport():
'''public MboRemote downtimereport(@WSMboKey("WORKORDER") final MboRemote wo, final Date statuschangedate, final String statuschangecode, final String operational)
'''
pass
def checkEAcfg():
'''public Map<String, Object> checkEAcfg()
'''
pass
def getEAToken():
'''public Map<String, Object> getEAToken()
'''
pass
def getJobPlans():
'''public MboSetRemote getJobPlans(@WSMboKey("WORKORDER") final WORemote wo, final Boolean jpincludeclassless, final Boolean jpassets)
'''
pass
def changeWOStatus():
'''public void changeWOStatus(@WSMboKey("WORKORDER") final WORemote wo, final String status, final Date date, final String memo)
'''
pass
def completeAssignment():
'''public void completeAssignment(@WSMboKey("ASSIGNMENT") final MboRemote assignment)
'''
pass
def getAvailableCrew():
'''public MboSetRemote getAvailableCrew(@WSMboKey("WORKORDER") final MboRemote wo, final Date fromdate, final Date todate, final String persongroup, final String amcrewtype, final String company, final Boolean assigned, final String siteid, final String orgid)
'''
pass
def getAssistUri():
'''public Map<String, Object> getAssistUri(final OslcRequest request)
'''
pass
