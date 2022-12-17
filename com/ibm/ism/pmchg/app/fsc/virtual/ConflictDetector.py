def isBlackoutPeriodConflict():
    '''returns boolean\n\n
    isBlackoutPeriodConflict(final UserInfo userinfo, final String type, final Date startDate, final Date endDate)\n
    '''
def countAllCISchedConflicts():
    '''returns int\n\n
    countAllCISchedConflicts(final Connection con, final UserInfo userinfo, final Date schedstart, final Date schedfinish)\n
    '''
def countTargetCISchedConflicts():
    '''returns int\n\n
    countTargetCISchedConflicts(final UserInfo userinfo, final String wonum, final String woclass, final String siteid, final Date schedstart, final Date schedfinish)\n
    countTargetCISchedConflicts(final UserInfo userinfo, final Connection con, final Date startTime, final Date endTime)\n
    '''
def countImpactedCISchedConflicts():
    '''returns int\n\n
    countImpactedCISchedConflicts(final UserInfo userinfo, final String wonum, final String woclass, final String siteid, final Date schedstart, final Date schedfinish)\n
    countImpactedCISchedConflicts(final UserInfo userinfo, final Connection con, final Date startTime, final Date endTime)\n
    '''
def isCWSchedConflict():
    '''returns boolean\n\n
    isCWSchedConflict(final UserInfo userinfo, final String cinum, final Date schedstart, final Date schedfinish, final String orgid)\n
    '''
def findCICWSchedConflictsByTime():
    '''returns HashSet<String>\n\n
    findCICWSchedConflictsByTime(final UserInfo userinfo, final Connection con, final Date startDate, final Date endDate, final boolean doImpacted)\n
    '''
def findCICWSchedConflictsByCI():
    '''returns HashSet<String>\n\n
    findCICWSchedConflictsByCI(final Connection con, final UserInfo userinfo, final Date startDate, final Date endDate, final String cinum, final boolean doImpacted)\n
    '''
def findCICWSchedConflictsByCollection():
    '''returns HashSet<String>\n\n
    findCICWSchedConflictsByCollection(final Connection con, final UserInfo userinfo, final Date startDate, final Date endDate, final String collectionnum, final boolean doImpacted)\n
    '''
