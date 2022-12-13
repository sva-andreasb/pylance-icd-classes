def startTiming():
    '''public static TimingInfo startTiming()
    '''
def startTimingFullSupport():
    '''public static TimingInfo startTimingFullSupport()
    public static TimingInfo startTimingFullSupport(final long startTimeNano)
    '''
def newTimingInfoFullSupport():
    '''public static TimingInfo newTimingInfoFullSupport(final long startTimeNano, final long endTimeNano)
    public static TimingInfo newTimingInfoFullSupport(final long startEpochTimeMilli, final long startTimeNano, final long endTimeNano)
    '''
def unmodifiableTimingInfo():
    '''public static TimingInfo unmodifiableTimingInfo(final long startTimeNano, final Long endTimeNano)
    public static TimingInfo unmodifiableTimingInfo(final long startEpochTimeMilli, final long startTimeNano, final Long endTimeNano)
    '''
def getStartTime():
    '''public final long getStartTime()
    '''
def getStartEpochTimeMilli():
    '''public final long getStartEpochTimeMilli()
    '''
def getStartEpochTimeMilliIfKnown():
    '''public final Long getStartEpochTimeMilliIfKnown()
    '''
def getStartTimeNano():
    '''public final long getStartTimeNano()
    '''
def getEndTime():
    '''public final long getEndTime()
    '''
def getEndEpochTimeMilli():
    '''public final long getEndEpochTimeMilli()
    '''
def getEndEpochTimeMilliIfKnown():
    '''public final Long getEndEpochTimeMilliIfKnown()
    '''
def getEndTimeNano():
    '''public final long getEndTimeNano()
    '''
def getEndTimeNanoIfKnown():
    '''public final Long getEndTimeNanoIfKnown()
    '''
def getTimeTakenMillis():
    '''public final double getTimeTakenMillis()
    '''
def getTimeTakenMillisIfKnown():
    '''public final Double getTimeTakenMillisIfKnown()
    '''
def durationMilliOf():
    '''public static double durationMilliOf(final long startTimeNano, final long endTimeNano)
    '''
def getElapsedTimeMillis():
    '''public final long getElapsedTimeMillis()
    '''
def isEndTimeKnown():
    '''public final boolean isEndTimeKnown()
    '''
def isStartEpochTimeMilliKnown():
    '''public final boolean isStartEpochTimeMilliKnown()
    '''
def toString():
    '''public final String toString()
    '''
def setEndTime():
    '''public void setEndTime(final long endTimeMilli)
    '''
def setEndTimeNano():
    '''public void setEndTimeNano(final long endTimeNano)
    '''
def endTiming():
    '''public TimingInfo endTiming()
    '''
def addSubMeasurement():
    '''public void addSubMeasurement(final String subMeasurementName, final TimingInfo timingInfo)
    '''
def getSubMeasurement():
    '''public TimingInfo getSubMeasurement(final String subMeasurementName)
    public TimingInfo getSubMeasurement(final String subMesurementName, final int index)
    '''
def getLastSubMeasurement():
    '''public TimingInfo getLastSubMeasurement(final String subMeasurementName)
    '''
def getAllSubMeasurements():
    '''public List<TimingInfo> getAllSubMeasurements(final String subMeasurementName)
    '''
def getSubMeasurementsByName():
    '''public Map<String, List<TimingInfo>> getSubMeasurementsByName()
    '''
def getCounter():
    '''public Number getCounter(final String key)
    '''
def getAllCounters():
    '''public Map<String, Number> getAllCounters()
    '''
def setCounter():
    '''public void setCounter(final String key, final long count)
    '''
def incrementCounter():
    '''public void incrementCounter(final String key)
    '''
