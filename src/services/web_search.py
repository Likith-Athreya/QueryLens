import os
from typing import List, Dict
from tavily import TavilyClient


class WebSearchService:
	def __init__(self):
		self.api_key = os.getenv('TAVILY_API_KEY')
		if not self.api_key:
			raise ValueError("TAVILY_API_KEY environment variable is required")
		self.client = TavilyClient(api_key=self.api_key)
	
	def search(self, query: str, max_results: int = 3) -> List[Dict]:
		try:
			response = self.client.search(
				query=query,
				max_results=max_results,
				search_depth="advanced"
			)
			sources = []
			for result in response.get('results', []):
				sources.append({
					'title': result.get('title', 'No title'),
					'url': result.get('url', ''),
					'snippet': result.get('content', ''),
					'score': result.get('score', 0)
				})
			return sources
		except Exception as e:
			return []
