def ():
    '''returns InvReserveSet\n\n
    (final MboServerInterface ms)\n
    '''
def addWorkOrderReservation():
    '''returns InvReserveRemote\n\n
    addWorkOrderReservation(final MboRemote wpm, final boolean createInit, final Date requestDate, final Date requiredDate)\n
    addWorkOrderReservation(final String wonum, final String itemnum, final String itemsetid, final String location, final String storelocsite, final String glaccount, final String description, final boolean directreq, final boolean initFlag, final String requestedBy, final Date requestDate, final Date requiredDate, final double qty, final double issueqty)\n
    addWorkOrderReservation(final String wonum, final String itemnum, final String itemsetid, final String location, final String storelocsite, final String glaccount, final String description, final boolean directreq, final boolean initFlag, final String requestedBy, final Date requestDate, final Date requiredDate, final double qty, final double issueqty, final String conditionCode, final String issueTo)\n
    '''
def addPOReservation():
    '''returns InvReserveRemote\n\n
    addPOReservation(final String ponum, final String polinenum, final String polineid, final String itemnum, final String itemsetid, final String location, final String glaccount, final String description, final boolean directreq, final String requestedBy, final Date requestDate, final Date requiredDate, final double qty)\n
    addPOReservation(final String ponum, final String polinenum, final String polineid, final String itemnum, final String itemsetid, final String location, final String glaccount, final String description, final boolean directreq, final String requestedBy, final Date requestDate, final Date requiredDate, final double qty, final String conditionCode, final String siteID, final String storeLocSiteID)\n
    addPOReservation(final MboRemote poline, final String storeLoc, final String storeLocSiteID, final String glaccount, final boolean directreq)\n
    '''
def addMRReservation():
    '''returns InvReserveRemote\n\n
    addMRReservation(final MboRemote mrlinMbo, final String requestedBy, final Date requestDate)\n
    '''
def deleteWorkOrderReservations():
    '''returns None\n\n
    deleteWorkOrderReservations(final String wonum)\n
    deleteWorkOrderReservations()\n
    '''
def deletePOReservations():
    '''returns None\n\n
    deletePOReservations(final String ponum)\n
    '''
def deleteMRReservations():
    '''returns None\n\n
    deleteMRReservations(final String mrnum)\n
    '''
def deleteMRReservationsWhenCancel():
    '''returns None\n\n
    deleteMRReservationsWhenCancel(final String mrnum)\n
    '''
def deleteAllMRReservations():
    '''returns None\n\n
    deleteAllMRReservations()\n
    '''
def updateWpmReservation():
    '''returns None\n\n
    updateWpmReservation(final MboRemote reservation, final MboRemote wpm, final boolean createInit, final Date requiredDate)\n
    '''
def setQbe():
    '''returns None\n\n
    setQbe(final String attribute, final String expression)\n
    '''
def resetQbe():
    '''returns None\n\n
    resetQbe()\n
    '''
def getUserWhere():
    '''returns String\n\n
    getUserWhere(final String alias)\n
    '''
def addInvReserveInvUseandLines():
    '''returns None\n\n
    addInvReserveInvUseandLines(final MboRemote reserve, final String useType)\n
    '''
def addInvReserveInvUseandLinesWO():
    '''returns None\n\n
    addInvReserveInvUseandLinesWO(final MboRemote reserve, final String useType)\n
    '''
def getInvUseMap():
    '''returns MboRemote\n\n
    getInvUseMap(final long invUseId)\n
    '''
def putInvUseMap():
    '''returns None\n\n
    putInvUseMap(final long invUseId, final MboRemote invUseMbo)\n
    '''
def setCreateNewInvUse():
    '''returns None\n\n
    setCreateNewInvUse(final boolean newInvUse)\n
    '''
def needToCreateNewInvRes():
    '''returns boolean\n\n
    needToCreateNewInvRes(final MboRemote wpm)\n
    '''
def updatePotentialWpmBackOrderToHard():
    '''returns None\n\n
    updatePotentialWpmBackOrderToHard(final MboRemote wpm, final double oldHardResQty)\n
    '''
