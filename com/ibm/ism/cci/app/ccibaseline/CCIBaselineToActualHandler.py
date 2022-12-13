IBM_COPYRIGHT = "String \n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n""
def CCIBaselineToActualHandler():
'''public CCIBaselineToActualHandler(final CCIBaselineRemote sourceBaseline)
'''
pass
def resolveTargetMember():
'''public CCITargetResolutionResult resolveTargetMember(final MboRemote sourceMember, final UserInfo userInfo)
'''
pass
def isLinkRuleBased():
'''public boolean isLinkRuleBased()
'''
pass
def getSourceMembers():
'''public MboSetRemote getSourceMembers()
'''
pass
def getSourceAttributes():
'''public MboSetRemote getSourceAttributes(final MboRemote sourceMember, final UserInfo userInfo)
'''
pass
def getTargetAttributes():
'''public MboSetRemote getTargetAttributes(final MboRemote targetMember, final UserInfo userInfo)
'''
pass
def getSourceDescriptor():
'''public CCIComparedObjectDescriptor getSourceDescriptor()
'''
pass
def getTargetDescriptor():
'''public CCIComparedObjectDescriptor getTargetDescriptor()
'''
pass
def registerAttributeDifference():
'''public synchronized boolean registerAttributeDifference(final MboRemote sourceMember, final MboRemote targetMember, final String assetAttrID, final String sourceAttrValue, final String targetAttrValue, final String sourceAttrUnitOfMeasure, final String targetAttrUnitOfMeasure, final CCIAttributeDifferenceEnum difference, final UserInfo userInfo)
'''
pass
def registerRelationDifference():
'''public synchronized boolean registerRelationDifference(final MboRemote sourceMember, final MboRemote targetMember, final MboRemote newRelation, final MboRemote deletedRelation, final boolean srcRelation, final UserInfo userInfo)
'''
pass
def registerMemberResult():
'''public synchronized void registerMemberResult(final MboRemote sourceMember, final CCIComparisonResultCodeEnum resultCode, final UserInfo userInfo)
'''
pass
def getRequestID():
'''public long getRequestID()
'''
pass
def getSourceMemberSourceRelations():
'''public MboSetRemote getSourceMemberSourceRelations(final MboRemote sourceMember, final UserInfo userInfo)
'''
pass
def getSourceMemberTargetRelations():
'''public MboSetRemote getSourceMemberTargetRelations(final MboRemote sourceMember, final UserInfo userInfo)
'''
pass
def getTargetMemberSourceRelations():
'''public MboSetRemote getTargetMemberSourceRelations(final MboRemote targetMember, final UserInfo userInfo)
'''
pass
def getTargetMemberTargetRelations():
'''public MboSetRemote getTargetMemberTargetRelations(final MboRemote targetMember, final UserInfo userInfo)
'''
pass
def isSourceMemberSourceRelationInTargetMemberSourceRelations():
'''public boolean isSourceMemberSourceRelationInTargetMemberSourceRelations(final MboRemote sourceMember, final MboRemote sourceMemberSourceRelation, final Map<String, MboRemote> targetMemberSourceRelationsMap, final UserInfo userInfo)
'''
pass
def isSourceMemberTargetRelationInTargetMemberTargetRelations():
'''public boolean isSourceMemberTargetRelationInTargetMemberTargetRelations(final MboRemote sourceMember, final MboRemote sourceMemberTargetRelation, final Map<String, MboRemote> targetMemberTargetRelationsMap, final UserInfo userInfo)
'''
pass
def getLinkedActCINumForCI():
'''public static String getLinkedActCINumForCI(final String cinum, final UserInfo userInfo)
public static String getLinkedActCINumForCI(final MboRemote ciRelation, final String attribute, final UserInfo userInfo)
'''
pass
def getSourceRelations():
'''public MboSetRemote getSourceRelations(final Date asOf, final String actCINum, final UserInfo userInfo)
'''
pass
def userIsAuthorizedToSourceRelation():
'''public boolean userIsAuthorizedToSourceRelation(final MboRemote sourceMember, final MboRemote sourceRelation, final UserInfo userInfo)
'''
pass
def userIsAuthorizedToTargetRelation():
'''public boolean userIsAuthorizedToTargetRelation(final MboRemote targetMember, final MboRemote targetRelation, final UserInfo userInfo)
'''
pass
def registerNoFullAccessAuthorizationError():
'''public synchronized void registerNoFullAccessAuthorizationError(final UserInfo userInfo)
'''
pass
def comparisonStarted():
'''public void comparisonStarted(final MboRemote sourceMember)
'''
pass
def comparisonCompleted():
'''public synchronized void comparisonCompleted(final MboRemote sourceMember)
'''
pass
def reacquireSourceMember():
'''public MboRemote reacquireSourceMember(final MboRemote sourceMember, final UserInfo userInfo)
'''
pass
