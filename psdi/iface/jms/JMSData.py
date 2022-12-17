MESSAGE_UNCOMPRESSED_LENGTH = "String  \"uncompressed_length\""
MESSAGE_COMPRESSED = "String  \"compressed\""
MESSAGE_UNIQUEID = "String  \"MEAMessageID\""
JMS_MESSAGEID = "String  \"JMSMessageID\""
DESTINATION_JNDI_NAME = "String  \"destjndiname\""
MESSAGE_REDELIVERED = "String  \"redelivered\""
DELIVERY_COUNT = "String  \"deliverycount\""
EXTRACTFILEID = "String  \"extractfileid\""
RECOVERY_STATUS = "String  \"recoverystatus\""
EXTRACTFILESEQ = "String  \"extractfileseq\""
MSGTYPE_TEXT = "String  \"textmsg\""
TEXT_ENCODING = "String  \"encoding\""
MIMETYPE = "String  \"mimetype\""
ACTIONTYPE = "String  \"actiontype\""
MAPPINGID = "String  \"mappingid\""
ALTKEY = "String  \"altkey\""
def ():
    '''returns JMSData\n\n
    (final byte[] msgBody, final Map<String, String> msgHeaders, final boolean compress)\n
    (final byte[] msgBody, final Map<String, String> msgHeaders)\n
    (final String textMsgBody, final Map<String, String> msgHeaders)\n
    '''
def getMessageBody():
    '''returns byte[]\n\n
    getMessageBody()\n
    '''
def getTextMessageBody():
    '''returns String\n\n
    getTextMessageBody()\n
    '''
def isCompress():
    '''returns boolean\n\n
    isCompress()\n
    '''
def isTextMessage():
    '''returns boolean\n\n
    isTextMessage()\n
    '''
