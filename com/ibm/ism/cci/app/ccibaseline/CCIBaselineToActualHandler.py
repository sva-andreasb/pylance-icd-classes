IBM_COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def ():
    '''returns CCIBaselineToActualHandler\n\n
    (final CCIBaselineRemote sourceBaseline)\n
    '''
def resolveTargetMember():
    '''returns CCITargetResolutionResult\n\n
    resolveTargetMember(final MboRemote sourceMember, final UserInfo userInfo)\n
    '''
def isLinkRuleBased():
    '''returns boolean\n\n
    isLinkRuleBased()\n
    '''
def getSourceMembers():
    '''returns MboSetRemote\n\n
    getSourceMembers()\n
    '''
def getSourceAttributes():
    '''returns MboSetRemote\n\n
    getSourceAttributes(final MboRemote sourceMember, final UserInfo userInfo)\n
    '''
def getTargetAttributes():
    '''returns MboSetRemote\n\n
    getTargetAttributes(final MboRemote targetMember, final UserInfo userInfo)\n
    '''
def getSourceDescriptor():
    '''returns CCIComparedObjectDescriptor\n\n
    getSourceDescriptor()\n
    '''
def getTargetDescriptor():
    '''returns CCIComparedObjectDescriptor\n\n
    getTargetDescriptor()\n
    '''
def getRequestID():
    '''returns long\n\n
    getRequestID()\n
    '''
def getSourceMemberSourceRelations():
    '''returns MboSetRemote\n\n
    getSourceMemberSourceRelations(final MboRemote sourceMember, final UserInfo userInfo)\n
    '''
def getSourceMemberTargetRelations():
    '''returns MboSetRemote\n\n
    getSourceMemberTargetRelations(final MboRemote sourceMember, final UserInfo userInfo)\n
    '''
def getTargetMemberSourceRelations():
    '''returns MboSetRemote\n\n
    getTargetMemberSourceRelations(final MboRemote targetMember, final UserInfo userInfo)\n
    '''
def getTargetMemberTargetRelations():
    '''returns MboSetRemote\n\n
    getTargetMemberTargetRelations(final MboRemote targetMember, final UserInfo userInfo)\n
    '''
def isSourceMemberSourceRelationInTargetMemberSourceRelations():
    '''returns boolean\n\n
    isSourceMemberSourceRelationInTargetMemberSourceRelations(final MboRemote sourceMember, final MboRemote sourceMemberSourceRelation, final Map<String, MboRemote> targetMemberSourceRelationsMap, final UserInfo userInfo)\n
    '''
def isSourceMemberTargetRelationInTargetMemberTargetRelations():
    '''returns boolean\n\n
    isSourceMemberTargetRelationInTargetMemberTargetRelations(final MboRemote sourceMember, final MboRemote sourceMemberTargetRelation, final Map<String, MboRemote> targetMemberTargetRelationsMap, final UserInfo userInfo)\n
    '''
def getSourceRelations():
    '''returns MboSetRemote\n\n
    getSourceRelations(final Date asOf, final String actCINum, final UserInfo userInfo)\n
    '''
def userIsAuthorizedToSourceRelation():
    '''returns boolean\n\n
    userIsAuthorizedToSourceRelation(final MboRemote sourceMember, final MboRemote sourceRelation, final UserInfo userInfo)\n
    '''
def userIsAuthorizedToTargetRelation():
    '''returns boolean\n\n
    userIsAuthorizedToTargetRelation(final MboRemote targetMember, final MboRemote targetRelation, final UserInfo userInfo)\n
    '''
def comparisonStarted():
    '''returns None\n\n
    comparisonStarted(final MboRemote sourceMember)\n
    '''
def reacquireSourceMember():
    '''returns MboRemote\n\n
    reacquireSourceMember(final MboRemote sourceMember, final UserInfo userInfo)\n
    '''
