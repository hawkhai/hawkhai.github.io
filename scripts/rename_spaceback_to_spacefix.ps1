param(
    [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
)

$ErrorActionPreference = 'Stop'

$relativePaths = @(
    '_posts/deep/2024-09-24-how-to-run-qwen-using-ollama.spaceback.json',
    '_posts/life/k2022-05-08-kaoyu-menu-v2.spaceback.json',
    '_posts/life/k2022-05-08-kaoyu-menu-v3.spaceback.json',
    'invisible/makepkg.spaceback.json',
    'invisible/README.spaceback.json',
    'invisible/kpdf/fastpdf-plan.spaceback.json',
    'invisible/kpdf/font_recog_mcp_agent_analysis.spaceback.json',
    'invisible/kpdf/font_recog_myocr_report.spaceback.json',
    'invisible/kpdf/myocr_research.spaceback.json',
    'invisible/kvision/8dewarp_v2.spaceback.json',
    'invisible/twiki/desoftware.spaceback.json',
    'kaoyu/index.spaceback.json'
)

Push-Location -LiteralPath $RepoRoot
try {
    $trackedSourcePaths = New-Object System.Collections.Generic.List[string]
    $targetPaths = New-Object System.Collections.Generic.List[string]
    $nestedInvisibleSourcePaths = New-Object System.Collections.Generic.List[string]
    $nestedInvisibleTargetPaths = New-Object System.Collections.Generic.List[string]

    foreach ($relativePath in $relativePaths) {
        $targetRelativePath = $relativePath -replace '\.spaceback\.json$', '.spacefix.json'
        $sourcePath = Join-Path $RepoRoot ($relativePath -replace '/', [System.IO.Path]::DirectorySeparatorChar)
        $targetPath = Join-Path $RepoRoot ($targetRelativePath -replace '/', [System.IO.Path]::DirectorySeparatorChar)
        $sourceExists = Test-Path -LiteralPath $sourcePath
        $targetExists = Test-Path -LiteralPath $targetPath

        if ($sourceExists -and $targetExists) {
            throw "Both source and target exist: $relativePath -> $targetRelativePath"
        }

        if ($sourceExists) {
            Move-Item -LiteralPath $sourcePath -Destination $targetPath
            Write-Host "Renamed $relativePath -> $targetRelativePath"
        }
        elseif ($targetExists) {
            Write-Host "Already renamed $targetRelativePath"
        }
        else {
            throw "Neither source nor target exists: $relativePath"
        }

        if ($relativePath.StartsWith('invisible/')) {
            $nestedInvisibleSourcePaths.Add($relativePath.Substring('invisible/'.Length))
            $nestedInvisibleTargetPaths.Add($targetRelativePath.Substring('invisible/'.Length))
        }
        else {
            $trackedPath = git ls-files -- $relativePath
            if ($trackedPath) {
                $trackedSourcePaths.Add($relativePath)
            }

            $targetPaths.Add($targetRelativePath)
        }
    }

    if ($trackedSourcePaths.Count -gt 0) {
        git add -A -- @trackedSourcePaths
    }

    if ($targetPaths.Count -gt 0) {
        git add -f -- @targetPaths
    }

    if ($nestedInvisibleTargetPaths.Count -gt 0) {
        Push-Location -LiteralPath (Join-Path $RepoRoot 'invisible')
        try {
            git add -A -- @nestedInvisibleSourcePaths
            git add -f -- @nestedInvisibleTargetPaths
        }
        finally {
            Pop-Location
        }
    }
}
finally {
    Pop-Location
}
