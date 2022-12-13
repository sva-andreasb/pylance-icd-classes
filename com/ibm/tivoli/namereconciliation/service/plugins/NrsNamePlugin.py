def getInstance():
'''public static final NrsNamePlugin getInstance()
'''
pass
def init():
'''public synchronized void init(final DataCleanser cleanser, final MetadataService metadata)
'''
pass
def isSuperior():
'''public boolean isSuperior(final String className)
'''
pass
def makeNames():
'''public NrsMasterAliasMap[] makeNames(final String classType, final NrsSuperiorInfo[] superiors, final Map identifyingAttributes)
'''
pass
def makeNewName():
'''public String makeNewName(final String oldName, final String classType, String oldSuperiorName, String newSuperiorName)
'''
pass
def getNamingRulesVersion():
'''public String getNamingRulesVersion()
'''
pass
def isIdentifyingAttribute():
'''public boolean isIdentifyingAttribute(final String classType, final String attribute)
'''
pass
def lockCache():
'''public void lockCache(final DisReadWriteLock.Usage usage)
'''
pass
def unlockCache():
'''public void unlockCache(final DisReadWriteLock.Usage usage)
'''
pass
