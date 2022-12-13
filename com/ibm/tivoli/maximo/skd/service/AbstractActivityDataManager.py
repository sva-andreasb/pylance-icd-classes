def applyActivityChange():
    '''    public void applyActivityChange(final MboRemote activityMboRemote, final MXTransaction txn)
    public void applyActivityChange(final MboRemote activityMboRemote, final String ids, final MXTransaction txn)
    '''
def applyScenarioChange():
    '''    public void applyScenarioChange(final MboRemote activityMboRemote, final MboRemote ParentActMboRemote, final MXTransaction txn)
    public void applyScenarioChange(final MboRemote activityMboRemote, final MboRemote ParentActMboRemote, final String ids, final MXTransaction txn)
    '''
def initializeActivity():
    '''    public void initializeActivity(final MXActivity activity, final String objectName, final MboRemote mboObject, final MXGanttModel model)
    public void initializeActivity(final MXActivity activity, final String objectName, final MboRemote mboObject)
    '''
def initializeActivityChildren():
    '''    public void initializeActivityChildren(final MXActivity activity, final String objectName, final MboRemote mboObject, final MXGanttModel model)
    '''
def loadActivity():
    '''    public void loadActivity(final MXActivity activity, final String objectName, final MboRemote mboObject)
    public void loadActivity(final MXActivity activity, final String objectName, final MXGanttModel model)
    '''
def populateActivities():
    '''    public void populateActivities(final HashMap<String, ArrayList<String>> queriesMap)
    '''
def populateActivityPropertyDetails():
    '''    public void populateActivityPropertyDetails()
    '''
def sortActivityChildren():
    '''    public List<IlvActivity> sortActivityChildren(final IlvActivity activity, final String objectName, final MXGanttModel model)
    '''
def activityRecordCount():
    '''    public int activityRecordCount(final HashMap<String, ArrayList<String>> queryMap)
    '''
def saveActivities():
    '''    public void saveActivities(final IlvGeneralActivity activity)
    public void saveActivities(final IlvGeneralActivity activity, final MXTransaction txn)
    '''
def duplicateProjectData():
    '''    public void duplicateProjectData(final String originalProjectId)
    '''
def deleteProjectData():
    '''    public void deleteProjectData()
    '''
def getAsyncCount():
    '''    public int getAsyncCount()
    '''
def loadAdditionalActivities():
    '''    public void loadAdditionalActivities(final MXGanttModel model, final SKDAppService.ActivityData activityData)
    '''
def linkChildDummyNode():
    '''    public List<IlvActivity> linkChildDummyNode(final MXActivity activity, final MXGanttModel mxganttmodel, final SKDAppService.ActivityData activityData)
    '''
def getModifiedActivityChildren():
    '''    public List<IlvActivity> getModifiedActivityChildren(final MXActivity activity, final String objectName, final MboRemote mboObject, final MXGanttModel model)
    '''
