$lines = Get-Content -Path "index.html"

$newContent = @"
          <!-- YouTube Video Slider -->
          <div class=`"col-12 position-relative px-4`">
            <div class=`"video-slider owl-carousel owl-theme`">
              <div class=`"item`">
                <div class=`"ratio ratio-16x9`" style=`"border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.3);`">
                  <iframe src=`"https://www.youtube.com/embed/Pj15bA7R_Qc`" frameborder=`"0`" allowfullscreen></iframe>
                </div>
              </div>
              <div class=`"item`">
                <div class=`"ratio ratio-16x9`" style=`"border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.3);`">
                  <iframe src=`"https://www.youtube.com/embed/Pj15bA7R_Qc`" frameborder=`"0`" allowfullscreen></iframe>
                </div>
              </div>
              <div class=`"item`">
                <div class=`"ratio ratio-16x9`" style=`"border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.3);`">
                  <iframe src=`"https://www.youtube.com/embed/Pj15bA7R_Qc`" frameborder=`"0`" allowfullscreen></iframe>
                </div>
              </div>
              <div class=`"item`">
                <div class=`"ratio ratio-16x9`" style=`"border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.3);`">
                  <iframe src=`"https://www.youtube.com/embed/Pj15bA7R_Qc`" frameborder=`"0`" allowfullscreen></iframe>
                </div>
              </div>
              <div class=`"item`">
                <div class=`"ratio ratio-16x9`" style=`"border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.3);`">
                  <iframe src=`"https://www.youtube.com/embed/Pj15bA7R_Qc`" frameborder=`"0`" allowfullscreen></iframe>
                </div>
              </div>
            </div>
            <script>
              document.addEventListener('DOMContentLoaded', function() {
                setTimeout(function() {
                   var checkExist = setInterval(function() {
                      if (jQuery().owlCarousel) {
                        jQuery('.video-slider').owlCarousel({
                          loop: true,
                          margin: 20,
                          nav: true,
                          dots: false,
                          autoplay: true,
                          autoplayTimeout: 5000,
                          smartSpeed: 800,
                          navText: ['<i class=`"ti-angle-left`"></i>', '<i class=`"ti-angle-right`"></i>'],
                          responsive: {
                            0: { items: 1 },
                            768: { items: 2 },
                            1000: { items: 3 }
                          }
                        });
                        clearInterval(checkExist);
                     }
                  }, 100);
                });
              });
            </script>
            <style>
              .video-slider .owl-nav { position: absolute; top: 50%; width: 100%; transform: translateY(-50%); margin: 0; }
              .video-slider .owl-prev, .video-slider .owl-next { position: absolute; background: var(--primary-maroon) !important; color: white !important; border-radius: 50% !important; width: 50px; height: 50px; display: flex !important; align-items: center; justify-content: center; font-size: 30px !important; box-shadow: 0 4px 10px rgba(0,0,0,0.3); }
              .video-slider .owl-prev { left: -30px; }
              .video-slider .owl-next { right: -30px; }
            </style>
          </div>
"@

$finalLines = $lines[0..1469] + $newContent.Split("`n").TrimEnd("`r") + $lines[1546..($lines.Length-1)]
Set-Content -Path "index.html" -Value $finalLines
