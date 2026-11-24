from returns import ownership_at_exit, moic, irr, exit_needed

assert abs(ownership_at_exit(0.10, [0.20, 0.15]) - 0.068) < 1e-12
assert moic(2_000_000, 500_000) == 4
assert abs(irr(4, 2) - 1.0) < 1e-12          # 4x in 2 years = 100% a year
assert abs(exit_needed(10, 500_000, 0.05) - 100_000_000) < 1e-6
print("All tests passed")
