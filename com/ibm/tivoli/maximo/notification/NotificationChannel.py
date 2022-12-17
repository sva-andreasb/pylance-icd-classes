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
def ():
    '''returns NotificationChannel\n\n
    ()\n
    '''
def notifyUser():
    '''returns None\n\n
    notifyUser(final String osName, final MboRemote mbo, final String eventName)\n
    notifyUser(final OSEvent event, final OSEventInfo eventInfo, final OSSubscriptionInfo notifcationInfo)\n
    '''
def writeDataToQueue():
    '''returns None\n\n
    writeDataToQueue(final MXTransaction mxtran, final String eventForUser, final Map<String, String> properties, final UserInfo userInfo, final byte[] queueData, final String textData)\n
    '''
