COPYRIGHT_NOTICE = "String  Copyright IBM Corporation 2005,2012""
ECLIPSE_PROJECT = "String  .project""
ECLIPSE_OPL_PROJECT = "String  .oplproject""
ECLIPSE_ODME_PROJECT = "String  .odmeproject""
ODMDS_EXTENSION = "String  .odmds""
def IloODMSIDEAppDeployer():
'''public IloODMSIDEAppDeployer(final IloODMSIDEProject project, final File deployedConfiguration)
'''
pass
def setCredential():
'''public void setCredential(final IloCredential creds)
'''
pass
def setDeployTemporary():
'''public void setDeployTemporary(final boolean deployTemporary)
'''
pass
def cleanTemporary():
'''public boolean cleanTemporary()
'''
pass
def accept():
'''public boolean accept(final File dir, final String name)
public boolean accept(final File dir, final String name)
'''
pass
def setDeployLocally():
'''public void setDeployLocally(final boolean deployLocally)
'''
pass
def setDeployOnServer():
'''public void setDeployOnServer(final boolean deployOnServer)
'''
pass
def setDefaultDeployer():
'''public void setDefaultDeployer(final IloDeploymentManager default_deployer)
'''
pass
def setStartedFromCommandLine():
'''public void setStartedFromCommandLine(final boolean startedFromCommandLine)
'''
pass
def run():
'''public void run(ProgressMonitor monitor)
'''
pass
def call():
'''public Void call()
'''
pass
def isAborted():
'''public boolean isAborted()
'''
pass
def wasDeployedOnServer():
'''public boolean wasDeployedOnServer()
'''
pass
def needToDeployOnServer():
'''public boolean needToDeployOnServer()
'''
pass
def getOdmAppLocation():
'''public File getOdmAppLocation()
'''
pass
def getComputedCheckSum():
'''public String getComputedCheckSum()
'''
pass
def setOdmAppLocation():
'''public void setOdmAppLocation(final File odmAppLocation)
'''
pass
def main():
'''public static void main(final String[] args)
'''
pass
def execute():
'''public static int execute(final String... args)
'''
pass
def guessOplProjectDirectory():
'''public static File guessOplProjectDirectory(final File odmeProjectFile)
'''
pass
def makeDeployableProject():
'''public static IloODMSIDEProject makeDeployableProject(final File firstFileOrDirectory)
public static IloODMSIDEProject makeDeployableProject(final File firstFileOrDirectory, final File secondFileOrDirectory)
'''
pass
def deploy():
'''public static IloODMSIDEAppDeployer deploy(final IloODMSIDEProject projectToDeploy, final File settingsFile, final boolean deployDefaultSettings, final boolean deployLocally, final boolean deployOnServer, final boolean deployTemporary, final boolean startedFromCommandLine, final boolean verbose)
'''
pass
def done():
'''public void done()
public void done()
'''
pass
def worked():
'''public void worked(final int work)
public void worked(final int work)
'''
pass
def beginTask():
'''public void beginTask(final String name, final int totalWork)
public void beginTask(final String name, final int totalWork)
'''
pass
def worked_():
'''public void worked_(final int work)
'''
pass
def subTask():
'''public void subTask(final String name)
public void subTask(final String name)
'''
pass