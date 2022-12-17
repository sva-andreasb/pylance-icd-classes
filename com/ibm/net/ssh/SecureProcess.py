SIG_ABRT = "String  \"ABRT\""
SIG_ALRM = "String  \"ALRM\""
SIG_FPE = "String  \"FPE\""
SIG_HUP = "String  \"HUP\""
SIG_ILL = "String  \"ILL\""
SIG_INT = "String  \"INT\""
SIG_KILL = "String  \"KILL\""
SIG_PIPE = "String  \"PIPE\""
SIG_QUIT = "String  \"QUIT\""
SIG_SEGV = "String  \"SEGV\""
SIG_TERM = "String  \"TERM\""
SIG_USR1 = "String  \"USR1\""
SIG_USR2 = "String  \"USR2\""
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
    '''
def signal():
    '''returns None\n\n
    signal(final String signalName)\n
    '''
def waitFor():
    '''returns int\n\n
    waitFor()\n
    '''
def getStandardOutput():
    '''returns String\n\n
    getStandardOutput()\n
    '''
def getStandardError():
    '''returns String\n\n
    getStandardError()\n
    '''
def getExitStatus():
    '''returns int\n\n
    getExitStatus()\n
    '''
def getExitSignal():
    '''returns String\n\n
    getExitSignal()\n
    '''
def didExitSignalDumpCore():
    '''returns boolean\n\n
    didExitSignalDumpCore()\n
    '''
def getExitSignalErrorMessage():
    '''returns String\n\n
    getExitSignalErrorMessage()\n
    '''
