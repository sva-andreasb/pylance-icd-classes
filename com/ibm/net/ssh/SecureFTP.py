SFTP_V1 = "int  1"
SFTP_V2 = "int  2"
SFTP_V3 = "int  3"
SFTP_V4 = "int  4"
SFTP_V5 = "int  5"
SFTP_V6 = "int  6"
ACCESS_READ_ONLY = "int  1"
ACCESS_WRITE_ONLY = "int  2"
ACCESS_READ_WRITE = "int  4"
ACCESS_APPEND = "int  8"
ACCESS_CREATE = "int  16"
ACCESS_OPEN_OR_CREATE = "int  32"
ACCESS_TRUNCATE = "int  64"
ACCESS_BLOCK_READ = "int  128"
ACCESS_BLOCK_WRITE = "int  256"
ACCESS_BLOCK_DELETE = "int  512"
ACCESS_BLOCK_ADVISORY = "int  1024"
ATTRIBUTE_SIZE = "int  1"
ATTRIBUTE_UIDGID = "int  2"
ATTRIBUTE_PERMISSIONS = "int  4"
ATTRIBUTE_ACCESSTIME = "int  8"
ATTRIBUTE_CREATETIME = "int  16"
ATTRIBUTE_MODIFYTIME = "int  32"
ATTRIBUTE_ACL = "int  64"
ATTRIBUTE_OWNERGROUP = "int  128"
ATTRIBUTE_SUBSECOND_TIMES = "int  256"
ATTRIBUTE_BITS = "int  512"
ATTRIBUTE_ALLOCATION_SIZE = "int  1024"
ATTRIBUTE_TEXT_HINT = "int  2048"
ATTRIBUTE_MIME_TYPE = "int  4096"
ATTRIBUTE_LINK_COUNT = "int  8192"
ATTRIBUTE_UNTRANSLATED = "int  16384"
PATH_NO_CHECK = "byte  1"
PATH_STAT_IF = "byte  2"
PATH_STAT_ALWAYS = "byte  3"
SEPARATOR = "String  /""
def getOutputStream():
'''public OutputStream getOutputStream()
'''
pass
def getInputStream():
'''public InputStream getInputStream()
'''
pass
def getErrorStream():
'''public InputStream getErrorStream()
'''
pass
def close():
'''public void close()
public void close()
public void close()
'''
pass
def getVersion():
'''public int getVersion()
'''
pass
def openFile():
'''public Handle openFile(final String filename, final int accessFlags)
public Handle openFile(final FileAttributes initialAttributes, final int accessFlags)
'''
pass
def closeHandle():
'''public Status closeHandle(Handle handle)
'''
pass
def getFileInputStream():
'''public InputStream getFileInputStream(final String filename)
'''
pass
def getFile():
'''public Status getFile(final String remoteFile, final File localFile, final boolean overwrite)
'''
pass
def run():
'''public Object run()
public Object run()
public Object run()
public Object run()
public void run()
'''
pass
def readFile():
'''public int readFile(final Handle fileHandle, final long offset, final int length, final byte[] output, final int outputOffset)
'''
pass
def getFileOutputStream():
'''public OutputStream getFileOutputStream(final String filename, final boolean append)
'''
pass
def putFile():
'''public Status putFile(final File localFile, String remotePath, final boolean overwrite)
'''
pass
def writeFile():
'''public Status writeFile(final Handle fileHandle, final long fileOffset, final byte[] data, final int offset, final int length)
'''
pass
def exists():
'''public boolean exists(final String path)
'''
pass
def getFileSize():
'''public long getFileSize(final String path)
'''
pass
def getAttributes():
'''public FileAttributes getAttributes(final String path, final int flags)
public FileAttributes getAttributes(final Handle fileHandle, final int flags)
'''
pass
def setAttributes():
'''public Status setAttributes(final FileAttributes attributes)
public Status setAttributes(final Handle fileHandle, final FileAttributes attributes)
'''
pass
def openDirectory():
'''public Handle openDirectory(String path)
'''
pass
def readDirectory():
'''public FileAttributes[] readDirectory(final Handle handle, final FileAttributesFilter filter)
public FileAttributes[] readDirectory(final Handle handle)
'''
pass
def removeFile():
'''public Status removeFile(final String filename)
'''
pass
def makeDirectory():
'''public Status makeDirectory(final String path)
public Status makeDirectory(final FileAttributes initialAttributes)
'''
pass
def makeDirectories():
'''public Status makeDirectories(final String path)
'''
pass
def removeDirectory():
'''public Status removeDirectory(final String path)
'''
pass
def getAbsolutePath():
'''public FileAttributes getAbsolutePath(final String path)
public FileAttributes getAbsolutePath(final String originalPath, final String composePath, final byte controlByte)
'''
pass
def getLinkAttributes():
'''public FileAttributes getLinkAttributes(final String path, final int flags)
'''
pass
def renameFile():
'''public Status renameFile(final String oldPath, final String newPath, final boolean overwrite)
'''
pass
def readLink():
'''public FileAttributes readLink(final String path)
'''
pass
def makeLink():
'''public Status makeLink(final String newLinkPath, final String existingPath, final boolean isSymbolic)
'''
pass
def checkFile():
'''public Status checkFile(final String filename, final long startOffset, final long length, final String hash)
public Status checkFile(final Handle fileHandle, final long startOffset, final long length, final String hash)
'''
pass
def getAvailableSpace():
'''public Status getAvailableSpace(final String path)
'''
pass
def getHomeDirectory():
'''public FileAttributes getHomeDirectory()
public FileAttributes getHomeDirectory(String username)
'''
pass
def lockFile():
'''public Status lockFile(final Handle handle, final long offset, final long length, final int lockMask)
'''
pass
def unlockFile():
'''public Status unlockFile(final Handle handle, final long offset, final long length)
'''
pass
def read():
'''public int read()
public int read(final byte[] data, final int offset, final int length)
'''
pass
def skip():
'''public long skip(final long n)
'''
pass
def available():
'''public int available()
'''
pass
def mark():
'''public void mark(final int readLimit)
'''
pass
def reset():
'''public void reset()
'''
pass
def markSupported():
'''public boolean markSupported()
'''
pass
def write():
'''public void write(final int data)
public void write(final byte[] data, final int offset, final int length)
'''
pass
def flush():
'''public void flush()
'''
pass
