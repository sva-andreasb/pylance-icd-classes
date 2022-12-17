ERP_EXIT = "int  1"
USER_EXIT = "int  2"
PREPROC_EXIT = "int  3"
def ():
    '''returns ExitProcessor\n\n
    ()\n
    '''
def processExitsOutForInProcess():
    '''returns byte[]\n\n
    processExitsOutForInProcess(final EnterpriseServiceInfo serviceInfo, final String extSystem, final byte[] pubXmlData, final MXTransaction mxTx, final List<MboRemote> usedMboList, final UserInfo userInfo)\n
    '''
def processExitsOut():
    '''returns byte[]\n\n
    processExitsOut(final InvokeInfo invkInfo, final byte[] xmlData, final MXTransaction mxTx, final List<MboRemote> usedMboList, final UserInfo userInfo)\n
    '''
def mapData():
    '''returns StructureData\n\n
    mapData(final byte[] inXML, final String mapName, final Map params)\n
    mapData(final StructureData inData, final String mapName, final Map params)\n
    '''
def processExitsIn():
    '''returns StructureData\n\n
    processExitsIn(final EnterpriseServiceInfo inInfo, final UserInfo userInfo, final String extSystem, final byte[] erData, final MXTransaction mxTrans)\n
    processExitsIn(final EnterpriseServiceInfo inInfo, final UserInfo userInfo, final String extSystem, final StructureData exitInputData, final MXTransaction mxTrans)\n
    processExitsIn(final InvokeInfo invkInfo, final byte[] xmlData, final MXTransaction mxTx, final UserInfo userInfo)\n
    '''
