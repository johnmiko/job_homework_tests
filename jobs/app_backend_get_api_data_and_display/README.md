# codetest-migration-johnmiko

Company - Colony Network

Overall Goal:

To make an API call and parse the results to then force the 3rd party to push an API call back to us for each customer
that is in their database.

Create a migration script in Python

Use argparse to manage command arguments.

would like to see the following command options:

check_only: This will only check what PATCH calls should be made, but will not actually make any PATCH calls log_file:
to output logs of the running process to. source_url: the URL to use for collecting the data destination_url: the URL to
use for the PATCH call access_token: the bearer token to use for the API calls.

What the python script should do:

Make an GET API call to the source_url using the access_token.

For each object in the list, it is matching to a ManagedWiFi record. You will need to go into the supportingResource and
loop through them until you find the type == Customer. You will grab the id from that Customer record and make a PATCH
call to the destination_url and replacing {id} with the id you got from the Customer record. The body of the PATCH call
should be {}

Source URL: https://uat-customer-services.cogeco.com:20443/loki/api/v2/wifi?depth=0&pageNumber=1&pageSize=1000
Access Token: 9caad17d-95a4-459c-bcf0-44f6185d5bc1 Destination
URL: https://uat-customer-services.cogeco.com:20443/loki/api/v2/customer/{id}

Should be logging the customer name and id that we will be making PATCH calls to (and these log entries should appear
even if check-only is enabled). Then should also be logging that each PATCH call was successful. Logging should be going
to stdout no matter what with the log-file command option to also stream to a log file as well.

Here is a sample result you will get back from the GET call. source_url_output.json(1).txt