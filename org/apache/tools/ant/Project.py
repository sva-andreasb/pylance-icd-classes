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
    '''returns None\n\n
    setInputHandler(final InputHandler handler)\n
    '''
def setDefaultInputStream():
    '''returns None\n\n
    setDefaultInputStream(final InputStream defaultInputStream)\n
    '''
def getDefaultInputStream():
    '''returns InputStream\n\n
    getDefaultInputStream()\n
    '''
def getInputHandler():
    '''returns InputHandler\n\n
    getInputHandler()\n
    '''
def ():
    '''returns Project\n\n
    ()\n
    '''
def createSubProject():
    '''returns Project\n\n
    createSubProject()\n
    '''
def initSubProject():
    '''returns None\n\n
    initSubProject(final Project subProject)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def initProperties():
    '''returns None\n\n
    initProperties()\n
    '''
def createClassLoader():
    '''returns AntClassLoader\n\n
    createClassLoader(final Path path)\n
    createClassLoader(final ClassLoader parent, final Path path)\n
    '''
def setCoreLoader():
    '''returns None\n\n
    setCoreLoader(final ClassLoader coreLoader)\n
    '''
def getCoreLoader():
    '''returns ClassLoader\n\n
    getCoreLoader()\n
    '''
def addBuildListener():
    '''returns None\n\n
    addBuildListener(final BuildListener listener)\n
    '''
def removeBuildListener():
    '''returns None\n\n
    removeBuildListener(final BuildListener listener)\n
    '''
def getBuildListeners():
    '''returns Vector\n\n
    getBuildListeners()\n
    '''
def log():
    '''returns None\n\n
    log(final String message)\n
    log(final String message, final int msgLevel)\n
    log(final String message, final Throwable throwable, final int msgLevel)\n
    log(final Task task, final String message, final int msgLevel)\n
    log(final Task task, final String message, final Throwable throwable, final int msgLevel)\n
    log(final Target target, final String message, final int msgLevel)\n
    log(final Target target, final String message, final Throwable throwable, final int msgLevel)\n
    '''
def getGlobalFilterSet():
    '''returns FilterSet\n\n
    getGlobalFilterSet()\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String name, final String value)\n
    '''
def setNewProperty():
    '''returns None\n\n
    setNewProperty(final String name, final String value)\n
    '''
def setUserProperty():
    '''returns None\n\n
    setUserProperty(final String name, final String value)\n
    '''
def setInheritedProperty():
    '''returns None\n\n
    setInheritedProperty(final String name, final String value)\n
    '''
def getProperty():
    '''returns String\n\n
    getProperty(final String propertyName)\n
    '''
def replaceProperties():
    '''returns String\n\n
    replaceProperties(final String value)\n
    '''
def getUserProperty():
    '''returns String\n\n
    getUserProperty(final String propertyName)\n
    '''
def getProperties():
    '''returns Hashtable\n\n
    getProperties()\n
    '''
def getUserProperties():
    '''returns Hashtable\n\n
    getUserProperties()\n
    '''
def getInheritedProperties():
    '''returns Hashtable\n\n
    getInheritedProperties()\n
    '''
def copyUserProperties():
    '''returns None\n\n
    copyUserProperties(final Project other)\n
    '''
def copyInheritedProperties():
    '''returns None\n\n
    copyInheritedProperties(final Project other)\n
    '''
def setDefaultTarget():
    '''returns None\n\n
    setDefaultTarget(final String defaultTarget)\n
    '''
def getDefaultTarget():
    '''returns String\n\n
    getDefaultTarget()\n
    '''
def setDefault():
    '''returns None\n\n
    setDefault(final String defaultTarget)\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setDescription():
    '''returns None\n\n
    setDescription(final String description)\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription()\n
    '''
def addFilter():
    '''returns None\n\n
    addFilter(final String token, final String value)\n
    '''
def getFilters():
    '''returns Hashtable\n\n
    getFilters()\n
    '''
def setBasedir():
    '''returns None\n\n
    setBasedir(final String baseD)\n
    '''
def setBaseDir():
    '''returns None\n\n
    setBaseDir(File baseDir)\n
    '''
def getBaseDir():
    '''returns File\n\n
    getBaseDir()\n
    '''
def setKeepGoingMode():
    '''returns None\n\n
    setKeepGoingMode(final boolean keepGoingMode)\n
    '''
def isKeepGoingMode():
    '''returns boolean\n\n
    isKeepGoingMode()\n
    '''
def setJavaVersionProperty():
    '''returns None\n\n
    setJavaVersionProperty()\n
    '''
def setSystemProperties():
    '''returns None\n\n
    setSystemProperties()\n
    '''
def addTaskDefinition():
    '''returns None\n\n
    addTaskDefinition(final String taskName, final Class taskClass)\n
    '''
def checkTaskClass():
    '''returns None\n\n
    checkTaskClass(final Class taskClass)\n
    '''
def getTaskDefinitions():
    '''returns Hashtable\n\n
    getTaskDefinitions()\n
    '''
def getCopyOfTaskDefinitions():
    '''returns Map\n\n
    getCopyOfTaskDefinitions()\n
    '''
def addDataTypeDefinition():
    '''returns None\n\n
    addDataTypeDefinition(final String typeName, final Class typeClass)\n
    '''
def getDataTypeDefinitions():
    '''returns Hashtable\n\n
    getDataTypeDefinitions()\n
    '''
def getCopyOfDataTypeDefinitions():
    '''returns Map\n\n
    getCopyOfDataTypeDefinitions()\n
    '''
def addTarget():
    '''returns None\n\n
    addTarget(final Target target)\n
    addTarget(final String targetName, final Target target)\n
    '''
def addOrReplaceTarget():
    '''returns None\n\n
    addOrReplaceTarget(final Target target)\n
    addOrReplaceTarget(final String targetName, final Target target)\n
    '''
def getTargets():
    '''returns Hashtable\n\n
    getTargets()\n
    '''
def getCopyOfTargets():
    '''returns Map\n\n
    getCopyOfTargets()\n
    '''
def createTask():
    '''returns Task\n\n
    createTask(final String taskType)\n
    '''
def createDataType():
    '''returns Object\n\n
    createDataType(final String typeName)\n
    '''
def setExecutor():
    '''returns None\n\n
    setExecutor(final Executor e)\n
    '''
def getExecutor():
    '''returns Executor\n\n
    getExecutor()\n
    '''
def executeTargets():
    '''returns None\n\n
    executeTargets(final Vector names)\n
    '''
def demuxOutput():
    '''returns None\n\n
    demuxOutput(final String output, final boolean isWarning)\n
    '''
def defaultInput():
    '''returns int\n\n
    defaultInput(final byte[] buffer, final int offset, final int length)\n
    '''
def demuxInput():
    '''returns int\n\n
    demuxInput(final byte[] buffer, final int offset, final int length)\n
    '''
def demuxFlush():
    '''returns None\n\n
    demuxFlush(final String output, final boolean isError)\n
    '''
def executeTarget():
    '''returns None\n\n
    executeTarget(final String targetName)\n
    '''
def executeSortedTargets():
    '''returns None\n\n
    executeSortedTargets(final Vector sortedTargets)\n
    '''
def resolveFile():
    '''returns File\n\n
    resolveFile(final String fileName, final File rootDir)\n
    resolveFile(final String fileName)\n
    '''
def copyFile():
    '''returns None\n\n
    copyFile(final String sourceFile, final String destFile)\n
    copyFile(final String sourceFile, final String destFile, final boolean filtering)\n
    copyFile(final String sourceFile, final String destFile, final boolean filtering, final boolean overwrite)\n
    copyFile(final String sourceFile, final String destFile, final boolean filtering, final boolean overwrite, final boolean preserveLastModified)\n
    copyFile(final File sourceFile, final File destFile)\n
    copyFile(final File sourceFile, final File destFile, final boolean filtering)\n
    copyFile(final File sourceFile, final File destFile, final boolean filtering, final boolean overwrite)\n
    copyFile(final File sourceFile, final File destFile, final boolean filtering, final boolean overwrite, final boolean preserveLastModified)\n
    '''
def setFileLastModified():
    '''returns None\n\n
    setFileLastModified(final File file, final long time)\n
    '''
def inheritIDReferences():
    '''returns None\n\n
    inheritIDReferences(final Project parent)\n
    '''
def addIdReference():
    '''returns None\n\n
    addIdReference(final String id, final Object value)\n
    '''
def addReference():
    '''returns None\n\n
    addReference(final String referenceName, final Object value)\n
    '''
def getReferences():
    '''returns Hashtable\n\n
    getReferences()\n
    '''
def hasReference():
    '''returns boolean\n\n
    hasReference(final String key)\n
    '''
def getCopyOfReferences():
    '''returns Map\n\n
    getCopyOfReferences()\n
    '''
def getReference():
    '''returns Object\n\n
    getReference(final String key)\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName(final Object element)\n
    '''
def fireBuildStarted():
    '''returns None\n\n
    fireBuildStarted()\n
    '''
def fireBuildFinished():
    '''returns None\n\n
    fireBuildFinished(final Throwable exception)\n
    '''
def fireSubBuildStarted():
    '''returns None\n\n
    fireSubBuildStarted()\n
    '''
def fireSubBuildFinished():
    '''returns None\n\n
    fireSubBuildFinished(final Throwable exception)\n
    '''
def registerThreadTask():
    '''returns None\n\n
    registerThreadTask(final Thread thread, final Task task)\n
    '''
def getThreadTask():
    '''returns Task\n\n
    getThreadTask(final Thread thread)\n
    '''
def getResource():
    '''returns Resource\n\n
    getResource(final String name)\n
    '''
def get():
    '''returns Object\n\n
    get(final Object key)\n
    '''
