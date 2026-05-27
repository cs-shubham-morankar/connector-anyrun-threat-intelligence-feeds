"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

import traceback
from connectors.cyops_utilities.builtins import create_file_from_string
from connectors.core.connector import get_logger, ConnectorError
from datetime import datetime, timedelta
from .constants import VERSION, DATE_TIME_FORMAT

from anyrun.connectors import FeedsConnector
from anyrun.iterators import FeedsIterator
from anyrun import RunTimeException

try:
    from connectors.cyops_utilities.files import save_file_in_env
    from connectors.cyops_utilities.files import get_ingestion_base_dir
except:
    # ignore. lower FSR version
    pass

try:
    from integrations.crudhub import trigger_ingest_playbook
except:
    pass

logger = get_logger('anyrun-threat-intelligence-feeds')


def exceptions_handler(function):
    """ Handles errors in functions """

    def wrapper(*args, **kwargs):

        try:
            return function(*args, **kwargs)
        except RunTimeException as error:
            logger.exception(str(error))
            raise ConnectorError(f'ANY.RUN Exception: {str(error)}')
        except Exception:
            error = traceback.format_exc()
            logger.exception(error)
            raise ConnectorError(f'Unspecified Exception: {error}')

    return wrapper


def get_params(params):
    """ Extracts input params """
    if params.get('collection_type'):
        params.pop('collection_type')
    params = {k: v for k, v in params.items() if v is not None and v != ''}
    return params


@exceptions_handler
def fetch_indicators(config, params, **kwargs):
    """ Fetch indicators from the ANY.RUN TI Feeds and saves them according to the specified parameters """
    params = get_params(params)
    mode = params.get('output_mode')
    collection = params.get('collectionType').lower()
    fetch_depth = params.get('feedFetchDepth')
    token = config.get('apiKey')
    verify_ssl = config.get('verify_ssl')

    indicators: list[dict | None] = []

    with FeedsConnector(api_key=token, integration=VERSION, verify_ssl=verify_ssl) as connector:
        for feeds in FeedsIterator.taxii_stix(
                connector,
                collection=collection,
                match_type='indicator',
                match_version='all',
                chunk_size=1000,
                modified_after=(
                        datetime.now() - timedelta(days=fetch_depth)
                ).strftime(DATE_TIME_FORMAT)
        ):
            for feed in feeds:
                indicators.append(feed)

    seen = set()
    deduped_indicators = [x for x in indicators if [x["pattern"] not in seen, seen.add(x["pattern"])][0]]

    if mode == 'Create as Feed Records in FortiSOAR':
        create_pb_id = params.get("create_pb_id")
        trigger_ingest_playbook(deduped_indicators, create_pb_id, parent_env=kwargs.get('env', {}), batch_size=1000,
                                dedup_field="pattern")
        return 'Successfully triggered playbooks to create feed records'

    objects = {'objects': deduped_indicators}

    if mode == 'Save to File':
        return create_file_from_string(contents=objects, filename=params.get('filename'))
    else:
        return objects


@exceptions_handler
def _check_health(config, **kwargs):
    """ Checks connection with ANY.RUN """
    token = config.get('apiKey')
    verify_ssl = config.get('verify_ssl')

    with FeedsConnector(api_key=token, integration=VERSION, verify_ssl=verify_ssl) as connector:
        connector.check_authorization()

    logger.info('Connector is available.')
    return True


operations = {
    'fetch_indicators': fetch_indicators
}
