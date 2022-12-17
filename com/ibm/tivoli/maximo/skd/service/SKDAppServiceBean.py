def ():
    '''returns SKDAppServiceBean\n\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def getUserInfo():
    '''returns UserInfo\n\n
    getUserInfo()\n
    '''
def getSKDAppService():
    '''returns SKDAppService\n\n
    getSKDAppService()\n
    '''
def setSKDAppService():
    '''returns None\n\n
    setSKDAppService(final SKDAppService skdAppService)\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(final String mboObjectName)\n
    '''
def getMboSetInfo():
    '''returns MboSetInfo\n\n
    getMboSetInfo(final String mboName)\n
    '''
def addModelChanges():
    '''returns None\n\n
    addModelChanges(final GanttModelChanges newModelChanges)\n
    '''
def clearModelChanges():
    '''returns None\n\n
    clearModelChanges()\n
    '''
def hasModelChanges():
    '''returns boolean\n\n
    hasModelChanges()\n
    '''
def getCurrentProjectid():
    '''returns String\n\n
    getCurrentProjectid()\n
    '''
def scenarioProjectidandname():
    '''returns String\n\n
    scenarioProjectidandname()\n
    '''
def saveModelChanges():
    '''returns None\n\n
    saveModelChanges()\n
    '''
def saveModelChangesFromAction():
    '''returns None\n\n
    saveModelChangesFromAction(final boolean saveBeforeAction)\n
    '''
def setConfigChanges():
    '''returns None\n\n
    setConfigChanges(final GanttConfigChanges newGanttConfigChanges)\n
    '''
def clearConfigChanges():
    '''returns None\n\n
    clearConfigChanges()\n
    '''
def saveConfigChanges():
    '''returns None\n\n
    saveConfigChanges()\n
    '''
def getProjectName():
    '''returns String\n\n
    getProjectName(final String projectId)\n
    '''
def getProjectScenarioName():
    '''returns String\n\n
    getProjectScenarioName(final String projectId)\n
    '''
def saveActivities():
    '''returns None\n\n
    saveActivities(final UserInfo userInfo, final MboRemote projectMbo, final IlvGeneralActivity activity)\n
    saveActivities(final UserInfo userInfo, final MboRemote projectMbo, final IlvGeneralActivity activity, final MXTransaction txn)\n
    '''
def saveConstraints():
    '''returns None\n\n
    saveConstraints(final UserInfo userInfo, final MboRemote projectMbo, final IlvGeneralConstraint constraint)\n
    '''
def saveUserPropertyChanges():
    '''returns None\n\n
    saveUserPropertyChanges(final UserPropertyChanges propertyChanges)\n
    '''
