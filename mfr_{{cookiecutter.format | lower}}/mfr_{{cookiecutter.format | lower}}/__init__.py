# -*- coding: utf-8 -*-

from mfr.core import FileHandler, get_file_extension

__version__ = '0.1.0'

EXTENSIONS = [
    # TODO: finish this list
]


class Handler(FileHandler):
    # Renderers and exporters are callables
    renderers = {
        # TODO
        # 'html': renderer
    }

    def detect(self, fp):
        return get_file_extension(fp.name) in EXTENSIONS