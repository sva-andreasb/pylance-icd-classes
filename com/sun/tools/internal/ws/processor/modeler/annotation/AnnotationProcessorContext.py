def ():
    '''returns SeiContext\n\n
    ()\n
    ()\n
    (final Name seiName)\n
    '''
def addSeiContext():
    '''returns None\n\n
    addSeiContext(final Name seiName, final SeiContext seiContext)\n
    '''
def getSeiContext():
    '''returns SeiContext\n\n
    getSeiContext(final Name seiName)\n
    getSeiContext(final TypeElement d)\n
    '''
def getSeiContexts():
    '''returns Collection<SeiContext>\n\n
    getSeiContexts()\n
    '''
def getRound():
    '''returns int\n\n
    getRound()\n
    '''
def incrementRound():
    '''returns None\n\n
    incrementRound()\n
    '''
def setModelCompleted():
    '''returns None\n\n
    setModelCompleted(final boolean modelCompleted)\n
    '''
def isModelCompleted():
    '''returns boolean\n\n
    isModelCompleted()\n
    '''
def setImplementsSei():
    '''returns None\n\n
    setImplementsSei(final boolean implementsSei)\n
    '''
def getImplementsSei():
    '''returns boolean\n\n
    getImplementsSei()\n
    '''
def setNamespaceUri():
    '''returns None\n\n
    setNamespaceUri(final String namespaceUri)\n
    '''
def getNamespaceUri():
    '''returns String\n\n
    getNamespaceUri()\n
    '''
def getSeiImplName():
    '''returns Name\n\n
    getSeiImplName()\n
    '''
def setSeiImplName():
    '''returns None\n\n
    setSeiImplName(final Name implName)\n
    '''
def setReqWrapperOperation():
    '''returns None\n\n
    setReqWrapperOperation(final ExecutableElement method, final WrapperInfo wrapperInfo)\n
    '''
def getReqOperationWrapper():
    '''returns WrapperInfo\n\n
    getReqOperationWrapper(final ExecutableElement method)\n
    '''
def setResWrapperOperation():
    '''returns None\n\n
    setResWrapperOperation(final ExecutableElement method, final WrapperInfo wrapperInfo)\n
    '''
def getResOperationWrapper():
    '''returns WrapperInfo\n\n
    getResOperationWrapper(final ExecutableElement method)\n
    '''
def methodToString():
    '''returns String\n\n
    methodToString(final ExecutableElement method)\n
    '''
def clearExceptionMap():
    '''returns None\n\n
    clearExceptionMap()\n
    '''
def addExceptionBeanEntry():
    '''returns None\n\n
    addExceptionBeanEntry(final Name exception, final FaultInfo faultInfo, final ModelBuilder builder)\n
    '''
def getExceptionBeanName():
    '''returns FaultInfo\n\n
    getExceptionBeanName(final Name exception)\n
    '''
