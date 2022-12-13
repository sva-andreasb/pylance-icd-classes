def getInstance():
'''public static final IoTServicesCache getInstance()
'''
pass
def getName():
'''public String getName()
'''
pass
def getAllIoTServices():
'''public Map getAllIoTServices()
'''
pass
def getDefaultHistorian():
'''public String getDefaultHistorian()
'''
pass
def getDefaultHistorianProcessor():
'''public String getDefaultHistorianProcessor()
'''
pass
def getDefaultHistorianEndPoint():
'''public String getDefaultHistorianEndPoint()
'''
pass
def getDefaultHistorianIotServiceName():
'''public String getDefaultHistorianIotServiceName()
'''
pass
def getAllServicesList():
'''public List getAllServicesList()
'''
pass
def getActiveServiceName():
'''public String getActiveServiceName()
'''
pass
def getJsonResourceForActiveService():
'''public String getJsonResourceForActiveService()
'''
pass
def getPayloadPropsForAllServices():
'''public Map<String, Map<String, String>> getPayloadPropsForAllServices()
'''
pass
def getPayloadProps():
'''public Map<String, String> getPayloadProps(final String service)
public Map<String, String> getPayloadProps(final String service, final String usedby)
'''
pass
def getPayloadPropsUsedBy():
'''public IoTPayloadPropsInfo getPayloadPropsUsedBy(final String service, final String property)
'''
pass
def isServiceActive():
'''public boolean isServiceActive(final String servicename)
'''
pass
def getIoTService():
'''public IoTServicesInfo getIoTService(final String servicename)
'''
pass
def getDeviceTypeInfoForActiveService():
'''public Map<String, IoTServiceDeviceTypeInfo> getDeviceTypeInfoForActiveService()
'''
pass
def getAllEndPointInfo():
'''public Map<String, List<IoTRestEndPointsInfo>> getAllEndPointInfo()
'''
pass
def getEndPointInfo():
'''public List<IoTRestEndPointsInfo> getEndPointInfo(final String servicename)
public IoTRestEndPointsInfo getEndPointInfo(final String servicename, final String usedwith)
'''
pass
def getEndPointValue():
'''public String getEndPointValue(final String servicename, final String usedwith)
'''
pass
