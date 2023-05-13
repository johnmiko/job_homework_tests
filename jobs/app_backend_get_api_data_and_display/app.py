import logging

import requests
from requests import RequestException


def create_logger(name, log_file):
    logging.basicConfig(filename=log_file,
                        filemode='a',
                        format='%(asctime)s, %(message)s',
                        datefmt='%Y-%M-%d %H:%M:%S',
                        level=logging.INFO)
    level = logging.INFO
    logger = logging.getLogger(name)
    logger.setLevel(level)
    c_handler = logging.StreamHandler()
    c_handler.setLevel(level)
    logger.addHandler(c_handler)
    return logger


def app(check_only, log_file, source_url, destination_url, access_token):
    logger = create_logger(__name__, log_file)
    print('running app')
    headers = {'Authorization': f'Bearer {access_token}'}
    r_get = requests.get(source_url, headers=headers)
    data = r_get.json()
    if r_get.status_code != 200:
        error_message = f'Error sending a get request to {source_url}\n' \
                        f'status_code: {r_get.status_code}\n' \
                        f'error: {data["error"]}\n' \
                        f'error description: {data["error_description"]}'
        logger.error(error_message)
        raise RequestException(error_message)

    for item in data:
        if item['type'] == 'ManagedWiFi':
            for resource in item['supportingResource']:
                logger.debug(resource['type'])
                # James said that each item can have multiple resources with type=Customer
                if resource['type'] == 'Customer':
                    id = resource["id"]
                    if check_only:
                        logger.info(
                            f'patch call SHOULD be made for customer name={resource["name"]},id={id}')
                    else:
                        destination_url_whole = f'{destination_url}{id}'
                        r_patch = requests.patch(destination_url_whole, headers=headers,
                                                 json={"Source URL": source_url,
                                                       "Access Token": access_token,
                                                       "Destination URL": destination_url_whole})
                        logger.info(
                            f'patch call WAS made for customer name={resource["name"]},id={id},status_code={r_patch.status_code},ok={r_patch.ok}')
    print('finished running app')


if __name__ == "__main__":
    check_only = True
    log_file = 'default_log_file.log'
    source_url = 'https://uat-customer-services.cogeco.com:20443/loki/api/v2/wifi?depth=0&pageNumber=1&pageSize=1000'
    access_token = '9caad17d-95a4-459c-bcf0-44f6185d5bc1'
    destination_url = 'https://uat-customer-services.cogeco.com:20443/loki/api/v2/customer/'
    app(check_only, log_file, source_url, destination_url, access_token)
