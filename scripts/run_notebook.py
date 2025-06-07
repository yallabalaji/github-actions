import os
import time
from gradient.api_sdk.clients import NotebooksClient

API_KEY = os.getenv("PAPERSPACE_API_KEY")
NOTEBOOK_ID = os.getenv("PAPERSPACE_NOTEBOOK_ID")

def main():
    client = NotebooksClient(api_key=API_KEY)

    # Start the notebook
    notebook_id = client.start(id=NOTEBOOK_ID)
    print(f"Started notebook with ID: {notebook_id}")

    # Poll notebook status (optional)
    for _ in range(20):  # Poll max 20 times, ~5 mins total if sleep 15s
        notebook = client.get(notebook_id)
        print(f"Notebook state: {notebook.state}")
        if notebook.state == "Stopped":
            print("Notebook run finished.")
            break
        time.sleep(15)
    else:
        print("Notebook run did not finish within timeout.")

if __name__ == "__main__":
    main()
