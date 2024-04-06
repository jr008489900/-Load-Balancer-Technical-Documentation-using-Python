# 負載均衡器（Load Balancer）實作練習3：資料轉發負載均衡器
本實作練習展示了如何使用Python實現一個負載均衡器，當發送請求至localhost:9000/test時，該負載均衡器將請求轉發至FASTAPI後端伺服器，並將FASTAPI的回應再傳回給請求者。

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
請求轉發說明：
當你訪問http://localhost:9000/test時，負載均衡器會將請求轉發至FASTAPI後端伺服器（根據Round Robin策略選擇），然後將FASTAPI的回應再傳回給請求者。

注意事項：
請確保FASTAPI伺服器已經正確運行在8000和8001端口。
本實作練習使用Round Robin策略來選擇後端伺服器，你可以根據需要進行調整。
在load_balancer.py同一目錄下，應該存在一個名為webserver的目錄，該目錄應包含你想要轉發的資料或資源。
以上是實作練習3的使用教學，這個負載均衡器會將請求轉發至FASTAPI後端伺服器，並將FASTAPI的回應再傳回給請求者。