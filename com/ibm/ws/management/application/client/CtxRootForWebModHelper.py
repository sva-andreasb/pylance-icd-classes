COLUMN_INDEX_WEB_MODULE = "int  0"
COLUMN_INDEX_URI = "int  1"
COLUMN_INDEX_CONTEXT_ROOT = "int  2"
DEFAULT_CONTEXT_ROOT = "String  \"/\""
def ():
    '''returns CtxRootForWebModHelper\n\n
    ()\n
    '''
def createTask():
    '''returns AppDeploymentTask\n\n
    createTask(final AppDeploymentController controller, final String taskName)\n
    '''
def prepareTask():
    '''returns None\n\n
    prepareTask(final AppDeploymentInfo installInfo, final AppDeploymentTask task)\n
    '''
def completeTask():
    '''returns None\n\n
    completeTask(final AppDeploymentInfo installInfo, final AppDeploymentTask task)\n
    '''
def taskData2DCBean():
    '''returns None\n\n
    taskData2DCBean(final AppDeploymentTask task, final DConfigBeanImpl dcBeanImpl, final String uri)\n
    '''
def dcBean2TaskData():
    '''returns None\n\n
    dcBean2TaskData(final AppDeploymentTask task, final Hashtable keys, final Hashtable props)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
