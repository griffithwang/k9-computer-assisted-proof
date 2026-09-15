# Public repository scope

The public Git repository is intended to host the manuscript, bibliography, citation metadata, reproducibility instructions, result hashes, and the small PDF preview. The complete offline runtime and certificate objects remain in `K9_Computer_Assisted_Proof_20260915.zip` because the package is about 505 MB and contains a Windows toolchain. Its SHA-256 is fixed in the sibling sidecar file and in `RESULTS.json`.

After GitHub authentication is restored, run from this directory:

```powershell
gh auth login -h github.com
powershell -NoProfile -ExecutionPolicy Bypass -File .\publish_github.ps1 -Repository k9-computer-assisted-proof
```

The script creates a public repository and pushes the manuscript. It aborts before pushing if `gh auth status` fails. The repository URL should then be copied into `CITATION.cff` in a follow-up commit. Creating the repository and publishing a release archive are separate operations; the archive can be attached as a release asset after the initial repository exists.
