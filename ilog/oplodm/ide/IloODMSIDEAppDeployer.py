COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
ECLIPSE_PROJECT = "String  \".project\""
ECLIPSE_OPL_PROJECT = "String  \".oplproject\""
ECLIPSE_ODME_PROJECT = "String  \".odmeproject\""
ODMDS_EXTENSION = "String  \".odmds\""
def ():
    '''returns IloODMSIDEAppDeployer\n\n
    (final IloODMSIDEProject project, final File deployedConfiguration)\n
    '''
def setCredential():
    '''returns None\n\n
    setCredential(final IloCredential creds)\n
    '''
def setDeployTemporary():
    '''returns None\n\n
    setDeployTemporary(final boolean deployTemporary)\n
    '''
def cleanTemporary():
    '''returns boolean\n\n
    cleanTemporary()\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final File dir, final String name)\n
    accept(final File dir, final String name)\n
    '''
def setDeployLocally():
    '''returns None\n\n
    setDeployLocally(final boolean deployLocally)\n
    '''
def setDeployOnServer():
    '''returns None\n\n
    setDeployOnServer(final boolean deployOnServer)\n
    '''
def setDefaultDeployer():
    '''returns None\n\n
    setDefaultDeployer(final IloDeploymentManager default_deployer)\n
    '''
def setStartedFromCommandLine():
    '''returns None\n\n
    setStartedFromCommandLine(final boolean startedFromCommandLine)\n
    '''
def run():
    '''returns None\n\n
    run(ProgressMonitor monitor)\n
    '''
def call():
    '''returns Void\n\n
    call()\n
    '''
def isAborted():
    '''returns boolean\n\n
    isAborted()\n
    '''
def wasDeployedOnServer():
    '''returns boolean\n\n
    wasDeployedOnServer()\n
    '''
def needToDeployOnServer():
    '''returns boolean\n\n
    needToDeployOnServer()\n
    '''
def getOdmAppLocation():
    '''returns File\n\n
    getOdmAppLocation()\n
    '''
def getComputedCheckSum():
    '''returns String\n\n
    getComputedCheckSum()\n
    '''
def setOdmAppLocation():
    '''returns None\n\n
    setOdmAppLocation(final File odmAppLocation)\n
    '''
def done():
    '''returns None\n\n
    done()\n
    done()\n
    '''
def worked():
    '''returns None\n\n
    worked(final int work)\n
    worked(final int work)\n
    '''
def beginTask():
    '''returns None\n\n
    beginTask(final String name, final int totalWork)\n
    beginTask(final String name, final int totalWork)\n
    '''
def worked_():
    '''returns None\n\n
    worked_(final int work)\n
    '''
def subTask():
    '''returns None\n\n
    subTask(final String name)\n
    subTask(final String name)\n
    '''
