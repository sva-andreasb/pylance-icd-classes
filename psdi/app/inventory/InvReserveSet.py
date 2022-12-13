def InvReserveSet():
'''public InvReserveSet(final MboServerInterface ms)
'''
pass
def addWorkOrderReservation():
'''public InvReserveRemote addWorkOrderReservation(final MboRemote wpm, final boolean createInit, final Date requestDate, final Date requiredDate)
public InvReserveRemote addWorkOrderReservation(final String wonum, final String itemnum, final String itemsetid, final String location, final String storelocsite, final String glaccount, final String description, final boolean directreq, final boolean initFlag, final String requestedBy, final Date requestDate, final Date requiredDate, final double qty, final double issueqty)
public InvReserveRemote addWorkOrderReservation(final String wonum, final String itemnum, final String itemsetid, final String location, final String storelocsite, final String glaccount, final String description, final boolean directreq, final boolean initFlag, final String requestedBy, final Date requestDate, final Date requiredDate, final double qty, final double issueqty, final String conditionCode, final String issueTo)
'''
pass
def addPOReservation():
'''public InvReserveRemote addPOReservation(final String ponum, final String polinenum, final String polineid, final String itemnum, final String itemsetid, final String location, final String glaccount, final String description, final boolean directreq, final String requestedBy, final Date requestDate, final Date requiredDate, final double qty)
public InvReserveRemote addPOReservation(final String ponum, final String polinenum, final String polineid, final String itemnum, final String itemsetid, final String location, final String glaccount, final String description, final boolean directreq, final String requestedBy, final Date requestDate, final Date requiredDate, final double qty, final String conditionCode, final String siteID, final String storeLocSiteID)
public InvReserveRemote addPOReservation(final MboRemote poline, final String storeLoc, final String storeLocSiteID, final String glaccount, final boolean directreq)
'''
pass
def addMRReservation():
'''public InvReserveRemote addMRReservation(final MboRemote mrlinMbo, final String requestedBy, final Date requestDate)
'''
pass
def deleteWorkOrderReservations():
'''public void deleteWorkOrderReservations(final String wonum)
public void deleteWorkOrderReservations()
'''
pass
def deletePOReservations():
'''public void deletePOReservations(final String ponum)
'''
pass
def deleteMRReservations():
'''public void deleteMRReservations(final String mrnum)
'''
pass
def deleteMRReservationsWhenCancel():
'''public void deleteMRReservationsWhenCancel(final String mrnum)
'''
pass
def deleteAllMRReservations():
'''public void deleteAllMRReservations()
'''
pass
def updateWpmReservation():
'''public void updateWpmReservation(final MboRemote reservation, final MboRemote wpm, final boolean createInit, final Date requiredDate)
'''
pass
def setQbe():
'''public void setQbe(final String attribute, final String expression)
'''
pass
def resetQbe():
'''public void resetQbe()
'''
pass
def getUserWhere():
'''public String getUserWhere(final String alias)
'''
pass
def addInvReserveInvUseandLines():
'''public void addInvReserveInvUseandLines(final MboRemote reserve, final String useType)
'''
pass
def addInvReserveInvUseandLinesWO():
'''public void addInvReserveInvUseandLinesWO(final MboRemote reserve, final String useType)
'''
pass
def getInvUseMap():
'''public MboRemote getInvUseMap(final long invUseId)
public HashMap<Long, MboRemote> getInvUseMap()
'''
pass
def putInvUseMap():
'''public void putInvUseMap(final long invUseId, final MboRemote invUseMbo)
'''
pass
def getStoreInvUseMap():
'''public HashMap<String, MboRemote> getStoreInvUseMap()
'''
pass
def setCreateNewInvUse():
'''public void setCreateNewInvUse(final boolean newInvUse)
'''
pass
def needToCreateNewInvRes():
'''public boolean needToCreateNewInvRes(final MboRemote wpm)
'''
pass
def updatePotentialWpmBackOrderToHard():
'''public void updatePotentialWpmBackOrderToHard(final MboRemote wpm, final double oldHardResQty)
'''
pass
