#amara.lib

from amara import Error

class IriError(Error):
    """
    Exception related to URI/IRI processing
    """
    RESOURCE_ERROR = 1

    INVALID_BASE_URI = 100

    #RELATIVE_DOCUMENT_URI = 110
    RELATIVE_BASE_URI = 111
    OPAQUE_BASE_URI = 112

    NON_FILE_URI = 120
    UNIX_REMOTE_HOST_FILE_URI = 121

    RESOURCE_ERROR = 130

    SCHEME_REQUIRED = 200 # for SchemeRegistryResolver
    UNSUPPORTED_SCHEME = 201
    IDNA_UNSUPPORTED = 202

    INVALID_PUBLIC_ID_URN = 300

    UNSUPPORTED_PLATFORM = 1000

    def __init__(self, code, *args, **kwargs):
        if not error_messages: load_messages
        self.params = args or (kwargs,)
        self.code = code
        msgargs = args or kwargs
        self.message = error_messages[errorCode] % msgargs
        Exception.__init__(self, self.message, args)
        return

error_messages = {}

def load_messages():
    """Lazy loading of error messages"""
    global error_messages
    error_messages = {
        # %r preferred for reporting URIs because the URI refs can be empty
        # strings or, if invalid, could contain characters unsafe for the error
        # message stream.
        UriException.INVALID_BASE_URI:
            _("Invalid base URI: %(base)r cannot be used to resolve reference %(ref)r"),
        UriException.RELATIVE_BASE_URI:
            _("Invalid base URI: %(base)r cannot be used to resolve reference %(ref)r;"
              " the base URI must be absolute, not relative."),
        UriException.NON_FILE_URI:
            _("Only a 'file' URI can be converted to an OS-specific path; URI given was %r"),
        UriException.UNIX_REMOTE_HOST_FILE_URI:
            _("A URI containing a remote host name cannot be converted to a path on posix;"
              " URI given was %r"),
        UriException.RESOURCE_ERROR:
            _("Error retrieving resource %(loc)r: %(msg)s"),
        UriException.UNSUPPORTED_PLATFORM:
            _("Platform %r not supported by URI function %s"),
        UriException.SCHEME_REQUIRED:
            _("Scheme-based resolution requires a URI with a scheme; "
              "neither the base URI %(base)r nor the reference %(ref)r have one."),
        UriException.INVALID_PUBLIC_ID_URN:
            _("A public ID cannot be derived from URN %(urn)r"
              " because it does not conform to RFC 3151."),
        UriException.UNSUPPORTED_SCHEME:
            _("The URI scheme %(scheme)s is not supported by resolver %(resolver)s"),
        UriException.IDNA_UNSUPPORTED:
            _("The URI ref %(uri)r cannot be made urllib-safe on this version of Python (IDNA encoding unsupported)."),
        }


