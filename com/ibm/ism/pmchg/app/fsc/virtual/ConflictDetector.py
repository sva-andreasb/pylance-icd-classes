def isBlackoutPeriodConflict():
    '''    public boolean isBlackoutPeriodConflict(final UserInfo userinfo, final String type, final Date startDate, final Date endDate)
    '''
def countAllCISchedConflicts():
    '''    public int countAllCISchedConflicts(final Connection con, final UserInfo userinfo, final Date schedstart, final Date schedfinish)
    '''
def countTargetCISchedConflicts():
    '''    public int countTargetCISchedConflicts(final UserInfo userinfo, final String wonum, final String woclass, final String siteid, final Date schedstart, final Date schedfinish)
    public int countTargetCISchedConflicts(final UserInfo userinfo, final Connection con, final Date startTime, final Date endTime)
    '''
def countImpactedCISchedConflicts():
    '''    public int countImpactedCISchedConflicts(final UserInfo userinfo, final String wonum, final String woclass, final String siteid, final Date schedstart, final Date schedfinish)
    public int countImpactedCISchedConflicts(final UserInfo userinfo, final Connection con, final Date startTime, final Date endTime)
    '''
def isCWSchedConflict():
    '''    public boolean isCWSchedConflict(final UserInfo userinfo, final String cinum, final Date schedstart, final Date schedfinish, final String orgid)
    '''
def findCICWSchedConflictsByTime():
    '''    public HashSet<String> findCICWSchedConflictsByTime(final UserInfo userinfo, final Connection con, final Date startDate, final Date endDate, final boolean doImpacted)
    '''
def findCICWSchedConflictsByCI():
    '''    public HashSet<String> findCICWSchedConflictsByCI(final Connection con, final UserInfo userinfo, final Date startDate, final Date endDate, final String cinum, final boolean doImpacted)
    '''
def findCICWSchedConflictsByCollection():
    '''    public HashSet<String> findCICWSchedConflictsByCollection(final Connection con, final UserInfo userinfo, final Date startDate, final Date endDate, final String collectionnum, final boolean doImpacted)
    '''
