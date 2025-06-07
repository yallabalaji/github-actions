import os
import time
from gradient.api_sdk.clients import NotebooksClient

API_KEY = os.getenv('PAPERSPACE_API_KEY')
NOTEBOOK_ID = os.getenv('PAPERSPACE_NOTEBOOK_ID')

def main():
    client = NotebooksClient(api_key=API_KEY)

    # Fetch notebook details to get machine_type
    notebook_info = client.get(NOTEBOOK_ID)
    machine_type = notebook_info.vm_type

    # Start notebook with machine_type
    notebook_id = client.start(id=NOTEBOOK_ID, machine_type=machine_type)
    print(f'Started notebook with ID: {notebook_id}')

    # Poll status until stopped or timeout
    for _ in range(20):
        notebook = client.get(notebook_id)
        print(f'Notebook state: {notebook.state}')
        if notebook.state == 'Stopped':
            print('Notebook run finished.')
            break
        time.sleep(15)
    else:
        print('Notebook run did not finish within timeout.')

if __name__ == '__main__':
    main()
