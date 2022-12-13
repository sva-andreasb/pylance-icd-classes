COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
ECLIPSE_PROJECT = "String  \".project\""
ECLIPSE_OPL_PROJECT = "String  \".oplproject\""
ECLIPSE_ODME_PROJECT = "String  \".odmeproject\""
ODMDS_EXTENSION = "String  \".odmds\""
def IloODMSIDEAppDeployer():
    '''    public IloODMSIDEAppDeployer(final IloODMSIDEProject project, final File deployedConfiguration)
    '''
def setCredential():
    '''    public void setCredential(final IloCredential creds)
    '''
def setDeployTemporary():
    '''    public void setDeployTemporary(final boolean deployTemporary)
    '''
def cleanTemporary():
    '''    public boolean cleanTemporary()
    '''
def accept():
    '''    public boolean accept(final File dir, final String name)
    public boolean accept(final File dir, final String name)
    '''
def setDeployLocally():
    '''    public void setDeployLocally(final boolean deployLocally)
    '''
def setDeployOnServer():
    '''    public void setDeployOnServer(final boolean deployOnServer)
    '''
def setDefaultDeployer():
    '''    public void setDefaultDeployer(final IloDeploymentManager default_deployer)
    '''
def setStartedFromCommandLine():
    '''    public void setStartedFromCommandLine(final boolean startedFromCommandLine)
    '''
def run():
    '''    public void run(ProgressMonitor monitor)
    '''
def call():
    '''    public Void call()
    '''
def isAborted():
    '''    public boolean isAborted()
    '''
def wasDeployedOnServer():
    '''    public boolean wasDeployedOnServer()
    '''
def needToDeployOnServer():
    '''    public boolean needToDeployOnServer()
    '''
def getOdmAppLocation():
    '''    public File getOdmAppLocation()
    '''
def getComputedCheckSum():
    '''    public String getComputedCheckSum()
    '''
def setOdmAppLocation():
    '''    public void setOdmAppLocation(final File odmAppLocation)
    '''
def main():
    '''    public static void main(final String[] args)
    '''
def execute():
    '''    public static int execute(final String... args)
    '''
def guessOplProjectDirectory():
    '''    public static File guessOplProjectDirectory(final File odmeProjectFile)
    '''
def makeDeployableProject():
    '''    public static IloODMSIDEProject makeDeployableProject(final File firstFileOrDirectory)
    public static IloODMSIDEProject makeDeployableProject(final File firstFileOrDirectory, final File secondFileOrDirectory)
    '''
def deploy():
    '''    public static IloODMSIDEAppDeployer deploy(final IloODMSIDEProject projectToDeploy, final File settingsFile, final boolean deployDefaultSettings, final boolean deployLocally, final boolean deployOnServer, final boolean deployTemporary, final boolean startedFromCommandLine, final boolean verbose)
    '''
def done():
    '''    public void done()
    public void done()
    '''
def worked():
    '''    public void worked(final int work)
    public void worked(final int work)
    '''
def beginTask():
    '''    public void beginTask(final String name, final int totalWork)
    public void beginTask(final String name, final int totalWork)
    '''
def worked_():
    '''    public void worked_(final int work)
    '''
def subTask():
    '''    public void subTask(final String name)
    public void subTask(final String name)
    '''
