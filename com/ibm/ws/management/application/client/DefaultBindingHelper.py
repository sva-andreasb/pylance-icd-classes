def ():
    '''returns DefaultBindingHelper\n\n
    ()\n
    (final Hashtable tbl)\n
    '''
def createTask():
    '''returns AppDeploymentTask\n\n
    createTask(final AppDeploymentController appController)\n
    createTask(final AppDeploymentController appController, final String taskName)\n
    '''
def prepareTask():
    '''returns None\n\n
    prepareTask(final String assetId, final String workspaceId, final AppDeploymentTask t)\n
    prepareTask(final String earFile, final AppDeploymentTask t)\n
    prepareTask(final AppDeploymentInfo appInstallInfo, final AppDeploymentTask t)\n
    '''
def completeTask():
    '''returns None\n\n
    completeTask(final AppDeploymentInfo appInstallInfo, final AppDeploymentTask t)\n
    '''
