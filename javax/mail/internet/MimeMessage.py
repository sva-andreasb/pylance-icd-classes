def getLineCount():
    '''    public int getLineCount()
    '''
def getSize():
    '''    public int getSize()
    '''
def saveChanges():
    '''    public void saveChanges()
    '''
def setFrom():
    '''    public void setFrom()
    public void setFrom(final Address address)
    '''
def getInputStream():
    '''    public InputStream getInputStream()
    '''
def getRawInputStream():
    '''    public InputStream getRawInputStream()
    '''
def writeTo():
    '''    public void writeTo(final OutputStream os)
    public void writeTo(final OutputStream os, final String[] ignoreList)
    '''
def getContent():
    '''    public Object getContent()
    '''
def getContentID():
    '''    public String getContentID()
    '''
def getContentMD5():
    '''    public String getContentMD5()
    '''
def getContentType():
    '''    public String getContentType()
    '''
def getDescription():
    '''    public String getDescription()
    '''
def getDisposition():
    '''    public String getDisposition()
    '''
def getEncoding():
    '''    public String getEncoding()
    '''
def getFileName():
    '''    public String getFileName()
    '''
def getMessageID():
    '''    public String getMessageID()
    '''
def getSubject():
    '''    public String getSubject()
    '''
def getContentLanguage():
    '''    public String[] getContentLanguage()
    '''
def addHeaderLine():
    '''    public void addHeaderLine(final String line)
    '''
def removeHeader():
    '''    public void removeHeader(final String name)
    '''
def setContentID():
    '''    public void setContentID(final String cid)
    '''
def setContentMD5():
    '''    public void setContentMD5(final String md5)
    '''
def setDescription():
    '''    public void setDescription(final String description)
    public void setDescription(final String description, final String charset)
    '''
def setDisposition():
    '''    public void setDisposition(final String disposition)
    '''
def setFileName():
    '''    public void setFileName(final String filename)
    '''
def setSubject():
    '''    public void setSubject(final String subject)
    public void setSubject(final String subject, final String charset)
    '''
def setText():
    '''    public void setText(final String text)
    public void setText(final String text, final String charset)
    '''
def isMimeType():
    '''    public boolean isMimeType(final String mimeType)
    '''
def setContentLanguage():
    '''    public void setContentLanguage(final String[] languages)
    '''
def getReceivedDate():
    '''    public Date getReceivedDate()
    '''
def getSentDate():
    '''    public Date getSentDate()
    '''
def setSentDate():
    '''    public void setSentDate(final Date d)
    '''
def getAllHeaderLines():
    '''    public Enumeration getAllHeaderLines()
    '''
def getAllHeaders():
    '''    public Enumeration getAllHeaders()
    '''
def getDataHandler():
    '''    public synchronized DataHandler getDataHandler()
    '''
def setDataHandler():
    '''    public synchronized void setDataHandler(final DataHandler dh)
    '''
def getSender():
    '''    public Address getSender()
    '''
def getAllRecipients():
    '''    public Address[] getAllRecipients()
    '''
def getFrom():
    '''    public Address[] getFrom()
    '''
def getReplyTo():
    '''    public Address[] getReplyTo()
    '''
def setSender():
    '''    public void setSender(final Address address)
    '''
def addFrom():
    '''    public void addFrom(final Address[] addresses)
    '''
def setReplyTo():
    '''    public void setReplyTo(final Address[] addresses)
    '''
def getFlags():
    '''    public synchronized Flags getFlags()
    '''
def setFlags():
    '''    public synchronized void setFlags(final Flags flag, final boolean set)
    '''
def isSet():
    '''    public synchronized boolean isSet(final Flags.Flag flag)
    '''
def reply():
    '''    public Message reply(final boolean replyToAll)
    '''
def setContent():
    '''    public void setContent(final Multipart mp)
    public void setContent(final Object o, final String type)
    '''
def MimeMessage():
    '''    public MimeMessage(final Session session)
    public MimeMessage(final MimeMessage source)
    public MimeMessage(final Session session, final InputStream is)
    '''
def getHeader():
    '''    public String[] getHeader(final String name)
    public String getHeader(final String name, final String delimiter)
    '''
def addHeader():
    '''    public void addHeader(final String name, final String value)
    '''
def setHeader():
    '''    public void setHeader(final String name, final String value)
    '''
def addRecipients():
    '''    public void addRecipients(final Message.RecipientType type, final String addresses)
    public void addRecipients(final Message.RecipientType type, final Address[] addresses)
    '''
def setRecipients():
    '''    public void setRecipients(final Message.RecipientType type, final String addresses)
    public void setRecipients(final Message.RecipientType type, final Address[] addresses)
    '''
def getMatchingHeaderLines():
    '''    public Enumeration getMatchingHeaderLines(final String[] names)
    '''
def getMatchingHeaders():
    '''    public Enumeration getMatchingHeaders(final String[] names)
    '''
def getNonMatchingHeaderLines():
    '''    public Enumeration getNonMatchingHeaderLines(final String[] names)
    '''
def getNonMatchingHeaders():
    '''    public Enumeration getNonMatchingHeaders(final String[] names)
    '''
def getRecipients():
    '''    public Address[] getRecipients(final Message.RecipientType type)
    '''
