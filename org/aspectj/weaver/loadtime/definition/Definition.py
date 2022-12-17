def ():
    '''returns DeclareErrorOrWarning\n\n
    ()\n
    (final String name, final String extend)\n
    (final String name, final String extend, final String precedence, final String perclause)\n
    (final String name, final String expression)\n
    (final DeclareAnnotationKind kind, final String pattern, final String annotation)\n
    (final AdviceKind adviceKind, final String pointcut, final String adviceClass, final String adviceMethod)\n
    (final boolean isError, final String pointcut, final String message)\n
    '''
def getWeaverOptions():
    '''returns String\n\n
    getWeaverOptions()\n
    '''
def getDumpPatterns():
    '''returns List<String>\n\n
    getDumpPatterns()\n
    '''
def setDumpBefore():
    '''returns None\n\n
    setDumpBefore(final boolean b)\n
    '''
def shouldDumpBefore():
    '''returns boolean\n\n
    shouldDumpBefore()\n
    '''
def setCreateDumpDirPerClassloader():
    '''returns None\n\n
    setCreateDumpDirPerClassloader(final boolean b)\n
    '''
def createDumpDirPerClassloader():
    '''returns boolean\n\n
    createDumpDirPerClassloader()\n
    '''
def getIncludePatterns():
    '''returns List<String>\n\n
    getIncludePatterns()\n
    '''
def getExcludePatterns():
    '''returns List<String>\n\n
    getExcludePatterns()\n
    '''
def getAspectClassNames():
    '''returns List<String>\n\n
    getAspectClassNames()\n
    '''
def getAspectExcludePatterns():
    '''returns List<String>\n\n
    getAspectExcludePatterns()\n
    '''
def getAspectIncludePatterns():
    '''returns List<String>\n\n
    getAspectIncludePatterns()\n
    '''
def getConcreteAspects():
    '''returns List<ConcreteAspect>\n\n
    getConcreteAspects()\n
    '''
def appendWeaverOptions():
    '''returns None\n\n
    appendWeaverOptions(final String option)\n
    '''
def addScopedAspect():
    '''returns None\n\n
    addScopedAspect(final String name, final String scopePattern)\n
    '''
def getScopeForAspect():
    '''returns String\n\n
    getScopeForAspect(final String name)\n
    '''
def setAspectRequires():
    '''returns None\n\n
    setAspectRequires(final String name, final String requiredType)\n
    '''
def getAspectRequires():
    '''returns String\n\n
    getAspectRequires(final String name)\n
    '''
