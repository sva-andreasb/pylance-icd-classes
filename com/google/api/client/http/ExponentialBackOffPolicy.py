DEFAULT_INITIAL_INTERVAL_MILLIS = "int  500"
DEFAULT_RANDOMIZATION_FACTOR = "double  0.5"
DEFAULT_MULTIPLIER = "double  1.5"
DEFAULT_MAX_INTERVAL_MILLIS = "int  60000"
DEFAULT_MAX_ELAPSED_TIME_MILLIS = "int  900000"
def ExponentialBackOffPolicy():
'''public ExponentialBackOffPolicy()
'''
pass
def isBackOffRequired():
'''public boolean isBackOffRequired(final int statusCode)
'''
pass
def reset():
'''public final void reset()
'''
pass
def getNextBackOffMillis():
'''public long getNextBackOffMillis()
'''
pass
def getInitialIntervalMillis():
'''public final int getInitialIntervalMillis()
public final int getInitialIntervalMillis()
'''
pass
def getRandomizationFactor():
'''public final double getRandomizationFactor()
public final double getRandomizationFactor()
'''
pass
def getCurrentIntervalMillis():
'''public final int getCurrentIntervalMillis()
'''
pass
def getMultiplier():
'''public final double getMultiplier()
public final double getMultiplier()
'''
pass
def getMaxIntervalMillis():
'''public final int getMaxIntervalMillis()
public final int getMaxIntervalMillis()
'''
pass
def getMaxElapsedTimeMillis():
'''public final int getMaxElapsedTimeMillis()
public final int getMaxElapsedTimeMillis()
'''
pass
def getElapsedTimeMillis():
'''public final long getElapsedTimeMillis()
'''
pass
def builder():
'''public static Builder builder()
'''
pass
def build():
'''public ExponentialBackOffPolicy build()
'''
pass
def setInitialIntervalMillis():
'''public Builder setInitialIntervalMillis(final int initialIntervalMillis)
'''
pass
def setRandomizationFactor():
'''public Builder setRandomizationFactor(final double randomizationFactor)
'''
pass
def setMultiplier():
'''public Builder setMultiplier(final double multiplier)
'''
pass
def setMaxIntervalMillis():
'''public Builder setMaxIntervalMillis(final int maxIntervalMillis)
'''
pass
def setMaxElapsedTimeMillis():
'''public Builder setMaxElapsedTimeMillis(final int maxElapsedTimeMillis)
'''
pass
def getNanoClock():
'''public final NanoClock getNanoClock()
'''
pass
def setNanoClock():
'''public Builder setNanoClock(final NanoClock nanoClock)
'''
pass
