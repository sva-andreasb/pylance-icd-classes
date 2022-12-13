MSG_ERR = "int  0"
MSG_WARN = "int  1"
MSG_INFO = "int  2"
MSG_VERBOSE = "int  3"
MSG_DEBUG = "int  4"
JAVA_1_0 = "String  1.0""
JAVA_1_1 = "String  1.1""
JAVA_1_2 = "String  1.2""
JAVA_1_3 = "String  1.3""
JAVA_1_4 = "String  1.4""
TOKEN_START = "String  @""
TOKEN_END = "String  @""
def setInputHandler():
'''public void setInputHandler(final InputHandler handler)
'''
pass
def setDefaultInputStream():
'''public void setDefaultInputStream(final InputStream defaultInputStream)
'''
pass
def getDefaultInputStream():
'''public InputStream getDefaultInputStream()
'''
pass
def getInputHandler():
'''public InputHandler getInputHandler()
'''
pass
def Project():
'''public Project()
'''
pass
def createSubProject():
'''public Project createSubProject()
'''
pass
def initSubProject():
'''public void initSubProject(final Project subProject)
'''
pass
def init():
'''public void init()
'''
pass
def initProperties():
'''public void initProperties()
'''
pass
def createClassLoader():
'''public AntClassLoader createClassLoader(final Path path)
public AntClassLoader createClassLoader(final ClassLoader parent, final Path path)
'''
pass
def setCoreLoader():
'''public void setCoreLoader(final ClassLoader coreLoader)
'''
pass
def getCoreLoader():
'''public ClassLoader getCoreLoader()
'''
pass
def addBuildListener():
'''public void addBuildListener(final BuildListener listener)
'''
pass
def removeBuildListener():
'''public void removeBuildListener(final BuildListener listener)
'''
pass
def getBuildListeners():
'''public Vector getBuildListeners()
'''
pass
def log():
'''public void log(final String message)
public void log(final String message, final int msgLevel)
public void log(final String message, final Throwable throwable, final int msgLevel)
public void log(final Task task, final String message, final int msgLevel)
public void log(final Task task, final String message, final Throwable throwable, final int msgLevel)
public void log(final Target target, final String message, final int msgLevel)
public void log(final Target target, final String message, final Throwable throwable, final int msgLevel)
'''
pass
def getGlobalFilterSet():
'''public FilterSet getGlobalFilterSet()
'''
pass
def setProperty():
'''public void setProperty(final String name, final String value)
'''
pass
def setNewProperty():
'''public void setNewProperty(final String name, final String value)
'''
pass
def setUserProperty():
'''public void setUserProperty(final String name, final String value)
'''
pass
def setInheritedProperty():
'''public void setInheritedProperty(final String name, final String value)
'''
pass
def getProperty():
'''public String getProperty(final String propertyName)
'''
pass
def replaceProperties():
'''public String replaceProperties(final String value)
'''
pass
def getUserProperty():
'''public String getUserProperty(final String propertyName)
'''
pass
def getProperties():
'''public Hashtable getProperties()
'''
pass
def getUserProperties():
'''public Hashtable getUserProperties()
'''
pass
def getInheritedProperties():
'''public Hashtable getInheritedProperties()
'''
pass
def copyUserProperties():
'''public void copyUserProperties(final Project other)
'''
pass
def copyInheritedProperties():
'''public void copyInheritedProperties(final Project other)
'''
pass
def setDefaultTarget():
'''public void setDefaultTarget(final String defaultTarget)
'''
pass
def getDefaultTarget():
'''public String getDefaultTarget()
'''
pass
def setDefault():
'''public void setDefault(final String defaultTarget)
'''
pass
def setName():
'''public void setName(final String name)
'''
pass
def getName():
'''public String getName()
'''
pass
def setDescription():
'''public void setDescription(final String description)
'''
pass
def getDescription():
'''public String getDescription()
'''
pass
def addFilter():
'''public void addFilter(final String token, final String value)
'''
pass
def getFilters():
'''public Hashtable getFilters()
'''
pass
def setBasedir():
'''public void setBasedir(final String baseD)
'''
pass
def setBaseDir():
'''public void setBaseDir(File baseDir)
'''
pass
def getBaseDir():
'''public File getBaseDir()
'''
pass
def setKeepGoingMode():
'''public void setKeepGoingMode(final boolean keepGoingMode)
'''
pass
def isKeepGoingMode():
'''public boolean isKeepGoingMode()
'''
pass
def getJavaVersion():
'''public static String getJavaVersion()
'''
pass
def setJavaVersionProperty():
'''public void setJavaVersionProperty()
'''
pass
def setSystemProperties():
'''public void setSystemProperties()
'''
pass
def addTaskDefinition():
'''public void addTaskDefinition(final String taskName, final Class taskClass)
'''
pass
def checkTaskClass():
'''public void checkTaskClass(final Class taskClass)
'''
pass
def getTaskDefinitions():
'''public Hashtable getTaskDefinitions()
'''
pass
def getCopyOfTaskDefinitions():
'''public Map getCopyOfTaskDefinitions()
'''
pass
def addDataTypeDefinition():
'''public void addDataTypeDefinition(final String typeName, final Class typeClass)
'''
pass
def getDataTypeDefinitions():
'''public Hashtable getDataTypeDefinitions()
'''
pass
def getCopyOfDataTypeDefinitions():
'''public Map getCopyOfDataTypeDefinitions()
'''
pass
def addTarget():
'''public void addTarget(final Target target)
public void addTarget(final String targetName, final Target target)
'''
pass
def addOrReplaceTarget():
'''public void addOrReplaceTarget(final Target target)
public void addOrReplaceTarget(final String targetName, final Target target)
'''
pass
def getTargets():
'''public Hashtable getTargets()
'''
pass
def getCopyOfTargets():
'''public Map getCopyOfTargets()
'''
pass
def createTask():
'''public Task createTask(final String taskType)
'''
pass
def createDataType():
'''public Object createDataType(final String typeName)
'''
pass
def setExecutor():
'''public void setExecutor(final Executor e)
'''
pass
def getExecutor():
'''public Executor getExecutor()
'''
pass
def executeTargets():
'''public void executeTargets(final Vector names)
'''
pass
def demuxOutput():
'''public void demuxOutput(final String output, final boolean isWarning)
'''
pass
def defaultInput():
'''public int defaultInput(final byte[] buffer, final int offset, final int length)
'''
pass
def demuxInput():
'''public int demuxInput(final byte[] buffer, final int offset, final int length)
'''
pass
def demuxFlush():
'''public void demuxFlush(final String output, final boolean isError)
'''
pass
def executeTarget():
'''public void executeTarget(final String targetName)
'''
pass
def executeSortedTargets():
'''public void executeSortedTargets(final Vector sortedTargets)
'''
pass
def resolveFile():
'''public File resolveFile(final String fileName, final File rootDir)
public File resolveFile(final String fileName)
'''
pass
def translatePath():
'''public static String translatePath(final String toProcess)
'''
pass
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
pass
def setFileLastModified():
'''public void setFileLastModified(final File file, final long time)
'''
pass
def toBoolean():
'''public static boolean toBoolean(final String s)
'''
pass
def getProject():
'''public static Project getProject(final Object o)
'''
pass
def topoSort():
'''public final Vector topoSort(final String root, final Hashtable targetTable)
public final Vector topoSort(final String root, final Hashtable targetTable, final boolean returnAll)
public final Vector topoSort(final String[] root, final Hashtable targetTable, final boolean returnAll)
'''
pass
def inheritIDReferences():
'''public void inheritIDReferences(final Project parent)
'''
pass
def addIdReference():
'''public void addIdReference(final String id, final Object value)
'''
pass
def addReference():
'''public void addReference(final String referenceName, final Object value)
'''
pass
def getReferences():
'''public Hashtable getReferences()
'''
pass
def hasReference():
'''public boolean hasReference(final String key)
'''
pass
def getCopyOfReferences():
'''public Map getCopyOfReferences()
'''
pass
def getReference():
'''public Object getReference(final String key)
'''
pass
def getElementName():
'''public String getElementName(final Object element)
'''
pass
def fireBuildStarted():
'''public void fireBuildStarted()
'''
pass
def fireBuildFinished():
'''public void fireBuildFinished(final Throwable exception)
'''
pass
def fireSubBuildStarted():
'''public void fireSubBuildStarted()
'''
pass
def fireSubBuildFinished():
'''public void fireSubBuildFinished(final Throwable exception)
'''
pass
def registerThreadTask():
'''public void registerThreadTask(final Thread thread, final Task task)
'''
pass
def getThreadTask():
'''public Task getThreadTask(final Thread thread)
'''
pass
def setProjectReference():
'''public final void setProjectReference(final Object obj)
'''
pass
def getResource():
'''public Resource getResource(final String name)
'''
pass
def get():
'''public Object get(final Object key)
'''
pass
