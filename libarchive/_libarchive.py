# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('__libarchive', [dirname(__file__)])
        except ImportError:
            import __libarchive
            return __libarchive
        if fp is not None:
            try:
                _mod = imp.load_module('__libarchive', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    __libarchive = swig_import_helper()
    del swig_import_helper
else:
    import __libarchive
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def archive_read_new():
  return __libarchive.archive_read_new()
archive_read_new = __libarchive.archive_read_new

def archive_read_free(*args):
  return __libarchive.archive_read_free(*args)
archive_read_free = __libarchive.archive_read_free

def archive_read_open_filename(*args):
  return __libarchive.archive_read_open_filename(*args)
archive_read_open_filename = __libarchive.archive_read_open_filename

def archive_read_open_memory(*args):
  return __libarchive.archive_read_open_memory(*args)
archive_read_open_memory = __libarchive.archive_read_open_memory

def archive_read_open_memory2(*args):
  return __libarchive.archive_read_open_memory2(*args)
archive_read_open_memory2 = __libarchive.archive_read_open_memory2

def archive_read_open_fd(*args):
  return __libarchive.archive_read_open_fd(*args)
archive_read_open_fd = __libarchive.archive_read_open_fd

def archive_read_close(*args):
  return __libarchive.archive_read_close(*args)
archive_read_close = __libarchive.archive_read_close

def archive_format(*args):
  return __libarchive.archive_format(*args)
archive_format = __libarchive.archive_format

def archive_read_next_header2(*args):
  return __libarchive.archive_read_next_header2(*args)
archive_read_next_header2 = __libarchive.archive_read_next_header2

def archive_entry_stat(*args):
  return __libarchive.archive_entry_stat(*args)
archive_entry_stat = __libarchive.archive_entry_stat

def archive_read_header_position(*args):
  return __libarchive.archive_read_header_position(*args)
archive_read_header_position = __libarchive.archive_read_header_position

def archive_read_data_skip(*args):
  return __libarchive.archive_read_data_skip(*args)
archive_read_data_skip = __libarchive.archive_read_data_skip

def archive_read_data_into_fd(*args):
  return __libarchive.archive_read_data_into_fd(*args)
archive_read_data_into_fd = __libarchive.archive_read_data_into_fd

def archive_read_support_filter_all(*args):
  return __libarchive.archive_read_support_filter_all(*args)
archive_read_support_filter_all = __libarchive.archive_read_support_filter_all

def archive_read_support_filter_bzip2(*args):
  return __libarchive.archive_read_support_filter_bzip2(*args)
archive_read_support_filter_bzip2 = __libarchive.archive_read_support_filter_bzip2

def archive_read_support_filter_compress(*args):
  return __libarchive.archive_read_support_filter_compress(*args)
archive_read_support_filter_compress = __libarchive.archive_read_support_filter_compress

def archive_read_support_filter_gzip(*args):
  return __libarchive.archive_read_support_filter_gzip(*args)
archive_read_support_filter_gzip = __libarchive.archive_read_support_filter_gzip

def archive_read_support_filter_lzip(*args):
  return __libarchive.archive_read_support_filter_lzip(*args)
archive_read_support_filter_lzip = __libarchive.archive_read_support_filter_lzip

def archive_read_support_filter_lzma(*args):
  return __libarchive.archive_read_support_filter_lzma(*args)
archive_read_support_filter_lzma = __libarchive.archive_read_support_filter_lzma

def archive_read_support_filter_none(*args):
  return __libarchive.archive_read_support_filter_none(*args)
archive_read_support_filter_none = __libarchive.archive_read_support_filter_none

def archive_read_support_filter_rpm(*args):
  return __libarchive.archive_read_support_filter_rpm(*args)
archive_read_support_filter_rpm = __libarchive.archive_read_support_filter_rpm

def archive_read_support_filter_uu(*args):
  return __libarchive.archive_read_support_filter_uu(*args)
archive_read_support_filter_uu = __libarchive.archive_read_support_filter_uu

def archive_read_support_filter_xz(*args):
  return __libarchive.archive_read_support_filter_xz(*args)
archive_read_support_filter_xz = __libarchive.archive_read_support_filter_xz

def archive_read_support_format_all(*args):
  return __libarchive.archive_read_support_format_all(*args)
archive_read_support_format_all = __libarchive.archive_read_support_format_all

def archive_read_support_format_7zip(*args):
  return __libarchive.archive_read_support_format_7zip(*args)
archive_read_support_format_7zip = __libarchive.archive_read_support_format_7zip

def archive_read_support_format_ar(*args):
  return __libarchive.archive_read_support_format_ar(*args)
archive_read_support_format_ar = __libarchive.archive_read_support_format_ar

def archive_read_support_format_cab(*args):
  return __libarchive.archive_read_support_format_cab(*args)
archive_read_support_format_cab = __libarchive.archive_read_support_format_cab

def archive_read_support_format_cpio(*args):
  return __libarchive.archive_read_support_format_cpio(*args)
archive_read_support_format_cpio = __libarchive.archive_read_support_format_cpio

def archive_read_support_format_empty(*args):
  return __libarchive.archive_read_support_format_empty(*args)
archive_read_support_format_empty = __libarchive.archive_read_support_format_empty

def archive_read_support_format_gnutar(*args):
  return __libarchive.archive_read_support_format_gnutar(*args)
archive_read_support_format_gnutar = __libarchive.archive_read_support_format_gnutar

def archive_read_support_format_iso9660(*args):
  return __libarchive.archive_read_support_format_iso9660(*args)
archive_read_support_format_iso9660 = __libarchive.archive_read_support_format_iso9660

def archive_read_support_format_lha(*args):
  return __libarchive.archive_read_support_format_lha(*args)
archive_read_support_format_lha = __libarchive.archive_read_support_format_lha

def archive_read_support_format_rar(*args):
  return __libarchive.archive_read_support_format_rar(*args)
archive_read_support_format_rar = __libarchive.archive_read_support_format_rar

def archive_read_support_format_raw(*args):
  return __libarchive.archive_read_support_format_raw(*args)
archive_read_support_format_raw = __libarchive.archive_read_support_format_raw

def archive_read_support_format_tar(*args):
  return __libarchive.archive_read_support_format_tar(*args)
archive_read_support_format_tar = __libarchive.archive_read_support_format_tar

def archive_read_support_format_xar(*args):
  return __libarchive.archive_read_support_format_xar(*args)
archive_read_support_format_xar = __libarchive.archive_read_support_format_xar

def archive_read_support_format_zip(*args):
  return __libarchive.archive_read_support_format_zip(*args)
archive_read_support_format_zip = __libarchive.archive_read_support_format_zip

def archive_write_new():
  return __libarchive.archive_write_new()
archive_write_new = __libarchive.archive_write_new

def archive_write_free(*args):
  return __libarchive.archive_write_free(*args)
archive_write_free = __libarchive.archive_write_free

def archive_write_open(*args):
  return __libarchive.archive_write_open(*args)
archive_write_open = __libarchive.archive_write_open

def archive_write_open_fd(*args):
  return __libarchive.archive_write_open_fd(*args)
archive_write_open_fd = __libarchive.archive_write_open_fd

def archive_write_open_filename(*args):
  return __libarchive.archive_write_open_filename(*args)
archive_write_open_filename = __libarchive.archive_write_open_filename

def archive_write_open_filename_w(*args):
  return __libarchive.archive_write_open_filename_w(*args)
archive_write_open_filename_w = __libarchive.archive_write_open_filename_w

def archive_write_open_memory(*args):
  return __libarchive.archive_write_open_memory(*args)
archive_write_open_memory = __libarchive.archive_write_open_memory

def archive_write_close(*args):
  return __libarchive.archive_write_close(*args)
archive_write_close = __libarchive.archive_write_close

def archive_write_header(*args):
  return __libarchive.archive_write_header(*args)
archive_write_header = __libarchive.archive_write_header

def archive_write_finish_entry(*args):
  return __libarchive.archive_write_finish_entry(*args)
archive_write_finish_entry = __libarchive.archive_write_finish_entry

def archive_write_add_filter_bzip2(*args):
  return __libarchive.archive_write_add_filter_bzip2(*args)
archive_write_add_filter_bzip2 = __libarchive.archive_write_add_filter_bzip2

def archive_write_add_filter_compress(*args):
  return __libarchive.archive_write_add_filter_compress(*args)
archive_write_add_filter_compress = __libarchive.archive_write_add_filter_compress

def archive_write_add_filter_gzip(*args):
  return __libarchive.archive_write_add_filter_gzip(*args)
archive_write_add_filter_gzip = __libarchive.archive_write_add_filter_gzip

def archive_write_add_filter_lzip(*args):
  return __libarchive.archive_write_add_filter_lzip(*args)
archive_write_add_filter_lzip = __libarchive.archive_write_add_filter_lzip

def archive_write_add_filter_lzma(*args):
  return __libarchive.archive_write_add_filter_lzma(*args)
archive_write_add_filter_lzma = __libarchive.archive_write_add_filter_lzma

def archive_write_add_filter_none(*args):
  return __libarchive.archive_write_add_filter_none(*args)
archive_write_add_filter_none = __libarchive.archive_write_add_filter_none

def archive_write_add_filter_xz(*args):
  return __libarchive.archive_write_add_filter_xz(*args)
archive_write_add_filter_xz = __libarchive.archive_write_add_filter_xz

def archive_write_set_format(*args):
  return __libarchive.archive_write_set_format(*args)
archive_write_set_format = __libarchive.archive_write_set_format

def archive_write_set_format_by_name(*args):
  return __libarchive.archive_write_set_format_by_name(*args)
archive_write_set_format_by_name = __libarchive.archive_write_set_format_by_name

def archive_write_set_format_ar_bsd(*args):
  return __libarchive.archive_write_set_format_ar_bsd(*args)
archive_write_set_format_ar_bsd = __libarchive.archive_write_set_format_ar_bsd

def archive_write_set_format_ar_svr4(*args):
  return __libarchive.archive_write_set_format_ar_svr4(*args)
archive_write_set_format_ar_svr4 = __libarchive.archive_write_set_format_ar_svr4

def archive_write_set_format_cpio(*args):
  return __libarchive.archive_write_set_format_cpio(*args)
archive_write_set_format_cpio = __libarchive.archive_write_set_format_cpio

def archive_write_set_format_cpio_newc(*args):
  return __libarchive.archive_write_set_format_cpio_newc(*args)
archive_write_set_format_cpio_newc = __libarchive.archive_write_set_format_cpio_newc

def archive_write_set_format_gnutar(*args):
  return __libarchive.archive_write_set_format_gnutar(*args)
archive_write_set_format_gnutar = __libarchive.archive_write_set_format_gnutar

def archive_write_set_format_iso9660(*args):
  return __libarchive.archive_write_set_format_iso9660(*args)
archive_write_set_format_iso9660 = __libarchive.archive_write_set_format_iso9660

def archive_write_set_format_pax(*args):
  return __libarchive.archive_write_set_format_pax(*args)
archive_write_set_format_pax = __libarchive.archive_write_set_format_pax

def archive_write_set_format_pax_restricted(*args):
  return __libarchive.archive_write_set_format_pax_restricted(*args)
archive_write_set_format_pax_restricted = __libarchive.archive_write_set_format_pax_restricted

def archive_write_set_format_shar(*args):
  return __libarchive.archive_write_set_format_shar(*args)
archive_write_set_format_shar = __libarchive.archive_write_set_format_shar

def archive_write_set_format_shar_dump(*args):
  return __libarchive.archive_write_set_format_shar_dump(*args)
archive_write_set_format_shar_dump = __libarchive.archive_write_set_format_shar_dump

def archive_write_set_format_ustar(*args):
  return __libarchive.archive_write_set_format_ustar(*args)
archive_write_set_format_ustar = __libarchive.archive_write_set_format_ustar

def archive_write_set_format_xar(*args):
  return __libarchive.archive_write_set_format_xar(*args)
archive_write_set_format_xar = __libarchive.archive_write_set_format_xar

def archive_write_set_format_zip(*args):
  return __libarchive.archive_write_set_format_zip(*args)
archive_write_set_format_zip = __libarchive.archive_write_set_format_zip

def archive_entry_new():
  return __libarchive.archive_entry_new()
archive_entry_new = __libarchive.archive_entry_new

def archive_entry_free(*args):
  return __libarchive.archive_entry_free(*args)
archive_entry_free = __libarchive.archive_entry_free

def archive_entry_pathname(*args):
  return __libarchive.archive_entry_pathname(*args)
archive_entry_pathname = __libarchive.archive_entry_pathname

def archive_entry_pathname_w(*args):
  return __libarchive.archive_entry_pathname_w(*args)
archive_entry_pathname_w = __libarchive.archive_entry_pathname_w

def archive_entry_size(*args):
  return __libarchive.archive_entry_size(*args)
archive_entry_size = __libarchive.archive_entry_size

def archive_entry_mtime(*args):
  return __libarchive.archive_entry_mtime(*args)
archive_entry_mtime = __libarchive.archive_entry_mtime

def archive_entry_symlink(*args):
  return __libarchive.archive_entry_symlink(*args)
archive_entry_symlink = __libarchive.archive_entry_symlink

def archive_entry_filetype(*args):
  return __libarchive.archive_entry_filetype(*args)
archive_entry_filetype = __libarchive.archive_entry_filetype

def archive_entry_perm(*args):
  return __libarchive.archive_entry_perm(*args)
archive_entry_perm = __libarchive.archive_entry_perm

def archive_entry_set_pathname(*args):
  return __libarchive.archive_entry_set_pathname(*args)
archive_entry_set_pathname = __libarchive.archive_entry_set_pathname

def archive_entry_set_size(*args):
  return __libarchive.archive_entry_set_size(*args)
archive_entry_set_size = __libarchive.archive_entry_set_size

def archive_entry_set_mtime(*args):
  return __libarchive.archive_entry_set_mtime(*args)
archive_entry_set_mtime = __libarchive.archive_entry_set_mtime

def archive_entry_set_symlink(*args):
  return __libarchive.archive_entry_set_symlink (*args)
archive_entry_set_symlink = __libarchive.archive_entry_set_symlink

def archive_entry_set_link(*args):
  return __libarchive.archive_entry_set_link (*args)
archive_entry_set_link = __libarchive.archive_entry_set_link

def archive_entry_set_filetype(*args):
  return __libarchive.archive_entry_set_filetype(*args)
archive_entry_set_filetype = __libarchive.archive_entry_set_filetype

def archive_entry_set_perm(*args):
  return __libarchive.archive_entry_set_perm(*args)
archive_entry_set_perm = __libarchive.archive_entry_set_perm

def archive_errno(*args):
  return __libarchive.archive_errno(*args)
archive_errno = __libarchive.archive_errno

def archive_error_string(*args):
  return __libarchive.archive_error_string(*args)
archive_error_string = __libarchive.archive_error_string
ARCHIVE_VERSION_NUMBER = __libarchive.ARCHIVE_VERSION_NUMBER
ARCHIVE_VERSION_STRING = __libarchive.ARCHIVE_VERSION_STRING
ARCHIVE_EOF = __libarchive.ARCHIVE_EOF
ARCHIVE_OK = __libarchive.ARCHIVE_OK
ARCHIVE_RETRY = __libarchive.ARCHIVE_RETRY
ARCHIVE_WARN = __libarchive.ARCHIVE_WARN
ARCHIVE_FAILED = __libarchive.ARCHIVE_FAILED
ARCHIVE_FATAL = __libarchive.ARCHIVE_FATAL
ARCHIVE_FILTER_NONE = __libarchive.ARCHIVE_FILTER_NONE
ARCHIVE_FILTER_GZIP = __libarchive.ARCHIVE_FILTER_GZIP
ARCHIVE_FILTER_BZIP2 = __libarchive.ARCHIVE_FILTER_BZIP2
ARCHIVE_FILTER_COMPRESS = __libarchive.ARCHIVE_FILTER_COMPRESS
ARCHIVE_FILTER_PROGRAM = __libarchive.ARCHIVE_FILTER_PROGRAM
ARCHIVE_FILTER_LZMA = __libarchive.ARCHIVE_FILTER_LZMA
ARCHIVE_FILTER_XZ = __libarchive.ARCHIVE_FILTER_XZ
ARCHIVE_FILTER_UU = __libarchive.ARCHIVE_FILTER_UU
ARCHIVE_FILTER_RPM = __libarchive.ARCHIVE_FILTER_RPM
ARCHIVE_FILTER_LZIP = __libarchive.ARCHIVE_FILTER_LZIP
ARCHIVE_FORMAT_BASE_MASK = __libarchive.ARCHIVE_FORMAT_BASE_MASK
ARCHIVE_FORMAT_CPIO = __libarchive.ARCHIVE_FORMAT_CPIO
ARCHIVE_FORMAT_CPIO_POSIX = __libarchive.ARCHIVE_FORMAT_CPIO_POSIX
ARCHIVE_FORMAT_CPIO_BIN_LE = __libarchive.ARCHIVE_FORMAT_CPIO_BIN_LE
ARCHIVE_FORMAT_CPIO_BIN_BE = __libarchive.ARCHIVE_FORMAT_CPIO_BIN_BE
ARCHIVE_FORMAT_CPIO_SVR4_NOCRC = __libarchive.ARCHIVE_FORMAT_CPIO_SVR4_NOCRC
ARCHIVE_FORMAT_CPIO_SVR4_CRC = __libarchive.ARCHIVE_FORMAT_CPIO_SVR4_CRC
ARCHIVE_FORMAT_CPIO_AFIO_LARGE = __libarchive.ARCHIVE_FORMAT_CPIO_AFIO_LARGE
ARCHIVE_FORMAT_SHAR = __libarchive.ARCHIVE_FORMAT_SHAR
ARCHIVE_FORMAT_SHAR_BASE = __libarchive.ARCHIVE_FORMAT_SHAR_BASE
ARCHIVE_FORMAT_SHAR_DUMP = __libarchive.ARCHIVE_FORMAT_SHAR_DUMP
ARCHIVE_FORMAT_TAR = __libarchive.ARCHIVE_FORMAT_TAR
ARCHIVE_FORMAT_TAR_USTAR = __libarchive.ARCHIVE_FORMAT_TAR_USTAR
ARCHIVE_FORMAT_TAR_PAX_INTERCHANGE = __libarchive.ARCHIVE_FORMAT_TAR_PAX_INTERCHANGE
ARCHIVE_FORMAT_TAR_PAX_RESTRICTED = __libarchive.ARCHIVE_FORMAT_TAR_PAX_RESTRICTED
ARCHIVE_FORMAT_TAR_GNUTAR = __libarchive.ARCHIVE_FORMAT_TAR_GNUTAR
ARCHIVE_FORMAT_ISO9660 = __libarchive.ARCHIVE_FORMAT_ISO9660
ARCHIVE_FORMAT_ISO9660_ROCKRIDGE = __libarchive.ARCHIVE_FORMAT_ISO9660_ROCKRIDGE
ARCHIVE_FORMAT_ZIP = __libarchive.ARCHIVE_FORMAT_ZIP
ARCHIVE_FORMAT_EMPTY = __libarchive.ARCHIVE_FORMAT_EMPTY
ARCHIVE_FORMAT_AR = __libarchive.ARCHIVE_FORMAT_AR
ARCHIVE_FORMAT_AR_GNU = __libarchive.ARCHIVE_FORMAT_AR_GNU
ARCHIVE_FORMAT_AR_BSD = __libarchive.ARCHIVE_FORMAT_AR_BSD
ARCHIVE_FORMAT_MTREE = __libarchive.ARCHIVE_FORMAT_MTREE
ARCHIVE_FORMAT_RAW = __libarchive.ARCHIVE_FORMAT_RAW
ARCHIVE_FORMAT_XAR = __libarchive.ARCHIVE_FORMAT_XAR
ARCHIVE_FORMAT_LHA = __libarchive.ARCHIVE_FORMAT_LHA
ARCHIVE_FORMAT_CAB = __libarchive.ARCHIVE_FORMAT_CAB
ARCHIVE_FORMAT_RAR = __libarchive.ARCHIVE_FORMAT_RAR
ARCHIVE_FORMAT_7ZIP = __libarchive.ARCHIVE_FORMAT_7ZIP
ARCHIVE_EXTRACT_OWNER = __libarchive.ARCHIVE_EXTRACT_OWNER
ARCHIVE_EXTRACT_PERM = __libarchive.ARCHIVE_EXTRACT_PERM
ARCHIVE_EXTRACT_TIME = __libarchive.ARCHIVE_EXTRACT_TIME
ARCHIVE_EXTRACT_NO_OVERWRITE = __libarchive.ARCHIVE_EXTRACT_NO_OVERWRITE
ARCHIVE_EXTRACT_UNLINK = __libarchive.ARCHIVE_EXTRACT_UNLINK
ARCHIVE_EXTRACT_ACL = __libarchive.ARCHIVE_EXTRACT_ACL
ARCHIVE_EXTRACT_FFLAGS = __libarchive.ARCHIVE_EXTRACT_FFLAGS
ARCHIVE_EXTRACT_XATTR = __libarchive.ARCHIVE_EXTRACT_XATTR
ARCHIVE_EXTRACT_SECURE_SYMLINKS = __libarchive.ARCHIVE_EXTRACT_SECURE_SYMLINKS
ARCHIVE_EXTRACT_SECURE_NODOTDOT = __libarchive.ARCHIVE_EXTRACT_SECURE_NODOTDOT
ARCHIVE_EXTRACT_NO_AUTODIR = __libarchive.ARCHIVE_EXTRACT_NO_AUTODIR
ARCHIVE_EXTRACT_NO_OVERWRITE_NEWER = __libarchive.ARCHIVE_EXTRACT_NO_OVERWRITE_NEWER
ARCHIVE_EXTRACT_SPARSE = __libarchive.ARCHIVE_EXTRACT_SPARSE
ARCHIVE_EXTRACT_MAC_METADATA = __libarchive.ARCHIVE_EXTRACT_MAC_METADATA

def archive_read_data_into_str(*args):
  return __libarchive.archive_read_data_into_str(*args)
archive_read_data_into_str = __libarchive.archive_read_data_into_str

def archive_write_data_from_str(*args):
  return __libarchive.archive_write_data_from_str(*args)
archive_write_data_from_str = __libarchive.archive_write_data_from_str
# This file is compatible with both classic and new-style classes.


