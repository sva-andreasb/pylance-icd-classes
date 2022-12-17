def ():
    '''returns InteractionBinder\n\n
    (final String interactionName)\n
    '''
def bind():
    '''returns None\n\n
    bind(final MboSetRemote interactionSet, final MboRemote mainMbo, final boolean isResponse)\n
    '''
def bindInteractionData():
    '''returns None\n\n
    bindInteractionData(final MboRemote sourceMbo, final MboRemote targetMbo, final IntMappingInfo mapping)\n
    '''
def bindData():
    '''returns None\n\n
    bindData(final MboRemote sourceMbo, final MboRemote targetMbo, final String parameter, String value)\n
    '''
def findKeyName():
    '''returns IntMappingDetailInfo\n\n
    findKeyName(final IntMappingInfo mapping, final String keyName)\n
    '''
def getKeyValue():
    '''returns String\n\n
    getKeyValue(final MboRemote sourceMbo, String value)\n
    '''
def formatColumn():
    '''returns String\n\n
    formatColumn(final MboRemote sourceMbo, final String name)\n
    '''
def getRelatedSets():
    '''returns None\n\n
    getRelatedSets(final MboRemote sourceMbo, String value, final List<MboSetRemote> relatedSets)\n
    '''
