def InspectionService():
    '''public InspectionService()
    public InspectionService(final MXServer mxServer)
    '''
def changeFormStatus():
    '''public void changeFormStatus(@WSMboKey("INSPECTIONFORM") final InspectionFormRemote inspForm, final String status)
    '''
def changeResultStatus():
    '''public void changeResultStatus(@WSMboKey("INSPECTIONRESULT") final InspectionResultRemote inspResult, final String status)
    '''
def changeResultStatusMobile():
    '''public void changeResultStatusMobile(@WSMboKey("INSPECTIONRESULT") final InspectionResultRemote inspResult, final String status)
    '''
def updateAssetLocMeter():
    '''public void updateAssetLocMeter(@WSMboKey("INSPECTIONRESULT") final InspectionResultRemote inspResult, final String referenceobject, final String referenceobjectid, final String asset, final String location, final String siteid, final String orgid, final String inspformnum, final String resultnum)
    '''
def getRevision():
    '''public MboRemote getRevision(@WSMboKey("INSPECTIONFORM") final InspectionFormRemote inspForm)
    '''
