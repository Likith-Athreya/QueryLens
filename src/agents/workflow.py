from langgraph.graph import StateGraph, END
from .state import ResearchState
from ..services.web_search import WebSearchService
from ..services.content_extractor import ContentExtractorService
from ..services.llm_service import LLMService
from ..database.report_db import ReportDatabase

class ResearchWorkflow:
	def __init__(self):
		self.web_search = WebSearchService()
		self.content_extractor = ContentExtractorService()
		self.llm_service = LLMService()
		self.database = ReportDatabase()
		self.workflow = self._create_workflow()
	
	def _create_workflow(self):
		workflow = StateGraph(ResearchState)
		workflow.add_node("search", self._search_node)
		workflow.add_node("extract", self._extract_node)
		workflow.add_node("summarize", self._summarize_node)
		workflow.add_node("save", self._save_node)
		workflow.set_entry_point("search")
		workflow.add_edge("search", "extract")
		workflow.add_edge("extract", "summarize")
		workflow.add_edge("summarize", "save")
		workflow.add_edge("save", END)
		return workflow.compile()
	
	def _search_node(self, state: ResearchState) -> ResearchState:
		state.sources = self.web_search.search(state.query)
		return state
	
	def _extract_node(self, state: ResearchState) -> ResearchState:
		state.content = self.content_extractor.extract_from_sources(state.sources)
		return state
	
	def _summarize_node(self, state: ResearchState) -> ResearchState:
		state.summary, state.key_points = self.llm_service.summarize_content(
			state.query, state.content
		)
		return state
	
	def _save_node(self, state: ResearchState) -> ResearchState:
		state.report_id = self.database.save_report(
			state.query, state.summary, state.sources, state.key_points
		)
		return state
	
	def process_query(self, query: str) -> dict:
		state = ResearchState()
		state.query = query
		result = self.workflow.invoke(state)
		if hasattr(result, 'report_id'):
			return {
				'status': 'success' if result.report_id else 'error',
				'report_id': result.report_id,
				'query': result.query,
				'summary': result.summary,
				'key_points': result.key_points,
				'sources': result.sources
			}
		else:
			return {
				'status': 'success' if result.get('report_id') else 'error',
				'report_id': result.get('report_id'),
				'query': result.get('query', query),
				'summary': result.get('summary', ''),
				'key_points': result.get('key_points', []),
				'sources': result.get('sources', [])
			}
