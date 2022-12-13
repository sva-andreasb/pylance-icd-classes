MUC_ROOMCONFIG_ROOMOWNERS = "String  \"muc#roomconfig_roomowners\""
MUC_ROOMCONFIG_MEMBERSONLY = "String  \"muc#roomconfig_membersonly\""
MUC_ROOMCONFIG_PASSWORDPROTECTEDROOM = "String  \"muc#roomconfig_passwordprotectedroom\""
MUC_ROOMCONFIG_ROOMSECRET = "String  \"muc#roomconfig_roomsecret\""
def supportsRoomOwners():
    '''public boolean supportsRoomOwners()
    '''
def setRoomOwners():
    '''public MucConfigFormManager setRoomOwners(final Collection<? extends Jid> newOwners)
    '''
def supportsMembersOnly():
    '''public boolean supportsMembersOnly()
    '''
def makeMembersOnly():
    '''public MucConfigFormManager makeMembersOnly()
    '''
def setMembersOnly():
    '''public MucConfigFormManager setMembersOnly(final boolean isMembersOnly)
    '''
def supportsPasswordProtected():
    '''public boolean supportsPasswordProtected()
    '''
def setAndEnablePassword():
    '''public MucConfigFormManager setAndEnablePassword(final String password)
    '''
def makePasswordProtected():
    '''public MucConfigFormManager makePasswordProtected()
    '''
def setIsPasswordProtected():
    '''public MucConfigFormManager setIsPasswordProtected(final boolean isPasswordProtected)
    '''
def setRoomSecret():
    '''public MucConfigFormManager setRoomSecret(final String secret)
    '''
def submitConfigurationForm():
    '''public void submitConfigurationForm()
    '''
