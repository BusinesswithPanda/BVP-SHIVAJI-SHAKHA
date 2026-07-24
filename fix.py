import sys

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

inserted_top = False
for i, line in enumerate(lines):
    if '});' in line and '<div class="item">' in ''.join(lines[i:i+5]):
        # Found the spot
        insert_idx = i + 1
        lines.insert(insert_idx, """      </script>
    </section>
    <!-- end activities slider -->

    <!-- start showcase section -->
    <section class="showcase-section section-dark-maroon dark-content-overrides"
      style="padding-top: 100px; padding-bottom: 100px;">
      <div class="container text-center mb-5">
        <div class="section-title">
          <span style="color: var(--premium-gold) !important;">Excellence & Recognition</span>
          <h2 style="font-size: 2.8rem; line-height: 1.2; color: #fff; max-width: 1000px; margin: 0 auto;">The Latest Buzz</h2>
        </div>
      </div>
      <div class="container">
        <div class="row g-4">
          <!-- YouTube Video Slider -->
          <div class="col-12 position-relative px-4">
            <div class="video-slider owl-carousel owl-theme">\n""")
        inserted_top = True
        break

inserted_bottom = False
for i, line in enumerate(lines):
    if '.video-slider .owl-nav { position: absolute;' in line:
        insert_idx = i - 1
        lines.insert(insert_idx, """            </div>
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
                          navText: ['<i class="ti-angle-left"></i>', '<i class="ti-angle-right"></i>'],
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
          </div>
        </div>
      </div>
    </section>\n""")
        inserted_bottom = True
        break

if inserted_top and inserted_bottom:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("SUCCESS")
else:
    print(f"FAILED. top: {inserted_top}, bottom: {inserted_bottom}")
