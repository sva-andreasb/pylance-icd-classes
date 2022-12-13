IMAGE_SETTINGS = "int  0"
TEXT_SETTINGS = "int  1"
BOT_SETTINGS = "int  2"
ELEMENT_NAME = "String  chat-settings""
NAMESPACE = "String  http://jivesoftware.com/protocol/workgroup""
def ChatSettings():
'''public ChatSettings()
public ChatSettings(final String key)
'''
pass
def setKey():
'''public void setKey(final String key)
'''
pass
def setType():
'''public void setType(final int type)
'''
pass
def addSetting():
'''public void addSetting(final ChatSetting setting)
'''
pass
def getSettings():
'''public Collection<ChatSetting> getSettings()
'''
pass
def getChatSetting():
'''public ChatSetting getChatSetting(final String key)
'''
pass
def getFirstEntry():
'''public ChatSetting getFirstEntry()
'''
pass
def parse():
'''public ChatSettings parse(final XmlPullParser parser, final int initialDepth)
'''
pass
