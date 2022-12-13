def applyActivityChange():
'''public void applyActivityChange(final MboRemote activityMboRemote, final MXTransaction txn)
public void applyActivityChange(final MboRemote activityMboRemote, final String ids, final MXTransaction txn)
'''
pass
def applyScenarioChange():
'''public void applyScenarioChange(final MboRemote activityMboRemote, final MboRemote ParentActMboRemote, final MXTransaction txn)
public void applyScenarioChange(final MboRemote activityMboRemote, final MboRemote ParentActMboRemote, final String ids, final MXTransaction txn)
'''
pass
def initializeActivity():
'''public void initializeActivity(final MXActivity activity, final String objectName, final MboRemote mboObject, final MXGanttModel model)
public void initializeActivity(final MXActivity activity, final String objectName, final MboRemote mboObject)
'''
pass
def initializeActivityChildren():
'''public void initializeActivityChildren(final MXActivity activity, final String objectName, final MboRemote mboObject, final MXGanttModel model)
'''
pass
def loadActivity():
'''public void loadActivity(final MXActivity activity, final String objectName, final MboRemote mboObject)
public void loadActivity(final MXActivity activity, final String objectName, final MXGanttModel model)
'''
pass
def populateActivities():
'''public void populateActivities(final HashMap<String, ArrayList<String>> queriesMap)
'''
pass
def populateActivityPropertyDetails():
'''public void populateActivityPropertyDetails()
'''
pass
def sortActivityChildren():
'''public List<IlvActivity> sortActivityChildren(final IlvActivity activity, final String objectName, final MXGanttModel model)
'''
pass
def activityRecordCount():
'''public int activityRecordCount(final HashMap<String, ArrayList<String>> queryMap)
'''
pass
def saveActivities():
'''public void saveActivities(final IlvGeneralActivity activity)
public void saveActivities(final IlvGeneralActivity activity, final MXTransaction txn)
'''
pass
def duplicateProjectData():
'''public void duplicateProjectData(final String originalProjectId)
'''
pass
def deleteProjectData():
'''public void deleteProjectData()
'''
pass
def getAsyncCount():
'''public int getAsyncCount()
'''
pass
def loadAdditionalActivities():
'''public void loadAdditionalActivities(final MXGanttModel model, final SKDAppService.ActivityData activityData)
'''
pass
def linkChildDummyNode():
'''public List<IlvActivity> linkChildDummyNode(final MXActivity activity, final MXGanttModel mxganttmodel, final SKDAppService.ActivityData activityData)
'''
pass
def getModifiedActivityChildren():
'''public List<IlvActivity> getModifiedActivityChildren(final MXActivity activity, final String objectName, final MboRemote mboObject, final MXGanttModel model)
'''
pass
