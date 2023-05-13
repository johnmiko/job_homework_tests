import argparse

from app import app

# For help on running python main.py --help
parser = argparse.ArgumentParser(
    description='Makes an API call to source_url and parses the results to then force the 3rd party to push an API '
                'call back to destination_url for each customer that is in their database')
parser.add_argument("--check_only",
                    help='True=only check what PATCH calls should be made, will not actually make any requests'
                         'calls', default=True, action=argparse.BooleanOptionalAction)
parser.add_argument("--log_file", help='Name of file to output logs of the running process to',
                    default='default_log_file.log')
parser.add_argument("--source_url", help='URL to use for collecting data',
                    default='https://uat-customer-services.cogeco.com:20443/loki/api/v2/wifi?depth=0&pageNumber=1'
                            '&pageSize=1000')
parser.add_argument("--destination_url", help='URL to use for the PATCH call',
                    default='https://uat-customer-services.cogeco.com:20443/loki/api/v2/customer/')
parser.add_argument("--access_token", help='the bearer token to use for the API calls',
                    default='9caad17d-95a4-459c-bcf0-44f6185d5bc1')
args = parser.parse_args()
app(args.check_only, args.log_file, args.source_url, args.destination_url, args.access_token)
