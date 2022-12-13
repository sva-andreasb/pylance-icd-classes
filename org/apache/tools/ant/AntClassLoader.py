def AntClassLoader():
    '''public AntClassLoader(final ClassLoader parent, final Project project, final Path classpath)
    public AntClassLoader()
    public AntClassLoader(final Project project, final Path classpath)
    public AntClassLoader(final ClassLoader parent, final Project project, final Path classpath, final boolean parentFirst)
    public AntClassLoader(final Project project, final Path classpath, final boolean parentFirst)
    public AntClassLoader(final ClassLoader parent, final boolean parentFirst)
    '''
def setProject():
    '''public void setProject(final Project project)
    '''
def setClassPath():
    '''public void setClassPath(final Path classpath)
    '''
def setParent():
    '''public void setParent(final ClassLoader parent)
    '''
def setParentFirst():
    '''public void setParentFirst(final boolean parentFirst)
    '''
def setThreadContextLoader():
    '''public void setThreadContextLoader()
    '''
def resetThreadContextLoader():
    '''public void resetThreadContextLoader()
    '''
def addPathElement():
    '''public void addPathElement(final String pathElement)
    '''
def addPathComponent():
    '''public void addPathComponent(final File file)
    '''
def getClasspath():
    '''public String getClasspath()
    '''
def setIsolated():
    '''public synchronized void setIsolated(final boolean isolated)
    '''
def initializeClass():
    '''public static void initializeClass(final Class theClass)
    '''
def addSystemPackageRoot():
    '''public void addSystemPackageRoot(final String packageRoot)
    '''
def addLoaderPackageRoot():
    '''public void addLoaderPackageRoot(final String packageRoot)
    '''
def forceLoadClass():
    '''public Class forceLoadClass(final String classname)
    '''
def forceLoadSystemClass():
    '''public Class forceLoadSystemClass(final String classname)
    '''
def getResourceAsStream():
    '''public InputStream getResourceAsStream(final String name)
    '''
def getResource():
    '''public URL getResource(final String name)
    '''
def getNamedResources():
    '''public Enumeration getNamedResources(final String name)
    '''
def findClass():
    '''public Class findClass(final String name)
    '''
def cleanup():
    '''public synchronized void cleanup()
    '''
def getConfiguredParent():
    '''public ClassLoader getConfiguredParent()
    '''
def buildStarted():
    '''public void buildStarted(final BuildEvent event)
    '''
def buildFinished():
    '''public void buildFinished(final BuildEvent event)
    '''
def subBuildFinished():
    '''public void subBuildFinished(final BuildEvent event)
    '''
def subBuildStarted():
    '''public void subBuildStarted(final BuildEvent event)
    '''
def targetStarted():
    '''public void targetStarted(final BuildEvent event)
    '''
def targetFinished():
    '''public void targetFinished(final BuildEvent event)
    '''
def taskStarted():
    '''public void taskStarted(final BuildEvent event)
    '''
def taskFinished():
    '''public void taskFinished(final BuildEvent event)
    '''
def messageLogged():
    '''public void messageLogged(final BuildEvent event)
    '''
def addJavaLibraries():
    '''public void addJavaLibraries()
    '''
def toString():
    '''public String toString()
    '''
def newAntClassLoader():
    '''public static AntClassLoader newAntClassLoader(final ClassLoader parent, final Project project, final Path path, final boolean parentFirst)
    '''
def hasMoreElements():
    '''public boolean hasMoreElements()
    '''
def nextElement():
    '''public Object nextElement()
    '''
