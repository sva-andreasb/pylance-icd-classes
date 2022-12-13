MSG_ERR = "int  0"
MSG_WARN = "int  1"
MSG_INFO = "int  2"
MSG_VERBOSE = "int  3"
MSG_DEBUG = "int  4"
JAVA_1_0 = "String  \"1.0\""
JAVA_1_1 = "String  \"1.1\""
JAVA_1_2 = "String  \"1.2\""
JAVA_1_3 = "String  \"1.3\""
JAVA_1_4 = "String  \"1.4\""
TOKEN_START = "String  \"@\""
TOKEN_END = "String  \"@\""
def setInputHandler():
    '''public void setInputHandler(final InputHandler handler)
    '''
def setDefaultInputStream():
    '''public void setDefaultInputStream(final InputStream defaultInputStream)
    '''
def getDefaultInputStream():
    '''public InputStream getDefaultInputStream()
    '''
def getInputHandler():
    '''public InputHandler getInputHandler()
    '''
def Project():
    '''public Project()
    '''
def createSubProject():
    '''public Project createSubProject()
    '''
def initSubProject():
    '''public void initSubProject(final Project subProject)
    '''
def init():
    '''public void init()
    '''
def initProperties():
    '''public void initProperties()
    '''
def createClassLoader():
    '''public AntClassLoader createClassLoader(final Path path)
    public AntClassLoader createClassLoader(final ClassLoader parent, final Path path)
    '''
def setCoreLoader():
    '''public void setCoreLoader(final ClassLoader coreLoader)
    '''
def getCoreLoader():
    '''public ClassLoader getCoreLoader()
    '''
def addBuildListener():
    '''public void addBuildListener(final BuildListener listener)
    '''
def removeBuildListener():
    '''public void removeBuildListener(final BuildListener listener)
    '''
def getBuildListeners():
    '''public Vector getBuildListeners()
    '''
def log():
    '''public void log(final String message)
    public void log(final String message, final int msgLevel)
    public void log(final String message, final Throwable throwable, final int msgLevel)
    public void log(final Task task, final String message, final int msgLevel)
    public void log(final Task task, final String message, final Throwable throwable, final int msgLevel)
    public void log(final Target target, final String message, final int msgLevel)
    public void log(final Target target, final String message, final Throwable throwable, final int msgLevel)
    '''
def getGlobalFilterSet():
    '''public FilterSet getGlobalFilterSet()
    '''
def setProperty():
    '''public void setProperty(final String name, final String value)
    '''
def setNewProperty():
    '''public void setNewProperty(final String name, final String value)
    '''
def setUserProperty():
    '''public void setUserProperty(final String name, final String value)
    '''
def setInheritedProperty():
    '''public void setInheritedProperty(final String name, final String value)
    '''
def getProperty():
    '''public String getProperty(final String propertyName)
    '''
def replaceProperties():
    '''public String replaceProperties(final String value)
    '''
def getUserProperty():
    '''public String getUserProperty(final String propertyName)
    '''
def getProperties():
    '''public Hashtable getProperties()
    '''
def getUserProperties():
    '''public Hashtable getUserProperties()
    '''
def getInheritedProperties():
    '''public Hashtable getInheritedProperties()
    '''
def copyUserProperties():
    '''public void copyUserProperties(final Project other)
    '''
def copyInheritedProperties():
    '''public void copyInheritedProperties(final Project other)
    '''
def setDefaultTarget():
    '''public void setDefaultTarget(final String defaultTarget)
    '''
def getDefaultTarget():
    '''public String getDefaultTarget()
    '''
def setDefault():
    '''public void setDefault(final String defaultTarget)
    '''
def setName():
    '''public void setName(final String name)
    '''
def getName():
    '''public String getName()
    '''
def setDescription():
    '''public void setDescription(final String description)
    '''
def getDescription():
    '''public String getDescription()
    '''
def addFilter():
    '''public void addFilter(final String token, final String value)
    '''
def getFilters():
    '''public Hashtable getFilters()
    '''
def setBasedir():
    '''public void setBasedir(final String baseD)
    '''
def setBaseDir():
    '''public void setBaseDir(File baseDir)
    '''
def getBaseDir():
    '''public File getBaseDir()
    '''
def setKeepGoingMode():
    '''public void setKeepGoingMode(final boolean keepGoingMode)
    '''
def isKeepGoingMode():
    '''public boolean isKeepGoingMode()
    '''
def getJavaVersion():
    '''public static String getJavaVersion()
    '''
def setJavaVersionProperty():
    '''public void setJavaVersionProperty()
    '''
def setSystemProperties():
    '''public void setSystemProperties()
    '''
def addTaskDefinition():
    '''public void addTaskDefinition(final String taskName, final Class taskClass)
    '''
def checkTaskClass():
    '''public void checkTaskClass(final Class taskClass)
    '''
def getTaskDefinitions():
    '''public Hashtable getTaskDefinitions()
    '''
def getCopyOfTaskDefinitions():
    '''public Map getCopyOfTaskDefinitions()
    '''
def addDataTypeDefinition():
    '''public void addDataTypeDefinition(final String typeName, final Class typeClass)
    '''
def getDataTypeDefinitions():
    '''public Hashtable getDataTypeDefinitions()
    '''
def getCopyOfDataTypeDefinitions():
    '''public Map getCopyOfDataTypeDefinitions()
    '''
def addTarget():
    '''public void addTarget(final Target target)
    public void addTarget(final String targetName, final Target target)
    '''
def addOrReplaceTarget():
    '''public void addOrReplaceTarget(final Target target)
    public void addOrReplaceTarget(final String targetName, final Target target)
    '''
def getTargets():
    '''public Hashtable getTargets()
    '''
def getCopyOfTargets():
    '''public Map getCopyOfTargets()
    '''
def createTask():
    '''public Task createTask(final String taskType)
    '''
def createDataType():
    '''public Object createDataType(final String typeName)
    '''
def setExecutor():
    '''public void setExecutor(final Executor e)
    '''
def getExecutor():
    '''public Executor getExecutor()
    '''
def executeTargets():
    '''public void executeTargets(final Vector names)
    '''
def demuxOutput():
    '''public void demuxOutput(final String output, final boolean isWarning)
    '''
def defaultInput():
    '''public int defaultInput(final byte[] buffer, final int offset, final int length)
    '''
def demuxInput():
    '''public int demuxInput(final byte[] buffer, final int offset, final int length)
    '''
def demuxFlush():
    '''public void demuxFlush(final String output, final boolean isError)
    '''
def executeTarget():
    '''public void executeTarget(final String targetName)
    '''
def executeSortedTargets():
    '''public void executeSortedTargets(final Vector sortedTargets)
    '''
def resolveFile():
    '''public File resolveFile(final String fileName, final File rootDir)
    public File resolveFile(final String fileName)
    '''
def translatePath():
    '''public static String translatePath(final String toProcess)
    '''
def copyFile():
    '''public void copyFile(final String sourceFile, final String destFile)
    public void copyFile(final String sourceFile, final String destFile, final boolean filtering)
    public void copyFile(final String sourceFile, final String destFile, final boolean filtering, final boolean overwrite)
    public void copyFile(final String sourceFile, final String destFile, final boolean filtering, final boolean overwrite, final boolean preserveLastModified)
    public void copyFile(final File sourceFile, final File destFile)
    public void copyFile(final File sourceFile, final File destFile, final boolean filtering)
    public void copyFile(final File sourceFile, final File destFile, final boolean filtering, final boolean overwrite)
    public void copyFile(final File sourceFile, final File destFile, final boolean filtering, final boolean overwrite, final boolean preserveLastModified)
    '''
def setFileLastModified():
    '''public void setFileLastModified(final File file, final long time)
    '''
def toBoolean():
    '''public static boolean toBoolean(final String s)
    '''
def getProject():
    '''public static Project getProject(final Object o)
    '''
def topoSort():
    '''public final Vector topoSort(final String root, final Hashtable targetTable)
    public final Vector topoSort(final String root, final Hashtable targetTable, final boolean returnAll)
    public final Vector topoSort(final String[] root, final Hashtable targetTable, final boolean returnAll)
    '''
def inheritIDReferences():
    '''public void inheritIDReferences(final Project parent)
    '''
def addIdReference():
    '''public void addIdReference(final String id, final Object value)
    '''
def addReference():
    '''public void addReference(final String referenceName, final Object value)
    '''
def getReferences():
    '''public Hashtable getReferences()
    '''
def hasReference():
    '''public boolean hasReference(final String key)
    '''
def getCopyOfReferences():
    '''public Map getCopyOfReferences()
    '''
def getReference():
    '''public Object getReference(final String key)
    '''
def getElementName():
    '''public String getElementName(final Object element)
    '''
def fireBuildStarted():
    '''public void fireBuildStarted()
    '''
def fireBuildFinished():
    '''public void fireBuildFinished(final Throwable exception)
    '''
def fireSubBuildStarted():
    '''public void fireSubBuildStarted()
    '''
def fireSubBuildFinished():
    '''public void fireSubBuildFinished(final Throwable exception)
    '''
def registerThreadTask():
    '''public void registerThreadTask(final Thread thread, final Task task)
    '''
def getThreadTask():
    '''public Task getThreadTask(final Thread thread)
    '''
def setProjectReference():
    '''public final void setProjectReference(final Object obj)
    '''
def getResource():
    '''public Resource getResource(final String name)
    '''
def get():
    '''public Object get(final Object key)
    '''
