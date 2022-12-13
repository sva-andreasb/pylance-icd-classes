def IOTMeterReadingExit():
    '''    public IOTMeterReadingExit()
    '''
def setDataIn():
    '''    public StructureData setDataIn(final StructureData erData)
    '''
def mapMeterReadings():
    '''    public StructureData mapMeterReadings(final JSONObject jo, final String deviceId, final Date readingDate, final IoTServiceDeviceTypeInfo deviceTypeInfo, final boolean historianMapping, final String meterName, final String processorClassName)
    '''
def mapRTIData():
    '''    public StructureData mapRTIData(final JSONObject jo, final String deviceId, final Date readingDate, final IoTServiceDeviceTypeInfo deviceTypeInfo)
    '''
def mapHistorianData():
    '''    public StructureData mapHistorianData(final JSONObject jo, final String deviceId, final Date readingDate, final IoTServiceDeviceTypeInfo deviceTypeInfo, final String meterName, final String processorClassName)
    '''
def setReadingsForRTIData():
    '''    public void setReadingsForRTIData(final JSONObject jo, final MboSetRemote set, final StructureData irData, final IoTServiceDeviceTypeInfo deviceTypeInfo)
    '''
def setReadingsForHistorianData():
    '''    public void setReadingsForHistorianData(final JSONObject jo, final StructureData irData, final Object feedData, final IoTMeterToPayloadMappingInfo mappingInfo, final Date readingDate)
    '''
