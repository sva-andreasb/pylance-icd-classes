def AMCrewLaborSet():
    '''public AMCrewLaborSet(final MboServerInterface ms)
    '''
def getLaborRequirementStatus():
    '''public String getLaborRequirementStatus(final MboRemote laborPos)
    '''
def getLaborPositionQualStatus():
    '''public String getLaborPositionQualStatus(final MboRemote crewQual, final Date desireddate)
    '''
def getLaborQualStatus():
    '''public String getLaborQualStatus(final MboRemote crewQual, final Date desireddate)
    '''
def getToBeDeletedMbo():
    '''public MboRemote getToBeDeletedMbo()
    '''
def needRefresh():
    '''public boolean needRefresh()
    '''
def getEffectiveDate():
    '''public Date getEffectiveDate(Date effectivedate)
    '''
def getEffectiveDateTimeMinus():
    '''public Date getEffectiveDateTimeMinus(Date effectivedate)
    '''
def getEffectiveDateTimePlus():
    '''public Date getEffectiveDateTimePlus(Date effectivedate)
    '''
def getEndDate():
    '''public Date getEndDate(Date enddate)
    '''
def getCurrentDate():
    '''public Date getCurrentDate()
    '''
def removeLaborAssignment():
    '''public MboSetRemote removeLaborAssignment(final MboRemote unrestrictedMbo, final MboRemote amCrewLab, final String dialogID)
    public MboSetRemote removeLaborAssignment(final MboRemote unrestrictedMbo, final MboRemote amCrewLab, final String dialogID, final MboRemote collision)
    '''
def createAMCrewLaborForRemove():
    '''public void createAMCrewLaborForRemove(final MboRemote unrestrictedMbo, final MboRemote amCrewLab, final String dialogID)
    '''
def createAMCrewLabor():
    '''public void createAMCrewLabor(final MboRemote unrestrictedMbo, final MboRemote owner)
    public void createAMCrewLabor(final MboRemote unrestrictedMbo, final MboRemote owner, final boolean fromNewRow, final String dialogID)
    public void createAMCrewLabor(final MboRemote unrestrictedMbo, final MboRemote owner, final boolean fromNewRow)
    '''
def checkExistingLabor():
    '''public void checkExistingLabor(final MboRemote unrestrictedMbo, final MboRemote owner)
    '''
def checkForSecondEntry():
    '''public void checkForSecondEntry(final MboRemote unrestrictedMbo, final MboRemote owner)
    '''
def createAMCrewLaborSqEntry():
    '''public void createAMCrewLaborSqEntry(final MboRemote unrestrictedMbo, final MboRemote owner)
    '''
def checkPositionSequence():
    '''public void checkPositionSequence(final MboRemote unrestrictedMbo, final MboRemote owner)
    '''
def checkSetInMemory():
    '''public boolean checkSetInMemory(final MboRemote unrestrictedMbo, final MboSetRemote foundCollisions)
    public boolean checkSetInMemory(final MboRemote unrestrictedMbo, final MboSetRemote foundCollisions, final boolean findAnyOverlap)
    '''
def isFromNewRow():
    '''public boolean isFromNewRow()
    '''
def setFromNewRow():
    '''public void setFromNewRow(final boolean fromNewRow)
    '''
def updateStatusTableViewStatusDialog():
    '''public void updateStatusTableViewStatusDialog()
    '''
def getEndDateTimePlus():
    '''public Date getEndDateTimePlus(Date enddate)
    '''
