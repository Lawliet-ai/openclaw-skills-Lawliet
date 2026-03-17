import asyncio
import json
import os
import time
from openai import AsyncOpenAI

async def run_agent(name, system_prompt, user_query, api_key, base_url, model, retries=3):
    client = AsyncOpenAI(api_key=api_key, base_url=base_url)
    tmp_dir = os.path.expanduser("~/.openclaw/swarm_tmp")
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    
    for attempt in range(retries):
        try:
            response = await client.chat.completions.create(
                model=model,
                messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_query}],
                temperature=0.7
            )
            output_path = os.path.join(tmp_dir, f"{name}.md")
            with open(output_path, "w") as f:
                f.write(f"# Result from {name}\n\n{response.choices[0].message.content}")
            return f"✅ [{name}] Success."
        except Exception as e:
            if "429" in str(e) and attempt < retries - 1:
                await asyncio.sleep((2 ** attempt) + 1)
                continue
            return f"❌ [{name}] Error: {str(e)}"

async def main():
    config_path = os.path.expanduser("~/.openclaw/swarm_tmp/task_config.json")
    if not os.path.exists(config_path):
        print("CRITICAL_ERROR: task_config.json missing.")
        return
    
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
    except Exception as e:
        print(f"CRITICAL_ERROR: Config parse failed: {str(e)}")
        return
    
    semaphore = asyncio.Semaphore(6)
    async def sem_run(task):
        async with semaphore: return await run_agent(**task)
    
    results = await asyncio.gather(*(sem_run(t) for t in config['tasks']))
    print("\n".join(results))

if __name__ == "__main__":
    asyncio.run(main())