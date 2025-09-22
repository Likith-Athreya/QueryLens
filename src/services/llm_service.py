import os
from typing import List, Tuple
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage


class LLMService:
	def __init__(self):
		self.api_key = os.getenv('GROQ_API_KEY')
		if not self.api_key:
			raise ValueError("GROQ_API_KEY environment variable is required")
		self.llm = ChatGroq(
			model="llama-3.1-8b-instant",
			api_key=self.api_key,
			temperature=0.3
		)
	
	def summarize_content(self, query: str, content: str) -> Tuple[str, List[str]]:
		try:
			prompt = f"""
			Based on the following sources about "{query}", create a comprehensive summary and extract key points.
			
			Sources:
			{content}
			
			Please provide:
			1. A 2-3 paragraph summary
			2. 5-7 key points as a bulleted list
			
			Format your response as:
			SUMMARY:
			[Your summary here]
			
			KEY POINTS:
			• [Point 1]
			• [Point 2]
			• [Point 3]
			• [Point 4]
			• [Point 5]
			"""
			response = self.llm.invoke([HumanMessage(content=prompt)])
			content_text = response.content
			if "SUMMARY:" in content_text and "KEY POINTS:" in content_text:
				parts = content_text.split("KEY POINTS:")
				summary = parts[0].replace("SUMMARY:", "").strip()
				key_points_text = parts[1].strip()
				key_points = [point.strip().lstrip('•-* ') 
							for point in key_points_text.split('\n') 
							if point.strip() and point.strip().startswith(('•', '-', '*'))]
				return summary, key_points
			else:
				return content_text, ["Key points could not be extracted"]
		except Exception as e:
			return f"Error generating summary: {e}", ["Error occurred during summarization"]
