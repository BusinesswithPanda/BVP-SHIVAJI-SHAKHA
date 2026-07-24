$regex = '(?s)([ \t]*)<li class="menu-item-has-children">\s*<a href="media\.html">Media</a>\s*</li>'
$replacement = '$1<li class="menu-item-has-children">
$1  <a href="media.html">Media</a>
$1  <ul class="sub-menu">
$1    <li><a href="photo.html">Photo</a></li>
$1    <li><a href="video.html">Video</a></li>
$1  </ul>
$1</li>'

$count = 0
Get-ChildItem -Path "d:\BVP.zip\*.html" -Exclude "index.html" | ForEach-Object {
    $content = [System.IO.File]::ReadAllText($_.FullName)
    if ($content -match $regex) {
        $content = $content -replace $regex, $replacement
        [System.IO.File]::WriteAllText($_.FullName, $content)
        Write-Host "Updated $($_.Name)"
        $count++
    }
}
Write-Host "Total files updated: $count"
