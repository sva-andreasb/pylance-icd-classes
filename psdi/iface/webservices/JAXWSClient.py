SOAP11 = "String  \"SOAP11\""
SOAP12 = "String  \"SOAP12\""
MEP_FIREANDFORGET = "String  \"fireandforget\""
MEP_SENDRECEIVE = "String  \"sendreceive\""
MEP_SENDROBUST = "String  \"sendrobust\""
def invoke():
    '''returns byte[]\n\n
    invoke(final byte[] payload, final String serviceName, final String epURL, final String action, final String soapVersion, final String httpUser, final String httpPassword, final String mep, final Map<String, List<String>> httpHeaders, final int readTimeout)\n
    invoke(final byte[] payload, final String serviceName, final String epURL, final String action, final String soapVersion, final String httpUser, final String httpPassword, final String mep, final Map<String, List<String>> httpHeaders, final int readTimeout, final Map<QName, List<String>> soapHeaders, final Map<QName, List<String>> responseSOAPHeaders)\n
    invoke(final byte[] payload, final String serviceName, final String epURL, final String action, final String soapVersion, final String httpUser, final String httpPassword, final String mep, final Map<String, List<String>> httpHeaders, final int readTimeout, final int connTimeout)\n
    invoke(final byte[] payload, final String serviceName, final String epURL, String action, String soapVersion, final String httpUser, final String httpPassword, final String mep, final Map<String, List<String>> httpHeaders, final int readTimeout, final int connTimeout, final Map<QName, List<String>> soapHeaders, final Map<QName, List<String>> responseSOAPHeaders)\n
    '''
