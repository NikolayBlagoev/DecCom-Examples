from deccom.protocols.peerdiscovery.kademliadiscovery import KademliaDiscovery
import asyncio
from deccom.cryptofuncs.hash import SHA256
from deccom.nodes import Node
from deccom.protocols.defaultprotocol import DefaultProtocol
from deccom.peers import Peer
from deccom.protocols.streamprotocol import StreamProtocol
from chat_protocol import ChatProtocol
import sys
n = Peer(("127.0.0.1", None), pub_key="10")
protocol = DefaultProtocol()
discovery = KademliaDiscovery([Peer(("127.0.0.1",10010),pub_key="0")],interval=12, always_split = True)
discovery.set_lower(protocol)
chat_protocol = ChatProtocol()
chat_protocol.set_lower(discovery)
me = Node(n, chat_protocol,ip_addr="127.0.0.1",call_back=print)
loop = asyncio.get_event_loop()
loop.run_until_complete(me.listen())
while True:
    print("SEND TO: ")
    pub_key = loop.run_until_complete(loop.run_in_executor(None, sys.stdin.readline))[:-1]
    print("MESSAGE: ")
    msg = loop.run_until_complete(loop.run_in_executor(None, sys.stdin.readline))[:-1]
    loop.run_until_complete(chat_protocol.send_msg(msg,pub_key))

loop.run_forever()
