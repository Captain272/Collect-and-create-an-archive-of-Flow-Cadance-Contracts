# Collect-and-create-an-archive-of-Flow-Cadance-Contracts

## Tasks :
- Explore Flow-py-sdk ✅
  [Reference](https://janezpodhostnik.github.io/flow-py-sdk/python_SDK_guide/)

  - Setup for flow-py-sdk incase of errors. [NoteBook](https://colab.research.google.com/drive/1y2cTggVR6AJn03YWPuOKgCeTIugPmTFA?usp=sharing)
  - Documentation for various terms in the sdk and FLOW. 
    The library uses gRPC to communicate with the access nodes and it must be configured with correct access node API URL.

    📖 Access API URLs can be found [here](https://developers.onflow.org/docs/access-api#access-nodes-apis). An error will be returned if the host is unreachable. The Access Nodes APIs hosted by DapperLabs are accessible at:

    - Testnet `access.devnet.nodes.onflow.org:9000`
    - Mainnet `access.mainnet.nodes.onflow.org:9000`
    - Local Emulator `127.0.0.1:3569`

    Example:

    ```python
    async with flow_client(
            host="127.0.0.1", port="3569"
    ) as flow_client:
        # do something with `flow_client`
        
        
    Tried a few calls and still exploring.

        
![image](https://user-images.githubusercontent.com/61205382/221141603-8464482a-b12f-48eb-9eb7-8eabadbb6d6e.png)
        
- Crawl Cadance Contracts: as many as possible (May be 1000?)✅
  ## Done with scraping the cadance contracts. using python contract the code is mentioned above.
  
- Create a corpus of Cadance Contracts✅
  ## And also stored in the repository.
- Upload it to Cloud Storage🎟️






This consist of work for listed tasks in flow.
