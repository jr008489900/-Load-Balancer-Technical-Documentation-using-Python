# 負載均衡器（Load Balancer）實作練習1：最簡單的Load Balancer
本實作練習展示了如何使用Python實現一個最簡單的負載均衡器，並將其與FASTAPI後端伺服器結合。這個負載均衡器會隨機選擇一個後端伺服器，以平衡請求的分配。

# 使用教學:
## Step 1: 啟動FASTAPI伺服器（假設在8000和8001端口）：
```
uvicorn webserver:app --port 8000
uvicorn webserver:app --port 8001
```
## Step 2: 啟動Python負載均衡器：
```
python load_balancer.py
```
## Step 3: 測試負載均衡器
當你連續多次訪問http://localhost:9000時，負載均衡器會隨機將請求轉發到不同的FASTAPI後端伺服器。

以上是實作練習1的使用教學。這個最簡單的負載均衡器使用隨機選擇的方式來分配請求，適合用於初學者了解基本的負載均衡概念。