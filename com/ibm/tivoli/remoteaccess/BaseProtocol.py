RAloggerName = "String  \"remoteAccess.logger\""
def BaseProtocol():
    '''    public BaseProtocol()
    public BaseProtocol(final String username, final byte[] password, final String hostname)
    '''
def setLogger():
    '''    public static void setLogger(final Logger logger)
    '''
def startLogging():
    '''    public static void startLogging()
    '''
def stopLogging():
    '''    public static void stopLogging()
    '''
def isLogging():
    '''    public static boolean isLogging()
    '''
def getRXAVersion():
    '''    public static String getRXAVersion()
    '''
def getRXABuild():
    '''    public static String getRXABuild()
    '''
def getTimeout():
    '''    public synchronized int getTimeout()
    '''
def setTimeout():
    '''    public synchronized void setTimeout(final int time)
    '''
def getHostname():
    '''    public String getHostname()
    '''
def setHostname():
    '''    public synchronized void setHostname(final String hostname)
    '''
def getUsername():
    '''    public String getUsername()
    '''
def setUsername():
    '''    public synchronized void setUsername(final String username)
    '''
def setPassword():
    '''    public synchronized void setPassword(final byte[] password)
    '''
def getPassword():
    '''    public byte[] getPassword()
    '''
def getLogger():
    '''    public static Logger getLogger()
    '''
def setLocale():
    '''    public static synchronized void setLocale(final Locale l)
    '''
def getConversionCharset():
    '''    public Charset getConversionCharset()
    '''
def setCharset():
    '''    public synchronized void setCharset(final String charsetName)
    '''
def setConversionCharset():
    '''    public synchronized void setConversionCharset(final Charset charset)
    '''
def clone():
    '''    public synchronized Object clone()
    '''
def beginSession():
    '''    public void beginSession(final String hostname)
    public void beginSession()
    '''
def endSession():
    '''    public void endSession()
    '''
def inSession():
    '''    public boolean inSession()
    '''
def getTextFile():
    '''    public void getTextFile(final String remoteFile, final String localPath)
    public synchronized void getTextFile(final String remoteFile, final String localPath, final boolean append)
    public synchronized void getTextFile(final String remoteFile, String localPath, final CharsetDecoder remoteDecoder, CharsetEncoder localEncoder, final boolean append)
    '''
def putTextFile():
    '''    public void putTextFile(final String localFile, final String remotePath)
    public synchronized void putTextFile(final String localFile, final String remotePath, final boolean append)
    public synchronized void putTextFile(final String localFile, String remotePath, CharsetDecoder localDecoder, final CharsetEncoder remoteEncoder, final boolean append)
    '''
def getFileReader():
    '''    public ConvertingReader getFileReader(final String fileName)
    public ConvertingReader getFileReader(final String filename, CharsetDecoder decoder, String lineSeparator)
    '''
def getFileWriter():
    '''    public ConvertingWriter getFileWriter(final String fileName, final boolean append)
    public ConvertingWriter getFileWriter(final String fileName, CharsetEncoder encoder, String lineSeparator, final boolean append)
    '''
def putDir():
    '''    public synchronized void putDir(final String localDir, final String remoteDir)
    '''
def _putDir():
    '''    public synchronized void _putDir(String localDir, String remoteDir, final boolean firstTimeThrough)
    '''
def getCanonicalHostname():
    '''    public String getCanonicalHostname()
    '''
def getCharset():
    '''    public String getCharset()
    '''
def getRemoteCharset():
    '''    public Charset getRemoteCharset()
    public Charset getRemoteCharset(final CharsetType type)
    '''
def getLineSeparator():
    '''    public synchronized String getLineSeparator()
    '''
def setLineSeparator():
    '''    public synchronized void setLineSeparator(final String separator)
    '''
def getRemoteOutputStream():
    '''    public synchronized RemoteOutputStream getRemoteOutputStream(final String remoteFile, final boolean append)
    '''
def getRemoteInputStream():
    '''    public synchronized RemoteInputStream getRemoteInputStream(final String remoteFile)
    '''
def invoke():
    '''    public Object invoke()
    '''
def cancel():
    '''    public void cancel()
    '''
