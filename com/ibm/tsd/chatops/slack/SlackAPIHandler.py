def oauth():
    '''    public static JSONObject oauth(final JSONObject body)
    '''
def createChannel():
    '''    public static SlackChannel createChannel(final String channelName, final String token)
    '''
def inviteToChannel():
    '''    public static void inviteToChannel(final String channel, final String user, final String token)
    '''
def setChannelTopic():
    '''    public static void setChannelTopic(final String channel, final String topic, final String token)
    '''
def postMessage():
    '''    public static void postMessage(final String channelId, final String userId, final boolean asUser, final JSONObject payload, final String token)
    '''
def postEphemeralMessage():
    '''    public static void postEphemeralMessage(final String channelId, final String userId, final boolean asUser, final JSONObject message, final String token)
    '''
def authorizeWorkspace():
    '''    public static JSONObject authorizeWorkspace(final String signingSecret)
    '''
def listChannels():
    '''    public static List<SlackChannel> listChannels(final String token)
    '''
def listChannelUsers():
    '''    public static List<SlackUser> listChannelUsers(final String token, final String channel)
    '''
def listTeamUsers():
    '''    public static List<SlackUser> listTeamUsers(final String token)
    '''
def openView():
    '''    public static JSONObject openView(final String triggerId, final JSONObject payload, final String token)
    '''
def updateView():
    '''    public static JSONObject updateView(final JSONObject payload, final String viewId, final String token)
    '''
