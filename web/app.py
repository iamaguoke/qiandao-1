#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: Binux<i@binux.me>
#         http://binux.me
# Created on 2014-07-30 12:22:52

import os
import logging
import jinja2
import tornado.web

import config
from web.handlers import handlers, ui_modules, ui_methods

class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
                template_path = os.path.join(os.path.dirname(__file__), "tpl"),
                static_path = os.path.join(os.path.dirname(__file__), "static"),
                debug = config.debug,
                gzip = config.gzip,
                )
        super(Application, self).__init__(handlers, **settings)

        self.jinja_env = jinja2.Environment(
                loader=jinja2.FileSystemLoader(settings['template_path']),
                extensions=['jinja2.ext.autoescape', 'jinja2.ext.loopcontrols', ],
                autoescape=True,
                auto_reload=config.debug)

        self.jinja_env.globals.update({
            'config': config,
            })
        self.jinja_env.filters.update(ui_methods)