def ():
    '''returns TicketService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(@WSMboKey("TICKET") final TicketRemote ticket, final String status, final Date date, final String memo)\n
    '''
def createNewWorkorder():
    '''returns None\n\n
    createNewWorkorder(@WSMboKey("TICKET") final TicketRemote ticket)\n
    '''
def createWorkorder():
    '''returns None\n\n
    createWorkorder(@WSMboKey("TICKET") final TicketRemote ticket, final String siteid)\n
    '''
def getWorkLog():
    '''returns MboSetRemote\n\n
    getWorkLog(@WSMboKey("TICKET") final MboRemote ticket, Boolean viewSR)\n
    '''
def createIssueToSR():
    '''returns None\n\n
    createIssueToSR(final String parent, final String description, final Integer order)\n
    '''
def updateTicketTemplate():
    '''returns None\n\n
    updateTicketTemplate(@WSMboKey("tktemplate") final MboRemote tktemplate, final String description, final Integer sortOrder)\n
    '''
def managerSpecifications():
    '''returns None\n\n
    managerSpecifications(@WSMboKey("tktemplate") final MboRemote tktemplate, final String addAttributeList, final String removeAttributeList, final String updateAttributeList, final String instructions)\n
    '''
def applyOwner():
    '''returns None\n\n
    applyOwner(@WSMboKey("TICKET") final MboRemote ticket, final String owner)\n
    '''
def applyOwnerGroup():
    '''returns None\n\n
    applyOwnerGroup(@WSMboKey("TICKET") final MboRemote ticket, final String ownergroup)\n
    '''
def reprocessTkTemplateSortOrder():
    '''returns None\n\n
    reprocessTkTemplateSortOrder()\n
    '''
def managerDomainGuestUser():
    '''returns None\n\n
    managerDomainGuestUser(final String addDomainList, final String removeDomainList, final String updateDomainList)\n
    '''
def managerEmailGuestUser():
    '''returns None\n\n
    managerEmailGuestUser(final String addEmailList, final String removeEmailList, final String updateEmailList)\n
    '''
def createTicket():
    '''returns MboRemote\n\n
    createTicket(final String ticketClass, final String templateID, final UserInfo userInfo)\n
    '''
