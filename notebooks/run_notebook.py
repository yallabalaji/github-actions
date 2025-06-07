import os
import time
import logging
from gradient.api_sdk.clients import NotebooksClient

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

API_KEY = os.getenv('PAPERSPACE_API_KEY')
NOTEBOOK_ID = os.getenv('PAPERSPACE_NOTEBOOK_ID')

def main():
    client = NotebooksClient(api_key=API_KEY)

    logging.info('Fetching notebook info...')
    notebook_info = client.get(NOTEBOOK_ID)
    machine_type = notebook_info.vm_type
    logging.info(f'Notebook VM type: {machine_type}')

    logging.info('Starting notebook...')
    notebook_id = client.start(id=NOTEBOOK_ID, machine_type=machine_type)
    logging.info(f'Started notebook with ID: {notebook_id}')

    for i in range(20):
        notebook = client.get(notebook_id)
        logging.info(f'[{i+1}/20] Notebook state: {notebook.state}')
        if notebook.state == 'Stopped':
            logging.info('Notebook run finished.')
            break
        time.sleep(15)
    else:
        logging.warning('Notebook run did not finish within timeout.')

if __name__ == '__main__':
    main()
  
