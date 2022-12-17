def ():
    '''returns AntXMLContext\n\n
    (final Project project)\n
    '''
def setBuildFile():
    '''returns None\n\n
    setBuildFile(final File buildFile)\n
    setBuildFile(final URL buildFile)\n
    '''
def getBuildFile():
    '''returns File\n\n
    getBuildFile()\n
    '''
def getBuildFileParent():
    '''returns File\n\n
    getBuildFileParent()\n
    '''
def getBuildFileURL():
    '''returns URL\n\n
    getBuildFileURL()\n
    '''
def getBuildFileParentURL():
    '''returns URL\n\n
    getBuildFileParentURL()\n
    '''
def getProject():
    '''returns Project\n\n
    getProject()\n
    '''
def getCurrentProjectName():
    '''returns String\n\n
    getCurrentProjectName()\n
    '''
def setCurrentProjectName():
    '''returns None\n\n
    setCurrentProjectName(final String name)\n
    '''
def currentWrapper():
    '''returns RuntimeConfigurable\n\n
    currentWrapper()\n
    '''
def parentWrapper():
    '''returns RuntimeConfigurable\n\n
    parentWrapper()\n
    '''
def pushWrapper():
    '''returns None\n\n
    pushWrapper(final RuntimeConfigurable wrapper)\n
    '''
def popWrapper():
    '''returns None\n\n
    popWrapper()\n
    '''
def getWrapperStack():
    '''returns Vector\n\n
    getWrapperStack()\n
    '''
def addTarget():
    '''returns None\n\n
    addTarget(final Target target)\n
    '''
def getCurrentTarget():
    '''returns Target\n\n
    getCurrentTarget()\n
    '''
def getImplicitTarget():
    '''returns Target\n\n
    getImplicitTarget()\n
    '''
def setCurrentTarget():
    '''returns None\n\n
    setCurrentTarget(final Target target)\n
    '''
def setImplicitTarget():
    '''returns None\n\n
    setImplicitTarget(final Target target)\n
    '''
def getTargets():
    '''returns Vector\n\n
    getTargets()\n
    '''
def configureId():
    '''returns None\n\n
    configureId(final Object element, final Attributes attr)\n
    '''
def getLocator():
    '''returns Locator\n\n
    getLocator()\n
    '''
def setLocator():
    '''returns None\n\n
    setLocator(final Locator locator)\n
    '''
def isIgnoringProjectTag():
    '''returns boolean\n\n
    isIgnoringProjectTag()\n
    '''
def setIgnoreProjectTag():
    '''returns None\n\n
    setIgnoreProjectTag(final boolean flag)\n
    '''
def startPrefixMapping():
    '''returns None\n\n
    startPrefixMapping(final String prefix, final String uri)\n
    '''
def endPrefixMapping():
    '''returns None\n\n
    endPrefixMapping(final String prefix)\n
    '''
def getPrefixMapping():
    '''returns String\n\n
    getPrefixMapping(final String prefix)\n
    '''
def getCurrentTargets():
    '''returns Map\n\n
    getCurrentTargets()\n
    '''
def setCurrentTargets():
    '''returns None\n\n
    setCurrentTargets(final Map currentTargets)\n
    '''
