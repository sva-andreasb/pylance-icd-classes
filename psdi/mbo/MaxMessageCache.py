def MaxMessageCache():
'''public MaxMessageCache()
'''
pass
def init():
'''public void init()
'''
pass
def reload():
'''public void reload()
public void reload(final String hashKey)
public void reload(final String group, final String key, final String langCode)
'''
pass
def getName():
'''public String getName()
'''
pass
def getMaxMessage():
'''public MaxMessage getMaxMessage(final String group, final String key, final UserInfo ui)
public MaxMessage getMaxMessage(final String group, final String key, final String langCode)
public MaxMessage getMaxMessage(final String group, final String key)
'''
pass
def getMessage():
'''public Message getMessage(final String group, final String key, final UserInfo ui)
public Message getMessage(final String group, final String key)
'''
pass
def getTaggedMessage():
'''public Message getTaggedMessage(final String group, final String key, final UserInfo ui)
public Message getTaggedMessage(final String group, final String key, final String langCode)
public Message getTaggedMessage(final String group, final String key)
public static Message getTaggedMessage(final MaxMessage mmsg)
public static Message getTaggedMessage(final MaxMessageBase mmsg)
'''
pass
def loadMsgGroup():
'''public void loadMsgGroup(final String group, final UserInfo ui)
'''
pass
def isMsgBundleLoaded():
'''public synchronized boolean isMsgBundleLoaded(final String msgGroup, final String langCode)
'''
pass
def clear():
'''public void clear()
'''
pass
def addElement():
'''public void addElement(String group, final String key, final String langCode, final MaxMessage msgRef)
'''
pass
def getElement():
'''public MaxMessage getElement(String group, final String key, final String langCode)
'''
pass
def getElementInAnyLanguage():
'''public MaxMessage getElementInAnyLanguage(String group, final String key)
'''
pass
def isGroupLoaded():
'''public boolean isGroupLoaded(String group, final String langCode)
'''
pass
def clearGroupForAllLanguage():
'''public void clearGroupForAllLanguage(final String group)
'''
pass
def clearMessageForAllLanguage():
'''public void clearMessageForAllLanguage(String group, final String key)
'''
pass
def getLoadedLanguages():
'''public String[] getLoadedLanguages(String group, final String key)
'''
pass
def clearMessage():
'''public void clearMessage(String group, final String key, final String langCode)
'''
pass
