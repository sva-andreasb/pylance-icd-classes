def ():
    '''returns Kind\n\n
    (final World world)\n
    (final String name, final String message)\n
    '''
def setAll():
    '''returns None\n\n
    setAll(final String messageKind)\n
    '''
def setFromMap():
    '''returns None\n\n
    setFromMap(final Map<String, String> lintOptionsMap)\n
    '''
def setFromProperties():
    '''returns None\n\n
    setFromProperties(final File file)\n
    setFromProperties(final Properties properties)\n
    '''
def loadDefaultProperties():
    '''returns None\n\n
    loadDefaultProperties()\n
    '''
def allKinds():
    '''returns Collection<Kind>\n\n
    allKinds()\n
    '''
def getLintKind():
    '''returns Kind\n\n
    getLintKind(final String name)\n
    '''
def suppressKinds():
    '''returns None\n\n
    suppressKinds(final Collection<Kind> lintKind)\n
    '''
def clearAllSuppressions():
    '''returns None\n\n
    clearAllSuppressions()\n
    '''
def clearSuppressions():
    '''returns None\n\n
    clearSuppressions(final Collection<Kind> lintKinds)\n
    '''
def fromKey():
    '''returns Kind\n\n
    fromKey(final String lintkey)\n
    '''
def setSuppressed():
    '''returns None\n\n
    setSuppressed(final boolean shouldBeSuppressed)\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setKind():
    '''returns None\n\n
    setKind(final IMessage.Kind kind)\n
    '''
def signal():
    '''returns None\n\n
    signal(final String info, final ISourceLocation location)\n
    signal(final String[] infos, final ISourceLocation location, final ISourceLocation[] extraLocations)\n
    '''
