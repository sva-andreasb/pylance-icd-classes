def ():
    '''returns AntClassLoader\n\n
    (final ClassLoader parent, final Project project, final Path classpath)\n
    ()\n
    (final Project project, final Path classpath)\n
    (final ClassLoader parent, final Project project, final Path classpath, final boolean parentFirst)\n
    (final Project project, final Path classpath, final boolean parentFirst)\n
    (final ClassLoader parent, final boolean parentFirst)\n
    '''
def setProject():
    '''returns None\n\n
    setProject(final Project project)\n
    '''
def setClassPath():
    '''returns None\n\n
    setClassPath(final Path classpath)\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final ClassLoader parent)\n
    '''
def setParentFirst():
    '''returns None\n\n
    setParentFirst(final boolean parentFirst)\n
    '''
def setThreadContextLoader():
    '''returns None\n\n
    setThreadContextLoader()\n
    '''
def resetThreadContextLoader():
    '''returns None\n\n
    resetThreadContextLoader()\n
    '''
def addPathElement():
    '''returns None\n\n
    addPathElement(final String pathElement)\n
    '''
def addPathComponent():
    '''returns None\n\n
    addPathComponent(final File file)\n
    '''
def getClasspath():
    '''returns String\n\n
    getClasspath()\n
    '''
def addSystemPackageRoot():
    '''returns None\n\n
    addSystemPackageRoot(final String packageRoot)\n
    '''
def addLoaderPackageRoot():
    '''returns None\n\n
    addLoaderPackageRoot(final String packageRoot)\n
    '''
def forceLoadClass():
    '''returns Class\n\n
    forceLoadClass(final String classname)\n
    '''
def forceLoadSystemClass():
    '''returns Class\n\n
    forceLoadSystemClass(final String classname)\n
    '''
def getResourceAsStream():
    '''returns InputStream\n\n
    getResourceAsStream(final String name)\n
    '''
def getResource():
    '''returns URL\n\n
    getResource(final String name)\n
    '''
def getNamedResources():
    '''returns Enumeration\n\n
    getNamedResources(final String name)\n
    '''
def findClass():
    '''returns Class\n\n
    findClass(final String name)\n
    '''
def getConfiguredParent():
    '''returns ClassLoader\n\n
    getConfiguredParent()\n
    '''
def buildStarted():
    '''returns None\n\n
    buildStarted(final BuildEvent event)\n
    '''
def buildFinished():
    '''returns None\n\n
    buildFinished(final BuildEvent event)\n
    '''
def subBuildFinished():
    '''returns None\n\n
    subBuildFinished(final BuildEvent event)\n
    '''
def subBuildStarted():
    '''returns None\n\n
    subBuildStarted(final BuildEvent event)\n
    '''
def targetStarted():
    '''returns None\n\n
    targetStarted(final BuildEvent event)\n
    '''
def targetFinished():
    '''returns None\n\n
    targetFinished(final BuildEvent event)\n
    '''
def taskStarted():
    '''returns None\n\n
    taskStarted(final BuildEvent event)\n
    '''
def taskFinished():
    '''returns None\n\n
    taskFinished(final BuildEvent event)\n
    '''
def messageLogged():
    '''returns None\n\n
    messageLogged(final BuildEvent event)\n
    '''
def addJavaLibraries():
    '''returns None\n\n
    addJavaLibraries()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def hasMoreElements():
    '''returns boolean\n\n
    hasMoreElements()\n
    '''
def nextElement():
    '''returns Object\n\n
    nextElement()\n
    '''
