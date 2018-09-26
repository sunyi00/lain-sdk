#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import yaml
from ..util import get_cfd


def load_template(filename):
    template_dir = os.path.join(get_cfd(__file__), 'templates')
    with open(os.path.join(template_dir, filename)) as f:
        return f.read()
