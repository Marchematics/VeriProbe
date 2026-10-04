
from pathlib import Path
import sys,json
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent; ROOT=HERE.parent
sys.path.insert(0,str(ROOT/'src'))
from veriprobe import challenge_rank

def trial(seed=0,strategic_frac=0.6,m=16,W=100,K=10):
    rng=np.random.default_rng(seed)
    q=rng.beta(2.2,4.0,size=W)
    hi=rng.choice(W,15,replace=False); q[hi]=rng.beta(6,2,size=15)
    strategic=rng.random(W)<strategic_frac
    report=np.clip(q+rng.normal(0,0.04,W),0,1)
    report[strategic]=np.maximum(report[strategic],rng.uniform(0.90,0.99,size=strategic.sum()))
    adaptive=strategic & (rng.random(W)<0.6)
    caught=np.zeros(W,dtype=bool)
    simple=strategic & ~adaptive
    caught[simple]=rng.random(simple.sum())<0.70
    caught[adaptive]=rng.random(adaptive.sum())<0.10
    det=report.copy(); det[caught]*=0.15
    succ=rng.binomial(m,q); probes=np.full(W,m)
    methods={
      'NaiveReport':np.argsort(-report)[:K],
      'Detector':np.argsort(-det)[:K],
      'VeriProbe':challenge_rank(succ,probes,K,delta=0.05),
      'Oracle':np.argsort(-q)[:K]
    }
    out={}
    for name,idx in methods.items():
        out[name+'_mean_true_quality']=q[idx].mean()
        out[name+'_min_true_quality']=q[idx].min()
        out[name+'_strategic_share']=strategic[idx].mean()
    return out

def main():
    rows=[]
    for m in [2,4,8,16,32,64]:
        df=pd.DataFrame([trial(s,m=m,strategic_frac=0.6) for s in range(300)])
        row={'probes_per_site':m}; row.update({c:df[c].mean() for c in df.columns}); rows.append(row)
    pd.DataFrame(rows).to_csv(ROOT/'results'/'probe_sweep.csv',index=False)

    rows=[]
    for frac in [0,0.2,0.4,0.6,0.8,1.0]:
        df=pd.DataFrame([trial(s,strategic_frac=frac,m=16) for s in range(300)])
        row={'strategic_fraction':frac}; row.update({c:df[c].mean() for c in df.columns}); rows.append(row)
    adf=pd.DataFrame(rows); adf.to_csv(ROOT/'results'/'strategic_fraction_sweep.csv',index=False)
    summary={'experiment':'strategic self-report + post-commit random evidence challenges',
             'claim_scope':'synthetic mechanism stress test; not a real GEO/AgentWebBench SOTA result',
             'strategic_sweep':adf.round(6).to_dict(orient='records')}
    (ROOT/'results'/'summary.json').write_text(json.dumps(summary,indent=2))
    print(adf[['strategic_fraction','NaiveReport_mean_true_quality','Detector_mean_true_quality','VeriProbe_mean_true_quality','Oracle_mean_true_quality']].to_string(index=False))
if __name__=='__main__':main()