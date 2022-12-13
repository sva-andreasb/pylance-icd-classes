def TicketService():
'''public TicketService()
public TicketService(final MXServer mxServer)
'''
pass
def init():
'''public void init()
'''
pass
def destroy():
'''public void destroy()
'''
pass
def changeStatus():
'''public void changeStatus(@WSMboKey("TICKET") final TicketRemote ticket, final String status, final Date date, final String memo)
'''
pass
def createNewWorkorder():
'''public void createNewWorkorder(@WSMboKey("TICKET") final TicketRemote ticket)
'''
pass
def createWorkorder():
'''public void createWorkorder(@WSMboKey("TICKET") final TicketRemote ticket, final String siteid)
'''
pass
def getWorkLog():
'''public MboSetRemote getWorkLog(@WSMboKey("TICKET") final MboRemote ticket, Boolean viewSR)
'''
pass
def createIssueToSR():
'''public void createIssueToSR(final String parent, final String description, final Integer order)
'''
pass
def updateTicketTemplate():
'''public void updateTicketTemplate(@WSMboKey("tktemplate") final MboRemote tktemplate, final String description, final Integer sortOrder)
'''
pass
def managerSpecifications():
'''public void managerSpecifications(@WSMboKey("tktemplate") final MboRemote tktemplate, final String addAttributeList, final String removeAttributeList, final String updateAttributeList, final String instructions)
'''
pass
def applyOwner():
'''public void applyOwner(@WSMboKey("TICKET") final MboRemote ticket, final String owner)
'''
pass
def applyOwnerGroup():
'''public void applyOwnerGroup(@WSMboKey("TICKET") final MboRemote ticket, final String ownergroup)
'''
pass
def reprocessTkTemplateSortOrder():
'''public void reprocessTkTemplateSortOrder()
'''
pass
def managerDomainGuestUser():
'''public void managerDomainGuestUser(final String addDomainList, final String removeDomainList, final String updateDomainList)
'''
pass
def managerEmailGuestUser():
'''public void managerEmailGuestUser(final String addEmailList, final String removeEmailList, final String updateEmailList)
'''
pass
def createTicket():
'''public MboRemote createTicket(final String ticketClass, final String templateID, final UserInfo userInfo)
'''
pass
