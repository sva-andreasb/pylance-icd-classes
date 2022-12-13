def getInstance():
    '''    public static final IoTServicesCache getInstance()
    '''
def getName():
    '''    public String getName()
    '''
def getAllIoTServices():
    '''    public Map getAllIoTServices()
    '''
def getDefaultHistorian():
    '''    public String getDefaultHistorian()
    '''
def getDefaultHistorianProcessor():
    '''    public String getDefaultHistorianProcessor()
    '''
def getDefaultHistorianEndPoint():
    '''    public String getDefaultHistorianEndPoint()
    '''
def getDefaultHistorianIotServiceName():
    '''    public String getDefaultHistorianIotServiceName()
    '''
def getAllServicesList():
    '''    public List getAllServicesList()
    '''
def getActiveServiceName():
    '''    public String getActiveServiceName()
    '''
def getJsonResourceForActiveService():
    '''    public String getJsonResourceForActiveService()
    '''
def getPayloadPropsForAllServices():
    '''    public Map<String, Map<String, String>> getPayloadPropsForAllServices()
    '''
def getPayloadProps():
    '''    public Map<String, String> getPayloadProps(final String service)
    public Map<String, String> getPayloadProps(final String service, final String usedby)
    '''
def getPayloadPropsUsedBy():
    '''    public IoTPayloadPropsInfo getPayloadPropsUsedBy(final String service, final String property)
    '''
def isServiceActive():
    '''    public boolean isServiceActive(final String servicename)
    '''
def getIoTService():
    '''    public IoTServicesInfo getIoTService(final String servicename)
    '''
def getDeviceTypeInfoForActiveService():
    '''    public Map<String, IoTServiceDeviceTypeInfo> getDeviceTypeInfoForActiveService()
    '''
def getAllEndPointInfo():
    '''    public Map<String, List<IoTRestEndPointsInfo>> getAllEndPointInfo()
    '''
def getEndPointInfo():
    '''    public List<IoTRestEndPointsInfo> getEndPointInfo(final String servicename)
    public IoTRestEndPointsInfo getEndPointInfo(final String servicename, final String usedwith)
    '''
def getEndPointValue():
    '''    public String getEndPointValue(final String servicename, final String usedwith)
    '''
