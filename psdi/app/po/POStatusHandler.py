def POStatusHandler():
'''public POStatusHandler(final StatefulMbo sm)
'''
pass
def canChangeStatus():
'''public void canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)
'''
pass
def checkStatusChangeAuthorization():
'''public void checkStatusChangeAuthorization(final String desiredExternalStatus)
'''
pass
def getOptionName():
'''public static String getOptionName(final String status)
'''
pass
def changeStatus():
'''public void changeStatus(final String currentStatus, final String desiredStatus, final Date date, final String memo)
'''
pass
def approve():
'''public void approve(final Date date)
'''
pass
def updateMboForStatus():
'''public void updateMboForStatus(final String status)
'''
pass
def revise():
'''public void revise()
'''
pass
def hold():
'''public void hold()
'''
pass
def pndrev():
'''public void pndrev()
'''
pass
def canPndRev():
'''public void canPndRev(final String currentMaxStatus)
'''
pass
def canRevise():
'''public void canRevise(final String currentMaxStatus)
'''
pass
def canHold():
'''public void canHold(final String currentMaxStatus)
'''
pass
def isPOFromPR():
'''public boolean isPOFromPR()
'''
pass
def isPOFromRFQ():
'''public boolean isPOFromRFQ()
'''
pass
def updatePRPRLine():
'''public void updatePRPRLine()
'''
pass
def updateRFQRFQLine():
'''public void updateRFQRFQLine()
'''
pass
def checkPndRevLines():
'''public void checkPndRevLines(final MboRemote poRemote, final MboSetRemote poLines)
'''
pass
def updatePndRevLines():
'''public void updatePndRevLines(final MboRemote poRemote, final MboSetRemote poLines)
'''
pass
def samePOlineOnTwoVersions():
'''public boolean samePOlineOnTwoVersions(final MboRemote prLineRemote)
'''
pass
