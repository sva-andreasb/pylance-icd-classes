WSDL_PORT_NAME = "String  \"wsdl.portName\""
def getId():
    '''    public static boolean getId(final String configId, final SOAPMessageContext context, final JAXRPCEntryInfo entryInfo)
    '''
def serialize():
    '''    public static byte[] serialize(final Object message)
    '''
def deserialize():
    '''    public static Object deserialize(final byte[] array)
    '''
def getValue():
    '''    public static Object getValue(final JAXRPCEntryInfo entryInfo)
    '''
def setValue():
    '''    public static void setValue(final JAXRPCEntryInfo entryInfo, final Object resp)
    '''
def returnToEntryInfoPool():
    '''    public static void returnToEntryInfoPool(final JAXRPCEntryInfo entryInfo)
    '''
def getFromEntryInfoPool():
    '''    public static JAXRPCEntryInfo getFromEntryInfoPool()
    '''
def JAXRPCEntryInfoObjectPool():
    '''    public JAXRPCEntryInfoObjectPool(final int size)
    '''
def createObject():
    '''    public Object createObject()
    '''
