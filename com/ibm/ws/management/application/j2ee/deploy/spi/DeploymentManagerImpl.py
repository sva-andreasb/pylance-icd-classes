EAR_MODULE = "String  \"Application\""
WAR_MODULE = "String  \"WebModule\""
EJB_MODULE = "String  \"EJBModule\""
RAR_MODULE = "String  \"RARModule\""
CAR_MODULE = "String  \"CARModule\""
EAR_EXT = "String  \".ear\""
JAR_EXT = "String  \".jar\""
WAR_EXT = "String  \".war\""
RAR_EXT = "String  \".rar\""
CAR_EXT = "String  \".car\""
def ():
    '''returns DeploymentManagerImpl\n\n
    ()\n
    '''
def connect():
    '''returns None\n\n
    connect(final String host, final String port, final String connectorType, final String user, final String password)\n
    '''
def getTargets():
    '''returns Target[]\n\n
    getTargets()\n
    '''
def getRunningModules():
    '''returns TargetModuleID[]\n\n
    getRunningModules(final ModuleType moduleType, final Target[] targetList)\n
    '''
def getNonRunningModules():
    '''returns TargetModuleID[]\n\n
    getNonRunningModules(final ModuleType moduleType, final Target[] targetList)\n
    '''
def getAvailableModules():
    '''returns TargetModuleID[]\n\n
    getAvailableModules(final ModuleType moduleType, final Target[] targetList)\n
    '''
def getAvailableRarModules():
    '''returns TargetModuleID[]\n\n
    getAvailableRarModules(final Target[] targetList)\n
    '''
def createConfiguration():
    '''returns DeploymentConfiguration\n\n
    createConfiguration(final DeployableObject deployObject)\n
    '''
def distribute():
    '''returns ProgressObject\n\n
    distribute(final Target[] targetList, final File moduleArchive, final File deploymentPlan)\n
    distribute(final Target[] targetList, final ModuleType type, final InputStream moduleArchive, final InputStream deploymentPlan)\n
    distribute(final Target[] targetList, final InputStream moduleArchive, final InputStream deploymentPlan)\n
    '''
def distributeInternal():
    '''returns ProgressObject\n\n
    distributeInternal(final Target[] targetList, final File moduleArchive, final File deploymentPlan, ModuleType mt)\n
    '''
def start():
    '''returns ProgressObject\n\n
    start(TargetModuleID[] moduleIDList)\n
    '''
def stop():
    '''returns ProgressObject\n\n
    stop(TargetModuleID[] moduleIDList)\n
    '''
def stopCommand():
    '''returns None\n\n
    stopCommand(final TargetModuleID[] moduleIDList, final ProgressObject po)\n
    '''
def undeploy():
    '''returns ProgressObject\n\n
    undeploy(TargetModuleID[] moduleIDList)\n
    '''
def handleNotification():
    '''returns None\n\n
    handleNotification(final Notification notf, final Object handback)\n
    '''
def isRedeploySupported():
    '''returns boolean\n\n
    isRedeploySupported()\n
    '''
def redeploy():
    '''returns ProgressObject\n\n
    redeploy(final TargetModuleID[] moduleIDList, final File moduleArchive, final File deploymentPlan)\n
    redeploy(final TargetModuleID[] moduleIDList, final InputStream moduleArchive, final InputStream deploymentPlan)\n
    '''
def release():
    '''returns None\n\n
    release()\n
    '''
def getDefaultLocale():
    '''returns Locale\n\n
    getDefaultLocale()\n
    '''
def getCurrentLocale():
    '''returns Locale\n\n
    getCurrentLocale()\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
    '''
def getSupportedLocales():
    '''returns Locale[]\n\n
    getSupportedLocales()\n
    '''
def isLocaleSupported():
    '''returns boolean\n\n
    isLocaleSupported(final Locale locale)\n
    '''
def getDConfigBeanVersion():
    '''returns DConfigBeanVersionType\n\n
    getDConfigBeanVersion()\n
    '''
def isDConfigBeanVersionSupported():
    '''returns boolean\n\n
    isDConfigBeanVersionSupported(final DConfigBeanVersionType type)\n
    '''
def setDConfigBeanVersion():
    '''returns None\n\n
    setDConfigBeanVersion(final DConfigBeanVersionType type)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def setProfileKey():
    '''returns None\n\n
    setProfileKey(final String key)\n
    '''
