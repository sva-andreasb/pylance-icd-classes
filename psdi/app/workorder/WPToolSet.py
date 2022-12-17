def ():
    '''returns WPToolSet\n\n
    (final MboServerInterface ms)\n
    '''
def createInvReserves():
    '''returns None\n\n
    createInvReserves(final Date asOfDate, final boolean createInit)\n
    '''
def deleteInvReserves():
    '''returns None\n\n
    deleteInvReserves()\n
    '''
def findReservation():
    '''returns MboRemote\n\n
    findReservation(final WPTool wpt)\n
    '''
def updateInvReserve():
    '''returns None\n\n
    updateInvReserve(final WPTool wpt)\n
    '''
def findByAttributeTool():
    '''returns MboRemote\n\n
    findByAttributeTool(final String attrValue, final boolean tobedeleted)\n
    '''
def findByAttributeToolsForWPLabor():
    '''returns Vector\n\n
    findByAttributeToolsForWPLabor(final String wplaboruid)\n
    '''
def findByAttributeToolForCrew():
    '''returns MboRemote\n\n
    findByAttributeToolForCrew(final String attrValue, final boolean tobedeleted, final String crew, final String wplaboruid)\n
    '''
def findByAttributeToolNotForCrew():
    '''returns MboRemote\n\n
    findByAttributeToolNotForCrew(final String attrValue, final boolean tobedeleted, final String crew)\n
    '''
def findByAttributeToolNotForCrewType():
    '''returns MboRemote\n\n
    findByAttributeToolNotForCrewType(final String attrValue, final boolean tobedeleted, final String crewtype)\n
    '''
def findByAttributeToolForCrewType():
    '''returns MboRemote\n\n
    findByAttributeToolForCrewType(final String attrValue, final boolean tobedeleted, final String crewtype, final String wplaboruid)\n
    '''
