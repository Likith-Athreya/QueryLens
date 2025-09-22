import streamlit as st
import os
from dotenv import load_dotenv
from ..agents.workflow import ResearchWorkflow
from ..database.report_db import ReportDatabase

load_dotenv()

st.set_page_config(page_title="QueryLens", page_icon="🔍", layout="wide")

if not os.getenv('GROQ_API_KEY') or not os.getenv('TAVILY_API_KEY'):
	st.error("⚠️ Please set GROQ_API_KEY and TAVILY_API_KEY in your .env file")
	st.stop()

@st.cache_resource
def get_workflow():
	return ResearchWorkflow()

@st.cache_resource
def get_database():
	return ReportDatabase()

def main():
	st.title("🔍 QueryLens - AI Research Agent")
	with st.sidebar:
		st.header("Navigation")
		page = st.selectbox("Choose page:", ["🏠 Research", "📋 Reports"])
		db = get_database()
		reports = db.get_all_reports()
		st.metric("Total Reports", len(reports))
	if page == "🏠 Research":
		research_page(get_workflow())
	elif page == "📋 Reports":
		reports_page(get_database())

def research_page(workflow):
	st.header("Start Your Research")
	with st.form("research_form"):
		query = st.text_area(
			"What would you like to research?",
			placeholder="e.g., Latest research on AI in education...",
			height=100
		)
		submitted = st.form_submit_button("🔍 Generate Report", use_container_width=True)
	if submitted and query:
		with st.spinner("🔍 Searching and analyzing..."):
			result = workflow.process_query(query)
			if result['status'] == 'success':
				st.success("✅ Report generated successfully!")
				st.subheader("📝 Summary")
				st.write(result['summary'])
				st.subheader("🎯 Key Points")
				for point in result['key_points']:
					st.write(f"• {point}")
				st.subheader("🔗 Sources")
				for i, source in enumerate(result['sources'], 1):
					with st.expander(f"{i}. {source['title']}"):
						st.write(f"**URL:** {source['url']}")
						st.write(f"**Snippet:** {source['snippet']}")
			else:
				st.error("❌ Failed to generate report")

def reports_page(database):
	st.header("Research Reports")
	reports = database.get_all_reports()
	if reports:
		for report in reports:
			with st.expander(f"📄 {report['query']} (ID: {report['id']})"):
				col1, col2 = st.columns([3, 1])
				with col1:
					st.write(f"**Created:** {report['created_at']}")
					st.write(f"**Summary:** {report['summary'][:200]}...")
				with col2:
					if st.button(f"View Full", key=f"view_{report['id']}"):
						st.session_state['view_report_id'] = report['id']
		if 'view_report_id' in st.session_state:
			view_report_page(database, st.session_state['view_report_id'])
	else:
		st.info("No reports yet. Start by creating your first research report!")

def view_report_page(database, report_id):
	report = database.get_report(report_id)
	if report:
		st.header(f"Report #{report_id}")
		if st.button("← Back to Reports"):
			del st.session_state['view_report_id']
			st.rerun()
		st.subheader("📝 Summary")
		st.write(report['summary'])
		st.subheader("🎯 Key Points")
		for point in report['key_points']:
			st.write(f"• {point}")
		st.subheader("🔗 Sources")
		for i, source in enumerate(report['sources'], 1):
			st.write(f"{i}. [{source['title']}]({source['url']})")

if __name__ == "__main__":
	main()
