import json
import asyncio
import os
import http.client
from urllib.parse import urlparse

async def run_worker(worker_data, session):
    """单节点异步请求"""
    print(f"[*] Starting Worker {worker_data['id']}: {worker_data['role']}")
    
    url = urlparse(session['base_url'])
    host = url.netloc
    path = f"{url.path}/chat/completions".replace("//", "/")
    
    headers = {
        "Authorization": f"Bearer {session['api_key']}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": session['model'],
        "messages": [
            {"role": "system", "content": worker_data['prompt']},
            {"role": "user", "content": worker_data['query']}
        ],
        "temperature": 0.7
    }

    try:
        # 使用异步方式进行 HTTPS 请求（这里简化逻辑以兼容环境）
        conn = http.client.HTTPSConnection(host)
        conn.request("POST", path, json.dumps(payload), headers)
        response = conn.getresponse()
        data = json.loads(response.read().decode())
        content = data['choices'][0]['message']['content']
        
        # 写入结果
        output_path = os.path.expanduser(f"~/.openclaw/swarm_tmp/worker_{worker_data['id']}.md")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(f"## Role: {worker_data['role']}\n\n{content}")
            
        print(f"[+] Worker {worker_data['id']} Completed.")
    except Exception as e:
        print(f"[!] Worker {worker_data['id']} Failed: {e}")

async def main():
    config_path = os.path.expanduser("~/.openclaw/swarm_tmp/task_config.json")
    if not os.path.exists(config_path):
        print("[!] Config not found.")
        return

    with open(config_path, "r") as f:
        config = json.load(f)

    # 启动 5 个并发任务
    tasks = [run_worker(w, config['session']) for w in config['workers']]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
