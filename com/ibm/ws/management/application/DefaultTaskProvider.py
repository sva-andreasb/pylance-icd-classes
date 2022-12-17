taskHelperSuffix = "String  \"Helper\""
def ():
    '''returns DefaultTaskProvider\n\n
    ()\n
    '''
def provideClientDeploymentTasks():
    '''returns None\n\n
    provideClientDeploymentTasks(final Vector taskInfo, final AppDeploymentInfo deploymentInfo, final Hashtable prefs)\n
    '''
def provideServerInstallExtensions():
    '''returns None\n\n
    provideServerInstallExtensions(final Vector installTasks, final InstallScheduler scheduler)\n
    '''
def provideServerUninstallExtensions():
    '''returns None\n\n
    provideServerUninstallExtensions(final Vector uninstallTasks, final Scheduler scheduler)\n
    '''
def provideServerExtensionsForEdit():
    '''returns None\n\n
    provideServerExtensionsForEdit(final Vector editTasks, final Scheduler scheduler)\n
    '''
def provideExtensionsForInstallFailure():
    '''returns None\n\n
    provideExtensionsForInstallFailure(final Vector cleanupTasks, final InstallScheduler scheduler)\n
    '''
def provideExtensionsForUninstallFailure():
    '''returns None\n\n
    provideExtensionsForUninstallFailure(final Vector cleanupTasks, final InstallScheduler scheduler)\n
    '''
def provideClientDeploymentTasksForEdit():
    '''returns None\n\n
    provideClientDeploymentTasksForEdit(final Vector taskInfo, final AppDeploymentInfo deploymentInfo, final Hashtable prefs)\n
    '''
def getAppDeploymentTaskInfoToTaskMapping():
    '''returns None\n\n
    getAppDeploymentTaskInfoToTaskMapping(final Vector tasks, final Hashtable table)\n
    '''
def providePreUpdateTasks():
    '''returns None\n\n
    providePreUpdateTasks(final Vector tasks, final UpdateScheduler sch)\n
    '''
def provideUpdateTasks():
    '''returns None\n\n
    provideUpdateTasks(final Vector tasks, final UpdateScheduler sch)\n
    '''
def isApplicationDeployable():
    '''returns None\n\n
    isApplicationDeployable(final String nodeName, final String clusterName, final String appName, final EARFile ear, final String workspaceID, final Locale locale, final List errors)\n
    '''
def validateOperation_Optional():
    '''returns None\n\n
    validateOperation_Optional(final Scheduler scheduler, final List errors)\n
    '''
def validateOperation_Required():
    '''returns None\n\n
    validateOperation_Required(final Scheduler scheduler, final List errors)\n
    '''
def provideAppDeploymentTaskListeners():
    '''returns Hashtable\n\n
    provideAppDeploymentTaskListeners(final Hashtable prefs)\n
    '''
