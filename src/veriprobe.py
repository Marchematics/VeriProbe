
import numpy as np

def hoeffding_lcb(successes, probes, n_sites, delta=0.05):
    successes=np.asarray(successes,float); probes=np.asarray(probes,float)
    rate=successes/np.maximum(probes,1)
    radius=np.sqrt(np.log(2*n_sites/delta)/(2*np.maximum(probes,1)))
    return np.clip(rate-radius,0,1)

def challenge_rank(successes, probes, k, delta=0.05):
    score=hoeffding_lcb(successes,probes,len(successes),delta)
    return np.argsort(-score)[:k]