import http.server
import socketserver
import random

# 定義後端伺服器的地址和端口
BACKEND_SERVERS = [
    ('localhost', 8000),
    ('localhost', 8001),
    # 你可以添加更多的後端伺服器
]

# 當收到請求時，隨機選擇一個後端伺服器
def get_backend_server():
    return random.choice(BACKEND_SERVERS)

class LoadBalancerHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # 獲取後端伺服器的地址和端口
        backend_server = get_backend_server()
        backend_host, backend_port = backend_server

        # 轉發HTTP請求到後端伺服器
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(f"Backend Server: {backend_host}:{backend_port}".encode())

if __name__ == "__main__":
    PORT = 9000

    # 啟動負載均衡器伺服器
    with socketserver.TCPServer(('0.0.0.0', PORT), LoadBalancerHandler) as httpd:
        print(f"Load balancer running on port {PORT}")
        httpd.serve_forever()
