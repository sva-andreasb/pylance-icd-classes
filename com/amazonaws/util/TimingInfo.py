def setEndTime():
    '''returns None\n\n
    setEndTime(final long endTimeMilli)\n
    '''
def setEndTimeNano():
    '''returns None\n\n
    setEndTimeNano(final long endTimeNano)\n
    '''
def endTiming():
    '''returns TimingInfo\n\n
    endTiming()\n
    '''
def addSubMeasurement():
    '''returns None\n\n
    addSubMeasurement(final String subMeasurementName, final TimingInfo timingInfo)\n
    '''
def getSubMeasurement():
    '''returns TimingInfo\n\n
    getSubMeasurement(final String subMeasurementName)\n
    getSubMeasurement(final String subMesurementName, final int index)\n
    '''
def getLastSubMeasurement():
    '''returns TimingInfo\n\n
    getLastSubMeasurement(final String subMeasurementName)\n
    '''
def getAllSubMeasurements():
    '''returns List<TimingInfo>\n\n
    getAllSubMeasurements(final String subMeasurementName)\n
    '''
def getCounter():
    '''returns Number\n\n
    getCounter(final String key)\n
    '''
def setCounter():
    '''returns None\n\n
    setCounter(final String key, final long count)\n
    '''
def incrementCounter():
    '''returns None\n\n
    incrementCounter(final String key)\n
    '''
