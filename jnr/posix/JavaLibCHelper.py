STDIN = "int  0"
STDOUT = "int  1"
STDERR = "int  2"
def ():
    '''returns PosixExec\n\n
    (final POSIXHandler handler)\n
    (final POSIXHandler handler)\n
    '''
def chmod():
    '''returns int\n\n
    chmod(final String filename, final int mode)\n
    '''
def chown():
    '''returns int\n\n
    chown(final String filename, final int user, final int group)\n
    '''
def getfd():
    '''returns int\n\n
    getfd(final FileDescriptor descriptor)\n
    '''
def getlogin():
    '''returns String\n\n
    getlogin()\n
    '''
def getpid():
    '''returns int\n\n
    getpid()\n
    '''
def getpwent():
    '''returns Passwd\n\n
    getpwent()\n
    '''
def setpwent():
    '''returns int\n\n
    setpwent()\n
    '''
def endpwent():
    '''returns int\n\n
    endpwent()\n
    '''
def getpwuid():
    '''returns Passwd\n\n
    getpwuid(final int which)\n
    '''
def isatty():
    '''returns int\n\n
    isatty(final int fd)\n
    '''
def link():
    '''returns int\n\n
    link(final String oldpath, final String newpath)\n
    '''
def lstat():
    '''returns int\n\n
    lstat(final String path, final FileStat stat)\n
    '''
def mkdir():
    '''returns int\n\n
    mkdir(final String path, final int mode)\n
    '''
def rmdir():
    '''returns int\n\n
    rmdir(final String path)\n
    '''
def stat():
    '''returns int\n\n
    stat(final String path, final FileStat stat)\n
    '''
def symlink():
    '''returns int\n\n
    symlink(final String oldpath, final String newpath)\n
    '''
def readlink():
    '''returns int\n\n
    readlink(final String oldpath, final ByteBuffer buffer, final int length)\n
    '''
def runAndWait():
    '''returns int\n\n
    runAndWait(final String... args)\n
    runAndWait(final OutputStream output, final String... args)\n
    runAndWait(final OutputStream output, final OutputStream error, final String... args)\n
    '''
def write():
    '''returns None\n\n
    write(final int b)\n
    '''
