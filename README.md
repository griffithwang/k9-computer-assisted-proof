# A Computer-Assisted Classification of Knots Realizable with At Most Nine Sticks

This directory is the arXiv-style manuscript and citation source for the K9 result. The theorem is a computer-assisted result with explicit external mathematical inputs. It is deliberately careful about the distinction between a finite certificate replay and a purely structural proof.

`main.tex` is the submission source and `references.bib` is the bibliography. `RESULTS.json` records the frozen headline counts. `REPRODUCIBILITY.md` explains how to audit the full Windows package. `CITATION.cff` supplies repository metadata.

The complete offline verifier is distributed separately as the Windows x64 release asset `K9_Computer_Assisted_Proof_20260915.zip` when the release is available. It contains the fixed runtime and all certificate objects. Its SHA-256 is recorded in `RESULTS.json` and in the archive sidecar in the research workspace.

Before arXiv submission, replace the project-author placeholder with the authors' names and affiliations, and compile with a current TeX distribution. The supplied PDF in the offline package is the Chinese referee report, not a substitute for compiling this manuscript.
