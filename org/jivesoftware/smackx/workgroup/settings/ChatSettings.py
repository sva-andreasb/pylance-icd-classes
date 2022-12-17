IMAGE_SETTINGS = "int  0"
TEXT_SETTINGS = "int  1"
BOT_SETTINGS = "int  2"
ELEMENT_NAME = "String  \"chat-settings\""
NAMESPACE = "String  \"http://jivesoftware.com/protocol/workgroup\""
def ():
    '''returns ChatSettings\n\n
    ()\n
    (final String key)\n
    '''
def setKey():
    '''returns None\n\n
    setKey(final String key)\n
    '''
def setType():
    '''returns None\n\n
    setType(final int type)\n
    '''
def addSetting():
    '''returns None\n\n
    addSetting(final ChatSetting setting)\n
    '''
def getSettings():
    '''returns Collection<ChatSetting>\n\n
    getSettings()\n
    '''
def getChatSetting():
    '''returns ChatSetting\n\n
    getChatSetting(final String key)\n
    '''
def getFirstEntry():
    '''returns ChatSetting\n\n
    getFirstEntry()\n
    '''
def parse():
    '''returns ChatSettings\n\n
    parse(final XmlPullParser parser, final int initialDepth)\n
    '''
