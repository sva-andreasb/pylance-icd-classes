MUC_ROOMCONFIG_ROOMOWNERS = "String  \"muc#roomconfig_roomowners\""
MUC_ROOMCONFIG_MEMBERSONLY = "String  \"muc#roomconfig_membersonly\""
MUC_ROOMCONFIG_PASSWORDPROTECTEDROOM = "String  \"muc#roomconfig_passwordprotectedroom\""
MUC_ROOMCONFIG_ROOMSECRET = "String  \"muc#roomconfig_roomsecret\""
def supportsRoomOwners():
    '''returns boolean\n\n
    supportsRoomOwners()\n
    '''
def setRoomOwners():
    '''returns MucConfigFormManager\n\n
    setRoomOwners(final Collection<? extends Jid> newOwners)\n
    '''
def supportsMembersOnly():
    '''returns boolean\n\n
    supportsMembersOnly()\n
    '''
def makeMembersOnly():
    '''returns MucConfigFormManager\n\n
    makeMembersOnly()\n
    '''
def setMembersOnly():
    '''returns MucConfigFormManager\n\n
    setMembersOnly(final boolean isMembersOnly)\n
    '''
def supportsPasswordProtected():
    '''returns boolean\n\n
    supportsPasswordProtected()\n
    '''
def setAndEnablePassword():
    '''returns MucConfigFormManager\n\n
    setAndEnablePassword(final String password)\n
    '''
def makePasswordProtected():
    '''returns MucConfigFormManager\n\n
    makePasswordProtected()\n
    '''
def setIsPasswordProtected():
    '''returns MucConfigFormManager\n\n
    setIsPasswordProtected(final boolean isPasswordProtected)\n
    '''
def setRoomSecret():
    '''returns MucConfigFormManager\n\n
    setRoomSecret(final String secret)\n
    '''
def submitConfigurationForm():
    '''returns None\n\n
    submitConfigurationForm()\n
    '''
