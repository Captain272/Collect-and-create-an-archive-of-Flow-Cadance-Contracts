import flow_py_sdk
from flow_py_sdk import flow_client
from asyncio import run
import asyncio
from flow_py_sdk.cadence import Address
# from asyncio import async


# fl=flow_client(host="access.devnet.nodes.onflow.org", port="9000")


# loop = asyncio.get_event_loop()
# loop.run_until_complete(fl.get_account_at_block_height(address=b'0x28e3764c0d5c5ead', block_height=0))

async def latest_block():
    async with flow_client(host="access.devnet.nodes.onflow.org", port=9000) as client:
        latest_block = await client.get_latest_block()
        block = await client.get_block_by_height(
            height=latest_block.height
        )
        print("Block ID: {}".format(block.id.hex()))
        print("Block data: {}".format(block.__dict__))
        print("Block height: {}".format(block.height))
        print("Block timestamp: [{}]".format(block.timestamp))

        add=Address.from_hex('0x912d5440f7e3769e')
        account = await client.get_account(
            address=add.bytes
        )
        print("Account Address: {}".format(account.address.hex()))
        print("Account Balance: {}".format(account.balance))
        print("Account Contracts: {}".format(len(account.contracts)))
        print("Account Keys: {}".format(len(account.keys)))


        block = await client.get_latest_block(is_sealed=True)
        collection_id = block.collection_guarantees[0].collection_id

        collection = await client.get_collection_by_i_d(id=collection_id)
        print("ID: {}".format(collection.id.hex()))
        print(
            "Transactions: [{}]".format(
                ", ".join(x.hex() for x in collection.transaction_ids)
            )
        )


run(latest_block())
# run(acc_data())


# loop = asyncio.get_event_loop()
# loop.run_until_complete(fl.get_account_at_block_height(address=b'0x28e3764c0d5c5ead', block_height=0))


# print()
# data=run(fl.get_account())
# for i in fl:
#     print(i.strip())


# from flow_py_sdk import account
# account_address = "0x99d6b420bf362b47223c95a34daf4c869ec4e2b87d57c3f1b2e539f00a992507"
# balance = account.get_balance(fl, account_address)
# print("Account Balance: {}".format(balance))

# account=fl.get_latest_block_header()
# (account)print("Block ID: {}".format(block.id.hex()))
# asyncio.await account()