WILD = "String  \"*\""
DEEPWILD = "String  \"**\""
def ChannelId():
    '''    public ChannelId(String id)
    '''
def isWild():
    '''    public boolean isWild()
    '''
def isShallowWild():
    '''    public boolean isShallowWild()
    '''
def isDeepWild():
    '''    public boolean isDeepWild()
    '''
def isMeta():
    '''    public boolean isMeta()
    public static boolean isMeta(final String channelId)
    '''
def isService():
    '''    public boolean isService()
    public static boolean isService(final String channelId)
    '''
def isBroadcast():
    '''    public boolean isBroadcast()
    public static boolean isBroadcast(final String channelId)
    '''
def equals():
    '''    public boolean equals(final Object obj)
    '''
def hashCode():
    '''    public int hashCode()
    '''
def matches():
    '''    public boolean matches(final ChannelId channelId)
    '''
def toString():
    '''    public String toString()
    '''
def depth():
    '''    public int depth()
    '''
def isAncestorOf():
    '''    public boolean isAncestorOf(final ChannelId id)
    '''
def isParentOf():
    '''    public boolean isParentOf(final ChannelId id)
    '''
def getParent():
    '''    public String getParent()
    '''
def getSegment():
    '''    public String getSegment(final int i)
    '''
def getWilds():
    '''    public List<String> getWilds()
    '''
