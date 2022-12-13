RAloggerName = "String  remoteAccess.logger""
def BaseProtocol():
'''public BaseProtocol()
public BaseProtocol(final String username, final byte[] password, final String hostname)
'''
pass
def setLogger():
'''public static void setLogger(final Logger logger)
'''
pass
def startLogging():
'''public static void startLogging()
'''
pass
def stopLogging():
'''public static void stopLogging()
'''
pass
def isLogging():
'''public static boolean isLogging()
'''
pass
def getRXAVersion():
'''public static String getRXAVersion()
'''
pass
def getRXABuild():
'''public static String getRXABuild()
'''
pass
def getTimeout():
'''public synchronized int getTimeout()
'''
pass
def setTimeout():
'''public synchronized void setTimeout(final int time)
'''
pass
def getHostname():
'''public String getHostname()
'''
pass
def setHostname():
'''public synchronized void setHostname(final String hostname)
'''
pass
def getUsername():
'''public String getUsername()
'''
pass
def setUsername():
'''public synchronized void setUsername(final String username)
'''
pass
def setPassword():
'''public synchronized void setPassword(final byte[] password)
'''
pass
def getPassword():
'''public byte[] getPassword()
'''
pass
def getLogger():
'''public static Logger getLogger()
'''
pass
def setLocale():
'''public static synchronized void setLocale(final Locale l)
'''
pass
def getConversionCharset():
'''public Charset getConversionCharset()
'''
pass
def setCharset():
'''public synchronized void setCharset(final String charsetName)
'''
pass
def setConversionCharset():
'''public synchronized void setConversionCharset(final Charset charset)
'''
pass
def clone():
'''public synchronized Object clone()
'''
pass
def beginSession():
'''public void beginSession(final String hostname)
public void beginSession()
'''
pass
def endSession():
'''public void endSession()
'''
pass
def inSession():
'''public boolean inSession()
'''
pass
def getTextFile():
'''public void getTextFile(final String remoteFile, final String localPath)
public synchronized void getTextFile(final String remoteFile, final String localPath, final boolean append)
public synchronized void getTextFile(final String remoteFile, String localPath, final CharsetDecoder remoteDecoder, CharsetEncoder localEncoder, final boolean append)
'''
pass
def putTextFile():
'''public void putTextFile(final String localFile, final String remotePath)
public synchronized void putTextFile(final String localFile, final String remotePath, final boolean append)
public synchronized void putTextFile(final String localFile, String remotePath, CharsetDecoder localDecoder, final CharsetEncoder remoteEncoder, final boolean append)
'''
pass
def getFileReader():
'''public ConvertingReader getFileReader(final String fileName)
public ConvertingReader getFileReader(final String filename, CharsetDecoder decoder, String lineSeparator)
'''
pass
def getFileWriter():
'''public ConvertingWriter getFileWriter(final String fileName, final boolean append)
public ConvertingWriter getFileWriter(final String fileName, CharsetEncoder encoder, String lineSeparator, final boolean append)
'''
pass
def putDir():
'''public synchronized void putDir(final String localDir, final String remoteDir)
'''
pass
def _putDir():
'''public synchronized void _putDir(String localDir, String remoteDir, final boolean firstTimeThrough)
'''
pass
def getCanonicalHostname():
'''public String getCanonicalHostname()
'''
pass
def getCharset():
'''public String getCharset()
'''
pass
def getRemoteCharset():
'''public Charset getRemoteCharset()
public Charset getRemoteCharset(final CharsetType type)
'''
pass
def getLineSeparator():
'''public synchronized String getLineSeparator()
'''
pass
def setLineSeparator():
'''public synchronized void setLineSeparator(final String separator)
'''
pass
def getRemoteOutputStream():
'''public synchronized RemoteOutputStream getRemoteOutputStream(final String remoteFile, final boolean append)
'''
pass
def getRemoteInputStream():
'''public synchronized RemoteInputStream getRemoteInputStream(final String remoteFile)
'''
pass
def invoke():
'''public Object invoke()
'''
pass
def cancel():
'''public void cancel()
'''
pass
