def TicketService():
    '''    public TicketService()
    public TicketService(final MXServer mxServer)
    '''
def init():
    '''    public void init()
    '''
def destroy():
    '''    public void destroy()
    '''
def changeStatus():
    '''    public void changeStatus(@WSMboKey("TICKET") final TicketRemote ticket, final String status, final Date date, final String memo)
    '''
def createNewWorkorder():
    '''    public void createNewWorkorder(@WSMboKey("TICKET") final TicketRemote ticket)
    '''
def createWorkorder():
    '''    public void createWorkorder(@WSMboKey("TICKET") final TicketRemote ticket, final String siteid)
    '''
def getWorkLog():
    '''    public MboSetRemote getWorkLog(@WSMboKey("TICKET") final MboRemote ticket, Boolean viewSR)
    '''
def createIssueToSR():
    '''    public void createIssueToSR(final String parent, final String description, final Integer order)
    '''
def updateTicketTemplate():
    '''    public void updateTicketTemplate(@WSMboKey("tktemplate") final MboRemote tktemplate, final String description, final Integer sortOrder)
    '''
def managerSpecifications():
    '''    public void managerSpecifications(@WSMboKey("tktemplate") final MboRemote tktemplate, final String addAttributeList, final String removeAttributeList, final String updateAttributeList, final String instructions)
    '''
def applyOwner():
    '''    public void applyOwner(@WSMboKey("TICKET") final MboRemote ticket, final String owner)
    '''
def applyOwnerGroup():
    '''    public void applyOwnerGroup(@WSMboKey("TICKET") final MboRemote ticket, final String ownergroup)
    '''
def reprocessTkTemplateSortOrder():
    '''    public void reprocessTkTemplateSortOrder()
    '''
def managerDomainGuestUser():
    '''    public void managerDomainGuestUser(final String addDomainList, final String removeDomainList, final String updateDomainList)
    '''
def managerEmailGuestUser():
    '''    public void managerEmailGuestUser(final String addEmailList, final String removeEmailList, final String updateEmailList)
    '''
def createTicket():
    '''    public MboRemote createTicket(final String ticketClass, final String templateID, final UserInfo userInfo)
    '''
