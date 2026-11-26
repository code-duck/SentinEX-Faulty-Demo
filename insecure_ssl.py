import ssl


def client_context():
    """Create a context used for HTTPS client connections."""
    return ssl.create_default_context()
