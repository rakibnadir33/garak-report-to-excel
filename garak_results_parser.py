import json
import pandas as pd

jsonl_path = input("Enter the path to your .jsonl file: ").strip().strip('"')

rows = []
with open(jsonl_path, "r", encoding="utf-8") as f:
    for line in f:
        entry = json.loads(line.strip())
        if entry.get("entry_type") == "attempt":
            probe = entry.get("probe_classname", "")

            try:
                prompt = entry["prompt"]["turns"][0]["role"]["user"]["content"]["text"]
            except:
                try:
                    prompt = entry["prompt"]["turns"][0]["content"]["text"]
                except:
                    prompt = str(entry.get("prompt", ""))

            outputs = entry.get("outputs", [])
            for output in outputs:
                try:
                    response = output["text"]
                except:
                    response = str(output)

                rows.append({
                    "probe": probe,
                    "prompt": prompt,
                    "response": response
                })

df = pd.DataFrame(rows)
df.to_excel("garak_results.xlsx", index=False)
print(f"Done. {len(df)} rows exported.")