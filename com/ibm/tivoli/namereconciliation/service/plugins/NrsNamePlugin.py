def getInstance():
    '''public static final NrsNamePlugin getInstance()
    '''
def init():
    '''public synchronized void init(final DataCleanser cleanser, final MetadataService metadata)
    '''
def isSuperior():
    '''public boolean isSuperior(final String className)
    '''
def makeNames():
    '''public NrsMasterAliasMap[] makeNames(final String classType, final NrsSuperiorInfo[] superiors, final Map identifyingAttributes)
    '''
def makeNewName():
    '''public String makeNewName(final String oldName, final String classType, String oldSuperiorName, String newSuperiorName)
    '''
def getNamingRulesVersion():
    '''public String getNamingRulesVersion()
    '''
def isIdentifyingAttribute():
    '''public boolean isIdentifyingAttribute(final String classType, final String attribute)
    '''
def lockCache():
    '''public void lockCache(final DisReadWriteLock.Usage usage)
    '''
def unlockCache():
    '''public void unlockCache(final DisReadWriteLock.Usage usage)
    '''
