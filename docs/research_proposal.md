
# VeriProbe: Research Proposal

## Thesis
The emerging Agentic Web creates a new strategic interface. A user agent asks site agents which of them can answer a task. If the site can self-report relevance, the economically rational behavior is to over-claim. If the selector relies on a learned detector, publishers can optimize against the detector just as SEO/GEO optimizes against rankers.

VeriProbe changes discovery from **claim-then-trust** to **commit-then-challenge**.

## Sharp contradiction
AgentWebBench models a decentralized Web of content agents and highlights the need for better site planning. GEO research simultaneously shows that Web publishers actively optimize for visibility and that malicious optimization is becoming adaptive. Cooperative site selection and strategic visibility incentives cannot both be the default assumption.

## Protocol
1. Before seeing the challenge, each content agent commits to a snapshot/evidence index.
2. The user agent samples random evidence facets derived from the query.
3. The site returns source-bound evidence for those facets.
4. A verifier marks each probe success/failure.
5. The router ranks sites by a conservative estimate of verified coverage/quality.

Self-reported relevance may remain as a cheap prior but cannot directly buy ranking mass.

## Statistical guarantee target
For site `i`, let each random challenge be a Bernoulli observation with mean verified evidence quality `q_i`. With `m_i` probes, an empirical mean plus a simultaneous Hoeffding bound gives a lower-confidence score. With probability at least `1-delta`, all site qualities lie above their lower bounds when the union bound is applied over sites.

This does not solve forged evidence by itself. The commitment and verifier are essential assumptions. The paper must explicitly state what the verifier proves: source presence, timestamp, citation support, or stronger factual entailment.

## Strategic property
Inflating an unaudited self-report has no direct effect on the VeriProbe score. A publisher must improve verifiable evidence on randomly sampled facets to improve expected routing probability. This is the mechanism-design goal.

## CPU-first evaluation
1. Extend AgentWebBench with strategic website agents that can inflate descriptions and selectively answer likely probes.
2. Build attack families from SEO/GEO rewriting and adaptive self-promotion.
3. Compare self-report ranking, reputation, detector defenses, random auditing, GEO-defense rerankers, and VeriProbe.
4. Sweep strategic-site fraction, challenge budget, adaptive attacks, stale commitments, and verifier error.
5. Report selected-site true evidence quality, task score, attack success, probe overhead, and false rejection of benign sites.

## Go / no-go gate
Proceed to a full WWW paper only if the real-corpus strategic benchmark shows:
- strong robustness to adaptive promotion attacks;
- quality close to an oracle at modest probe cost;
- better benign-site retention than detector-only defenses;
- a defensible commitment/verifier construction.

## Current evidence
In the synthetic game, detector-based routing collapses once most strategic sites use adaptive inflation, while random post-commit probing tracks the oracle as probe count rises. This is a mechanism signal only.

## Main risk
If probe facets are predictable or the verifier is weak, strategic sites can optimize the challenge channel itself. The strongest version should randomize challenges after an authenticated content commitment and quantify verifier error.