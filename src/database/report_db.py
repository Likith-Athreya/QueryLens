import sqlite3
import json
from typing import List, Dict, Optional

class ReportDatabase:
	def __init__(self, db_path: str = "reports.db"):
		self.db_path = db_path
		self._init_database()
	
	def _init_database(self):
		with sqlite3.connect(self.db_path) as conn:
			cursor = conn.cursor()
			cursor.execute('''
				CREATE TABLE IF NOT EXISTS reports (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					query TEXT,
					summary TEXT,
					sources TEXT,
					key_points TEXT,
					created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
				)
			''')
			conn.commit()
	
	def save_report(self, query: str, summary: str, sources: List[Dict], key_points: List[str]) -> Optional[int]:
		try:
			with sqlite3.connect(self.db_path) as conn:
				cursor = conn.cursor()
				cursor.execute('''
					INSERT INTO reports (query, summary, sources, key_points)
					VALUES (?, ?, ?, ?)
				''', (
					query,
					summary,
					json.dumps(sources),
					json.dumps(key_points)
				))
				conn.commit()
				return cursor.lastrowid
		except Exception as e:
			return None
	
	def get_report(self, report_id: int) -> Optional[Dict]:
		try:
			with sqlite3.connect(self.db_path) as conn:
				cursor = conn.cursor()
				cursor.execute('SELECT * FROM reports WHERE id = ?', (report_id,))
				row = cursor.fetchone()
				if row:
					return {
						'id': row[0],
						'query': row[1],
						'summary': row[2],
						'sources': json.loads(row[3]),
						'key_points': json.loads(row[4]),
						'created_at': row[5]
					}
				return None
		except Exception as e:
			return None
	
	def get_all_reports(self) -> List[Dict]:
		try:
			with sqlite3.connect(self.db_path) as conn:
				cursor = conn.cursor()
				cursor.execute('SELECT * FROM reports ORDER BY created_at DESC')
				rows = cursor.fetchall()
				reports = []
				for row in rows:
					reports.append({
						'id': row[0],
						'query': row[1],
						'summary': row[2],
						'sources': json.loads(row[3]),
						'key_points': json.loads(row[4]),
						'created_at': row[5]
					})
				return reports
		except Exception as e:
			print(f"Database get all error: {e}")
			return []
	
	def search_reports(self, search_term: str) -> List[Dict]:
		try:
			with sqlite3.connect(self.db_path) as conn:
				cursor = conn.cursor()
				cursor.execute('''
					SELECT * FROM reports 
					WHERE query LIKE ? OR summary LIKE ?
					ORDER BY created_at DESC
				''', (f'%{search_term}%', f'%{search_term}%'))
				rows = cursor.fetchall()
				reports = []
				for row in rows:
					reports.append({
						'id': row[0],
						'query': row[1],
						'summary': row[2],
						'sources': json.loads(row[3]),
						'key_points': json.loads(row[4]),
						'created_at': row[5]
					})
				return reports
		except Exception as e:
			print(f"Database search error: {e}")
			return []
