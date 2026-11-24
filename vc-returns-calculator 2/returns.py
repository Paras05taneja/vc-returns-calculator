"""VC returns calculator: how dilution and exit value turn into MOIC and IRR."""


def ownership_at_exit(entry_ownership, dilution_per_round):
    """Each later round dilutes you: ownership * (1 - dilution)."""
    own = entry_ownership
    for d in dilution_per_round:
        own *= (1 - d)
    return own


def moic(proceeds, invested):
    """Multiple on invested capital."""
    return proceeds / invested


def irr(multiple, years):
    """Annual return for a single cash-in, single cash-out investment."""
    return multiple ** (1 / years) - 1


def exit_needed(target_multiple, invested, final_ownership):
    """Company exit value needed for the investment to return `target_multiple`."""
    return target_multiple * invested / final_ownership


if __name__ == "__main__":
    invested = 500_000        # seed check, $
    entry_own = 0.10          # 10% at entry
    dilution = [0.20, 0.15]   # Series A dilutes 20%, Series B dilutes 15%
    exit_value = 200_000_000  # company sold for $200M
    years = 7

    final_own = ownership_at_exit(entry_own, dilution)
    proceeds = exit_value * final_own
    m = moic(proceeds, invested)

    print(f"Ownership at entry:     {entry_own:.1%}")
    print(f"Ownership at exit:      {final_own:.2%}  (after dilution {dilution})")
    print(f"Proceeds at ${exit_value/1e6:.0f}M exit:  ${proceeds:,.0f}")
    print(f"MOIC:                   {m:.1f}x")
    print(f"IRR over {years} years:      {irr(m, years):.1%}")
    print()
    print("Exit value needed for a given return on this investment:")
    for t in (3, 10, 30, 100):
        print(f"  {t:>3}x  ->  ${exit_needed(t, invested, final_own)/1e6:,.0f}M")
