def startTiming():
'''public static TimingInfo startTiming()
'''
pass
def startTimingFullSupport():
'''public static TimingInfo startTimingFullSupport()
public static TimingInfo startTimingFullSupport(final long startTimeNano)
'''
pass
def newTimingInfoFullSupport():
'''public static TimingInfo newTimingInfoFullSupport(final long startTimeNano, final long endTimeNano)
public static TimingInfo newTimingInfoFullSupport(final long startEpochTimeMilli, final long startTimeNano, final long endTimeNano)
'''
pass
def unmodifiableTimingInfo():
'''public static TimingInfo unmodifiableTimingInfo(final long startTimeNano, final Long endTimeNano)
public static TimingInfo unmodifiableTimingInfo(final long startEpochTimeMilli, final long startTimeNano, final Long endTimeNano)
'''
pass
def getStartTime():
'''public final long getStartTime()
'''
pass
def getStartEpochTimeMilli():
'''public final long getStartEpochTimeMilli()
'''
pass
def getStartEpochTimeMilliIfKnown():
'''public final Long getStartEpochTimeMilliIfKnown()
'''
pass
def getStartTimeNano():
'''public final long getStartTimeNano()
'''
pass
def getEndTime():
'''public final long getEndTime()
'''
pass
def getEndEpochTimeMilli():
'''public final long getEndEpochTimeMilli()
'''
pass
def getEndEpochTimeMilliIfKnown():
'''public final Long getEndEpochTimeMilliIfKnown()
'''
pass
def getEndTimeNano():
'''public final long getEndTimeNano()
'''
pass
def getEndTimeNanoIfKnown():
'''public final Long getEndTimeNanoIfKnown()
'''
pass
def getTimeTakenMillis():
'''public final double getTimeTakenMillis()
'''
pass
def getTimeTakenMillisIfKnown():
'''public final Double getTimeTakenMillisIfKnown()
'''
pass
def durationMilliOf():
'''public static double durationMilliOf(final long startTimeNano, final long endTimeNano)
'''
pass
def getElapsedTimeMillis():
'''public final long getElapsedTimeMillis()
'''
pass
def isEndTimeKnown():
'''public final boolean isEndTimeKnown()
'''
pass
def isStartEpochTimeMilliKnown():
'''public final boolean isStartEpochTimeMilliKnown()
'''
pass
def toString():
'''public final String toString()
'''
pass
def setEndTime():
'''public void setEndTime(final long endTimeMilli)
'''
pass
def setEndTimeNano():
'''public void setEndTimeNano(final long endTimeNano)
'''
pass
def endTiming():
'''public TimingInfo endTiming()
'''
pass
def addSubMeasurement():
'''public void addSubMeasurement(final String subMeasurementName, final TimingInfo timingInfo)
'''
pass
def getSubMeasurement():
'''public TimingInfo getSubMeasurement(final String subMeasurementName)
public TimingInfo getSubMeasurement(final String subMesurementName, final int index)
'''
pass
def getLastSubMeasurement():
'''public TimingInfo getLastSubMeasurement(final String subMeasurementName)
'''
pass
def getAllSubMeasurements():
'''public List<TimingInfo> getAllSubMeasurements(final String subMeasurementName)
'''
pass
def getSubMeasurementsByName():
'''public Map<String, List<TimingInfo>> getSubMeasurementsByName()
'''
pass
def getCounter():
'''public Number getCounter(final String key)
'''
pass
def getAllCounters():
'''public Map<String, Number> getAllCounters()
'''
pass
def setCounter():
'''public void setCounter(final String key, final long count)
'''
pass
def incrementCounter():
'''public void incrementCounter(final String key)
'''
pass
