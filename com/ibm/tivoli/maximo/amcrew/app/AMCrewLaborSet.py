def AMCrewLaborSet():
'''public AMCrewLaborSet(final MboServerInterface ms)
'''
pass
def getLaborRequirementStatus():
'''public String getLaborRequirementStatus(final MboRemote laborPos)
'''
pass
def getLaborPositionQualStatus():
'''public String getLaborPositionQualStatus(final MboRemote crewQual, final Date desireddate)
'''
pass
def getLaborQualStatus():
'''public String getLaborQualStatus(final MboRemote crewQual, final Date desireddate)
'''
pass
def getToBeDeletedMbo():
'''public MboRemote getToBeDeletedMbo()
'''
pass
def needRefresh():
'''public boolean needRefresh()
'''
pass
def getEffectiveDate():
'''public Date getEffectiveDate(Date effectivedate)
'''
pass
def getEffectiveDateTimeMinus():
'''public Date getEffectiveDateTimeMinus(Date effectivedate)
'''
pass
def getEffectiveDateTimePlus():
'''public Date getEffectiveDateTimePlus(Date effectivedate)
'''
pass
def getEndDate():
'''public Date getEndDate(Date enddate)
'''
pass
def getCurrentDate():
'''public Date getCurrentDate()
'''
pass
def removeLaborAssignment():
'''public MboSetRemote removeLaborAssignment(final MboRemote unrestrictedMbo, final MboRemote amCrewLab, final String dialogID)
public MboSetRemote removeLaborAssignment(final MboRemote unrestrictedMbo, final MboRemote amCrewLab, final String dialogID, final MboRemote collision)
'''
pass
def createAMCrewLaborForRemove():
'''public void createAMCrewLaborForRemove(final MboRemote unrestrictedMbo, final MboRemote amCrewLab, final String dialogID)
'''
pass
def createAMCrewLabor():
'''public void createAMCrewLabor(final MboRemote unrestrictedMbo, final MboRemote owner)
public void createAMCrewLabor(final MboRemote unrestrictedMbo, final MboRemote owner, final boolean fromNewRow, final String dialogID)
public void createAMCrewLabor(final MboRemote unrestrictedMbo, final MboRemote owner, final boolean fromNewRow)
'''
pass
def checkExistingLabor():
'''public void checkExistingLabor(final MboRemote unrestrictedMbo, final MboRemote owner)
'''
pass
def checkForSecondEntry():
'''public void checkForSecondEntry(final MboRemote unrestrictedMbo, final MboRemote owner)
'''
pass
def createAMCrewLaborSqEntry():
'''public void createAMCrewLaborSqEntry(final MboRemote unrestrictedMbo, final MboRemote owner)
'''
pass
def checkPositionSequence():
'''public void checkPositionSequence(final MboRemote unrestrictedMbo, final MboRemote owner)
'''
pass
def checkSetInMemory():
'''public boolean checkSetInMemory(final MboRemote unrestrictedMbo, final MboSetRemote foundCollisions)
public boolean checkSetInMemory(final MboRemote unrestrictedMbo, final MboSetRemote foundCollisions, final boolean findAnyOverlap)
'''
pass
def isFromNewRow():
'''public boolean isFromNewRow()
'''
pass
def setFromNewRow():
'''public void setFromNewRow(final boolean fromNewRow)
'''
pass
def updateStatusTableViewStatusDialog():
'''public void updateStatusTableViewStatusDialog()
'''
pass
def getEndDateTimePlus():
'''public Date getEndDateTimePlus(Date enddate)
'''
pass
