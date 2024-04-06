# 負載均衡器（Load Balancer）基本概念
負載均衡器是一種網絡設備或服務，它將入站的請求分發到多個伺服器，以實現資源的平衡使用和提高服務的可用性、可擴展性和容錯能力。負載均衡器可以根據不同的演算法（如加權輪詢、最少連接、最少負載等）來分配請求，並且可以進行健康檢查以確保後端伺服器的正常運作。

## 基本特點：

分發請求：將入站的請求分發到多個伺服器。
提高性能：平衡伺服器負載，防止單一伺服器過載。
提高可用性和可擴展性：即使其中一台伺服器出現問題，服務仍然可用。
容錯能力：提供故障轉移和恢復功能。
結合 FASTAPI 的架構圖
以下是一個簡單的架構圖，展示了如何結合FASTAPI和負載均衡器（以Nginx或Python實現）：
```
      +----------------+
      |   User/Client  |
      +----------------+
               |
               v
      +----------------+
      |  負載均衡器 (LB)  |
      +----------------+
       /       |        \
      /        |         \
     v         v          v
+--------+ +--------+ +--------+
| FASTAPI| | FASTAPI| | FASTAPI|
| Server1| | Server2| | Server3|
+--------+ +--------+ +--------+
```
User/Client：終端用戶或客戶端，發起HTTP請求。
負載均衡器 (LB)：處理入站請求，並根據特定的演算法分發到多個FASTAPI伺服器。
FASTAPI Server1, Server2, Server3：後端伺服器，運行FASTAPI應用程式，處理請求並返回回應。

# 負載均衡器與FASTAPI應用程式

本項目展示了如何使用Python實現一個基本的負載均衡器，並將其與FASTAPI應用程式結合。負載均衡器會將入站的請求分發到多個FASTAPI伺服器，以實現資源的平衡使用和提高服務的可用性、可擴展性和容錯能力。

## 負載均衡器基本概念

負載均衡器是一種網絡設備或服務，它將入站的請求分發到多個伺服器。它的主要特點包括：

- 分發請求
- 提高性能
- 提高可用性和可擴展性
- 容錯能力


# 程式撰寫

負載均衡器與FASTAPI應用程式實作
本項目包含三個實作練習，展示了如何使用Python實現不同類型的負載均衡器，並將其與FASTAPI應用程式結合。

練習概述
practice1：最簡單的負載均衡器，可以回傳使用哪一台後端伺服器的資訊。
practice2：Round-robin負載均衡器，會輪流調用不同的後端伺服器。
practice3：根據後端伺服器的URL資訊，調用web server的資料並回傳給前端。

## practice1
啟動FASTAPI伺服器（假設在8000和8001端口）：

```
uvicorn webserver:app --port 8000
uvicorn webserver:app --port 8001
```
啟動Python負載均衡器：
```
python load_balancer.py
```
當你訪問http://localhost:9000時，負載均衡器會將請求轉發到其中一個FASTAPI伺服器，並返回使用的後端伺服器資訊。

## practice2
啟動FASTAPI伺服器（假設在8000和8001端口）：

```
uvicorn webserver:app --port 8000
uvicorn webserver:app --port 8001
```
啟動Python負載均衡器：
```
python load_balancer.py
```
當你連續多次訪問http://localhost:9000時，負載均衡器會輪流將請求轉發到不同的FASTAPI伺服器。

## practice3
啟動FASTAPI伺服器（假設在8000和8001端口）：

```
uvicorn webserver:app --port 8000
uvicorn webserver:app --port 8001
```
啟動Python負載均衡器：

```
python load_balancer.py
```
當你訪問http://localhost:9000/test時，負載均衡器會根據後端伺服器的URL資訊，調用web server的資料並回傳給前端。

注意事項
請確保所有FASTAPI伺服器和負載均衡器都正確運行並聽取相應的端口。
在實際生產環境中，考慮使用Nginx或其他高效的負載均衡器和反向代理伺服器。
這個README提供了項目的基本說明、各實作練習的概述、架構圖和如何運行項目的步驟。你可以根據你的項目需求進一步自定義和擴展。





