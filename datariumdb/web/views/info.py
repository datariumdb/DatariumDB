""" API Index endpoint """

import flask
from flask_restful import Resource

import datariumdb
from datariumdb.web.views.base import base_ws_uri
from datariumdb import version
from datariumdb.web.websocket_server import EVENTS_ENDPOINT


class RootIndex(Resource):
    def get(self):
        docs_url = [
            'https://docs.datariumdb.com/projects/server/en/v',
            version.__version__ + '/'
        ]
        return flask.jsonify({
            'api': {
                'v1': get_api_v1_info('/api/v1/')
            },
            'docs': ''.join(docs_url),
            'software': 'DatariumDB',
            'version': version.__version__,
            'public_key': datariumdb.config['keypair']['public'],
            'keyring': datariumdb.config['keyring']
        })


class ApiV1Index(Resource):
    def get(self):
        return flask.jsonify(get_api_v1_info('/'))


def get_api_v1_info(api_prefix):
    """
    Return a dict with all the information specific for the v1 of the
    api.
    """
    websocket_root = base_ws_uri() + EVENTS_ENDPOINT
    docs_url = [
        'https://docs.datariumdb.com/projects/server/en/v',
        version.__version__,
        '/http-client-server-api.html',
    ]

    return {
        'docs': ''.join(docs_url),
        'transactions': '{}transactions/'.format(api_prefix),
        'statuses': '{}statuses/'.format(api_prefix),
        'assets': '{}assets/'.format(api_prefix),
        'outputs': '{}outputs/'.format(api_prefix),
        'streams': websocket_root
    }
