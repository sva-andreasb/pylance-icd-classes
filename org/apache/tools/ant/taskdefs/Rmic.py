ERROR_RMIC_FAILED = "String  \"Rmic failed; see the compiler error output for details.\""
ERROR_UNABLE_TO_VERIFY_CLASS = "String  \"Unable to verify class \""
ERROR_NOT_FOUND = "String  \". It could not be found.\""
ERROR_NOT_DEFINED = "String  \". It is not defined.\""
ERROR_LOADING_CAUSED_EXCEPTION = "String  \". Loading caused Exception: \""
ERROR_NO_BASE_EXISTS = "String  \"base or destdir does not exist: \""
ERROR_NOT_A_DIR = "String  \"base or destdir is not a directory:\""
ERROR_BASE_NOT_SET = "String  \"base or destdir attribute must be set!\""
def ():
    '''returns Rmic\n\n
    ()\n
    '''
def setBase():
    '''returns None\n\n
    setBase(final File base)\n
    '''
def setDestdir():
    '''returns None\n\n
    setDestdir(final File destdir)\n
    '''
def getDestdir():
    '''returns File\n\n
    getDestdir()\n
    '''
def getOutputDir():
    '''returns File\n\n
    getOutputDir()\n
    '''
def getBase():
    '''returns File\n\n
    getBase()\n
    '''
def setClassname():
    '''returns None\n\n
    setClassname(final String classname)\n
    '''
def getClassname():
    '''returns String\n\n
    getClassname()\n
    '''
def setSourceBase():
    '''returns None\n\n
    setSourceBase(final File sourceBase)\n
    '''
def getSourceBase():
    '''returns File\n\n
    getSourceBase()\n
    '''
def setStubVersion():
    '''returns None\n\n
    setStubVersion(final String stubVersion)\n
    '''
def getStubVersion():
    '''returns String\n\n
    getStubVersion()\n
    '''
def setFiltering():
    '''returns None\n\n
    setFiltering(final boolean filter)\n
    '''
def getFiltering():
    '''returns boolean\n\n
    getFiltering()\n
    '''
def setDebug():
    '''returns None\n\n
    setDebug(final boolean debug)\n
    '''
def getDebug():
    '''returns boolean\n\n
    getDebug()\n
    '''
def setClasspathRef():
    '''returns None\n\n
    setClasspathRef(final Reference pathRef)\n
    '''
def getClasspath():
    '''returns Path\n\n
    getClasspath()\n
    '''
def setVerify():
    '''returns None\n\n
    setVerify(final boolean verify)\n
    '''
def getVerify():
    '''returns boolean\n\n
    getVerify()\n
    '''
def setIiop():
    '''returns None\n\n
    setIiop(final boolean iiop)\n
    '''
def getIiop():
    '''returns boolean\n\n
    getIiop()\n
    '''
def setIiopopts():
    '''returns None\n\n
    setIiopopts(final String iiopOpts)\n
    '''
def getIiopopts():
    '''returns String\n\n
    getIiopopts()\n
    '''
def setIdl():
    '''returns None\n\n
    setIdl(final boolean idl)\n
    '''
def getIdl():
    '''returns boolean\n\n
    getIdl()\n
    '''
def setIdlopts():
    '''returns None\n\n
    setIdlopts(final String idlOpts)\n
    '''
def getIdlopts():
    '''returns String\n\n
    getIdlopts()\n
    '''
def getFileList():
    '''returns Vector\n\n
    getFileList()\n
    '''
def setIncludeantruntime():
    '''returns None\n\n
    setIncludeantruntime(final boolean include)\n
    '''
def getIncludeantruntime():
    '''returns boolean\n\n
    getIncludeantruntime()\n
    '''
def setIncludejavaruntime():
    '''returns None\n\n
    setIncludejavaruntime(final boolean include)\n
    '''
def getIncludejavaruntime():
    '''returns boolean\n\n
    getIncludejavaruntime()\n
    '''
def getExtdirs():
    '''returns Path\n\n
    getExtdirs()\n
    '''
def getCompileList():
    '''returns Vector\n\n
    getCompileList()\n
    '''
def setCompiler():
    '''returns None\n\n
    setCompiler(final String compiler)\n
    setCompiler(final String impl)\n
    '''
def getCompiler():
    '''returns String\n\n
    getCompiler()\n
    '''
def createCompilerArg():
    '''returns ImplementationSpecificArgument\n\n
    createCompilerArg()\n
    '''
def getCurrentCompilerArgs():
    '''returns String[]\n\n
    getCurrentCompilerArgs()\n
    '''
def setExecutable():
    '''returns None\n\n
    setExecutable(final String ex)\n
    '''
def getExecutable():
    '''returns String\n\n
    getExecutable()\n
    '''
def createCompilerClasspath():
    '''returns Path\n\n
    createCompilerClasspath()\n
    '''
def setListfiles():
    '''returns None\n\n
    setListfiles(final boolean list)\n
    '''
def add():
    '''returns None\n\n
    add(final RmicAdapter adapter)\n
    '''
def execute():
    '''returns None\n\n
    execute()\n
    '''
def isValidRmiRemote():
    '''returns boolean\n\n
    isValidRmiRemote(final String classname)\n
    '''
def getRemoteInterface():
    '''returns Class\n\n
    getRemoteInterface(final Class testClass)\n
    '''
def getLoader():
    '''returns ClassLoader\n\n
    getLoader()\n
    '''
