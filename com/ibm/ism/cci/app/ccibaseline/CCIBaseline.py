IBM_COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def ():
    '''returns CCIBaseline\n\n
    (final MboSet ms)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def newcopy():
    '''returns MboRemote\n\n
    newcopy()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def undelete():
    '''returns None\n\n
    undelete(final long accessModifier)\n
    '''
def activate():
    '''returns boolean\n\n
    activate()\n
    '''
def copySelectedCollectionMembers():
    '''returns int\n\n
    copySelectedCollectionMembers(final MboSetRemote collMbo)\n
    '''
def copySelectedRelTargetMembers():
    '''returns int\n\n
    copySelectedRelTargetMembers(final MboSetRemote collMbo)\n
    '''
def copySelectedRelSourceMembers():
    '''returns int\n\n
    copySelectedRelSourceMembers(final MboSetRemote collMbo)\n
    '''
def validateBaseline():
    '''returns None\n\n
    validateBaseline(final boolean forActivate)\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def createOrUpdateCollection():
    '''returns Object[]\n\n
    createOrUpdateCollection(final String selectedCollection)\n
    '''
def hasUnauthorizedMembers():
    '''returns boolean\n\n
    hasUnauthorizedMembers()\n
    '''
def compareToActual():
    '''returns long\n\n
    compareToActual()\n
    '''
def getMembersFromDatabase():
    '''returns MboSetRemote\n\n
    getMembersFromDatabase()\n
    getMembersFromDatabase(final boolean readOnly)\n
    '''
def setAuthorizedMembersWhere():
    '''returns None\n\n
    setAuthorizedMembersWhere(final MboSetRemote members)\n
    '''
def setUnauthorizedMembersWhere():
    '''returns None\n\n
    setUnauthorizedMembersWhere(final MboSetRemote members)\n
    '''
def getAuthorizedMembers():
    '''returns MboSetRemote\n\n
    getAuthorizedMembers()\n
    '''
def getUnauthorizedMembers():
    '''returns MboSetRemote\n\n
    getUnauthorizedMembers()\n
    '''
def isAuthorizedMemberSetInitialized():
    '''returns boolean\n\n
    isAuthorizedMemberSetInitialized()\n
    '''
def setAuthorizedMemberSetInitialized():
    '''returns None\n\n
    setAuthorizedMemberSetInitialized(final boolean authorizedMemberSetInitialized)\n
    '''
def getAuthorizedMembersWhereCondition():
    '''returns String\n\n
    getAuthorizedMembersWhereCondition()\n
    '''
def setAuthorizedMembersWhereCondition():
    '''returns None\n\n
    setAuthorizedMembersWhereCondition(final String authorizedMembersWhereCondition)\n
    '''
def isBuiltWhereConditions():
    '''returns boolean\n\n
    isBuiltWhereConditions()\n
    '''
def setBuiltWhereConditions():
    '''returns None\n\n
    setBuiltWhereConditions(final boolean builtWhereConditions)\n
    '''
def isUnauthorizedMemberSetInitialized():
    '''returns boolean\n\n
    isUnauthorizedMemberSetInitialized()\n
    '''
def setUnauthorizedMemberSetInitialized():
    '''returns None\n\n
    setUnauthorizedMemberSetInitialized(final boolean unauthorizedMemberSetInitialized)\n
    '''
def getUnauthorizedMembersWhereCondition():
    '''returns String\n\n
    getUnauthorizedMembersWhereCondition()\n
    '''
def setUnauthorizedMembersWhereCondition():
    '''returns None\n\n
    setUnauthorizedMembersWhereCondition(final String unauthorizedMembersWhereCondition)\n
    '''
def markActCIRelationsWithBaselineDate():
    '''returns None\n\n
    markActCIRelationsWithBaselineDate(final CCIBaselineMemberRemote aBaselineMember, final Date asOf)\n
    '''
def getWhereclauseForCIsPromotedWithMember():
    '''returns String\n\n
    getWhereclauseForCIsPromotedWithMember(final CCIBaselineMemberRemote member)\n
    '''
