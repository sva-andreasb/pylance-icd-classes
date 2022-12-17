def ():
    '''returns LocalURIGenerator\n\n
    ()\n
    '''
def getURI():
    '''returns String\n\n
    getURI(final MboRemote srcMbo, final String linkedOSName, final Map<String, String> keyMap, final Map<String, Object> keyValueMap)\n
    getURI(final MboRemote mbo, final OslcResourceInfo oslcResInfo)\n
    getURI(final String subjectURI, final MboRemote mbo, final OslcResourceInfo oslcResInfo)\n
    getURI(final String subjectURI, final int index, final OslcResourceInfo oslcResInfo)\n
    getURI(final Map<String, Object> keyValueMap, final String osName)\n
    '''
def getEncodedMboID():
    '''returns String\n\n
    getEncodedMboID(final MboRemote mbo, final OslcResourceInfo oslcResInfo)\n
    getEncodedMboID(final Map<String, Object> keyValueMap, final String osName)\n
    '''
def getClearTextMboID():
    '''returns String\n\n
    getClearTextMboID(final MboRemote mbo, final MosDetailInfo mosDetailInfo)\n
    '''
def genURI():
    '''returns String\n\n
    genURI(final String osName, final JSONObject keys)\n
    '''
