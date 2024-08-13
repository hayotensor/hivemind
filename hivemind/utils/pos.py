from datetime import datetime
from typing import Dict
from hivemind.p2p import PeerID

class ProofOfStake:
  """
  """
  checkpoint: int = 86400

  def __init__(self):
    self.peer_id_to_stake: Dict[PeerID, bool] = dict()
    self.peer_id_to_checkpoint: Dict[PeerID, int] = dict()

  def check_proof_of_stake(self, peer_id: PeerID) -> bool:
    now = datetime.now().timestamp()
    last_checkpoint = self.peer_id_to_checkpoint.get(peer_id)

    # validate pos for the first time or reevaluate pos again
    if last_checkpoint is None or now - last_checkpoint > self.checkpoint:
      pos = self._proof_of_stake(peer_id)
      if pos:
        self.add_or_update_peer(peer_id)
      else:
        self.add_or_update_peer(peer_id, pos=False)

    # at this point they should be stored 
    return self.peer_id_to_stake[peer_id]

  def _proof_of_stake(self, peer_id: PeerID) -> bool:
    return True

  def add_or_update_peer(self, peer_id: PeerID, pos=True):
    """Add or update a peers staking to True"""
    self.peer_id_to_stake[peer_id] = True
    self.peer_id_to_checkpoint[peer_id] = datetime.now().timestamp()