import datetime
import logging
import os
import random

import azure.functions as func
from azure.storage.blob import BlobServiceClient

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

   #if mytimer.past_due:
        #logging.info('The timer is past due!')

    # assign random number to variable
    rand = random.randint(1, 1000)

    logging.info(rand)


    # Write to console
    #print('RAND: %s - Python timer trigger function ran at %s', rand, utc_timestamp)

    # Write to Azure Blob Storage
    blob_service_client = BlobServiceClient.from_connection_string(os.environ["AzureWebJobsStorage"])
    container_name = "azure-webjobs-hosts"
    blob_name = f"{utc_timestamp}.txt"
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    #blob_client.upload_blob(f"Python timer trigger function ran at {utc_timestamp}")