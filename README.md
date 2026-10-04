
# VeriProbe

**Challenge-before-Routing for Strategic Content Agents**

Agentic-Web benchmarks usually assume website/content agents are cooperative. The real Web gives publishers SEO/GEO incentives to overstate relevance or tailor responses to the selector.

VeriProbe uses **commit-before-challenge**: a site commits its evidence state, then receives random query-facet probes. Routing is based on verified probe success rather than self-reported relevance.

Run `python experiments/pretest.py`. Included numbers are synthetic strategic-game stress tests, not public-benchmark SOTA.