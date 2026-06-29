from pydantic import BaseModel
from typing import List, Optional

class Party(BaseModel):
    id: Optional[str] = None
    tag: str  # Owner, Buyer, Witness
    name: Optional[str] = ""
    address: Optional[str] = ""
    id_number: Optional[str] = ""

class AgreementState(BaseModel):
    document_type: str = "General Agreement"
    parties: List[Party]
    clauses: List[str] = []