MODULE_COLUMN = "int  0"
URI_COLUMN = "int  1"
ADD_PLAN_COLUMN = "int  2"
REMOVE_PLAN_COLUMN = "int  3"
TOTAL_COLUMNS = "int  4"
def createTask():
    '''returns AppDeploymentTask\n\n
    createTask(final AppDeploymentController controller, final String taskName)\n
    '''
def prepareTask():
    '''returns None\n\n
    prepareTask(final AppDeploymentInfo info, final AppDeploymentTask task)\n
    '''
def completeTask():
    '''returns None\n\n
    completeTask(final AppDeploymentInfo info, final AppDeploymentTask t)\n
    '''
def validate():
    '''returns String[]\n\n
    validate(final AppDeploymentTask t, final AppDeploymentInfo info)\n
    '''
