import fnmatch
import os
import shutil
import logging
log = logging.getLogger(__name__)

def copy(source, dest):
    matches = []
    source_len = len(source)
    for root, dirnames, filenames in os.walk(source):
        for filename in filenames:
            source_filename = os.path.join(root, filename)
            dest_filename = os.path.join(dest, source_filename[source_len:])
            log.info("Copying: {} to {}".format(source_filename, dest_filename))
            if os.path.exists(dest_filename):
            	os.unlink(dest_filename)
            log.info(os.path.basename(dest_filename))
            try:
            	os.makedirs(os.path.dirname(dest_filename))
            except OSError:
            	pass
            shutil.copy(source_filename, dest_filename)
