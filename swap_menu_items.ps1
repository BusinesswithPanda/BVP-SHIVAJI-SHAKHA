$regex = '(?s)(<li><a href="miscellaneous\.html">Miscellaneous</a></li>)(\s*)(<li><a href="healths\.html">Healths</a></li>)'
$replacement = '$3$2$1'

$count = 0
Get-ChildItem -Path "d:\BVP.zip\*.html" | ForEach-Object {
    $content = [System.IO.File]::ReadAllText($_.FullName)
    if ($content -match $regex) {
        $content = $content -replace $regex, $replacement
        [System.IO.File]::WriteAllText($_.FullName, $content)
        Write-Host "Updated $($_.Name)"
        $count++
    }
}
Write-Host "Total files updated: $count"
