$utf8 = New-Object System.Text.UTF8Encoding $false
$footerHtml = [System.IO.File]::ReadAllText("contact.html", $utf8)
$startMarker = "<!-- start footer -->"
$endMarker = "<!-- end footer -->"

$startIndex = $footerHtml.IndexOf($startMarker)
$endIndex = $footerHtml.IndexOf($endMarker) + $endMarker.Length
$newFooter = $footerHtml.Substring($startIndex, $endIndex - $startIndex)

$files = Get-ChildItem -Path "*.html"

$updated = 0
foreach ($file in $files) {
    $filePath = $file.FullName
    if ($file.Name -eq "contact.html") { continue }
    $content = [System.IO.File]::ReadAllText($filePath, $utf8)
    
    if ($content.Contains($startMarker) -and $content.Contains($endMarker)) {
        $contentStartIndex = $content.IndexOf($startMarker)
        $contentEndIndex = $content.IndexOf($endMarker) + $endMarker.Length
        
        $oldFooter = $content.Substring($contentStartIndex, $contentEndIndex - $contentStartIndex)
        
        if ($oldFooter -ne $newFooter) {
            $newContent = $content.Replace($oldFooter, $newFooter)
            [System.IO.File]::WriteAllText($filePath, $newContent, $utf8)
            $updated++
        }
    }
}
Write-Output "Updated footer in $updated HTML files."
