MESSAGE_UNCOMPRESSED_LENGTH = "String  uncompressed_length""
MESSAGE_COMPRESSED = "String  compressed""
MESSAGE_UNIQUEID = "String  MEAMessageID""
JMS_MESSAGEID = "String  JMSMessageID""
DESTINATION_JNDI_NAME = "String  destjndiname""
MESSAGE_REDELIVERED = "String  redelivered""
DELIVERY_COUNT = "String  deliverycount""
EXTRACTFILEID = "String  extractfileid""
RECOVERY_STATUS = "String  recoverystatus""
EXTRACTFILESEQ = "String  extractfileseq""
MSGTYPE_TEXT = "String  textmsg""
TEXT_ENCODING = "String  encoding""
MIMETYPE = "String  mimetype""
ACTIONTYPE = "String  actiontype""
MAPPINGID = "String  mappingid""
ALTKEY = "String  altkey""
def JMSData():
'''public JMSData(final byte[] msgBody, final Map<String, String> msgHeaders, final boolean compress)
public JMSData(final byte[] msgBody, final Map<String, String> msgHeaders)
public JMSData(final String textMsgBody, final Map<String, String> msgHeaders)
'''
pass
def getMessageProperties():
'''public Map<String, String> getMessageProperties()
'''
pass
def getMessageBody():
'''public byte[] getMessageBody()
'''
pass
def getTextMessageBody():
'''public String getTextMessageBody()
'''
pass
def isCompress():
'''public boolean isCompress()
'''
pass
def isTextMessage():
'''public boolean isTextMessage()
'''
pass