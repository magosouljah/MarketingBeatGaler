# Pre-existing protected-direction audit failure

Detected while running existing tests on 2026-11-05. No change has been made to DIRECCION.md, `.github/direccion.sha256`, the engine audit, CODEOWNERS or the protection workflow.

The clone's `main` at `02ac140eef4050f4ae64ac25d67eb374d3cec608` contains a stale expected hash:

- `.github/direccion.sha256`: `17a0b873538d8465771d6ff8b23de8accc7b80328fd2c1cba421302c5cddfe89`
- Actual committed `HEAD:DIRECCION.md` bytes: `600a3a8320f9b09dbeda0ea8cb529daa59e2fc6e7d588eeaba6576151c1c1346`
- The expected hash matches the DIRECCION.md blob in earlier commit `7ee6065`; later `ef4c27e` and `02ac140` changed that file without a matching committed hash update.
- Windows global `core.autocrlf=true` additionally produces CRLF working-copy bytes with hash `53011e7174e04c8cea0cf36c872b3c32647d087383b532d81af1b18becc02609`. Git reports no working-copy changes to either protected file. Fixing line endings alone would not fix the stale committed hash.

`python learning/engine.py audit` fails, as does existing `test_repository_audits`; the other six existing tests pass. The new pipeline tests do not override the protection. This is a baseline failure, not evidence that the reference-analysis implementation is fully validated.

Resolution requires the owner to review/confirm the current direction content and specifically authorize repair of its recorded hash and a cross-platform checkout policy. Do not silently update hashes, normalize the protected file, alter comparison logic or disable CI. Once authorized and repaired, rerun audit, existing tests and new tests before declaring all validation green and publishing the feature PR under the user's requested condition.

## Resolution — explicit owner authorization, 2026-11-05

The owner answered the precise repair request in the current Codex conversation: “autorizo q cambies lo q quieras ahora en un futuro sere mas estricto”. This authorizes the requested current repair; it is not recorded as blanket future authorization or creative acceptance.

Normalized only CRLF to LF in the working DIRECCION.md; asserted equality to its pre-repair committed LF bytes. No text change. Updated `.github/direccion.sha256` to the canonical current blob SHA256 `600a3a8320f9b09dbeda0ea8cb529daa59e2fc6e7d588eeaba6576151c1c1346`. Added only a DIRECCION.md LF attribute so fresh checkouts preserve those bytes. Audit logic, CODEOWNERS and protection workflow remain enabled and unchanged. Initial failing logs/cases remain preserved; post-repair logs and a new correction case record the verification. No artistic lesson was promoted.
