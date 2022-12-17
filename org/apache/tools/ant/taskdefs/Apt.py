EXECUTABLE_NAME = "String  \"apt\""
ERROR_IGNORING_COMPILER_OPTION = "String  \"Ignoring compiler attribute for the APT task, as it is fixed\""
ERROR_WRONG_JAVA_VERSION = "String  \"Apt task requires Java 1.5+\""
WARNING_IGNORING_FORK = "String  \"Apt only runs in its own JVM; fork=false option ignored\""
def ():
    '''returns Apt\n\n
    ()\n
    '''
def getAptExecutable():
    '''returns String\n\n
    getAptExecutable()\n
    '''
def setCompiler():
    '''returns None\n\n
    setCompiler(final String compiler)\n
    '''
def setFork():
    '''returns None\n\n
    setFork(final boolean fork)\n
    '''
def getCompiler():
    '''returns String\n\n
    getCompiler()\n
    '''
def isCompile():
    '''returns boolean\n\n
    isCompile()\n
    '''
def setCompile():
    '''returns None\n\n
    setCompile(final boolean compile)\n
    '''
def getFactory():
    '''returns String\n\n
    getFactory()\n
    '''
def setFactory():
    '''returns None\n\n
    setFactory(final String factory)\n
    '''
def setFactoryPathRef():
    '''returns None\n\n
    setFactoryPathRef(final Reference ref)\n
    '''
def createFactoryPath():
    '''returns Path\n\n
    createFactoryPath()\n
    '''
def getFactoryPath():
    '''returns Path\n\n
    getFactoryPath()\n
    '''
def createOption():
    '''returns Option\n\n
    createOption()\n
    '''
def getOptions():
    '''returns Vector\n\n
    getOptions()\n
    '''
def getPreprocessDir():
    '''returns File\n\n
    getPreprocessDir()\n
    '''
def setPreprocessDir():
    '''returns None\n\n
    setPreprocessDir(final File preprocessDir)\n
    '''
def execute():
    '''returns None\n\n
    execute()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getValue():
    '''returns String\n\n
    getValue()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final String value)\n
    '''
