$htmlPath = "d:\BVP.zip\index.html"
$htmlContent = Get-Content -Raw -Path $htmlPath

# Find the features-overlap-section block
$featuresRegex = '(?s)(<!-- Start features Overlap -->.*?</style>)\s*(<!-- start of static-hero-->)'
if ($htmlContent -match $featuresRegex) {
    $featuresBlock = $matches[1]
    
    # Remove the features block from its original position
    $htmlContent = $htmlContent -replace $featuresRegex, '$2'
    
    # Now find the start of static hero container
    $heroRegex = '(?s)(<section class="static-hero section-light-maroon"\s*style="padding: 20px 0 20px !important; background: url\(''assets/images/bvpp\.webp''\) no-repeat center center; background-size: cover;">)'
    
    if ($htmlContent -match $heroRegex) {
        # Modify the features block margin-bottom
        $modifiedFeatures = $featuresBlock -replace 'margin-bottom: -30px;', 'margin-bottom: 40px;'
        
        # Insert inside static-hero
        $replacement = "$1`n    $modifiedFeatures"
        $htmlContent = $htmlContent -replace $heroRegex, $replacement
        
        # Also let's change static-hero padding to 0 0 20px !important to align perfectly
        $htmlContent = $htmlContent -replace 'padding: 20px 0 20px !important;', 'padding: 0 0 20px !important;'
        
        Set-Content -Path $htmlPath -Value $htmlContent
        Write-Host "Successfully moved features section inside static-hero!"
    } else {
        Write-Host "Could not find static-hero to insert."
    }
} else {
    Write-Host "Could not find features block."
}
