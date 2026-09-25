from __future__ import annotations

"""Engine 4 on-screen notification recorder. Trading logic is untouched."""
import argparse, json, os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
OUT=Path('output/engine4'); ET=ZoneInfo('America/New_York')

def _read_json(path: Path):
    try: return json.loads(path.read_text(encoding='utf-8'))
    except Exception: return {}

def _candidate_line(r):
    failures=r.get('premarket_failures') or 'NONE'
    return f"{r.get('ticker','?')} — score={r.get('score','?')} grade={r.get('premarket_grade','?')} eligible={r.get('premarket_eligible')} status={r.get('status') or r.get('tier') or 'N/A'} failures={failures}"

def _all_80(kind):
    if kind=='deep': rows=_read_json(OUT/'deep_ranked.json').get('ranked',[])
    elif kind=='freeze':
        p=_read_json(OUT/'top25_frozen.json'); rows=p.get('ranked',[]) or p.get('candidates',[])
    else: return ''
    high=[]
    for r in rows:
        try:
            if float(r.get('score',-1))>=80: high.append(r)
        except Exception: pass
    high.sort(key=lambda r: float(r.get('score',0)), reverse=True)
    return '\n'.join(['ALL >=80 CANDIDATES (survivors AND rejects):']+[_candidate_line(r) for r in high]) if high else 'ALL >=80 CANDIDATES: NONE'

def _signal_for(kind,supplied):
    if kind=='final': return _read_json(OUT/'final_signal.json')
    if kind=='recovery': return _read_json(OUT/'recovery_signal.json')
    if kind=='complete':
        p=_read_json(OUT/'final_signal.json'); r=_read_json(OUT/'recovery_signal.json'); b=_read_json(OUT/'watch_bench_report.json')
        ps=str(p.get('status') or 'UNAVAILABLE').upper(); rs=str(r.get('status') or 'UNAVAILABLE').upper()
        outcome='BUY/ARM SIGNAL PRESENT' if {ps,rs}&{'BUY','ARM'} else 'NO BUY SIGNAL TODAY'
        watch=', '.join(str(x.get('ticker')) for x in b.get('candidates',[]) if x.get('ticker')) or 'NONE'
        return {'status':'COMPLETE','ticker':'SYSTEM','message':supplied or f'{outcome}\nPrimary: {ps}\nRecovery: {rs}\nWatchlist: {watch}'}
    defaults={'preflight':('CHECKING','SYSTEM','Engine 4 early preflight is active.'),'launch':('DISPATCHED','SYSTEM','Engine 4 early controller dispatched production.'),'watchdog':('RECOVERY_DISPATCHED','SYSTEM','Engine 4 watchdog dispatched a recovery wake.'),'start':('STARTED','SYSTEM','Engine 4 scheduled run started.'),'prescreen':('COMPLETED','MARKET','Engine 4 prescreen stage completed.'),'deep':('COMPLETED','MARKET','Engine 4 deep stage completed.'),'freeze':('COMPLETED','MARKET','Engine 4 freeze stage completed.'),'bench':('COMPLETED','MARKET','Engine 4 bench stage completed.'),'failure':('PIPELINE_FAILURE','SYSTEM','ENGINE 4 DATA/PIPELINE FAILURE'),'test':('TEST','SYSTEM','Engine 4 notification test.')}
    s,t,m=defaults.get(kind,('UNKNOWN','MARKET','Engine 4 notification.')); return {'status':s,'ticker':t,'message':supplied or m}

def notify(kind,supplied=None,dry_run=False):
    OUT.mkdir(parents=True,exist_ok=True); signal=_signal_for(kind,supplied)
    status=str(signal.get('status') or 'UNKNOWN').upper(); ticker=str(signal.get('ticker') or 'MARKET').upper(); message=str(signal.get('message') or signal.get('reason') or supplied or 'No message supplied.')
    extra=_all_80(kind)
    if extra: message=f'{message}\n{extra}'
    date_et=str(signal.get('target_date_et') or datetime.now(ET).date()); run_id=os.getenv('GITHUB_RUN_ID','').strip(); generated=datetime.now(ET).strftime('%Y-%m-%d %I:%M:%S %p ET')
    heading=f'ENGINE 4 {kind.upper()}: {status} — {ticker}'; progress='The full Engine 4 run is NOT complete. Recovery watch and terminal verification continue.' if kind=='final' else ''
    text='\n'.join(x for x in (heading,message,progress,f'Run {run_id}' if run_id else '',f'Generated {generated}','Confirm the live broker quote before any order.') if x)
    marker=f'ENGINE4-ALERT:{date_et}:{kind}:{status}:{ticker}:RUN:{run_id or "NO-RUN"}'
    record={'delivery':'SAVED_ONSCREEN','marker':marker,'kind':kind,'status':status,'ticker':ticker,'target_date_et':date_et,'generated_et':generated,'run_id':run_id,'message':message,'notification_text':text,'dry_run':dry_run}
    (OUT/f'notification_{kind}.txt').write_text(text+'\n',encoding='utf-8'); (OUT/f'notification_{kind}.json').write_text(json.dumps(record,indent=2),encoding='utf-8'); (OUT/'notification_audit.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
    lp=OUT/'notification_audit_log.json'
    try:
        h=json.loads(lp.read_text(encoding='utf-8')); h=h if isinstance(h,list) else []
    except Exception: h=[]
    h.append(record); lp.write_text(json.dumps(h,indent=2),encoding='utf-8')
    print('=== ENGINE 4 ON-SCREEN NOTIFICATION ==='); print(text); print('=== END ENGINE 4 NOTIFICATION ===',flush=True); return record

def main():
    p=argparse.ArgumentParser(); p.add_argument('kind',choices=('preflight','launch','watchdog','start','prescreen','deep','freeze','bench','final','recovery','complete','failure','test')); p.add_argument('--message'); p.add_argument('--dry-run',action='store_true'); p.add_argument('--require-delivery',action='store_true'); a=p.parse_args(); r=notify(a.kind,a.message,a.dry_run); print(json.dumps(r,indent=2),flush=True)
    if a.require_delivery and r.get('delivery')!='SAVED_ONSCREEN': raise SystemExit(1)
if __name__=='__main__': main()
