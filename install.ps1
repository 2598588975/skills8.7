param(
  [string]$Target = "$env:USERPROFILE\.codex\skills"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$source = Join-Path $repoRoot "skills"

if (-not (Test-Path -LiteralPath $source)) {
  throw "Cannot find skills directory: $source"
}

New-Item -ItemType Directory -Force -Path $Target | Out-Null

Get-ChildItem -LiteralPath $source -Directory | ForEach-Object {
  $destination = Join-Path $Target $_.Name
  Copy-Item -LiteralPath $_.FullName -Destination $destination -Recurse -Force
  Write-Host "Installed skill:" $_.Name
}

Write-Host ""
Write-Host "Done. Restart Codex to reload skills."

