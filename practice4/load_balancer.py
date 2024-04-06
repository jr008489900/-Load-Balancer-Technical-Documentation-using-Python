import http.server
import socketserver

# 定義後端伺服器的地址和端口，以及初始負載
BACKEND_SERVERS = {
    ('localhost', 8000): 0,
    ('localhost', 8001): 0,
    ('localhost', 8002): 0,
    # 你可以添加更多的後端伺服器
}

# 增加伺服器負載
def increase_load(server):
    BACKEND_SERVERS[server] += 1

# 減少伺服器負載
def decrease_load(server):
    BACKEND_SERVERS[server] -= 1 if BACKEND_SERVERS[server] > 0 else 0

# 選擇最少負載的伺服器
def least_load_server():
    min_load = min(BACKEND_SERVERS.values())
    least_loaded_servers = [server for server, load in BACKEND_SERVERS.items() if load == min_load]
    return least_loaded_servers[0]

class LoadBalancerHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # 獲取後端伺服器的地址和端口
        backend_server = least_load_server()
        backend_host, backend_port = backend_server

        # 轉發HTTP請求到後端伺服器
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(f"Backend Server: {backend_host}:{backend_port}".encode())

        # 增加選擇的後端伺服器的負載
        increase_load(backend_server)

    def log_message(self, format, *args):
        # 覆寫log_message方法以禁止預設的請求日誌輸出
        return

if __name__ == "__main__":
    PORT = 9000

    # 啟動負載均衡器伺服器
    with socketserver.TCPServer(('0.0.0.0', PORT), LoadBalancerHandler) as httpd:
        print(f"Load balancer running on port {PORT}")
        httpd.serve_forever()
