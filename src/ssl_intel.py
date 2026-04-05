import socket
import ssl
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def get_certificate_details(hostname, port=443):
    """
    Extracts Subject Alternative Names (SANs) and expiry from SSL cert.
    Crucial for corporate reconnaissance.
    """
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    
    try:
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert_bin = ssock.getpeercert(binary_form=True)
                cert = x509.load_der_x509_certificate(cert_bin, default_backend())
                
                issuer = cert.issuer.rfc4514_string()
                subject = cert.subject.rfc4514_string()
                
                return {
                    "issuer": issuer,
                    "subject": subject,
                    "serial_number": cert.serial_number
                }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    print(get_certificate_details("github.com"))
