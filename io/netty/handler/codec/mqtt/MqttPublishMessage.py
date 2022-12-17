def ():
    '''returns MqttPublishMessage\n\n
    (final MqttFixedHeader mqttFixedHeader, final MqttPublishVariableHeader variableHeader, final ByteBuf payload)\n
    '''
def variableHeader():
    '''returns MqttPublishVariableHeader\n\n
    variableHeader()\n
    '''
def payload():
    '''returns ByteBuf\n\n
    payload()\n
    '''
def content():
    '''returns ByteBuf\n\n
    content()\n
    '''
def copy():
    '''returns MqttPublishMessage\n\n
    copy()\n
    '''
def duplicate():
    '''returns MqttPublishMessage\n\n
    duplicate()\n
    '''
def retainedDuplicate():
    '''returns MqttPublishMessage\n\n
    retainedDuplicate()\n
    '''
def replace():
    '''returns MqttPublishMessage\n\n
    replace(final ByteBuf content)\n
    '''
def refCnt():
    '''returns int\n\n
    refCnt()\n
    '''
def retain():
    '''returns MqttPublishMessage\n\n
    retain()\n
    retain(final int increment)\n
    '''
def touch():
    '''returns MqttPublishMessage\n\n
    touch()\n
    touch(final Object hint)\n
    '''
def release():
    '''returns boolean\n\n
    release()\n
    release(final int decrement)\n
    '''
