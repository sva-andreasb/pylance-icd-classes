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
    '''public OutputStream getOutputStream()
    '''
def getInputStream():
    '''public InputStream getInputStream()
    '''
def getErrorStream():
    '''public InputStream getErrorStream()
    '''
def close():
    '''public void close()
    '''
def signal():
    '''public void signal(final String signalName)
    '''
def waitFor():
    '''public int waitFor()
    '''
def getStandardOutput():
    '''public String getStandardOutput()
    '''
def getStandardError():
    '''public String getStandardError()
    '''
def getExitStatus():
    '''public int getExitStatus()
    '''
def getExitSignal():
    '''public String getExitSignal()
    '''
def didExitSignalDumpCore():
    '''public boolean didExitSignalDumpCore()
    '''
def getExitSignalErrorMessage():
    '''public String getExitSignalErrorMessage()
    '''
