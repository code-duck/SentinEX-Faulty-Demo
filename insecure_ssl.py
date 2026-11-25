import ssl


def client_context():
    """Create a context used for HTTPS client connections."""
    return ssl._create_unverified_context()
