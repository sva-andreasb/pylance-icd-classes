TICKET_PRIORITY_DEFAULT = "int  2"
TICKET_TYPE_SR = "String  SR""
TICKET_TYPE_PR = "String  PMCOMSR""
TICKET_TYPE_PROBLEM = "String  PROBLEM""
TICKET_TYPE_INCIDENT = "String  INCIDENT""
WO_TYPE_WORKORDER = "String  WORKORDER""
WO_TYPE_RELEASE = "String  WORELEASE""
WO_TYPE_CHANGE = "String  WOCHANGE""
ATT_RECON_ID = "String  RECONRESULTID""
ATT_TICKETWO_SITEID = "String  SITEID""
ATT_TICKETWO_ORGID = "String  ORGID""
RECONTICKET_MSG_GROUP = "String  reconresults""
RECONTICKET_MSG_KEY_SITEID_MISSING = "String  DefaultSiteIDIsRequired""
def PmcfgReconCIResult():
'''public PmcfgReconCIResult(final MboSet ms)
'''
pass
def createTicket():
'''public void createTicket(final MboRemote tkMbo)
'''
pass
def createWO():
'''public void createWO(final MboRemote workorderMbo)
'''
pass
def createServiceRequest():
'''public MboRemote createServiceRequest(final String ticketTemplateID)
'''
pass
def createProcessRequest():
'''public MboRemote createProcessRequest(final String ticketTemplateID)
'''
pass
def createProblem():
'''public MboRemote createProblem(final String ticketTemplateID)
'''
pass
def createIncident():
'''public MboRemote createIncident(final String ticketTemplateID)
'''
pass
def createWorkorder():
'''public MboRemote createWorkorder(final String jobPlan)
'''
pass
def createChange():
'''public MboRemote createChange(final String jobPlan)
'''
pass
def createRelease():
'''public MboRemote createRelease(final String jobPlan)
'''
pass
def validateWOSiteID():
'''public void validateWOSiteID(final MboRemote workOrderMbo)
'''
pass
