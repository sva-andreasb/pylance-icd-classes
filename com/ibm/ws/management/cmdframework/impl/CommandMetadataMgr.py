def getParamDataEClass():
    '''returns EClass\n\n
    getParamDataEClass(final String cmdName)\n
    '''
def createParamDataEClass():
    '''returns EClass\n\n
    createParamDataEClass(final String paramEClassName, final List paramMetadataList)\n
    '''
def createParamDataEObject():
    '''returns EObject\n\n
    createParamDataEObject(final String cmdName)\n
    createParamDataEObject(final String taskCmdName, final String stepName)\n
    createParamDataEObject(final String taskCmdName, final String stepName, final CommandMetadata cmdMetadata)\n
    '''
def listCommandGroups():
    '''returns Collection\n\n
    listCommandGroups()\n
    '''
def listCommands():
    '''returns Collection\n\n
    listCommands(final String commandGroup)\n
    listCommands()\n
    '''
def listAllCommands():
    '''returns Collection\n\n
    listAllCommands()\n
    '''
def getCommandProvider():
    '''returns CommandProvider\n\n
    getCommandProvider(final String commandName)\n
    getCommandProvider(final String taskCommandName, final String stepName)\n
    '''
def getCommandMetadata():
    '''returns CommandMetadata\n\n
    getCommandMetadata(final String commandName)\n
    '''
def getCommandGroupMetadata():
    '''returns CommandGroupMetadata\n\n
    getCommandGroupMetadata(final String commandGrp)\n
    '''
def getStepEClassName():
    '''returns String\n\n
    getStepEClassName(final String taskCmdName, final String stepName)\n
    '''
def getTaskStepName():
    '''returns String[]\n\n
    getTaskStepName(final String stepEClassName)\n
    '''
def getCommandMetadataNoDynamicSteps():
    '''returns CommandMetadata\n\n
    getCommandMetadataNoDynamicSteps(final String commandName)\n
    '''
def isDynamicStepCommand():
    '''returns boolean\n\n
    isDynamicStepCommand(final CommandMetadata metadata)\n
    '''
def ():
    '''returns ProviderTableEntry\n\n
    (final Bundle bundle)\n
    (final ClassLoader loader)\n
    (final String inImplClass, final String inResouceBundle)\n
    '''
def locateClass():
    '''returns Class\n\n
    locateClass(final String className)\n
    locateClass(final String className)\n
    '''
def run():
    '''returns Object\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def locateResources():
    '''returns Enumeration\n\n
    locateResources(final String resourceName)\n
    locateResources(final String resourceName)\n
    '''
def getImplClass():
    '''returns String\n\n
    getImplClass()\n
    '''
def getResouceBundle():
    '''returns String\n\n
    getResouceBundle()\n
    '''
def setImplClass():
    '''returns None\n\n
    setImplClass(final String inImplClass)\n
    '''
def setResouceBundle():
    '''returns None\n\n
    setResouceBundle(final String inResouceBundle)\n
    '''
