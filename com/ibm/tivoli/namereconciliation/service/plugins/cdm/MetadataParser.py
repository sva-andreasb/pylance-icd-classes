def ():
    '''returns MetadataParser\n\n
    (final MetadataService metadata)\n
    '''
def containsMultipleSuperiors():
    '''returns boolean\n\n
    containsMultipleSuperiors(final String className)\n
    '''
def getNamingPolicyForClass():
    '''returns NamingPolicy\n\n
    getNamingPolicyForClass(final String className)\n
    '''
def getNamingRulesVersion():
    '''returns String\n\n
    getNamingRulesVersion(final MetadataService mds)\n
    getNamingRulesVersion(final String namingRulesLocation)\n
    '''
def getNextNamingPolicy():
    '''returns NamingPolicy\n\n
    getNextNamingPolicy(final String duplicateClassName)\n
    '''
def isParent():
    '''returns boolean\n\n
    isParent(final String parent, final String child)\n
    '''
def isSuperiorClass():
    '''returns boolean\n\n
    isSuperiorClass(final String className)\n
    '''
def loadNamingRules():
    '''returns None\n\n
    loadNamingRules()\n
    '''
def isIdentifyingAttribute():
    '''returns boolean\n\n
    isIdentifyingAttribute(final String classType, final String attribute)\n
    '''
