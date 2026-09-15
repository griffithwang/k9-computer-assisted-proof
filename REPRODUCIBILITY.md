# Reproducibility

The full artifact is the sibling Windows x64 package `K9_Computer_Assisted_Proof_20260915`. From its root:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\verify.ps1 -Mode Preflight
powershell -NoProfile -ExecutionPolicy Bypass -File .\verify.ps1 -Mode Full
```

The accepted full receipt is `runs/relocated_full_01/report.json`. It records G1, graph/G2--G4, and G5 as fresh runs, with preflight and postflight hashes equal. The independent review is `validation/adapter_review/FINAL_REVIEW.md`. The archive and package manifests are outside this directory so that the article repository remains suitable for ordinary Git hosting.

The reported counts are 43,545,600 source contexts, 5,269,252 retained height assignments, 83,023 signed records, 52,347 flip-normalized representatives, and 38 exact inclusion witnesses. The exact-nine corollary has 26 types after removing Calvo's 12 at-most-eight types.
