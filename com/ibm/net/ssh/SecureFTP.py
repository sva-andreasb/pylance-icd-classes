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
SEPARATOR = "String  \"/\""
def getOutputStream():
    '''returns OutputStream\n\n
    getOutputStream()\n
    '''
def getInputStream():
    '''returns InputStream\n\n
    getInputStream()\n
    '''
def getErrorStream():
    '''returns InputStream\n\n
    getErrorStream()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    close()\n
    close()\n
    '''
def getVersion():
    '''returns int\n\n
    getVersion()\n
    '''
def openFile():
    '''returns Handle\n\n
    openFile(final String filename, final int accessFlags)\n
    openFile(final FileAttributes initialAttributes, final int accessFlags)\n
    '''
def closeHandle():
    '''returns Status\n\n
    closeHandle(Handle handle)\n
    '''
def getFileInputStream():
    '''returns InputStream\n\n
    getFileInputStream(final String filename)\n
    '''
def getFile():
    '''returns Status\n\n
    getFile(final String remoteFile, final File localFile, final boolean overwrite)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def readFile():
    '''returns int\n\n
    readFile(final Handle fileHandle, final long offset, final int length, final byte[] output, final int outputOffset)\n
    '''
def getFileOutputStream():
    '''returns OutputStream\n\n
    getFileOutputStream(final String filename, final boolean append)\n
    '''
def putFile():
    '''returns Status\n\n
    putFile(final File localFile, String remotePath, final boolean overwrite)\n
    '''
def writeFile():
    '''returns Status\n\n
    writeFile(final Handle fileHandle, final long fileOffset, final byte[] data, final int offset, final int length)\n
    '''
def exists():
    '''returns boolean\n\n
    exists(final String path)\n
    '''
def getFileSize():
    '''returns long\n\n
    getFileSize(final String path)\n
    '''
def getAttributes():
    '''returns FileAttributes\n\n
    getAttributes(final String path, final int flags)\n
    getAttributes(final Handle fileHandle, final int flags)\n
    '''
def setAttributes():
    '''returns Status\n\n
    setAttributes(final FileAttributes attributes)\n
    setAttributes(final Handle fileHandle, final FileAttributes attributes)\n
    '''
def openDirectory():
    '''returns Handle\n\n
    openDirectory(String path)\n
    '''
def readDirectory():
    '''returns FileAttributes[]\n\n
    readDirectory(final Handle handle, final FileAttributesFilter filter)\n
    readDirectory(final Handle handle)\n
    '''
def removeFile():
    '''returns Status\n\n
    removeFile(final String filename)\n
    '''
def makeDirectory():
    '''returns Status\n\n
    makeDirectory(final String path)\n
    makeDirectory(final FileAttributes initialAttributes)\n
    '''
def makeDirectories():
    '''returns Status\n\n
    makeDirectories(final String path)\n
    '''
def removeDirectory():
    '''returns Status\n\n
    removeDirectory(final String path)\n
    '''
def getAbsolutePath():
    '''returns FileAttributes\n\n
    getAbsolutePath(final String path)\n
    getAbsolutePath(final String originalPath, final String composePath, final byte controlByte)\n
    '''
def getLinkAttributes():
    '''returns FileAttributes\n\n
    getLinkAttributes(final String path, final int flags)\n
    '''
def renameFile():
    '''returns Status\n\n
    renameFile(final String oldPath, final String newPath, final boolean overwrite)\n
    '''
def readLink():
    '''returns FileAttributes\n\n
    readLink(final String path)\n
    '''
def makeLink():
    '''returns Status\n\n
    makeLink(final String newLinkPath, final String existingPath, final boolean isSymbolic)\n
    '''
def checkFile():
    '''returns Status\n\n
    checkFile(final String filename, final long startOffset, final long length, final String hash)\n
    checkFile(final Handle fileHandle, final long startOffset, final long length, final String hash)\n
    '''
def getAvailableSpace():
    '''returns Status\n\n
    getAvailableSpace(final String path)\n
    '''
def getHomeDirectory():
    '''returns FileAttributes\n\n
    getHomeDirectory()\n
    getHomeDirectory(String username)\n
    '''
def lockFile():
    '''returns Status\n\n
    lockFile(final Handle handle, final long offset, final long length, final int lockMask)\n
    '''
def unlockFile():
    '''returns Status\n\n
    unlockFile(final Handle handle, final long offset, final long length)\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] data, final int offset, final int length)\n
    '''
def skip():
    '''returns long\n\n
    skip(final long n)\n
    '''
def available():
    '''returns int\n\n
    available()\n
    '''
def mark():
    '''returns None\n\n
    mark(final int readLimit)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def markSupported():
    '''returns boolean\n\n
    markSupported()\n
    '''
def write():
    '''returns None\n\n
    write(final int data)\n
    write(final byte[] data, final int offset, final int length)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
