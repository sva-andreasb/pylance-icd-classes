MAXPRIORITY = "int  999"
def WOService():
    '''    public WOService()
    public WOService(final MXServer mxServer)
    '''
def restart():
    '''    public void restart()
    '''
def calculateWorkPriority():
    '''    public void calculateWorkPriority(final MboRemote forWO, final UserInfo ui)
    '''
def calculateResponseDate():
    '''    public void calculateResponseDate(final WO forWO)
    '''
def getEditSettings():
    '''    public WoEditSettings getEditSettings(final WO forWO)
    '''
def getWorkTypeAttribute():
    '''    public boolean getWorkTypeAttribute(final WO forWO, final String attr)
    '''
def updateWoForMovedAsset():
    '''    public void updateWoForMovedAsset(final MboRemote movedAsset)
    '''
def initCriteriaList():
    '''    public void initCriteriaList(final Hashtable criteriaTable)
    '''
def tagoutsMustBelongToHazards():
    '''    public boolean tagoutsMustBelongToHazards()
    '''
def init():
    '''    public void init()
    '''
def destroy():
    '''    public void destroy()
    '''
def changeStatus():
    '''    public void changeStatus(@WSMboKey("WORKORDER") final WORemote wo, final String status, final Date date, final String memo)
    '''
def getISCalEditSettings():
    '''    public WoEditSettings getISCalEditSettings(final WO wo)
    '''
def getAssingment():
    '''    public Assignment getAssingment(final String assignmentid, final UserInfo userInfo)
    '''
def getLaborCode():
    '''    public Labor getLaborCode(final UserInfo userInfo)
    '''
def ownership():
    '''    public void ownership(@WSMboKey("WORKORDER") final MboRemote wo)
    '''
def removeWorkPlan():
    '''    public boolean removeWorkPlan(@WSMboKey("WORKORDER") final MboRemote wo)
    '''
def removeSafetyPlan():
    '''    public void removeSafetyPlan(@WSMboKey("WORKORDER") final MboRemote wo)
    '''
def reportDowntime():
    '''    public void reportDowntime(@WSMboKey("WORKORDER") final MboRemote wo, final Date startDate, final Date endDate, final double hoursDown, final String code, final boolean operational)
    '''
def startTimer():
    '''    public void startTimer(@WSMboKey("WORKORDER") final MboRemote wo)
    '''
def startTimerStartDate():
    '''    public void startTimerStartDate(@WSMboKey("WORKORDER") final MboRemote wo, final Date startDateTime, final Long anywhererefid, final String transtype)
    '''
def stopTimer():
    '''    public void stopTimer(@WSMboKey("WORKORDER") final MboRemote wo)
    '''
def stopTimerStartFinishDates():
    '''    public void stopTimerStartFinishDates(@WSMboKey("WORKORDER") final MboRemote wo, final Date finishDateTime, final Date startDateTime, final Boolean noStopTimerPopup)
    '''
def createFollowUp():
    '''    public MboRemote createFollowUp(@WSMboKey("WORKORDER") final MboRemote wo)
    '''
def createChange():
    '''    public MboRemote createChange(@WSMboKey("WORKORDER") final MboRemote wo)
    '''
def getQuickReportingWO():
    '''    public MboRemote getQuickReportingWO(final UserInfo userInfo)
    '''
def createProblem():
    '''    public MboRemote createProblem(@WSMboKey("WORKORDER") final MboRemote wo)
    '''
def createJPFromWO():
    '''    public MboRemote createJPFromWO(@WSMboKey("WORKORDER") final MboRemote wo, String jpnum, final String description, final String longdescription)
    '''
def getParentsInChangeStatus():
    '''    public Vector getParentsInChangeStatus()
    '''
def clearParentsInChangeStatus():
    '''    public void clearParentsInChangeStatus()
    '''
def assignLabor():
    '''    public void assignLabor(@WSMboKey("ASSIGNMENT") final MboRemote assignment, final String laborcode, final String orgid)
    '''
def startAssignment():
    '''    public void startAssignment(@WSMboKey("ASSIGNMENT") final MboRemote assignment)
    '''
def interruptAssignment():
    '''    public void interruptAssignment(@WSMboKey("ASSIGNMENT") final MboRemote assignment)
    '''
def finishAssignment():
    '''    public void finishAssignment(@WSMboKey("ASSIGNMENT") final MboRemote assignment)
    '''
def getLaborCraftRateSet():
    '''    public MboSetRemote getLaborCraftRateSet(final MboRemote assignment)
    '''
def createAssignmentwithAssignedLabor():
    '''    public void createAssignmentwithAssignedLabor(@WSMboKey("WORKORDER") final MboRemote workorder, final String laborcode, final String orgid, final String laborhrs, final Date starttime)
    '''
def getAvailableLabor():
    '''    public MboSetRemote getAvailableLabor(@WSMboKey("WORKORDER") final MboRemote wo, final Date fromdate, final Date todate, final String vendor, final String contractnum, final String location, final Boolean assigned, final String siteid, final String craft, final String skilllevel, final String orgid)
    '''
def applyOwner():
    '''    public void applyOwner(@WSMboKey("WORKORDER") final MboRemote wo, final String owner)
    '''
def applyOwnerGroup():
    '''    public void applyOwnerGroup(@WSMboKey("WORKORDER") final MboRemote wo, final String ownergroup)
    '''
def getWorkLog():
    '''    public MboSetRemote getWorkLog(@WSMboKey("WORKORDER") final MboRemote wo, Boolean viewSR)
    '''
def generateWORelRecord():
    '''    public void generateWORelRecord(@WSMboKey("WORKORDER") final MboRemote wo, final String wonum, final String siteId)
    '''
def downtimereport():
    '''    public MboRemote downtimereport(@WSMboKey("WORKORDER") final MboRemote wo, final Date statuschangedate, final String statuschangecode, final String operational)
    '''
def checkEAcfg():
    '''    public Map<String, Object> checkEAcfg()
    '''
def getEAToken():
    '''    public Map<String, Object> getEAToken()
    '''
def getJobPlans():
    '''    public MboSetRemote getJobPlans(@WSMboKey("WORKORDER") final WORemote wo, final Boolean jpincludeclassless, final Boolean jpassets)
    '''
def changeWOStatus():
    '''    public void changeWOStatus(@WSMboKey("WORKORDER") final WORemote wo, final String status, final Date date, final String memo)
    '''
def completeAssignment():
    '''    public void completeAssignment(@WSMboKey("ASSIGNMENT") final MboRemote assignment)
    '''
def getAvailableCrew():
    '''    public MboSetRemote getAvailableCrew(@WSMboKey("WORKORDER") final MboRemote wo, final Date fromdate, final Date todate, final String persongroup, final String amcrewtype, final String company, final Boolean assigned, final String siteid, final String orgid)
    '''
def getAssistUri():
    '''    public Map<String, Object> getAssistUri(final OslcRequest request)
    '''
