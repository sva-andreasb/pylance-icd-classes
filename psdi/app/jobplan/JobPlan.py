def JobPlan():
'''public JobPlan(final MboSet ms)
'''
pass
def init():
'''public void init()
'''
pass
def initFieldFlagsOnMbo():
'''public void initFieldFlagsOnMbo(final String attrName)
'''
pass
def add():
'''public void add()
'''
pass
def delete():
'''public void delete(final long accessModifier)
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def generateAutoKey():
'''public void generateAutoKey()
'''
pass
def duplicate():
'''public MboRemote duplicate()
'''
pass
def getTotals():
'''public Vector getTotals(final String siteid)
'''
pass
def copySparePartsToJPMatSet():
'''public void copySparePartsToJPMatSet(final MboSetRemote sparePartSet)
'''
pass
def createJPTaskFromWOTask():
'''public Mbo createJPTaskFromWOTask(final Mbo fromWO, final Mbo fromWOTask, final MboSet jpTasks)
'''
pass
def createJPTaskFromWOChild():
'''public Mbo createJPTaskFromWOChild(final Mbo fromWO, final Mbo fromWOChild, final MboSet jpTasks)
'''
pass
def createJPLaborFromWOLabor():
'''public Mbo createJPLaborFromWOLabor(final Mbo fromWO, final Mbo fromWOLabor, final MboSet jpLabors)
'''
pass
def createJPMaterialFromWOMaterial():
'''public Mbo createJPMaterialFromWOMaterial(final Mbo fromWO, final Mbo fromWOMaterial, final MboSet jpMaterials)
'''
pass
def createJPServiceFromWPService():
'''public Mbo createJPServiceFromWPService(final Mbo fromWO, final Mbo fromWPService, final MboSet jpServiceSet)
'''
pass
def createJPToolFromWOTool():
'''public Mbo createJPToolFromWOTool(final Mbo fromWO, final Mbo fromWOTool, final MboSet jpTools)
'''
pass
def createJPAssetFromWOAsset():
'''public void createJPAssetFromWOAsset(final Mbo fromWO, final MboSet jpAssets)
'''
pass
def createJPTaskRelFromWOTaskRel():
'''public Mbo createJPTaskRelFromWOTaskRel(final Mbo fromWO, final Mbo fromWOTaskRel, final MboSet jptaskRelations, final Map<String, Mbo> woTaskLookup)
'''
pass
def appValidate():
'''public void appValidate()
'''
pass
def validateJPKey():
'''public void validateJPKey()
'''
pass
def getMboSet():
'''public MboSetRemote getMboSet(final String name)
'''
pass
def deleteJobTaskComponents():
'''public void deleteJobTaskComponents(final int jptask, String taskorg, String tasksite)
'''
pass
def undeleteJobTaskComponents():
'''public void undeleteJobTaskComponents(final int jptask, String taskorg, String tasksite)
'''
pass
def updatePredecessorFields():
'''public void updatePredecessorFields()
'''
pass
def componentAdded():
'''public void componentAdded()
'''
pass
def getStatusListName():
'''public String getStatusListName()
'''
pass
def changeStatus():
'''public void changeStatus(final String status, Date date, final String memo, final long accessModifier)
'''
pass
def canChangeStatus():
'''public void canChangeStatus(final JobPlanRemote jobplan, String currentStatus, String desiredStatus)
'''
pass
def nestedJobPlans():
'''public boolean nestedJobPlans(final JobPlanRemote jobplan, String currentStatus, String desiredStatus)
'''
pass
def doChangeStatus():
'''public void doChangeStatus(final JobPlanRemote jobplan, String currentStatus, String desiredStatus, final Date date, final String memo)
'''
pass
def getJobPlanComponentSet():
'''public MboSetRemote getJobPlanComponentSet(final String maxRelName, final String orgid, final String siteid)
'''
pass
def clearClassification():
'''public void clearClassification()
'''
pass
def validateProcessFlow():
'''public void validateProcessFlow()
'''
pass
def validateNetwork():
'''public void validateNetwork(final Hashtable<String, LinkedList> htSuccessors, final LinkedList<String> startingNodes, final boolean printDebugMsgs)
'''
pass
def findMatchingTasks():
'''public Stack<MboRemote> findMatchingTasks(final MboSetRemote taskSet, final String orgid, final String siteid, final String jptask)
'''
pass
def suspendChildrensProcessFlow():
'''public void suspendChildrensProcessFlow(final boolean torf)
'''
pass
def setChildrensFlowControl():
'''public void setChildrensFlowControl(final boolean torf)
'''
pass
def changeChildrensFieldValue():
'''public void changeChildrensFieldValue(final String fieldname, final String fieldvalue, final long accessModifier)
'''
pass
def propagateRevisionStatus():
'''public void propagateRevisionStatus(final JobPlanRemote newRevision)
'''
pass
def propagateRevisionNumber():
'''public void propagateRevisionNumber(final JobPlanRemote newRevision)
'''
pass
def revise():
'''public MboRemote revise(final String revDescription)
'''
pass
def canRevise():
'''public void canRevise()
'''
pass
def setReadOnlyFields():
'''public void setReadOnlyFields()
'''
pass
def isRevEnabled():
'''public boolean isRevEnabled()
'''
pass
def isRevisionStatusNotAllowed():
'''public boolean isRevisionStatusNotAllowed()
'''
pass
def setStatusHistoryFields():
'''public void setStatusHistoryFields(final JobPlan jp, final Date date, final String memo)
'''
pass
def active():
'''public void active(final MboRemote jobplan, final String currentMaxStatus, final String desiredStatus, final Date date)
'''
pass
def getNextRevNum():
'''public int getNextRevNum()
'''
pass
def getMaxValidStatusRevNum():
'''public int getMaxValidStatusRevNum()
'''
pass
def getSpecificStringOfSites():
'''public String getSpecificStringOfSites(final MboSetRemote jobPlanSubSets)
'''
pass
def copyCrewTypeToWpLaborSet():
'''public void copyCrewTypeToWpLaborSet(final MboSetRemote crewTypeSet)
'''
pass
def getHistoryFlag():
'''public boolean getHistoryFlag()
'''
pass
def canDeleteAttachedDocs():
'''public void canDeleteAttachedDocs()
'''
pass
def initRelationship():
'''public void initRelationship(final String relationName, final MboSetRemote mboSet)
'''
pass
def setRelatedMboEditibility():
'''public void setRelatedMboEditibility(final String relationName, final MboSetRemote relatedSet)
'''
pass
def setRevisedStatus():
'''public void setRevisedStatus(final boolean value)
'''
pass
def getRevisedStatus():
'''public boolean getRevisedStatus()
'''
pass
def setListPage():
'''public void setListPage(final boolean value)
'''
pass
def getListPage():
'''public boolean getListPage()
'''
pass
def isDuringDUPLICATE():
'''public boolean isDuringDUPLICATE()
'''
pass
def setDuringDUPLICATE():
'''public void setDuringDUPLICATE(final boolean value)
'''
pass
