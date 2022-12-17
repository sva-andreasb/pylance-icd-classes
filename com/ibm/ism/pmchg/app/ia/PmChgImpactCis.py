COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
FULL_IMPACTS = "int  0"
UNIQUE_IMPACTS = "int  1"
UNIQUE_PATHS = "int  2"
def ():
    '''returns PmChgImpactCis\n\n
    (final MboRemote mbo)\n
    (final MboRemote mbo, final int resultType)\n
    '''
def getImpacts():
    '''returns ArrayList<PmChgRuleResultRecord>\n\n
    getImpacts(final String cinum)\n
    '''
def getAndSaveImpactMboSet():
    '''returns PmChgRuleRsltSet\n\n
    getAndSaveImpactMboSet(final MboSetRemote set, final String cinum)\n
    '''
def getMaxDepth():
    '''returns int\n\n
    getMaxDepth()\n
    '''
def setMaxDepth():
    '''returns None\n\n
    setMaxDepth(final int maxDepth)\n
    '''
def getResultType():
    '''returns int\n\n
    getResultType()\n
    '''
def setResultType():
    '''returns None\n\n
    setResultType(final int resultType)\n
    '''
def isFullCheck():
    '''returns boolean\n\n
    isFullCheck()\n
    '''
def setFullCheck():
    '''returns None\n\n
    setFullCheck(final boolean fullCheck)\n
    '''
def isOnlyReturnMatches():
    '''returns boolean\n\n
    isOnlyReturnMatches()\n
    '''
def setOnlyReturnMatches():
    '''returns None\n\n
    setOnlyReturnMatches(final boolean onlyReturnMatches)\n
    '''
