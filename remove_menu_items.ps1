$regex = '(?m)^[ \t]*<li><a href="(swach-bharat|sasaket-bharat)\.html">.*?(Swach|Sasaket) Bharat</a></li>\r?\n'

$count = 0
Get-ChildItem -Path "d:\BVP.zip\*.html" | ForEach-Object {
    $content = [System.IO.File]::ReadAllText($_.FullName)
    if ($content -match $regex) {
        $content = $content -replace $regex, ''
        [System.IO.File]::WriteAllText($_.FullName, $content)
        Write-Host "Updated $($_.Name)"
        $count++
    }
}
Write-Host "Total files updated: $count"
