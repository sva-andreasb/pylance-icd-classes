def OslcUITextCacheImpl():
    '''public OslcUITextCacheImpl()
    '''
def init():
    '''public void init()
    '''
def reload():
    '''public void reload()
    public void reload(final String key)
    '''
def getName():
    '''public String getName()
    '''
def getUITextForAppPropertyID():
    '''public String getUITextForAppPropertyID(final String app, final String property, final String id, final UserInfo userInfo)
    public String getUITextForAppPropertyID(final String app, final String property, final String id, final UserInfo userInfo, final String langcode)
    '''
def isSupportedLangCode():
    '''public boolean isSupportedLangCode(final String langCode)
    '''
def getUITextForAppProperty():
    '''public Map<String, String> getUITextForAppProperty(final String app, final String property, final UserInfo userInfo)
    public Map<String, String> getUITextForAppProperty(final String app, final String property, final UserInfo userInfo, final String langcode)
    '''
def getUITextForApp():
    '''public Map<String, Map<String, String>> getUITextForApp(final String app, final UserInfo userInfo)
    public Map<String, Map<String, String>> getUITextForApp(final String app, final UserInfo userInfo, final String langcode)
    '''
