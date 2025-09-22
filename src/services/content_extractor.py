import requests
import trafilatura
from pypdf import PdfReader
import io
from typing import List, Dict

class ContentExtractorService:
	def __init__(self):
		self.session = requests.Session()
		self.session.headers.update({
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
		})
	
	def extract_from_sources(self, sources: List[Dict]) -> str:
		content_parts = []
		for source in sources:
			try:
				response = self.session.get(source['url'], timeout=10)
				if 'pdf' in response.headers.get('content-type', '').lower():
					content = self._extract_pdf_content(response.content)
				else:
					content = self._extract_html_content(response.text)
				if content:
					content_parts.append(f"Source: {source['title']}\nContent: {content[:2000]}")
				else:
					content_parts.append(f"Source: {source['title']}\nContent: {source['snippet']}")
			except Exception as e:
				content_parts.append(f"Source: {source['title']}\nContent: {source['snippet']}")
		return "\n\n".join(content_parts)
	
	def _extract_html_content(self, html_content: str) -> str:
		try:
			extracted = trafilatura.extract(html_content)
			return extracted or ""
		except Exception as e:
			return ""
	
	def _extract_pdf_content(self, pdf_content: bytes) -> str:
		try:
			pdf_file = io.BytesIO(pdf_content)
			reader = PdfReader(pdf_file)
			text = ""
			for page in reader.pages:
				text += page.extract_text() + "\n"
			return text.strip()
		except Exception as e:
			return ""
