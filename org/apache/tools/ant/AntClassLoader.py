def AntClassLoader():
'''public AntClassLoader(final ClassLoader parent, final Project project, final Path classpath)
public AntClassLoader()
public AntClassLoader(final Project project, final Path classpath)
public AntClassLoader(final ClassLoader parent, final Project project, final Path classpath, final boolean parentFirst)
public AntClassLoader(final Project project, final Path classpath, final boolean parentFirst)
public AntClassLoader(final ClassLoader parent, final boolean parentFirst)
'''
pass
def setProject():
'''public void setProject(final Project project)
'''
pass
def setClassPath():
'''public void setClassPath(final Path classpath)
'''
pass
def setParent():
'''public void setParent(final ClassLoader parent)
'''
pass
def setParentFirst():
'''public void setParentFirst(final boolean parentFirst)
'''
pass
def setThreadContextLoader():
'''public void setThreadContextLoader()
'''
pass
def resetThreadContextLoader():
'''public void resetThreadContextLoader()
'''
pass
def addPathElement():
'''public void addPathElement(final String pathElement)
'''
pass
def addPathComponent():
'''public void addPathComponent(final File file)
'''
pass
def getClasspath():
'''public String getClasspath()
'''
pass
def setIsolated():
'''public synchronized void setIsolated(final boolean isolated)
'''
pass
def initializeClass():
'''public static void initializeClass(final Class theClass)
'''
pass
def addSystemPackageRoot():
'''public void addSystemPackageRoot(final String packageRoot)
'''
pass
def addLoaderPackageRoot():
'''public void addLoaderPackageRoot(final String packageRoot)
'''
pass
def forceLoadClass():
'''public Class forceLoadClass(final String classname)
'''
pass
def forceLoadSystemClass():
'''public Class forceLoadSystemClass(final String classname)
'''
pass
def getResourceAsStream():
'''public InputStream getResourceAsStream(final String name)
'''
pass
def getResource():
'''public URL getResource(final String name)
'''
pass
def getNamedResources():
'''public Enumeration getNamedResources(final String name)
'''
pass
def findClass():
'''public Class findClass(final String name)
'''
pass
def cleanup():
'''public synchronized void cleanup()
'''
pass
def getConfiguredParent():
'''public ClassLoader getConfiguredParent()
'''
pass
def buildStarted():
'''public void buildStarted(final BuildEvent event)
'''
pass
def buildFinished():
'''public void buildFinished(final BuildEvent event)
'''
pass
def subBuildFinished():
'''public void subBuildFinished(final BuildEvent event)
'''
pass
def subBuildStarted():
'''public void subBuildStarted(final BuildEvent event)
'''
pass
def targetStarted():
'''public void targetStarted(final BuildEvent event)
'''
pass
def targetFinished():
'''public void targetFinished(final BuildEvent event)
'''
pass
def taskStarted():
'''public void taskStarted(final BuildEvent event)
'''
pass
def taskFinished():
'''public void taskFinished(final BuildEvent event)
'''
pass
def messageLogged():
'''public void messageLogged(final BuildEvent event)
'''
pass
def addJavaLibraries():
'''public void addJavaLibraries()
'''
pass
def toString():
'''public String toString()
'''
pass
def newAntClassLoader():
'''public static AntClassLoader newAntClassLoader(final ClassLoader parent, final Project project, final Path path, final boolean parentFirst)
'''
pass
def hasMoreElements():
'''public boolean hasMoreElements()
'''
pass
def nextElement():
'''public Object nextElement()
'''
pass
