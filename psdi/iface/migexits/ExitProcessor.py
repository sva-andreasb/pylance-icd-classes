ERP_EXIT = "int  1"
USER_EXIT = "int  2"
PREPROC_EXIT = "int  3"
def ExitProcessor():
    '''    public ExitProcessor()
    '''
def processExitsOutForInProcess():
    '''    public byte[] processExitsOutForInProcess(final EnterpriseServiceInfo serviceInfo, final String extSystem, final byte[] pubXmlData, final MXTransaction mxTx, final List<MboRemote> usedMboList, final UserInfo userInfo)
    '''
def processExitsOut():
    '''    public byte[] processExitsOut(final InvokeInfo invkInfo, final byte[] xmlData, final MXTransaction mxTx, final List<MboRemote> usedMboList, final UserInfo userInfo)
    '''
def processExitsAndRulesOut():
    '''    public Map<String, ExternalDataInfo> processExitsAndRulesOut(final PublishInfo pubInfo, final String forExtSystem, final byte[] pubXmlData, final boolean isEvent, final MXTransaction mxTx, final List<MboRemote> usedMboList, final UserInfo userInfo)
    '''
def getExitHandle():
    '''    public static Object getExitHandle(final String exitClassName, final int type)
    '''
def mapData():
    '''    public byte[] mapData(final byte[] inXML, final String mapName, final Map params)
    public StructureData mapData(final StructureData inData, final String mapName, final Map params)
    '''
def processExitsIn():
    '''    public StructureData processExitsIn(final EnterpriseServiceInfo inInfo, final UserInfo userInfo, final String extSystem, final byte[] erData, final MXTransaction mxTrans)
    public StructureData processExitsIn(final EnterpriseServiceInfo inInfo, final UserInfo userInfo, final String extSystem, final StructureData exitInputData, final MXTransaction mxTrans)
    public StructureData processExitsIn(final InvokeInfo invkInfo, final byte[] xmlData, final MXTransaction mxTx, final UserInfo userInfo)
    '''
