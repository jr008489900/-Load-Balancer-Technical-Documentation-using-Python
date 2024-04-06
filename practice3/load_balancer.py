import http.server
import socketserver
import requests

# 定義後端伺服器的地址和端口
BACKEND_SERVERS = [
    ('localhost', 8000),
    ('localhost', 8001),
    # 你可以添加更多的後端伺服器
]

# 初始化全局變數，用於存儲當前選擇的後端伺服器索引
current_server_index = 0

# 輪流選擇一個後端伺服器
def get_backend_server():
    global current_server_index
    backend_server = BACKEND_SERVERS[current_server_index]
    
    # 更新後端伺服器索引
    current_server_index = (current_server_index + 1) % len(BACKEND_SERVERS)
    
    return backend_server

class LoadBalancerHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/test':
            # 獲取後端伺服器的地址和端口
            backend_server = get_backend_server()
            backend_host, backend_port = backend_server

            # 轉發HTTP請求到後端伺服器的FASTAPI
            response = requests.get(f"http://{backend_host}:{backend_port}/test")
            
            # 將後端伺服器的回應返回給請求者
            self.send_response(response.status_code)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(response.content)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Not Found".encode())

if __name__ == "__main__":
    PORT = 9000

    # 啟動負載均衡器伺服器
    with socketserver.TCPServer(('0.0.0.0', PORT), LoadBalancerHandler) as httpd:
        print(f"Load balancer running on port {PORT}")
        httpd.serve_forever()
