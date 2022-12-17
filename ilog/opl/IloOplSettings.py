def ():
    '''returns IloOplSettings\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final IloOplErrorHandler handler)\n
    '''
def setOwn():
    '''returns None\n\n
    setOwn(final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def getConsoleOutput():
    '''returns PrintStream\n\n
    getConsoleOutput()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def setExecutionController():
    '''returns None\n\n
    setExecutionController(final IloOplExecutionController controller)\n
    '''
def removeExecutionController():
    '''returns None\n\n
    removeExecutionController(final IloOplExecutionController controller)\n
    '''
def getExecutionController():
    '''returns IloOplExecutionController\n\n
    getExecutionController()\n
    '''
def setWithLocations():
    '''returns None\n\n
    setWithLocations(final boolean with)\n
    '''
def isWithLocations():
    '''returns boolean\n\n
    isWithLocations()\n
    '''
def setWithNames():
    '''returns None\n\n
    setWithNames(final boolean with)\n
    '''
def isWithNames():
    '''returns boolean\n\n
    isWithNames()\n
    '''
def setSkipAssert():
    '''returns None\n\n
    setSkipAssert(final boolean with)\n
    '''
def isSkipAssert():
    '''returns boolean\n\n
    isSkipAssert()\n
    '''
def isDistributedMIP():
    '''returns boolean\n\n
    isDistributedMIP()\n
    '''
def getDistributedMIPConfig():
    '''returns String\n\n
    getDistributedMIPConfig()\n
    '''
def setDistributedMIPConfig():
    '''returns None\n\n
    setDistributedMIPConfig(final String path)\n
    '''
def isExportInternalData():
    '''returns boolean\n\n
    isExportInternalData()\n
    '''
def getExportInternalData():
    '''returns String\n\n
    getExportInternalData()\n
    '''
def setExportInternalData():
    '''returns None\n\n
    setExportInternalData(final String path)\n
    '''
def isExportExternalData():
    '''returns boolean\n\n
    isExportExternalData()\n
    '''
def getExportExternalData():
    '''returns String\n\n
    getExportExternalData()\n
    '''
def setExportExternalData():
    '''returns None\n\n
    setExportExternalData(final String path)\n
    '''
def setWithWarnings():
    '''returns None\n\n
    setWithWarnings(final boolean with)\n
    '''
def isWithWarnings():
    '''returns boolean\n\n
    isWithWarnings()\n
    '''
def setWithDataChecks():
    '''returns None\n\n
    setWithDataChecks(final boolean with)\n
    '''
def isWithDataChecks():
    '''returns boolean\n\n
    isWithDataChecks()\n
    '''
def setForceElementUsage():
    '''returns None\n\n
    setForceElementUsage(final boolean onoff)\n
    '''
def isForceElementUsage():
    '''returns boolean\n\n
    isForceElementUsage()\n
    '''
def setSkipWarnNeverUsedElements():
    '''returns None\n\n
    setSkipWarnNeverUsedElements(final boolean with)\n
    '''
def isSkipWarnNeverUsedElements():
    '''returns boolean\n\n
    isSkipWarnNeverUsedElements()\n
    '''
def setUseSortedSets():
    '''returns None\n\n
    setUseSortedSets(final boolean with)\n
    '''
def isUseSortedSets():
    '''returns boolean\n\n
    isUseSortedSets()\n
    '''
def setDisplayWidth():
    '''returns None\n\n
    setDisplayWidth(final int value)\n
    '''
def getDisplayWidth():
    '''returns int\n\n
    getDisplayWidth()\n
    '''
def setDisplayPrecision():
    '''returns None\n\n
    setDisplayPrecision(final int value)\n
    '''
def getDisplayPrecision():
    '''returns int\n\n
    getDisplayPrecision()\n
    '''
def setDisplayWithIndex():
    '''returns None\n\n
    setDisplayWithIndex(final boolean with)\n
    '''
def isDisplayWithIndex():
    '''returns boolean\n\n
    isDisplayWithIndex()\n
    '''
def setDisplayWithComponentName():
    '''returns None\n\n
    setDisplayWithComponentName(final boolean with)\n
    '''
def isDisplayWithComponentName():
    '''returns boolean\n\n
    isDisplayWithComponentName()\n
    '''
def setDisplayOnePerLine():
    '''returns None\n\n
    setDisplayOnePerLine(final boolean onoff)\n
    '''
def isDisplayOnePerLine():
    '''returns boolean\n\n
    isDisplayOnePerLine()\n
    '''
def setBigMapThreshold():
    '''returns None\n\n
    setBigMapThreshold(final int value)\n
    '''
def getBigMapThreshold():
    '''returns int\n\n
    getBigMapThreshold()\n
    '''
def setMainEndEnabled():
    '''returns None\n\n
    setMainEndEnabled(final boolean value)\n
    '''
def isMainEndEnabled():
    '''returns boolean\n\n
    isMainEndEnabled()\n
    '''
def setSlicingCache():
    '''returns None\n\n
    setSlicingCache(final boolean value)\n
    '''
def hasSlicingCache():
    '''returns boolean\n\n
    hasSlicingCache()\n
    '''
def setMemoryEmphasis():
    '''returns None\n\n
    setMemoryEmphasis(final boolean value)\n
    '''
def isMemoryEmphasis():
    '''returns boolean\n\n
    isMemoryEmphasis()\n
    '''
def getResolverPath():
    '''returns String\n\n
    getResolverPath()\n
    '''
def setResolverPath():
    '''returns None\n\n
    setResolverPath(final String path)\n
    '''
def getTmpDir():
    '''returns String\n\n
    getTmpDir()\n
    '''
def setTmpDir():
    '''returns None\n\n
    setTmpDir(final String path)\n
    '''
def setKeepTmpFiles():
    '''returns None\n\n
    setKeepTmpFiles(final boolean value)\n
    '''
def isKeepTmpFiles():
    '''returns boolean\n\n
    isKeepTmpFiles()\n
    '''
def setRelaxationLevel():
    '''returns None\n\n
    setRelaxationLevel(final int value)\n
    '''
def getRelaxationLevel():
    '''returns int\n\n
    getRelaxationLevel()\n
    '''
def hasProfiler():
    '''returns boolean\n\n
    hasProfiler()\n
    '''
def getProfiler():
    '''returns IloOplProfiler\n\n
    getProfiler()\n
    '''
def setProfiler():
    '''returns None\n\n
    setProfiler(final IloOplProfiler profiler)\n
    '''
def getErrorHandler():
    '''returns IloOplErrorHandler\n\n
    getErrorHandler()\n
    '''
def removeProfiler():
    '''returns None\n\n
    removeProfiler()\n
    '''
def setResourceResolver():
    '''returns None\n\n
    setResourceResolver(final IloOplResourceResolver resolver)\n
    '''
def getResourceResolver():
    '''returns IloOplResourceResolver\n\n
    getResourceResolver()\n
    '''
def getRunSettings():
    '''returns IloOplRunSettings\n\n
    getRunSettings()\n
    '''
def setUndefinedDataError():
    '''returns None\n\n
    setUndefinedDataError(final boolean value)\n
    '''
def isUndefinedDataError():
    '''returns boolean\n\n
    isUndefinedDataError()\n
    '''
def setWithMultiEnv():
    '''returns None\n\n
    setWithMultiEnv(final boolean value)\n
    '''
def isWithMultiEnv():
    '''returns boolean\n\n
    isWithMultiEnv()\n
    '''
def setGC():
    '''returns None\n\n
    setGC(final boolean value)\n
    '''
def usesGC():
    '''returns boolean\n\n
    usesGC()\n
    '''
