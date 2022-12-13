COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def guessOplProjectDirectory():
    '''    public static File guessOplProjectDirectory(final File odmeProjectFile)
    '''
def makeDeployableProject():
    '''    public static IloODMSIDEProject makeDeployableProject(final File firstFileOrDirectory)
    public static IloODMSIDEProject makeDeployableProject(final File firstFileOrDirectory, final File secondFileOrDirectory)
    '''
def createOdmConfig():
    '''    public static IloOdmConfigSetBean createOdmConfig(final IloODMSIDEProject project, final File deployedConfiguration, final boolean relativeUrls)
    '''
def findNLSSettingsFiles():
    '''    public static List<URL> findNLSSettingsFiles(List<URL> urlList, final IloODMSIDEProject project, String baseRelPath, String extension)
    '''
def readOdmAppDeployment():
    '''    public static Element readOdmAppDeployment(final File odmdsFile)
    '''
def getDeploymentConfig():
    '''    public static IloDeploymentProfileImpl getDeploymentConfig(final Element odmAppDeployment)
    '''
def getDeploymentClasspathEntries():
    '''    public static String[] getDeploymentClasspathEntries(final Element odmAppDeployment)
    '''
def getDeploymentRepositoryProfile():
    '''    public static IloRepositoryAccessProfileImpl getDeploymentRepositoryProfile(final Element odmAppDeployment)
    '''
