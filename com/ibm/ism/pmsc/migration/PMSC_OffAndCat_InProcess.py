COPYRIGHT = "String  \"IBM Confidential OCO Source Material\n5725-E24 (C) COPYRIGHT International Business Machines Corp. 2007, 2017\nThe source code for this program is not published or otherwise divested\nof its trade secrets, irrespective of what has been deposited with the\nU.S. Copyright Office.\""
def ():
    '''returns PMSC_OffAndCat_InProcess\n\n
    ()\n
    '''
def getKeyArray():
    '''returns String[]\n\n
    getKeyArray(final MicSetInfo info)\n
    getKeyArray(final String name)\n
    '''
def checkBusinessRules():
    '''returns int\n\n
    checkBusinessRules(final MboSetRemote mboSet, final String tableName)\n
    '''
def setAdditionalData():
    '''returns None\n\n
    setAdditionalData(final MboSetRemote mboSet, final String tableName)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final MboRemote setMbo, final String stat, final String memo)\n
    '''
def createMboSet():
    '''returns MboSetRemote\n\n
    createMboSet(final boolean primaryMbo, final MboRemote parentMbo, final MosDetailInfo mdi, final String processTable)\n
    '''
