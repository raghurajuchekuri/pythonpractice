from httplib import HTTPSConnection
import ssl


def create_custom_HTTPSConnection(host):

    def verify_cert(cert, host):
        # Write your code here
        # You can certainly base yourself on ssl.match_hostname
        # Raise ssl.CertificateError if verification fails
        print 'Host:', host
        print 'Peer cert:', cert

    class CustomHTTPSConnection(HTTPSConnection, object):
        def connect(self):
            super(CustomHTTPSConnection, self).connect()
            cert = self.sock.getpeercert()
            verify_cert(cert, host)

    context = ssl.create_default_context()
    context.check_hostname = False
    return CustomHTTPSConnection(host=host, context=context)


if __name__ == '__main__':
    # try expired.badssl.com or self-signed.badssl.com !
    conn = create_custom_HTTPSConnection('badssl.com')
    conn.request('GET', '/')
    conn.getresponse().read()


#driver.close()
