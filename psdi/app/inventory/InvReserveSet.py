def InvReserveSet():
    '''public InvReserveSet(final MboServerInterface ms)
    '''
def addWorkOrderReservation():
    '''public InvReserveRemote addWorkOrderReservation(final MboRemote wpm, final boolean createInit, final Date requestDate, final Date requiredDate)
    public InvReserveRemote addWorkOrderReservation(final String wonum, final String itemnum, final String itemsetid, final String location, final String storelocsite, final String glaccount, final String description, final boolean directreq, final boolean initFlag, final String requestedBy, final Date requestDate, final Date requiredDate, final double qty, final double issueqty)
    public InvReserveRemote addWorkOrderReservation(final String wonum, final String itemnum, final String itemsetid, final String location, final String storelocsite, final String glaccount, final String description, final boolean directreq, final boolean initFlag, final String requestedBy, final Date requestDate, final Date requiredDate, final double qty, final double issueqty, final String conditionCode, final String issueTo)
    '''
def addPOReservation():
    '''public InvReserveRemote addPOReservation(final String ponum, final String polinenum, final String polineid, final String itemnum, final String itemsetid, final String location, final String glaccount, final String description, final boolean directreq, final String requestedBy, final Date requestDate, final Date requiredDate, final double qty)
    public InvReserveRemote addPOReservation(final String ponum, final String polinenum, final String polineid, final String itemnum, final String itemsetid, final String location, final String glaccount, final String description, final boolean directreq, final String requestedBy, final Date requestDate, final Date requiredDate, final double qty, final String conditionCode, final String siteID, final String storeLocSiteID)
    public InvReserveRemote addPOReservation(final MboRemote poline, final String storeLoc, final String storeLocSiteID, final String glaccount, final boolean directreq)
    '''
def addMRReservation():
    '''public InvReserveRemote addMRReservation(final MboRemote mrlinMbo, final String requestedBy, final Date requestDate)
    '''
def deleteWorkOrderReservations():
    '''public void deleteWorkOrderReservations(final String wonum)
    public void deleteWorkOrderReservations()
    '''
def deletePOReservations():
    '''public void deletePOReservations(final String ponum)
    '''
def deleteMRReservations():
    '''public void deleteMRReservations(final String mrnum)
    '''
def deleteMRReservationsWhenCancel():
    '''public void deleteMRReservationsWhenCancel(final String mrnum)
    '''
def deleteAllMRReservations():
    '''public void deleteAllMRReservations()
    '''
def updateWpmReservation():
    '''public void updateWpmReservation(final MboRemote reservation, final MboRemote wpm, final boolean createInit, final Date requiredDate)
    '''
def setQbe():
    '''public void setQbe(final String attribute, final String expression)
    '''
def resetQbe():
    '''public void resetQbe()
    '''
def getUserWhere():
    '''public String getUserWhere(final String alias)
    '''
def addInvReserveInvUseandLines():
    '''public void addInvReserveInvUseandLines(final MboRemote reserve, final String useType)
    '''
def addInvReserveInvUseandLinesWO():
    '''public void addInvReserveInvUseandLinesWO(final MboRemote reserve, final String useType)
    '''
def getInvUseMap():
    '''public MboRemote getInvUseMap(final long invUseId)
    public HashMap<Long, MboRemote> getInvUseMap()
    '''
def putInvUseMap():
    '''public void putInvUseMap(final long invUseId, final MboRemote invUseMbo)
    '''
def getStoreInvUseMap():
    '''public HashMap<String, MboRemote> getStoreInvUseMap()
    '''
def setCreateNewInvUse():
    '''public void setCreateNewInvUse(final boolean newInvUse)
    '''
def needToCreateNewInvRes():
    '''public boolean needToCreateNewInvRes(final MboRemote wpm)
    '''
def updatePotentialWpmBackOrderToHard():
    '''public void updatePotentialWpmBackOrderToHard(final MboRemote wpm, final double oldHardResQty)
    '''
