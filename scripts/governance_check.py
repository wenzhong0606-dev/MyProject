from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=['AGENTS.md','README.md','docs/governance/product-lifecycle.md','docs/governance/design-gates.md','docs/governance/traceability.csv']
missing=[p for p in REQUIRED if not (ROOT/p).is_file()]
if missing: raise SystemExit('缺少治理文件: '+', '.join(missing))
with (ROOT/'docs/governance/traceability.csv').open(encoding='utf-8-sig',newline='') as f:
 reader=csv.DictReader(f)
 if not reader.fieldnames or 'requirement_id' not in reader.fieldnames: raise SystemExit('追踪矩阵缺少 requirement_id')
 rows=list(reader)
 ids=[r['requirement_id'] for r in rows if r['requirement_id']]
 if len(ids)!=len(set(ids)): raise SystemExit('追踪矩阵存在重复 requirement_id')
print('治理基础结构检查通过；不代表业务或代码已验证。')
