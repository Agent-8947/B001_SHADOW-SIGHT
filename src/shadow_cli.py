"""
SHADOW SIGHT — AUTONOMOUS OSINT RECON TOOL
NEXUS FACTORY V5.0

This is the main CLI entry point for Shadow Sight.
"""

import sys
import json
from domain_intel import bulk_check, subdomains, whois_lookup

def process_target(target):
    print(f"[*] Shadow Sight initializing intelligence gathering for: {target}")
    
    print("[*] Launching Certificate Transparency log analysis (Subdomains)...")
    subs = subdomains(target, limit=50)
    
    print(f"[*] Extracting WHOIS intelligence for {target}...")
    whois_data = whois_lookup(target)
    
    print("[*] Running parallel bulk deep-scan (DNS & SSL)...")
    deep = bulk_check([target], checks=["ssl", "dns"])

    dossier = {
        "target": target,
        "recon_data": {
            "subdomains_found": subs.get("count"),
            "subdomains": subs.get("subdomains"),
            "whois": whois_data,
            "deep_scan": deep.get("results")
        }
    }
    
    print("\n[+] RECONNAISSANCE COMPLETE. DOSSIER GENERATED:")
    print(json.dumps(dossier, indent=2))
    
    with open(f"shadow_dossier_{target}.json", "w", encoding="utf-8") as f:
        json.dump(dossier, f, indent=2)
    print(f"\n[+] Saved to shadow_dossier_{target}.json")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python shadow_cli.py <domain_or_company>")
        sys.exit(1)
        
    process_target(sys.argv[1])
