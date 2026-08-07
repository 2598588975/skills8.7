# Codex Personal Skills Backup

This repository is a plain, unencrypted backup of personal Codex skills from:

`C:\Users\codex\.codex\skills`

It intentionally stores the skills as normal folders under `skills/` so another Codex account can clone or download the repository and copy them into its own Codex skills directory.

## What Is Included

Included:

- Personal/custom skills under `skills/`
- Nested sub-skills, reference files, scripts, examples, and bundled assets contained in those skill folders

Not included:

- `.system` skills from Codex itself
- Plugin cache skills from `.codex/plugins/cache`
- Credentials, tokens, API keys, or encrypted material

## Install On Windows

From the cloned repository root:

```powershell
.\install.ps1
```

This copies every folder under `skills/` into:

```text
$env:USERPROFILE\.codex\skills
```

Existing skill folders with the same names are overwritten.

## Manual Install

Copy all folders inside `skills/` into your Codex skills directory:

```text
C:\Users\<your-user>\.codex\skills
```

Restart Codex after copying so it reloads the skill list.

## Upload To GitHub

After creating an empty GitHub repository, run:

```powershell
git remote add origin https://github.com/<your-user>/<your-repo>.git
git branch -M main
git push -u origin main
```

If GitHub asks you to sign in, use your GitHub account or a personal access token.

