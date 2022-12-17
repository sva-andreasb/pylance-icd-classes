def newProcessMaker():
    '''returns ProcessMaker\n\n
    newProcessMaker(final String... command)\n
    newProcessMaker()\n
    '''
def chmod():
    '''returns int\n\n
    chmod(final String filename, final int mode)\n
    '''
def fchmod():
    '''returns int\n\n
    fchmod(final int fd, final int mode)\n
    '''
def chown():
    '''returns int\n\n
    chown(final String filename, final int user, final int group)\n
    '''
def fchown():
    '''returns int\n\n
    fchown(final int fd, final int user, final int group)\n
    '''
def crypt():
    '''returns byte[]\n\n
    crypt(final CharSequence key, final CharSequence salt)\n
    crypt(final byte[] key, final byte[] salt)\n
    '''
def exec():
    '''returns int\n\n
    exec(final String path, final String... args)\n
    exec(final String path, final String[] args, final String[] envp)\n
    '''
def execv():
    '''returns int\n\n
    execv(final String path, final String[] args)\n
    '''
def execve():
    '''returns int\n\n
    execve(final String path, final String[] args, final String[] env)\n
    '''
def fstat():
    '''returns int\n\n
    fstat(final FileDescriptor fileDescriptor)\n
    fstat(final int fd)\n
    fstat(final FileDescriptor fileDescriptor, final FileStat stat)\n
    fstat(final int fd, final FileStat stat)\n
    '''
def environ():
    '''returns Pointer\n\n
    environ()\n
    '''
def getenv():
    '''returns String\n\n
    getenv(final String envName)\n
    '''
def getegid():
    '''returns int\n\n
    getegid()\n
    '''
def geteuid():
    '''returns int\n\n
    geteuid()\n
    '''
def getgid():
    '''returns int\n\n
    getgid()\n
    '''
def getdtablesize():
    '''returns int\n\n
    getdtablesize()\n
    '''
def getlogin():
    '''returns String\n\n
    getlogin()\n
    '''
def getpgid():
    '''returns int\n\n
    getpgid()\n
    getpgid(final int pid)\n
    '''
def getpgrp():
    '''returns int\n\n
    getpgrp()\n
    '''
def getpid():
    '''returns int\n\n
    getpid()\n
    '''
def getppid():
    '''returns int\n\n
    getppid()\n
    '''
def getpwent():
    '''returns Passwd\n\n
    getpwent()\n
    '''
def getpwuid():
    '''returns Passwd\n\n
    getpwuid(final int which)\n
    '''
def getpwnam():
    '''returns Passwd\n\n
    getpwnam(final String which)\n
    '''
def getgrent():
    '''returns Group\n\n
    getgrent()\n
    '''
def getgrgid():
    '''returns Group\n\n
    getgrgid(final int which)\n
    '''
def getgrnam():
    '''returns Group\n\n
    getgrnam(final String which)\n
    '''
def setpwent():
    '''returns int\n\n
    setpwent()\n
    '''
def endpwent():
    '''returns int\n\n
    endpwent()\n
    '''
def setgrent():
    '''returns int\n\n
    setgrent()\n
    '''
def endgrent():
    '''returns int\n\n
    endgrent()\n
    '''
def getuid():
    '''returns int\n\n
    getuid()\n
    '''
def getrlimit():
    '''returns RLimit\n\n
    getrlimit(final int resource, final RLimit rlim)\n
    getrlimit(final int resource, final Pointer rlim)\n
    getrlimit(final int resource)\n
    '''
def setrlimit():
    '''returns int\n\n
    setrlimit(final int resource, final RLimit rlim)\n
    setrlimit(final int resource, final Pointer rlim)\n
    setrlimit(final int resource, final long rlimCur, final long rlimMax)\n
    '''
def setegid():
    '''returns int\n\n
    setegid(final int egid)\n
    '''
def seteuid():
    '''returns int\n\n
    seteuid(final int euid)\n
    '''
def setgid():
    '''returns int\n\n
    setgid(final int gid)\n
    '''
def getfd():
    '''returns int\n\n
    getfd(final FileDescriptor descriptor)\n
    '''
def setpgid():
    '''returns int\n\n
    setpgid(final int pid, final int pgid)\n
    '''
def setpgrp():
    '''returns int\n\n
    setpgrp(final int pid, final int pgrp)\n
    '''
def setsid():
    '''returns int\n\n
    setsid()\n
    '''
def setuid():
    '''returns int\n\n
    setuid(final int uid)\n
    '''
def kill():
    '''returns int\n\n
    kill(final int pid, final int signal)\n
    kill(final long pid, final int signal)\n
    '''
def signal():
    '''returns None\n\n
    signal(final Signal sig, final SignalHandler handler)\n
    signal(final int sig)\n
    '''
def lchmod():
    '''returns int\n\n
    lchmod(final String filename, final int mode)\n
    '''
def lchown():
    '''returns int\n\n
    lchown(final String filename, final int user, final int group)\n
    '''
def link():
    '''returns int\n\n
    link(final String oldpath, final String newpath)\n
    '''
def lstat():
    '''returns int\n\n
    lstat(final String path)\n
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
def setenv():
    '''returns int\n\n
    setenv(final String envName, final String envValue, final int overwrite)\n
    '''
def stat():
    '''returns int\n\n
    stat(final String path)\n
    stat(final String path, final FileStat stat)\n
    '''
def symlink():
    '''returns int\n\n
    symlink(final String oldpath, final String newpath)\n
    '''
def readlink():
    '''returns int\n\n
    readlink(final String oldpath)\n
    readlink(final CharSequence path, final byte[] buf, final int bufsize)\n
    readlink(final CharSequence path, final ByteBuffer buf, final int bufsize)\n
    readlink(final CharSequence path, final Pointer bufPtr, final int bufsize)\n
    '''
def unsetenv():
    '''returns int\n\n
    unsetenv(final String envName)\n
    '''
def umask():
    '''returns int\n\n
    umask(final int mask)\n
    '''
def utimes():
    '''returns int\n\n
    utimes(final String path, final long[] atimeval, final long[] mtimeval)\n
    utimes(final String path, final Pointer times)\n
    '''
def futimes():
    '''returns int\n\n
    futimes(final int fd, final long[] atimeval, final long[] mtimeval)\n
    '''
def lutimes():
    '''returns int\n\n
    lutimes(final String path, final long[] atimeval, final long[] mtimeval)\n
    '''
def fork():
    '''returns int\n\n
    fork()\n
    '''
def waitpid():
    '''returns int\n\n
    waitpid(final int pid, final int[] status, final int flags)\n
    waitpid(final long pid, final int[] status, final int flags)\n
    '''
def wait():
    '''returns int\n\n
    wait(final int[] status)\n
    '''
def getpriority():
    '''returns int\n\n
    getpriority(final int which, final int who)\n
    '''
def setpriority():
    '''returns int\n\n
    setpriority(final int which, final int who, final int prio)\n
    '''
def isatty():
    '''returns int\n\n
    isatty(final FileDescriptor fd)\n
    isatty(final int fd)\n
    '''
def errno():
    '''returns None\n\n
    errno()\n
    errno(final int value)\n
    '''
def chdir():
    '''returns int\n\n
    chdir(final String path)\n
    '''
def isNative():
    '''returns boolean\n\n
    isNative()\n
    '''
def posix_spawnp():
    '''returns long\n\n
    posix_spawnp(final String path, final Collection<? extends SpawnFileAction> fileActions, final CharSequence[] argv, final CharSequence[] envp)\n
    posix_spawnp(final String path, final Collection<? extends SpawnFileAction> fileActions, final Collection<? extends CharSequence> argv, final Collection<? extends CharSequence> envp)\n
    posix_spawnp(final String path, final Collection<? extends SpawnFileAction> fileActions, final Collection<? extends SpawnAttribute> spawnAttributes, final Collection<? extends CharSequence> argv, final Collection<? extends CharSequence> envp)\n
    posix_spawnp(final String path, final Collection<? extends SpawnFileAction> fileActions, final Collection<? extends SpawnAttribute> spawnAttributes, final CharSequence[] argv, final CharSequence[] envp)\n
    '''
def flock():
    '''returns int\n\n
    flock(final int fd, final int mode)\n
    '''
def dup():
    '''returns int\n\n
    dup(final int fd)\n
    '''
def dup2():
    '''returns int\n\n
    dup2(final int oldFd, final int newFd)\n
    '''
def fcntlInt():
    '''returns int\n\n
    fcntlInt(final int fd, final Fcntl fcntl, final int arg)\n
    '''
def fcntl():
    '''returns int\n\n
    fcntl(final int fd, final Fcntl fcntl)\n
    fcntl(final int fd, final Fcntl fcntl, final int... arg)\n
    '''
def access():
    '''returns int\n\n
    access(final CharSequence path, final int amode)\n
    '''
def close():
    '''returns int\n\n
    close(final int fd)\n
    '''
def sysconf():
    '''returns long\n\n
    sysconf(final Sysconf name)\n
    '''
def times():
    '''returns Times\n\n
    times()\n
    '''
def unlink():
    '''returns int\n\n
    unlink(final CharSequence path)\n
    '''
def open():
    '''returns int\n\n
    open(final CharSequence path, final int flags, final int perm)\n
    '''
def read():
    '''returns int\n\n
    read(final int fd, final byte[] buf, final long n)\n
    read(final int fd, final ByteBuffer buf, final long n)\n
    read(final int fd, final byte[] buf, final int n)\n
    read(final int fd, final ByteBuffer buf, final int n)\n
    '''
def write():
    '''returns int\n\n
    write(final int fd, final byte[] buf, final long n)\n
    write(final int fd, final ByteBuffer buf, final long n)\n
    write(final int fd, final byte[] buf, final int n)\n
    write(final int fd, final ByteBuffer buf, final int n)\n
    '''
def pread():
    '''returns int\n\n
    pread(final int fd, final byte[] buf, final long n, final long offset)\n
    pread(final int fd, final ByteBuffer buf, final long n, final long offset)\n
    pread(final int fd, final byte[] buf, final int n, final int offset)\n
    pread(final int fd, final ByteBuffer buf, final int n, final int offset)\n
    '''
def pwrite():
    '''returns int\n\n
    pwrite(final int fd, final byte[] buf, final long n, final long offset)\n
    pwrite(final int fd, final ByteBuffer buf, final long n, final long offset)\n
    pwrite(final int fd, final byte[] buf, final int n, final int offset)\n
    pwrite(final int fd, final ByteBuffer buf, final int n, final int offset)\n
    '''
def lseek():
    '''returns int\n\n
    lseek(final int fd, final long offset, final int whence)\n
    '''
def lseekLong():
    '''returns long\n\n
    lseekLong(final int fd, final long offset, final int whence)\n
    '''
def pipe():
    '''returns int\n\n
    pipe(final int[] fds)\n
    '''
def socketpair():
    '''returns int\n\n
    socketpair(final int domain, final int type, final int protocol, final int[] fds)\n
    '''
def sendmsg():
    '''returns int\n\n
    sendmsg(final int socket, final MsgHdr message, final int flags)\n
    '''
def recvmsg():
    '''returns int\n\n
    recvmsg(final int socket, final MsgHdr message, final int flags)\n
    '''
def truncate():
    '''returns int\n\n
    truncate(final CharSequence path, final long length)\n
    '''
def ftruncate():
    '''returns int\n\n
    ftruncate(final int fd, final long offset)\n
    '''
def rename():
    '''returns int\n\n
    rename(final CharSequence oldName, final CharSequence newName)\n
    '''
def getcwd():
    '''returns String\n\n
    getcwd()\n
    '''
def fsync():
    '''returns int\n\n
    fsync(final int fd)\n
    '''
def fdatasync():
    '''returns int\n\n
    fdatasync(final int fd)\n
    '''
def mkfifo():
    '''returns int\n\n
    mkfifo(final String filename, final int mode)\n
    '''
def daemon():
    '''returns int\n\n
    daemon(final int nochdir, final int noclose)\n
    '''
def getgroups():
    '''returns int\n\n
    getgroups()\n
    getgroups(final int size, final int[] groups)\n
    '''
def nl_langinfo():
    '''returns String\n\n
    nl_langinfo(final int item)\n
    '''
def setlocale():
    '''returns String\n\n
    setlocale(final int category, final String locale)\n
    '''
def strerror():
    '''returns String\n\n
    strerror(final int code)\n
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
def toNative():
    '''returns Pointer\n\n
    toNative(final FileStat value, final ToNativeContext context)\n
    toNative(final NativeTimes value, final ToNativeContext context)\n
    toNative(final Constant value, final ToNativeContext context)\n
    toNative(final MsgHdr value, final ToNativeContext context)\n
    '''
def nativeType():
    '''returns Class\n\n
    nativeType()\n
    nativeType()\n
    nativeType()\n
    nativeType()\n
    nativeType()\n
    '''
