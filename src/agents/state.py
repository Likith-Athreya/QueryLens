from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class ResearchState:
	query: str = ""
	sources: List[Dict] = None
	content: str = ""
	summary: str = ""
	key_points: List[str] = None
	report_id: Optional[int] = None
	
	def __post_init__(self):
		if self.sources is None:
			self.sources = []
		if self.key_points is None:
			self.key_points = []
