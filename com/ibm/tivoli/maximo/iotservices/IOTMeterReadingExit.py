def ():
    '''returns IOTMeterReadingExit\n\n
    ()\n
    '''
def setDataIn():
    '''returns StructureData\n\n
    setDataIn(final StructureData erData)\n
    '''
def mapMeterReadings():
    '''returns StructureData\n\n
    mapMeterReadings(final JSONObject jo, final String deviceId, final Date readingDate, final IoTServiceDeviceTypeInfo deviceTypeInfo, final boolean historianMapping, final String meterName, final String processorClassName)\n
    '''
def mapRTIData():
    '''returns StructureData\n\n
    mapRTIData(final JSONObject jo, final String deviceId, final Date readingDate, final IoTServiceDeviceTypeInfo deviceTypeInfo)\n
    '''
def mapHistorianData():
    '''returns StructureData\n\n
    mapHistorianData(final JSONObject jo, final String deviceId, final Date readingDate, final IoTServiceDeviceTypeInfo deviceTypeInfo, final String meterName, final String processorClassName)\n
    '''
def setReadingsForRTIData():
    '''returns None\n\n
    setReadingsForRTIData(final JSONObject jo, final MboSetRemote set, final StructureData irData, final IoTServiceDeviceTypeInfo deviceTypeInfo)\n
    '''
def setReadingsForHistorianData():
    '''returns None\n\n
    setReadingsForHistorianData(final JSONObject jo, final StructureData irData, final Object feedData, final IoTMeterToPayloadMappingInfo mappingInfo, final Date readingDate)\n
    '''
