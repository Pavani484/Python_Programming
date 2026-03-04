
from fastapi import FastAPI, Request
from pydantic import BaseModel
import sqlite3, uuid, time, hashlib, json, os

app = FastAPI()
DB = 'data.db'
CHAIN = 'chain.json'
os.makedirs('data', exist_ok=True)

# init sqlite
conn = sqlite3.connect(DB, check_same_thread=False)
conn.execute('''CREATE TABLE IF NOT EXISTS records(
 id TEXT PRIMARY KEY, payload TEXT, integrity REAL, created INTEGER)''')
conn.commit()

def init_chain():
    if not os.path.exists(CHAIN):
        with open(CHAIN,'w') as f:
            json.dump([], f)
init_chain()

class Submission(BaseModel):
    answers: dict
    paradata: dict
    meta: dict = {}

def compute_integrity(paradata, answers):
    # simple heuristic + logistic-like mapping
    score = 100.0
    for q,t in paradata.get('time_per_q', {}).items():
        if t < 2:
            score -= 40
        elif t < 5:
            score -= 10
    edits = sum(paradata.get('edit_counts', {}).values())
    if edits == 0:
        score -= 20
    return max(0, round(score,1))

def append_chain(entry):
    with open(CHAIN,'r+') as f:
        chain = json.load(f)
        prev = chain[-1]['hash'] if chain else ''
        entry['prev'] = prev
        entry_str = json.dumps(entry, sort_keys=True)
        entry_hash = hashlib.sha256(entry_str.encode()).hexdigest()
        entry['hash'] = entry_hash
        chain.append(entry)
        f.seek(0); f.truncate(); json.dump(chain, f, indent=2)
    return entry_hash

@app.post('/submit')
async def submit(s: Submission):
    rid = str(uuid.uuid4())
    now = int(time.time())
    integrity = compute_integrity(s.paradata, s.answers)
    payload = {'answers': s.answers, 'paradata': s.paradata, 'meta': s.meta}
    conn.execute("INSERT INTO records(id,payload,integrity,created) VALUES (?,?,?,?)",
                 (rid, json.dumps(payload), integrity, now))
    conn.commit()
    # append a chain proof (only hashed summary)
    summary = {'id': rid, 'integrity': integrity, 'ts': now, 'paradata_summary': {
        'times': s.paradata.get('time_per_q',{}), 'edits': s.paradata.get('edit_counts', {})
    }}
    h = append_chain(summary)
    return {'record_id': rid, 'integrity_score': integrity, 'chain_hash': h}

@app.get('/record/{rid}')
async def get_record(rid: str):
    cur = conn.execute("SELECT payload,integrity,created FROM records WHERE id=?", (rid,))
    row = cur.fetchone()
    if not row:
        return {'error':'not found'}
    payload, integrity, created = row
    return {'id': rid, 'payload': json.loads(payload), 'integrity': integrity, 'created': created}
