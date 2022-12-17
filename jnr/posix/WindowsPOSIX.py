FILE_FLAG_BACKUP_SEMANTICS = "int  33554432"
def allocateStat():
    '''returns FileStat\n\n
    allocateStat()\n
    '''
def allocateMsgHdr():
    '''returns MsgHdr\n\n
    allocateMsgHdr()\n
    '''
def socketMacros():
    '''returns SocketMacros\n\n
    socketMacros()\n
    '''
def kill():
    '''returns int\n\n
    kill(final int pid, final int signal)\n
    kill(final long pid, final int signal)\n
    '''
def chmod():
    '''returns int\n\n
    chmod(final String filename, final int mode)\n
    '''
def chdir():
    '''returns int\n\n
    chdir(final String path)\n
    '''
def chown():
    '''returns int\n\n
    chown(final String filename, final int user, final int group)\n
    '''
def exec():
    '''returns int\n\n
    exec(final String path, final String[] argv)\n
    exec(final String path, final String[] argv, final String[] envp)\n
    '''
def crypt():
    '''returns byte[]\n\n
    crypt(final CharSequence key, final CharSequence salt)\n
    crypt(final byte[] key, final byte[] salt)\n
    '''
def execv():
    '''returns int\n\n
    execv(final String path, final String[] argv)\n
    '''
def getegid():
    '''returns int\n\n
    getegid()\n
    '''
def setegid():
    '''returns int\n\n
    setegid(final int egid)\n
    '''
def geteuid():
    '''returns int\n\n
    geteuid()\n
    '''
def seteuid():
    '''returns int\n\n
    seteuid(final int euid)\n
    '''
def getuid():
    '''returns int\n\n
    getuid()\n
    '''
def setuid():
    '''returns int\n\n
    setuid(final int uid)\n
    '''
def getgid():
    '''returns int\n\n
    getgid()\n
    '''
def setgid():
    '''returns int\n\n
    setgid(final int gid)\n
    '''
def getpgid():
    '''returns int\n\n
    getpgid(final int pid)\n
    getpgid()\n
    '''
def setpgid():
    '''returns int\n\n
    setpgid(final int pid, final int pgid)\n
    '''
def getpriority():
    '''returns int\n\n
    getpriority(final int which, final int who)\n
    '''
def setpriority():
    '''returns int\n\n
    setpriority(final int which, final int who, final int prio)\n
    '''
def getpid():
    '''returns int\n\n
    getpid()\n
    '''
def getppid():
    '''returns int\n\n
    getppid()\n
    '''
def lchmod():
    '''returns int\n\n
    lchmod(final String filename, final int mode)\n
    '''
def lchown():
    '''returns int\n\n
    lchown(final String filename, final int user, final int group)\n
    '''
def fstat():
    '''returns int\n\n
    fstat(final int fd)\n
    fstat(final FileDescriptor fileDescriptor, final FileStat stat)\n
    '''
def lstat():
    '''returns int\n\n
    lstat(final String path)\n
    lstat(final String path, final FileStat stat)\n
    '''
def stat():
    '''returns int\n\n
    stat(final String path, final FileStat stat)\n
    '''
def findFirstFile():
    '''returns int\n\n
    findFirstFile(final String path, final FileStat stat)\n
    '''
def readlink():
    '''returns String\n\n
    readlink(final String oldpath)\n
    '''
def environ():
    '''returns Pointer\n\n
    environ()\n
    '''
def setenv():
    '''returns int\n\n
    setenv(final String envName, final String envValue, final int overwrite)\n
    '''
def umask():
    '''returns int\n\n
    umask(final int mask)\n
    '''
def unsetenv():
    '''returns int\n\n
    unsetenv(final String envName)\n
    '''
def utimes():
    '''returns int\n\n
    utimes(final String path, final long[] atimeval, final long[] mtimeval)\n
    '''
def wait():
    '''returns int\n\n
    wait(final int[] status)\n
    '''
def waitpid():
    '''returns int\n\n
    waitpid(final int pid, final int[] status, final int flags)\n
    waitpid(final long pid, final int[] status, final int flags)\n
    '''
def getlogin():
    '''returns String\n\n
    getlogin()\n
    '''
def endgrent():
    '''returns int\n\n
    endgrent()\n
    '''
def endpwent():
    '''returns int\n\n
    endpwent()\n
    '''
def getgrent():
    '''returns Group\n\n
    getgrent()\n
    '''
def getpwent():
    '''returns Passwd\n\n
    getpwent()\n
    '''
def getgrgid():
    '''returns Group\n\n
    getgrgid(final int which)\n
    '''
def getpwnam():
    '''returns Passwd\n\n
    getpwnam(final String which)\n
    '''
def getgrnam():
    '''returns Group\n\n
    getgrnam(final String which)\n
    '''
def setgrent():
    '''returns int\n\n
    setgrent()\n
    '''
def setpwent():
    '''returns int\n\n
    setpwent()\n
    '''
def getpwuid():
    '''returns Passwd\n\n
    getpwuid(final int which)\n
    '''
def isatty():
    '''returns int\n\n
    isatty(final FileDescriptor fd)\n
    isatty(final int fd)\n
    '''
def mkdir():
    '''returns int\n\n
    mkdir(final String path, final int mode)\n
    '''
def rmdir():
    '''returns int\n\n
    rmdir(final String path)\n
    '''
def link():
    '''returns int\n\n
    link(final String oldpath, final String newpath)\n
    '''
def aspawn():
    '''returns int\n\n
    aspawn(final boolean overlay, final String program, final String[] argv, final String path, final String[] envp)\n
    '''
def pipe():
    '''returns int\n\n
    pipe(final int[] fds)\n
    '''
def truncate():
    '''returns int\n\n
    truncate(final CharSequence path, final long length)\n
    '''
def fcntlInt():
    '''returns int\n\n
    fcntlInt(final int fd, final Fcntl fcntl, final int arg)\n
    '''
def spawn():
    '''returns int\n\n
    spawn(final boolean overlay, final String command, final String program, final String path, final String[] envp)\n
    '''
def mkfifo():
    '''returns int\n\n
    mkfifo(final String filename, final int mode)\n
    '''
def allocateTimeval():
    '''returns Timeval\n\n
    allocateTimeval()\n
    '''
def gettimeofday():
    '''returns int\n\n
    gettimeofday(final Timeval tv)\n
    '''
def fromNative():
    '''returns Object\n\n
    fromNative(final Object arg, final FromNativeContext ctx)\n
    '''
