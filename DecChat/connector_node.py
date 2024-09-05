from deccom.protocols.peerdiscovery.kademliadiscovery import KademliaDiscovery
import asyncio
from deccom.cryptofuncs.hash import SHA256
from deccom.nodes import Node
from deccom.protocols.defaultprotocol import DefaultProtocol
from deccom.peers import Peer
from deccom.protocols.streamprotocol import StreamProtocol

n = Peer(("127.0.0.1", 10010), pub_key="0")
protocol = DefaultProtocol()
discovery = KademliaDiscovery([],interval=12, always_split = True)
discovery.set_lower(protocol)
me = Node(n , discovery,ip_addr="127.0.0.1",port = 10010,call_back=print)
loop = asyncio.get_event_loop()
loop.run_until_complete(me.listen())
loop.run_forever()
