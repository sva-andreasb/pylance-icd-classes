def applyActivityChange():
    '''returns None\n\n
    applyActivityChange(final MboRemote activityMboRemote, final MXTransaction txn)\n
    applyActivityChange(final MboRemote activityMboRemote, final String ids, final MXTransaction txn)\n
    '''
def applyScenarioChange():
    '''returns None\n\n
    applyScenarioChange(final MboRemote activityMboRemote, final MboRemote ParentActMboRemote, final MXTransaction txn)\n
    applyScenarioChange(final MboRemote activityMboRemote, final MboRemote ParentActMboRemote, final String ids, final MXTransaction txn)\n
    '''
def initializeActivity():
    '''returns None\n\n
    initializeActivity(final MXActivity activity, final String objectName, final MboRemote mboObject, final MXGanttModel model)\n
    initializeActivity(final MXActivity activity, final String objectName, final MboRemote mboObject)\n
    '''
def initializeActivityChildren():
    '''returns None\n\n
    initializeActivityChildren(final MXActivity activity, final String objectName, final MboRemote mboObject, final MXGanttModel model)\n
    '''
def loadActivity():
    '''returns None\n\n
    loadActivity(final MXActivity activity, final String objectName, final MboRemote mboObject)\n
    loadActivity(final MXActivity activity, final String objectName, final MXGanttModel model)\n
    '''
def populateActivities():
    '''returns None\n\n
    populateActivities(final HashMap<String, ArrayList<String>> queriesMap)\n
    '''
def populateActivityPropertyDetails():
    '''returns None\n\n
    populateActivityPropertyDetails()\n
    '''
def sortActivityChildren():
    '''returns List<IlvActivity>\n\n
    sortActivityChildren(final IlvActivity activity, final String objectName, final MXGanttModel model)\n
    '''
def activityRecordCount():
    '''returns int\n\n
    activityRecordCount(final HashMap<String, ArrayList<String>> queryMap)\n
    '''
def saveActivities():
    '''returns None\n\n
    saveActivities(final IlvGeneralActivity activity)\n
    saveActivities(final IlvGeneralActivity activity, final MXTransaction txn)\n
    '''
def duplicateProjectData():
    '''returns None\n\n
    duplicateProjectData(final String originalProjectId)\n
    '''
def deleteProjectData():
    '''returns None\n\n
    deleteProjectData()\n
    '''
def getAsyncCount():
    '''returns int\n\n
    getAsyncCount()\n
    '''
def loadAdditionalActivities():
    '''returns None\n\n
    loadAdditionalActivities(final MXGanttModel model, final SKDAppService.ActivityData activityData)\n
    '''
def linkChildDummyNode():
    '''returns List<IlvActivity>\n\n
    linkChildDummyNode(final MXActivity activity, final MXGanttModel mxganttmodel, final SKDAppService.ActivityData activityData)\n
    '''
def getModifiedActivityChildren():
    '''returns List<IlvActivity>\n\n
    getModifiedActivityChildren(final MXActivity activity, final String objectName, final MboRemote mboObject, final MXGanttModel model)\n
    '''
