import logging

import connexion
from flask_testing import TestCase


class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('DEBUG')
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.add_api('app.yaml')
        return app.app
