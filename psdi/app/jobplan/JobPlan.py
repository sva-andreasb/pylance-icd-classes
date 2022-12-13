def JobPlan():
    '''public JobPlan(final MboSet ms)
    '''
def init():
    '''public void init()
    '''
def initFieldFlagsOnMbo():
    '''public void initFieldFlagsOnMbo(final String attrName)
    '''
def add():
    '''public void add()
    '''
def delete():
    '''public void delete(final long accessModifier)
    '''
def canDelete():
    '''public void canDelete()
    '''
def generateAutoKey():
    '''public void generateAutoKey()
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def getTotals():
    '''public Vector getTotals(final String siteid)
    '''
def copySparePartsToJPMatSet():
    '''public void copySparePartsToJPMatSet(final MboSetRemote sparePartSet)
    '''
def createJPTaskFromWOTask():
    '''public Mbo createJPTaskFromWOTask(final Mbo fromWO, final Mbo fromWOTask, final MboSet jpTasks)
    '''
def createJPTaskFromWOChild():
    '''public Mbo createJPTaskFromWOChild(final Mbo fromWO, final Mbo fromWOChild, final MboSet jpTasks)
    '''
def createJPLaborFromWOLabor():
    '''public Mbo createJPLaborFromWOLabor(final Mbo fromWO, final Mbo fromWOLabor, final MboSet jpLabors)
    '''
def createJPMaterialFromWOMaterial():
    '''public Mbo createJPMaterialFromWOMaterial(final Mbo fromWO, final Mbo fromWOMaterial, final MboSet jpMaterials)
    '''
def createJPServiceFromWPService():
    '''public Mbo createJPServiceFromWPService(final Mbo fromWO, final Mbo fromWPService, final MboSet jpServiceSet)
    '''
def createJPToolFromWOTool():
    '''public Mbo createJPToolFromWOTool(final Mbo fromWO, final Mbo fromWOTool, final MboSet jpTools)
    '''
def createJPAssetFromWOAsset():
    '''public void createJPAssetFromWOAsset(final Mbo fromWO, final MboSet jpAssets)
    '''
def createJPTaskRelFromWOTaskRel():
    '''public Mbo createJPTaskRelFromWOTaskRel(final Mbo fromWO, final Mbo fromWOTaskRel, final MboSet jptaskRelations, final Map<String, Mbo> woTaskLookup)
    '''
def appValidate():
    '''public void appValidate()
    '''
def validateJPKey():
    '''public void validateJPKey()
    '''
def getMboSet():
    '''public MboSetRemote getMboSet(final String name)
    '''
def deleteJobTaskComponents():
    '''public void deleteJobTaskComponents(final int jptask, String taskorg, String tasksite)
    '''
def undeleteJobTaskComponents():
    '''public void undeleteJobTaskComponents(final int jptask, String taskorg, String tasksite)
    '''
def updatePredecessorFields():
    '''public void updatePredecessorFields()
    '''
def componentAdded():
    '''public void componentAdded()
    '''
def getStatusListName():
    '''public String getStatusListName()
    '''
def changeStatus():
    '''public void changeStatus(final String status, Date date, final String memo, final long accessModifier)
    '''
def canChangeStatus():
    '''public void canChangeStatus(final JobPlanRemote jobplan, String currentStatus, String desiredStatus)
    '''
def nestedJobPlans():
    '''public boolean nestedJobPlans(final JobPlanRemote jobplan, String currentStatus, String desiredStatus)
    '''
def doChangeStatus():
    '''public void doChangeStatus(final JobPlanRemote jobplan, String currentStatus, String desiredStatus, final Date date, final String memo)
    '''
def getJobPlanComponentSet():
    '''public MboSetRemote getJobPlanComponentSet(final String maxRelName, final String orgid, final String siteid)
    '''
def clearClassification():
    '''public void clearClassification()
    '''
def validateProcessFlow():
    '''public void validateProcessFlow()
    '''
def validateNetwork():
    '''public void validateNetwork(final Hashtable<String, LinkedList> htSuccessors, final LinkedList<String> startingNodes, final boolean printDebugMsgs)
    '''
def findMatchingTasks():
    '''public Stack<MboRemote> findMatchingTasks(final MboSetRemote taskSet, final String orgid, final String siteid, final String jptask)
    '''
def suspendChildrensProcessFlow():
    '''public void suspendChildrensProcessFlow(final boolean torf)
    '''
def setChildrensFlowControl():
    '''public void setChildrensFlowControl(final boolean torf)
    '''
def changeChildrensFieldValue():
    '''public void changeChildrensFieldValue(final String fieldname, final String fieldvalue, final long accessModifier)
    '''
def propagateRevisionStatus():
    '''public void propagateRevisionStatus(final JobPlanRemote newRevision)
    '''
def propagateRevisionNumber():
    '''public void propagateRevisionNumber(final JobPlanRemote newRevision)
    '''
def revise():
    '''public MboRemote revise(final String revDescription)
    '''
def canRevise():
    '''public void canRevise()
    '''
def setReadOnlyFields():
    '''public void setReadOnlyFields()
    '''
def isRevEnabled():
    '''public boolean isRevEnabled()
    '''
def isRevisionStatusNotAllowed():
    '''public boolean isRevisionStatusNotAllowed()
    '''
def setStatusHistoryFields():
    '''public void setStatusHistoryFields(final JobPlan jp, final Date date, final String memo)
    '''
def active():
    '''public void active(final MboRemote jobplan, final String currentMaxStatus, final String desiredStatus, final Date date)
    '''
def getNextRevNum():
    '''public int getNextRevNum()
    '''
def getMaxValidStatusRevNum():
    '''public int getMaxValidStatusRevNum()
    '''
def getSpecificStringOfSites():
    '''public String getSpecificStringOfSites(final MboSetRemote jobPlanSubSets)
    '''
def copyCrewTypeToWpLaborSet():
    '''public void copyCrewTypeToWpLaborSet(final MboSetRemote crewTypeSet)
    '''
def getHistoryFlag():
    '''public boolean getHistoryFlag()
    '''
def canDeleteAttachedDocs():
    '''public void canDeleteAttachedDocs()
    '''
def initRelationship():
    '''public void initRelationship(final String relationName, final MboSetRemote mboSet)
    '''
def setRelatedMboEditibility():
    '''public void setRelatedMboEditibility(final String relationName, final MboSetRemote relatedSet)
    '''
def setRevisedStatus():
    '''public void setRevisedStatus(final boolean value)
    '''
def getRevisedStatus():
    '''public boolean getRevisedStatus()
    '''
def setListPage():
    '''public void setListPage(final boolean value)
    '''
def getListPage():
    '''public boolean getListPage()
    '''
def isDuringDUPLICATE():
    '''public boolean isDuringDUPLICATE()
    '''
def setDuringDUPLICATE():
    '''public void setDuringDUPLICATE(final boolean value)
    '''
