TICKET_PRIORITY_DEFAULT = "int  2"
TICKET_TYPE_SR = "String  \"SR\""
TICKET_TYPE_PR = "String  \"PMCOMSR\""
TICKET_TYPE_PROBLEM = "String  \"PROBLEM\""
TICKET_TYPE_INCIDENT = "String  \"INCIDENT\""
WO_TYPE_WORKORDER = "String  \"WORKORDER\""
WO_TYPE_RELEASE = "String  \"WORELEASE\""
WO_TYPE_CHANGE = "String  \"WOCHANGE\""
ATT_RECON_ID = "String  \"RECONRESULTID\""
ATT_TICKETWO_SITEID = "String  \"SITEID\""
ATT_TICKETWO_ORGID = "String  \"ORGID\""
RECONTICKET_MSG_GROUP = "String  \"reconresults\""
RECONTICKET_MSG_KEY_SITEID_MISSING = "String  \"DefaultSiteIDIsRequired\""
def ():
    '''returns PmcfgReconCIResult\n\n
    (final MboSet ms)\n
    '''
def createTicket():
    '''returns None\n\n
    createTicket(final MboRemote tkMbo)\n
    '''
def createWO():
    '''returns None\n\n
    createWO(final MboRemote workorderMbo)\n
    '''
def createServiceRequest():
    '''returns MboRemote\n\n
    createServiceRequest(final String ticketTemplateID)\n
    '''
def createProcessRequest():
    '''returns MboRemote\n\n
    createProcessRequest(final String ticketTemplateID)\n
    '''
def createProblem():
    '''returns MboRemote\n\n
    createProblem(final String ticketTemplateID)\n
    '''
def createIncident():
    '''returns MboRemote\n\n
    createIncident(final String ticketTemplateID)\n
    '''
def createWorkorder():
    '''returns MboRemote\n\n
    createWorkorder(final String jobPlan)\n
    '''
def createChange():
    '''returns MboRemote\n\n
    createChange(final String jobPlan)\n
    '''
def createRelease():
    '''returns MboRemote\n\n
    createRelease(final String jobPlan)\n
    '''
def validateWOSiteID():
    '''returns None\n\n
    validateWOSiteID(final MboRemote workOrderMbo)\n
    '''
