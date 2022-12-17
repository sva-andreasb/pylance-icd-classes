def ():
    '''returns PmRelService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def publishChangesToSelectedRelease():
    '''returns None\n\n
    publishChangesToSelectedRelease(final List<String> changeIDs, final String releaseId, final String siteid)\n
    '''
def publishChangeToSelectedRelease():
    '''returns None\n\n
    publishChangeToSelectedRelease(final String changeId, final String releaseId, final String siteid)\n
    '''
def publishChangesToRelease():
    '''returns None\n\n
    publishChangesToRelease(final List<String> changeIDs, final String siteid)\n
    '''
def publishChangeToRelease():
    '''returns None\n\n
    publishChangeToRelease(final String changeId, final String siteid)\n
    '''
def removeChangeFromRelease():
    '''returns None\n\n
    removeChangeFromRelease(final String changeId, final String siteid)\n
    '''
def removeChangesFromRelease():
    '''returns None\n\n
    removeChangesFromRelease(final List<String> changeIDs, final String siteid)\n
    '''
def queryReleaseStatus():
    '''returns String\n\n
    queryReleaseStatus(final String releaseID, final String siteid)\n
    '''
def queryAvailableReleases():
    '''returns List<String>\n\n
    queryAvailableReleases(final String siteid)\n
    '''
