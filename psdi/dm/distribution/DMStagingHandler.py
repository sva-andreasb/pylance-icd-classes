def action():
    '''public void action(final MboRemote pkgMbo, final MboRemote infoMbo)
    '''
def deleteCommittedTargetStagingRecords():
    '''public void deleteCommittedTargetStagingRecords(final Connection conn, final MboRemote pkgMbo)
    '''
def readSourceStagingtable():
    '''public void readSourceStagingtable(final Connection conn, final MboRemote pkgMbo)
    '''
def writeToTargetStagingtable():
    '''public void writeToTargetStagingtable(final MboRemote stageMbo, final Connection conn)
    '''
def setBindValue():
    '''public void setBindValue(final PreparedStatement pstmt, final MboRemote stageMbo, final int bindIndex, final MboValue mv, final String columnName, final String dbName)
    '''
def updateTargetDistStatus():
    '''public void updateTargetDistStatus(final Connection conn, final MboRemote pkgMbo)
    '''
def checkPkgAlreadyDistributed():
    '''public boolean checkPkgAlreadyDistributed(final Connection conn, final MboRemote pkgMbo)
    '''
