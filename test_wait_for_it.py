import socket
import subprocess
import sys
import threading
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

class QuietHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")
    def log_message(self, format, *args):
        pass

def run_tests():
    # 1. Start test HTTP server on an ephemeral loopback port
    server = HTTPServer(("127.0.0.1", 0), QuietHandler)
    port = server.server_port
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()

    # Test 1: Active port should succeed (exit code 0)
    res = subprocess.run(["bash", "wait-for-it.sh", f"127.0.0.1:{port}", "-t", "5", "--", "echo", "server_ready"], capture_output=True, text=True)
    assert res.returncode == 0, f"Expected 0 for open port, got {res.returncode}. stderr: {res.stderr}"
    assert "server_ready" in res.stdout, f"Expected child command output, got: {res.stdout}"

    # Shut down server
    server.shutdown()
    server.server_close()
    thread.join()

    # Test 2: Find a closed port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    closed_port = s.getsockname()[1]
    s.close()

    # Closed port with strict timeout must fail (exit code non-zero)
    res_fail = subprocess.run(["bash", "wait-for-it.sh", f"127.0.0.1:{closed_port}", "-t", "1", "--strict", "-q"], capture_output=True, text=True)
    assert res_fail.returncode != 0, f"Expected non-zero exit for closed port, got {res_fail.returncode}"

    print("ALL TESTS PASSED")

if __name__ == "__main__":
    run_tests()
