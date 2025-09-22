import sys
import os
from ..agents.workflow import ResearchWorkflow
from ..database.report_db import ReportDatabase


def main():
	if len(sys.argv) < 2:
		print("Usage: python -m src.utils.cli <query>")
		print("Example: python -m src.utils.cli 'Latest research on AI in education'")
		sys.exit(1)
	query = " ".join(sys.argv[1:])
	print(f"🔍 Processing query: {query}")
	try:
		workflow = ResearchWorkflow()
		result = workflow.process_query(query)
		if result['status'] == 'success':
			print(f"\n✅ Report generated successfully! (ID: {result['report_id']})")
			print(f"\n📝 Summary:")
			print(result['summary'])
			print(f"\n🎯 Key Points:")
			for point in result['key_points']:
				print(f"• {point}")
			print(f"\n🔗 Sources:")
			for i, source in enumerate(result['sources'], 1):
				print(f"{i}. {source['title']} - {source['url']}")
		else:
			print("❌ Failed to generate report")
	except Exception as e:
		print(f"❌ Error: {e}")

if __name__ == "__main__":
	main()
