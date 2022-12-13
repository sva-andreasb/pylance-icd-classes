def getLineCount():
'''public int getLineCount()
'''
pass
def getSize():
'''public int getSize()
'''
pass
def saveChanges():
'''public void saveChanges()
'''
pass
def setFrom():
'''public void setFrom()
public void setFrom(final Address address)
'''
pass
def getInputStream():
'''public InputStream getInputStream()
'''
pass
def getRawInputStream():
'''public InputStream getRawInputStream()
'''
pass
def writeTo():
'''public void writeTo(final OutputStream os)
public void writeTo(final OutputStream os, final String[] ignoreList)
'''
pass
def getContent():
'''public Object getContent()
'''
pass
def getContentID():
'''public String getContentID()
'''
pass
def getContentMD5():
'''public String getContentMD5()
'''
pass
def getContentType():
'''public String getContentType()
'''
pass
def getDescription():
'''public String getDescription()
'''
pass
def getDisposition():
'''public String getDisposition()
'''
pass
def getEncoding():
'''public String getEncoding()
'''
pass
def getFileName():
'''public String getFileName()
'''
pass
def getMessageID():
'''public String getMessageID()
'''
pass
def getSubject():
'''public String getSubject()
'''
pass
def getContentLanguage():
'''public String[] getContentLanguage()
'''
pass
def addHeaderLine():
'''public void addHeaderLine(final String line)
'''
pass
def removeHeader():
'''public void removeHeader(final String name)
'''
pass
def setContentID():
'''public void setContentID(final String cid)
'''
pass
def setContentMD5():
'''public void setContentMD5(final String md5)
'''
pass
def setDescription():
'''public void setDescription(final String description)
public void setDescription(final String description, final String charset)
'''
pass
def setDisposition():
'''public void setDisposition(final String disposition)
'''
pass
def setFileName():
'''public void setFileName(final String filename)
'''
pass
def setSubject():
'''public void setSubject(final String subject)
public void setSubject(final String subject, final String charset)
'''
pass
def setText():
'''public void setText(final String text)
public void setText(final String text, final String charset)
'''
pass
def isMimeType():
'''public boolean isMimeType(final String mimeType)
'''
pass
def setContentLanguage():
'''public void setContentLanguage(final String[] languages)
'''
pass
def getReceivedDate():
'''public Date getReceivedDate()
'''
pass
def getSentDate():
'''public Date getSentDate()
'''
pass
def setSentDate():
'''public void setSentDate(final Date d)
'''
pass
def getAllHeaderLines():
'''public Enumeration getAllHeaderLines()
'''
pass
def getAllHeaders():
'''public Enumeration getAllHeaders()
'''
pass
def getDataHandler():
'''public synchronized DataHandler getDataHandler()
'''
pass
def setDataHandler():
'''public synchronized void setDataHandler(final DataHandler dh)
'''
pass
def getSender():
'''public Address getSender()
'''
pass
def getAllRecipients():
'''public Address[] getAllRecipients()
'''
pass
def getFrom():
'''public Address[] getFrom()
'''
pass
def getReplyTo():
'''public Address[] getReplyTo()
'''
pass
def setSender():
'''public void setSender(final Address address)
'''
pass
def addFrom():
'''public void addFrom(final Address[] addresses)
'''
pass
def setReplyTo():
'''public void setReplyTo(final Address[] addresses)
'''
pass
def getFlags():
'''public synchronized Flags getFlags()
'''
pass
def setFlags():
'''public synchronized void setFlags(final Flags flag, final boolean set)
'''
pass
def isSet():
'''public synchronized boolean isSet(final Flags.Flag flag)
'''
pass
def reply():
'''public Message reply(final boolean replyToAll)
'''
pass
def setContent():
'''public void setContent(final Multipart mp)
public void setContent(final Object o, final String type)
'''
pass
def MimeMessage():
'''public MimeMessage(final Session session)
public MimeMessage(final MimeMessage source)
public MimeMessage(final Session session, final InputStream is)
'''
pass
def getHeader():
'''public String[] getHeader(final String name)
public String getHeader(final String name, final String delimiter)
'''
pass
def addHeader():
'''public void addHeader(final String name, final String value)
'''
pass
def setHeader():
'''public void setHeader(final String name, final String value)
'''
pass
def addRecipients():
'''public void addRecipients(final Message.RecipientType type, final String addresses)
public void addRecipients(final Message.RecipientType type, final Address[] addresses)
'''
pass
def setRecipients():
'''public void setRecipients(final Message.RecipientType type, final String addresses)
public void setRecipients(final Message.RecipientType type, final Address[] addresses)
'''
pass
def getMatchingHeaderLines():
'''public Enumeration getMatchingHeaderLines(final String[] names)
'''
pass
def getMatchingHeaders():
'''public Enumeration getMatchingHeaders(final String[] names)
'''
pass
def getNonMatchingHeaderLines():
'''public Enumeration getNonMatchingHeaderLines(final String[] names)
'''
pass
def getNonMatchingHeaders():
'''public Enumeration getNonMatchingHeaders(final String[] names)
'''
pass
def getRecipients():
'''public Address[] getRecipients(final Message.RecipientType type)
'''
pass
