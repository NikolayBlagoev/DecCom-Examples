from deccom.protocols.peerdiscovery.kademliadiscovery import KademliaDiscovery
import asyncio
from deccom.cryptofuncs.hash import SHA256
from deccom.nodes import Node
from deccom.protocols.defaultprotocol import DefaultProtocol
from deccom.peers import Peer
from deccom.protocols.streamprotocol import StreamProtocol
from chat_protocol import ChatProtocol
for i in range(1,10):
    n = Peer(("127.0.0.1", None), pub_key=str(i))
    protocol = DefaultProtocol()
    discovery = KademliaDiscovery([Peer(("127.0.0.1",10010),pub_key="0")],interval=12, always_split = True)
    discovery.set_lower(protocol)
    chat_protocol = ChatProtocol()
    chat_protocol.set_lower(discovery)
    me = Node(n, chat_protocol,ip_addr="127.0.0.1",call_back=print)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(me.listen())
loop.run_forever()
