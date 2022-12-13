def getLineCount():
    '''public int getLineCount()
    '''
def getSize():
    '''public int getSize()
    '''
def MimeBodyPart():
    '''public MimeBodyPart()
    public MimeBodyPart(InputStream is)
    public MimeBodyPart(final InternetHeaders headers, final byte[] content)
    '''
def getInputStream():
    '''public InputStream getInputStream()
    '''
def getRawInputStream():
    '''public InputStream getRawInputStream()
    '''
def writeTo():
    '''public void writeTo(final OutputStream os)
    '''
def getContent():
    '''public Object getContent()
    '''
def getContentID():
    '''public String getContentID()
    '''
def getContentMD5():
    '''public String getContentMD5()
    '''
def getContentType():
    '''public String getContentType()
    '''
def getDescription():
    '''public String getDescription()
    '''
def getDisposition():
    '''public String getDisposition()
    '''
def getEncoding():
    '''public String getEncoding()
    '''
def getFileName():
    '''public String getFileName()
    '''
def getContentLanguage():
    '''public String[] getContentLanguage()
    '''
def addHeaderLine():
    '''public void addHeaderLine(final String line)
    '''
def removeHeader():
    '''public void removeHeader(final String name)
    '''
def setContentID():
    '''public void setContentID(final String cid)
    '''
def setContentMD5():
    '''public void setContentMD5(final String md5)
    '''
def setDescription():
    '''public void setDescription(final String description)
    public void setDescription(final String description, final String charset)
    '''
def setDisposition():
    '''public void setDisposition(final String disposition)
    '''
def setFileName():
    '''public void setFileName(final String filename)
    '''
def setText():
    '''public void setText(final String text)
    public void setText(final String text, final String charset)
    '''
def isMimeType():
    '''public boolean isMimeType(final String mimeType)
    '''
def setContentLanguage():
    '''public void setContentLanguage(final String[] languages)
    '''
def getAllHeaderLines():
    '''public Enumeration getAllHeaderLines()
    '''
def getAllHeaders():
    '''public Enumeration getAllHeaders()
    '''
def getDataHandler():
    '''public DataHandler getDataHandler()
    '''
def setDataHandler():
    '''public void setDataHandler(final DataHandler dh)
    '''
def setContent():
    '''public void setContent(final Multipart mp)
    public void setContent(final Object o, final String type)
    '''
def getHeader():
    '''public String[] getHeader(final String name)
    public String getHeader(final String name, final String delimiter)
    '''
def addHeader():
    '''public void addHeader(final String name, final String value)
    '''
def setHeader():
    '''public void setHeader(final String name, final String value)
    '''
def getMatchingHeaderLines():
    '''public Enumeration getMatchingHeaderLines(final String[] names)
    '''
def getMatchingHeaders():
    '''public Enumeration getMatchingHeaders(final String[] names)
    '''
def getNonMatchingHeaderLines():
    '''public Enumeration getNonMatchingHeaderLines(final String[] names)
    '''
def getNonMatchingHeaders():
    '''public Enumeration getNonMatchingHeaders(final String[] names)
    '''
