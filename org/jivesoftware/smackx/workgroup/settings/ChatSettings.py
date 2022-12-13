IMAGE_SETTINGS = "int  0"
TEXT_SETTINGS = "int  1"
BOT_SETTINGS = "int  2"
ELEMENT_NAME = "String  \"chat-settings\""
NAMESPACE = "String  \"http://jivesoftware.com/protocol/workgroup\""
def ChatSettings():
    '''    public ChatSettings()
    public ChatSettings(final String key)
    '''
def setKey():
    '''    public void setKey(final String key)
    '''
def setType():
    '''    public void setType(final int type)
    '''
def addSetting():
    '''    public void addSetting(final ChatSetting setting)
    '''
def getSettings():
    '''    public Collection<ChatSetting> getSettings()
    '''
def getChatSetting():
    '''    public ChatSetting getChatSetting(final String key)
    '''
def getFirstEntry():
    '''    public ChatSetting getFirstEntry()
    '''
def parse():
    '''    public ChatSettings parse(final XmlPullParser parser, final int initialDepth)
    '''
