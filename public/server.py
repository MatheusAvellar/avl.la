import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
	def do_GET(self):
		# Check if the path has no extension
		if '.' not in os.path.basename(self.path):
			# Attempt to append .html
			potential_html_path = self.path + ".html"
			if os.path.exists(self.translate_path(potential_html_path)):
				self.path = potential_html_path

		# Call the original do_GET method to serve the file
		super().do_GET()

PORT = 8000
with HTTPServer(("", PORT), CustomHandler) as httpd:
	print(f"Serving at port {PORT}")
	httpd.serve_forever()
