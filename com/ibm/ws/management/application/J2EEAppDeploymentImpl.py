TEMP_EXTRACT_DIR = "String  \"Temp extraction dir for multiserver\""
CONFIG_ROOT = "String  \"Config Root for variable map\""
def ():
    '''returns J2EEAppDeploymentImpl\n\n
    (final Hashtable tbl)\n
    '''
def getGlobalSettings():
    '''returns Hashtable\n\n
    getGlobalSettings()\n
    '''
def getTargets():
    '''returns Target[]\n\n
    getTargets(final Hashtable prefs, final String wID)\n
    '''
def getRunningModules():
    '''returns TargetModuleID[]\n\n
    getRunningModules(final String type, final Target[] targetList, final Hashtable prefs, final String wsId)\n
    '''
def getNonRunningModules():
    '''returns TargetModuleID[]\n\n
    getNonRunningModules(final String type, final Target[] targetList, final Hashtable prefs, final String wsId)\n
    '''
def getAvailableModules():
    '''returns TargetModuleID[]\n\n
    getAvailableModules(final String type, final Target[] targetList, final Hashtable prefs, final String wsId)\n
    '''
def getAvailableChildren():
    '''returns TargetModuleID[]\n\n
    getAvailableChildren(final String appName, final TargetModuleID parent, final Hashtable prefs, final String wsID)\n
    getAvailableChildren(final AppManagement appM, final String appName, final TargetModuleID parent, final Hashtable prefs, final String wsID)\n
    '''
