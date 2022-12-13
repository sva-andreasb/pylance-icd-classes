PERSONTONOTIFY = "String  \"persontonotify\""
USERTONOTIFY = "String  \"usertonotify\""
PERSONENDPOINT = "String  \"personendpoint\""
EVENTOBJECTID = "String  \"eventobjectid\""
EVENTOSNAME = "String  \"eventosname\""
NOTIFICATION = "String  \"notification\""
NOTIFICATIONTIME = "String  \"notificationtime\""
EVENTNAME = "String  \"eventname\""
USERNOTFOPTION = "String  \"usernotfoption\""
MAXPUSHPROJECTNAME = "String  \"maxpushprojectname\""
def NotificationChannel():
    '''public NotificationChannel()
    '''
def notifyUser():
    '''public void notifyUser(final String osName, final MboRemote mbo, final String eventName)
    public void notifyUser(final OSEvent event, final OSEventInfo eventInfo, final OSSubscriptionInfo notifcationInfo)
    '''
def writeDataToQueue():
    '''public void writeDataToQueue(final MXTransaction mxtran, final String eventForUser, final Map<String, String> properties, final UserInfo userInfo, final byte[] queueData, final String textData)
    '''
