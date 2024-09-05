from deccom.protocols.abstractprotocol import AbstractProtocol
from deccom.protocols.wrappers import bindto
from deccom.peers import Peer
from deccom.cryptofuncs import SHA256

class ChatProtocol(AbstractProtocol):
    def __init__(self, submodule = None, callback = lambda addr, data: ...):
        super().__init__(submodule,callback)

    @bindto("find_peer")
    async def _lower_find_peer(self, node_id) -> Peer:
        return

    
    def process_datagram(self,addr,msg):
        print(self.peer.pub_key, ": RECEIVED MESSAGE ", msg.decode("utf-8"))


    async def send_msg(self, msg, pub_key):
        node_id = SHA256(pub_key)
        print("sending",msg,"to",pub_key)
        p = await self._lower_find_peer(node_id)
        await self.send_datagram(msg.encode("utf-8"),p.addr)

    

