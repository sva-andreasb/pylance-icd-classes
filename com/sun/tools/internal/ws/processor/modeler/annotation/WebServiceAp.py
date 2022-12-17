DO_NOT_OVERWRITE = "String  \"doNotOverWrite\""
IGNORE_NO_WEB_SERVICE_FOUND_WARNING = "String  \"ignoreNoWebServiceFoundWarning\""
def ():
    '''returns WebServiceAp\n\n
    ()\n
    (final WsgenOptions options, final PrintStream out)\n
    '''
def process():
    '''returns boolean\n\n
    process(final Set<? extends TypeElement> annotations, final RoundEnvironment roundEnv)\n
    '''
def processWarning():
    '''returns None\n\n
    processWarning(final String message)\n
    '''
def processError():
    '''returns None\n\n
    processError(final String message)\n
    processError(final String message, final Element element)\n
    '''
def canOverWriteClass():
    '''returns boolean\n\n
    canOverWriteClass(final String className)\n
    '''
def getSourceDir():
    '''returns File\n\n
    getSourceDir()\n
    '''
def isRemote():
    '''returns boolean\n\n
    isRemote(final TypeElement typeElement)\n
    '''
def isServiceException():
    '''returns boolean\n\n
    isServiceException(final TypeMirror typeMirror)\n
    '''
def getHolderValueType():
    '''returns TypeMirror\n\n
    getHolderValueType(final TypeMirror type)\n
    '''
def checkAndSetProcessed():
    '''returns boolean\n\n
    checkAndSetProcessed(final TypeElement typeElement)\n
    '''
def log():
    '''returns None\n\n
    log(String message)\n
    '''
def getOptions():
    '''returns WsgenOptions\n\n
    getOptions()\n
    '''
def getProcessingEnvironment():
    '''returns ProcessingEnvironment\n\n
    getProcessingEnvironment()\n
    '''
def getOperationName():
    '''returns String\n\n
    getOperationName(final Name messageName)\n
    '''
def getSupportedSourceVersion():
    '''returns SourceVersion\n\n
    getSupportedSourceVersion()\n
    '''
