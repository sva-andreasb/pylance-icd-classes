ELEMENT_NAME = "String  \"occupants-info\""
NAMESPACE = "String  \"http://jivesoftware.com/protocol/workgroup\""
def OccupantsInfo():
    '''public OccupantsInfo(final String roomID)
    '''
def getRoomID():
    '''public String getRoomID()
    '''
def getOccupantsCount():
    '''public int getOccupantsCount()
    '''
def getOccupants():
    '''public Set<OccupantInfo> getOccupants()
    '''
def OccupantInfo():
    '''public OccupantInfo(final String jid, final String nickname, final Date joined)
    '''
def getJID():
    '''public String getJID()
    '''
def getNickname():
    '''public String getNickname()
    '''
def getJoined():
    '''public Date getJoined()
    '''
def parse():
    '''public OccupantsInfo parse(final XmlPullParser parser, final int initialDepth)
    '''
