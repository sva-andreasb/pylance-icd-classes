DEFAULT_INITIAL_INTERVAL_MILLIS = "int  500"
DEFAULT_RANDOMIZATION_FACTOR = "double  0.5"
DEFAULT_MULTIPLIER = "double  1.5"
DEFAULT_MAX_INTERVAL_MILLIS = "int  60000"
DEFAULT_MAX_ELAPSED_TIME_MILLIS = "int  900000"
def ():
    '''returns ExponentialBackOffPolicy\n\n
    ()\n
    '''
def isBackOffRequired():
    '''returns boolean\n\n
    isBackOffRequired(final int statusCode)\n
    '''
def getNextBackOffMillis():
    '''returns long\n\n
    getNextBackOffMillis()\n
    '''
def build():
    '''returns ExponentialBackOffPolicy\n\n
    build()\n
    '''
def setInitialIntervalMillis():
    '''returns Builder\n\n
    setInitialIntervalMillis(final int initialIntervalMillis)\n
    '''
def setRandomizationFactor():
    '''returns Builder\n\n
    setRandomizationFactor(final double randomizationFactor)\n
    '''
def setMultiplier():
    '''returns Builder\n\n
    setMultiplier(final double multiplier)\n
    '''
def setMaxIntervalMillis():
    '''returns Builder\n\n
    setMaxIntervalMillis(final int maxIntervalMillis)\n
    '''
def setMaxElapsedTimeMillis():
    '''returns Builder\n\n
    setMaxElapsedTimeMillis(final int maxElapsedTimeMillis)\n
    '''
def setNanoClock():
    '''returns Builder\n\n
    setNanoClock(final NanoClock nanoClock)\n
    '''
