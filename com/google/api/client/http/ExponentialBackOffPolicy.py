DEFAULT_INITIAL_INTERVAL_MILLIS = "int  500"
DEFAULT_RANDOMIZATION_FACTOR = "double  0.5"
DEFAULT_MULTIPLIER = "double  1.5"
DEFAULT_MAX_INTERVAL_MILLIS = "int  60000"
DEFAULT_MAX_ELAPSED_TIME_MILLIS = "int  900000"
def ExponentialBackOffPolicy():
    '''    public ExponentialBackOffPolicy()
    '''
def isBackOffRequired():
    '''    public boolean isBackOffRequired(final int statusCode)
    '''
def reset():
    '''    public final void reset()
    '''
def getNextBackOffMillis():
    '''    public long getNextBackOffMillis()
    '''
def getInitialIntervalMillis():
    '''    public final int getInitialIntervalMillis()
    public final int getInitialIntervalMillis()
    '''
def getRandomizationFactor():
    '''    public final double getRandomizationFactor()
    public final double getRandomizationFactor()
    '''
def getCurrentIntervalMillis():
    '''    public final int getCurrentIntervalMillis()
    '''
def getMultiplier():
    '''    public final double getMultiplier()
    public final double getMultiplier()
    '''
def getMaxIntervalMillis():
    '''    public final int getMaxIntervalMillis()
    public final int getMaxIntervalMillis()
    '''
def getMaxElapsedTimeMillis():
    '''    public final int getMaxElapsedTimeMillis()
    public final int getMaxElapsedTimeMillis()
    '''
def getElapsedTimeMillis():
    '''    public final long getElapsedTimeMillis()
    '''
def builder():
    '''    public static Builder builder()
    '''
def build():
    '''    public ExponentialBackOffPolicy build()
    '''
def setInitialIntervalMillis():
    '''    public Builder setInitialIntervalMillis(final int initialIntervalMillis)
    '''
def setRandomizationFactor():
    '''    public Builder setRandomizationFactor(final double randomizationFactor)
    '''
def setMultiplier():
    '''    public Builder setMultiplier(final double multiplier)
    '''
def setMaxIntervalMillis():
    '''    public Builder setMaxIntervalMillis(final int maxIntervalMillis)
    '''
def setMaxElapsedTimeMillis():
    '''    public Builder setMaxElapsedTimeMillis(final int maxElapsedTimeMillis)
    '''
def getNanoClock():
    '''    public final NanoClock getNanoClock()
    '''
def setNanoClock():
    '''    public Builder setNanoClock(final NanoClock nanoClock)
    '''
