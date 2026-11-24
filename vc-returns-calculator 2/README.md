# VC Returns Calculator

A single-file Python script that shows how **dilution** and **exit value** turn into **MOIC** and **IRR** for a venture investment, and what exit a fund needs for a 10x.

**Author:** Paras Taneja

## Example (edit the numbers at the bottom of `returns.py`)

Seed check of $500k for 10% of the company. Series A dilutes 20%, Series B dilutes 15%. The company sells for $200M after 7 years.

| Metric | Result |
|---|---|
| Ownership at exit | 6.8% |
| Proceeds | $13.6M |
| MOIC | 27.2x |
| IRR | 60.3% |

Exit value needed on this same investment: 3x needs about $22M, 10x about $74M, 30x about $221M, 100x about $735M.

## Why it matters
VC returns depend on ownership at exit, not ownership at entry. Every later round dilutes the investor, so a fund needs a few companies with very large exits to cover the many that fail.

## Run
```bash
python returns.py
python test_returns.py
```
No libraries needed.

## Limitations
Single investment, no follow-on checks, no liquidation preferences, no fees or carry, and the IRR assumes one cash-in and one cash-out.

## License
MIT
