def MaxMessageCache():
    '''    public MaxMessageCache()
    '''
def init():
    '''    public void init()
    '''
def reload():
    '''    public void reload()
    public void reload(final String hashKey)
    public void reload(final String group, final String key, final String langCode)
    '''
def getName():
    '''    public String getName()
    '''
def getMaxMessage():
    '''    public MaxMessage getMaxMessage(final String group, final String key, final UserInfo ui)
    public MaxMessage getMaxMessage(final String group, final String key, final String langCode)
    public MaxMessage getMaxMessage(final String group, final String key)
    '''
def getMessage():
    '''    public Message getMessage(final String group, final String key, final UserInfo ui)
    public Message getMessage(final String group, final String key)
    '''
def getTaggedMessage():
    '''    public Message getTaggedMessage(final String group, final String key, final UserInfo ui)
    public Message getTaggedMessage(final String group, final String key, final String langCode)
    public Message getTaggedMessage(final String group, final String key)
    public static Message getTaggedMessage(final MaxMessage mmsg)
    public static Message getTaggedMessage(final MaxMessageBase mmsg)
    '''
def loadMsgGroup():
    '''    public void loadMsgGroup(final String group, final UserInfo ui)
    '''
def isMsgBundleLoaded():
    '''    public synchronized boolean isMsgBundleLoaded(final String msgGroup, final String langCode)
    '''
def clear():
    '''    public void clear()
    '''
def addElement():
    '''    public void addElement(String group, final String key, final String langCode, final MaxMessage msgRef)
    '''
def getElement():
    '''    public MaxMessage getElement(String group, final String key, final String langCode)
    '''
def getElementInAnyLanguage():
    '''    public MaxMessage getElementInAnyLanguage(String group, final String key)
    '''
def isGroupLoaded():
    '''    public boolean isGroupLoaded(String group, final String langCode)
    '''
def clearGroupForAllLanguage():
    '''    public void clearGroupForAllLanguage(final String group)
    '''
def clearMessageForAllLanguage():
    '''    public void clearMessageForAllLanguage(String group, final String key)
    '''
def getLoadedLanguages():
    '''    public String[] getLoadedLanguages(String group, final String key)
    '''
def clearMessage():
    '''    public void clearMessage(String group, final String key, final String langCode)
    '''
