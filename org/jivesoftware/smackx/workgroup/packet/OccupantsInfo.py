ELEMENT_NAME = "String  \"occupants-info\""
NAMESPACE = "String  \"http://jivesoftware.com/protocol/workgroup\""
def ():
    '''returns OccupantInfo\n\n
    (final String roomID)\n
    (final String jid, final String nickname, final Date joined)\n
    '''
def getRoomID():
    '''returns String\n\n
    getRoomID()\n
    '''
def getOccupantsCount():
    '''returns int\n\n
    getOccupantsCount()\n
    '''
def getOccupants():
    '''returns Set<OccupantInfo>\n\n
    getOccupants()\n
    '''
def getJID():
    '''returns String\n\n
    getJID()\n
    '''
def getNickname():
    '''returns String\n\n
    getNickname()\n
    '''
def getJoined():
    '''returns Date\n\n
    getJoined()\n
    '''
def parse():
    '''returns OccupantsInfo\n\n
    parse(final XmlPullParser parser, final int initialDepth)\n
    '''
