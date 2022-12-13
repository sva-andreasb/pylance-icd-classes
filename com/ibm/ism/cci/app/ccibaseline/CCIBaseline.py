IBM_COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def CCIBaseline():
    '''public CCIBaseline(final MboSet ms)
    '''
def add():
    '''public void add()
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def newcopy():
    '''public MboRemote newcopy()
    '''
def init():
    '''public void init()
    '''
def delete():
    '''public void delete(final long accessModifier)
    '''
def undelete():
    '''public void undelete(final long accessModifier)
    '''
def activate():
    '''public boolean activate()
    '''
def copySelectedCollectionMembers():
    '''public int copySelectedCollectionMembers(final MboSetRemote collMbo)
    '''
def copySelectedRelTargetMembers():
    '''public int copySelectedRelTargetMembers(final MboSetRemote collMbo)
    '''
def copySelectedRelSourceMembers():
    '''public int copySelectedRelSourceMembers(final MboSetRemote collMbo)
    '''
def validateBaseline():
    '''public void validateBaseline(final boolean forActivate)
    '''
def modify():
    '''public void modify()
    '''
def createOrUpdateCollection():
    '''public Object[] createOrUpdateCollection(final String selectedCollection)
    '''
def hasUnauthorizedMembers():
    '''public boolean hasUnauthorizedMembers()
    '''
def compareToActual():
    '''public long compareToActual()
    '''
def getMembersFromDatabase():
    '''public MboSetRemote getMembersFromDatabase()
    public MboSetRemote getMembersFromDatabase(final boolean readOnly)
    '''
def setAuthorizedMembersWhere():
    '''public void setAuthorizedMembersWhere(final MboSetRemote members)
    '''
def setUnauthorizedMembersWhere():
    '''public void setUnauthorizedMembersWhere(final MboSetRemote members)
    '''
def getAuthorizedMembers():
    '''public MboSetRemote getAuthorizedMembers()
    '''
def getUnauthorizedMembers():
    '''public MboSetRemote getUnauthorizedMembers()
    '''
def isAuthorizedMemberSetInitialized():
    '''public boolean isAuthorizedMemberSetInitialized()
    '''
def setAuthorizedMemberSetInitialized():
    '''public void setAuthorizedMemberSetInitialized(final boolean authorizedMemberSetInitialized)
    '''
def getAuthorizedMembersWhereCondition():
    '''public String getAuthorizedMembersWhereCondition()
    '''
def setAuthorizedMembersWhereCondition():
    '''public void setAuthorizedMembersWhereCondition(final String authorizedMembersWhereCondition)
    '''
def isBuiltWhereConditions():
    '''public boolean isBuiltWhereConditions()
    '''
def setBuiltWhereConditions():
    '''public void setBuiltWhereConditions(final boolean builtWhereConditions)
    '''
def isUnauthorizedMemberSetInitialized():
    '''public boolean isUnauthorizedMemberSetInitialized()
    '''
def setUnauthorizedMemberSetInitialized():
    '''public void setUnauthorizedMemberSetInitialized(final boolean unauthorizedMemberSetInitialized)
    '''
def getUnauthorizedMembersWhereCondition():
    '''public String getUnauthorizedMembersWhereCondition()
    '''
def setUnauthorizedMembersWhereCondition():
    '''public void setUnauthorizedMembersWhereCondition(final String unauthorizedMembersWhereCondition)
    '''
def markActCIRelationsWithBaselineDate():
    '''public void markActCIRelationsWithBaselineDate(final CCIBaselineMemberRemote aBaselineMember, final Date asOf)
    '''
def getWhereclauseForCIsPromotedWithMember():
    '''public String getWhereclauseForCIsPromotedWithMember(final CCIBaselineMemberRemote member)
    '''
