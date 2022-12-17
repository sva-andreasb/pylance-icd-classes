def isSuperior():
    '''returns boolean\n\n
    isSuperior(final String className)\n
    '''
def makeNames():
    '''returns NrsMasterAliasMap[]\n\n
    makeNames(final String classType, final NrsSuperiorInfo[] superiors, final Map identifyingAttributes)\n
    '''
def makeNewName():
    '''returns String\n\n
    makeNewName(final String oldName, final String classType, String oldSuperiorName, String newSuperiorName)\n
    '''
def getNamingRulesVersion():
    '''returns String\n\n
    getNamingRulesVersion()\n
    '''
def isIdentifyingAttribute():
    '''returns boolean\n\n
    isIdentifyingAttribute(final String classType, final String attribute)\n
    '''
def lockCache():
    '''returns None\n\n
    lockCache(final DisReadWriteLock.Usage usage)\n
    '''
def unlockCache():
    '''returns None\n\n
    unlockCache(final DisReadWriteLock.Usage usage)\n
    '''
