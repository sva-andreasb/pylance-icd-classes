def ():
    '''returns MatchResult\n\n
    (final MboSet ms)\n
    (final String inRespParty, final String inRespPartyGroup)\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def validateLevels():
    '''returns None\n\n
    validateLevels()\n
    '''
def validGroupDefault():
    '''returns MboRemote\n\n
    validGroupDefault()\n
    '''
def duplicateCheck():
    '''returns None\n\n
    duplicateCheck()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def getResponsibleParty():
    '''returns PersonGroupTeamSetRemote\n\n
    getResponsibleParty()\n
    '''
def getAvailablePersonforBroadcast():
    '''returns PersonSetRemote\n\n
    getAvailablePersonforBroadcast(final String orgID, final String siteID)\n
    '''
def getCurrentFirstAvailablePerson():
    '''returns PersonRemote\n\n
    getCurrentFirstAvailablePerson(final Date date, final String orgID, final String siteID)\n
    getCurrentFirstAvailablePerson(final Date date, final String orgID, final String siteID, final boolean treatNoCalAsAvailable)\n
    '''
def getCurrentResponsiblePerson():
    '''returns PersonRemote\n\n
    getCurrentResponsiblePerson(final Date date)\n
    getCurrentResponsiblePerson(final Date date, final String orgID, final String siteID)\n
    getCurrentResponsiblePerson(final Date date, final String orgID, final String siteID, final boolean treatNoCalAsAvailable)\n
    '''
def getResponsiblePeople():
    '''returns PersonSetRemote\n\n
    getResponsiblePeople()\n
    '''
def getNextAvailablePerson():
    '''returns PersonRemote\n\n
    getNextAvailablePerson(final Date date, final String skipPersonId)\n
    getNextAvailablePerson(final Date date, String orgID, String siteID, String skipPersonId)\n
    '''
def getRespParty():
    '''returns String\n\n
    getRespParty()\n
    '''
def setRespParty():
    '''returns None\n\n
    setRespParty(final String inRespParty)\n
    '''
def getRespPartyGroup():
    '''returns String\n\n
    getRespPartyGroup()\n
    '''
def setRespPartyGroup():
    '''returns None\n\n
    setRespPartyGroup(final String inRespPartyGroup)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
