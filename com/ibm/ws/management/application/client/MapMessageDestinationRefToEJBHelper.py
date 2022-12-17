AppVersionColumn = "int  0"
ModuleVersionColumn = "int  1"
moduleColumn = "int  2"
ejbColumn = "int  3"
uriColumn = "int  4"
messageDestinationObjectColumn = "int  5"
isMD = "int  6"
messageDestinationRefNameColumn = "int  7"
jndiColumn = "int  8"
destJndiColumn = "int  9"
def createTask():
    '''returns AppDeploymentTask\n\n
    createTask(final AppDeploymentController appController, final String taskName)\n
    '''
def prepareTask():
    '''returns None\n\n
    prepareTask(final AppDeploymentInfo appInstallInfo, final AppDeploymentTask t)\n
    '''
def completeTask():
    '''returns None\n\n
    completeTask(final AppDeploymentInfo appInstallInfo, final AppDeploymentTask t)\n
    '''
def getXPathInfo():
    '''returns Hashtable\n\n
    getXPathInfo(final Vector allTypes)\n
    '''
def taskData2DCBean():
    '''returns None\n\n
    taskData2DCBean(final AppDeploymentTask task, final DConfigBeanImpl dcImpl, final String uri)\n
    '''
def dcBean2TaskData():
    '''returns None\n\n
    dcBean2TaskData(final AppDeploymentTask task, final Hashtable keys, final Hashtable props)\n
    '''
def validate():
    '''returns String[]\n\n
    validate(final AppDeploymentTask task, final AppDeploymentInfo taskInfo)\n
    '''
