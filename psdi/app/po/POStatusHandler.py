def POStatusHandler():
    '''public POStatusHandler(final StatefulMbo sm)
    '''
def canChangeStatus():
    '''public void canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)
    '''
def checkStatusChangeAuthorization():
    '''public void checkStatusChangeAuthorization(final String desiredExternalStatus)
    '''
def getOptionName():
    '''public static String getOptionName(final String status)
    '''
def changeStatus():
    '''public void changeStatus(final String currentStatus, final String desiredStatus, final Date date, final String memo)
    '''
def approve():
    '''public void approve(final Date date)
    '''
def updateMboForStatus():
    '''public void updateMboForStatus(final String status)
    '''
def revise():
    '''public void revise()
    '''
def hold():
    '''public void hold()
    '''
def pndrev():
    '''public void pndrev()
    '''
def canPndRev():
    '''public void canPndRev(final String currentMaxStatus)
    '''
def canRevise():
    '''public void canRevise(final String currentMaxStatus)
    '''
def canHold():
    '''public void canHold(final String currentMaxStatus)
    '''
def isPOFromPR():
    '''public boolean isPOFromPR()
    '''
def isPOFromRFQ():
    '''public boolean isPOFromRFQ()
    '''
def updatePRPRLine():
    '''public void updatePRPRLine()
    '''
def updateRFQRFQLine():
    '''public void updateRFQRFQLine()
    '''
def checkPndRevLines():
    '''public void checkPndRevLines(final MboRemote poRemote, final MboSetRemote poLines)
    '''
def updatePndRevLines():
    '''public void updatePndRevLines(final MboRemote poRemote, final MboSetRemote poLines)
    '''
def samePOlineOnTwoVersions():
    '''public boolean samePOlineOnTwoVersions(final MboRemote prLineRemote)
    '''
