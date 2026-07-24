$content = [System.IO.File]::ReadAllText("d:\BVP.zip\healths.html")

$oldStr = '                    <a class="theme-btn" href="contact.html">Join Us</a>
                z-index: 1;'

$newStr = '                    <a class="theme-btn" href="contact.html">Join Us</a>
                  </div>
                </div>
              </div>
            </div>
          </div><!-- end of container -->
        </nav>
      </div>

    </header>
    <!-- end of header -->

        <div class="breadcumb-area" id="page-banner"
            style="background-image: url(''assets/images/branch.png''); background-size: cover; background-position: top center; min-height: 480px; display: flex; align-items: flex-end; padding-bottom: 30px;">
            <div class="container" style="position: relative; z-index: 2;">
                <div class="row">
                    <div class="col-12">
                        <div class="breadcumb-wrap" id="page-title-wrap">
                            <h2>Bharat Vikas Parishad</h2>
                            <h3 id="page-heading">Swach Bharat Sasaket Bharat</h3>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <style>
            #page-banner {
                position: relative;
                overflow: hidden;
            }

            #page-banner::before {
                content: '''';
                position: absolute;
                inset: 0;
                background: linear-gradient(to bottom, rgba(0, 0, 0, 0.1) 50%, rgba(0, 0, 0, 0.7) 100%);
                z-index: 1;'

$content = $content.Replace($oldStr, $newStr)
[System.IO.File]::WriteAllText("d:\BVP.zip\healths.html", $content)
Write-Host "healths.html repaired successfully."
