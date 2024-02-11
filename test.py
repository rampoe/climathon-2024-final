from bs4 import BeautifulSoup
from django.urls import reverse

# Assuming you have the HTML content in a variable named 'html_content'
# You can replace this with your actual HTML content

html_content = """

{% extends "_base.html" %}



{% block content %}
            <!-- Content Wrapper Start -->
            <div class="content-wrapper">

              <!-- Breadcrumb Start -->
              <div class="breadcrumb-wrap bg-f br-1">
                  <div class="container">
                      <div class="breadcrumb-title">
                          <h2>About Us</h2>
                          <ul class="breadcrumb-menu list-style">
                              <li><a href="index.html">Home </a></li>
                              <li>About Us</li>
                          </ul>
                      </div>
                  </div>
              </div>
              <!-- Breadcrumb End -->

              <!-- About Section Start -->
              <section class="about-wrap style1 ptb-100">
                  <img src="assets/img/about/about-shape-2.png" alt="Image" class="about-shape-one">
                  <img src="assets/img/shape-2.png" alt="Image" class="about-shape-two flyUp">
                  <img src="assets/img/about/deer.png" alt="Image" class="about-shape-three moveHorizontal">
                  <div class="container">
                      <div class="row align-items-center gx-5">
                          <div class="col-lg-6">
                              <div class="about-img-wrap bg-f">
                                  <div class="about-quote">
                                      <i class="flaticon-right-quote"></i>
                                      <p>Lorem ipsum dolor sit amet conse ctet adip elit ollicitu din conse ctetur netus dui ultrice lectus ac egestas ips ctetur ctet adip  ivamus tellu aliq. </p>
                                  </div>
                              </div>
                          </div>
                          <div class="col-lg-6">
                              <div class="about-content">
                                  <div class="content-title style1">
                                      <span>A Little Introduction<img src="assets/img/section-shape.png" alt="Image"></span>
                                      <h2>Protect Our Earth Against Climate Change</h2>
                                      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sollicitudin consectetur netus dui, ultrices or lectus ac egestas. Vivamus tellus vestibulum aliquet arcu a duis. Sollicitudin consectetur netus du ultric. </p>
                                  </div>
                                  <ul class="content-feature-list list-style mb-0">
                                      <li><i class="ri-checkbox-circle-line"></i>Curabitur vitae ullamcorper libe roras id augue 
                                      </li>
                                      <li><i class="ri-checkbox-circle-line"></i>Felis cras luctus nisi in tincidunt blandit 
                                      </li>
                                      <li><i class="ri-checkbox-circle-line"></i>Sapien mi vestibulum est commodo lobortis metus 
                                      </li>
                                      <li><i class="ri-checkbox-circle-line"></i>Mauris vitae purus blandit fermentum </li>
                                  </ul>
                              </div>
                          </div>
                      </div>
                  </div>
              </section>
              <!-- About Section End -->

              <!-- Team Section Start -->
              <section class="team-wrap ptb-100 bg-sand">
                  <div class="container">
                      <div class="section-title style1 text-center mb-40">
                          <span>Our Volunteer <img src="assets/img/section-shape.png" alt="Image"></span>
                          <h2>Our Experts Volunteer</h2>
                      </div>
                      <div class="team-slider-one owl-carousel">
                          <div class="team-card style1">
                              <img src="assets/img/team/team-1.jpg" alt="Image">
                              <div class="team-info">
                                  <img src="assets/img/team/team-shape-2.png" alt="IMage" class="team-shape">
                                  <h3><a href="team-details.html">Kevin Thompson</a></h3>
                                  <span>Founder &amp; CEO</span>
                                  <ul class="social-profile style1 list-style">
                                      <li>
                                          <a href="https://facebook.com/" target="_blank">
                                              <i class="ri-facebook-fill"></i>
                                          </a>
                                      </li>
                                      <li>
                                          <a href="https://twitter.com/" target="_blank">
                                              <i class="ri-twitter-fill"></i>
                                          </a>
                                      </li>
                                      <li>
                                          <a href="https://instagram.com/" target="_blank">
                                              <i class="ri-instagram-line"></i>
                                          </a>
                                      </li>
                                      <li>
                                          <a href="https://linkedin.com/" target="_blank">
                                              <i class="ri-linkedin-fill"></i>
                                          </a>
                                      </li>
                                  </ul>
                              </div>
                          </div>
                          <div class="team-card style1">
                              <img src="assets/img/team/team-2.jpg" alt="Image">
                              <div class="team-info">
                                  <img src="assets/img/team/team-shape-2.png" alt="IMage" class="team-shape">
                                  <h3><a href="team-details.html">Isabella Woods</a></h3>
                                  <span>Cheif Marketing Officer</span>
                                  <ul class="social-profile style1 list-style">
                                      <li>
                                          <a href="https://facebook.com/" target="_blank">
                                              <i class="ri-facebook-fill"></i>
                                          </a>
                                      </li>
                                      <li>
                                         <a href="https://twitter.com/" target="_blank">
                                              <i class="ri-twitter-fill"></i>
                                          </a>
                                      </li>
                                      <li>
                                          <a href="https://instagram.com/" target="_blank">
                                              <i class="ri-instagram-line"></i>
                                          </a>
                                      </li>
                                      <li>
                                         <a href="https://linkedin.com/" target="_blank">
                                              <i class="ri-linkedin-fill"></i>
                                          </a>
                                      </li>
                                  </ul>
                              </div>
                          </div>
                          <div class="team-card style1">
                              <img src="assets/img/team/team-3.jpg" alt="Image">
                              <div class="team-info">
                                  <img src="assets/img/team/team-shape-2.png" alt="IMage" class="team-shape">
                                  <h3><a href="team-details.html">Liam Stokes</a></h3>
                                  <span>Senior Executive</span>
                                  <ul class="social-profile style1 list-style">
                                      <li>
                                          <a href="https://facebook.com/" target="_blank">
                                              <i class="ri-facebook-fill"></i>
                                          </a>
                                      </li>
                                      <li>
                                         <a href="https://twitter.com/" target="_blank">
                                              <i class="ri-twitter-fill"></i>
                                          </a>
                                      </li>
                                      <li>
                                          <a href="https://instagram.com/" target="_blank">
                                              <i class="ri-instagram-line"></i>
                                          </a>
                                      </li>
                                      <li>
                                         <a href="https://linkedin.com/" target="_blank">
                                              <i class="ri-linkedin-fill"></i>
                                          </a>
                                      </li>
                                  </ul>
                              </div>
                          </div>
                          <div class="team-card style1">
                              <img src="assets/img/team/team-4.jpg" alt="Image">
                              <div class="team-info">
                                  <img src="assets/img/team/team-shape-2.png" alt="IMage" class="team-shape">
                                  <h3><a href="team-details.html">Lucy Floyd</a></h3>
                                  <span>Accounts Manager</span>
                                  <ul class="social-profile style1 list-style">
                                      <li>
                                          <a href="https://facebook.com/" target="_blank">
                                              <i class="ri-facebook-fill"></i>
                                          </a>
                                      </li>
                                      <li>
                                         <a href="https://twitter.com/" target="_blank">
                                              <i class="ri-twitter-fill"></i>
                                          </a>
                                      </li>
                                      <li>
                                          <a href="https://instagram.com/" target="_blank">
                                              <i class="ri-instagram-line"></i>
                                          </a>
                                      </li>
                                      <li>
                                         <a href="https://linkedin.com/" target="_blank">
                                              <i class="ri-linkedin-fill"></i>
                                          </a>
                                      </li>
                                  </ul>
                              </div>
                          </div>
                          <div class="team-card style1">
                              <img src="assets/img/team/team-5.jpg" alt="Image">
                              <div class="team-info">
                                  <img src="assets/img/team/team-shape-2.png" alt="IMage" class="team-shape">
                                  <h3><a href="team-details.html">Hannah Adison</a></h3>
                                  <span>Marketing Manager</span>
                                  <ul class="social-profile style1 list-style">
                                      <li>
                                          <a href="https://facebook.com/" target="_blank">
                                              <i class="ri-facebook-fill"></i>
                                          </a>
                                      </li>
                                      <li>
                                         <a href="https://twitter.com/" target="_blank">
                                              <i class="ri-twitter-fill"></i>
                                          </a>
                                      </li>
                                      <li>
                                          <a href="https://instagram.com/" target="_blank">
                                              <i class="ri-instagram-line"></i>
                                          </a>
                                      </li>
                                      <li>
                                         <a href="https://linkedin.com/" target="_blank">
                                              <i class="ri-linkedin-fill"></i>
                                          </a>
                                      </li>
                                  </ul>
                              </div>
                          </div>
                          <div class="team-card style1">
                              <img src="assets/img/team/team-6.jpg" alt="Image">
                              <div class="team-info">
                                  <img src="assets/img/team/team-shape-2.png" alt="IMage" class="team-shape">
                                  <h3><a href="team-details.html">Jaylen Mills </a></h3>
                                  <span>Senior Executive</span>
                                  <ul class="social-profile style1 list-style">
                                      <li>
                                          <a href="https://facebook.com/" target="_blank">
                                              <i class="ri-facebook-fill"></i>
                                          </a>
                                      </li>
                                      <li>
                                         <a href="https://twitter.com/" target="_blank">
                                              <i class="ri-twitter-fill"></i>
                                          </a>
                                      </li>
                                      <li>
                                          <a href="https://instagram.com/" target="_blank">
                                              <i class="ri-instagram-line"></i>
                                          </a>
                                      </li>
                                      <li>
                                         <a href="https://linkedin.com/" target="_blank">
                                              <i class="ri-linkedin-fill"></i>
                                          </a>
                                      </li>
                                  </ul>
                              </div>
                          </div>
                      </div>
                  </div>
              </section>
              <!-- Team Section End -->

              <div class="container mt-100">
                  <div class="donate-box ptb-100">
                      <img src="assets/img/shape-6.png" alt="Image" class="donate-shape-one">
                      <div class="content-title style2 text-center mb-40">
                          <span>You Can Donate<img src="assets/img/section-shape.png" alt="Image"></span>
                          <h2>Your Donation Matters</h2>
                      </div>
                      <ul class="donate-amt list-style">
                          <li><button type="button">$20</button></li>
                          <li><button type="button">$50</button></li>
                          <li><button type="button">$100</button></li>
                          <li><button type="button">$500</button></li>
                          <li><button type="button">$1000</button></li>
                          <li><button type="button">Other</button></li>
                      </ul>
                      <button type="submit" class="btn style2">Donate Now</button>
                  </div>
              </div>

              <!-- Counter Section Start -->
              <div class="counter-wrap style1">
                  <img src="assets/img/shape-13.png" alt="Image" class="counter-shape-one">
                  <img src="assets/img/about/skull.png" alt="Image" class="counter-shape-two moveHorizontal">
                  <img src="assets/img/about/leaves.png" alt="Image" class="counter-shape-three waving_left">
                  <div class="container-fluid ">
                      <div class="row gx-5">
                          <div class="col-xl-7 col-lg-6">
                              <div class="promo-video style1 bg-f">
                                  <a class="play-now" data-fancybox="" href="https://www.youtube.com/watch?v=UNSSuTSQI9I">
                                      <i class="ri-play-fill"></i>
                                      <span class="ripple"></span>
                                  </a>
                              </div>
                          </div>
                          <div class="col-xl-5 col-lg-6">
                              <div class="counter-card-wrap style1">
                                  <div class="counter-card style1">
                                      <div class="counter-text">
                                          <h2 class="counter-num">
                                              <span class="odometer" data-count="8705"></span>
                                          </h2>
                                          <p>Donations</p>
                                      </div>
                                  </div>
                                  <div class="counter-card style2">
                                      <div class="counter-text">
                                          <h2 class="counter-num">
                                              <span class="odometer" data-count="380"></span>
                                          </h2>
                                          <p>Campaigns</p>
                                      </div>
                                  </div>
                                  <div class="counter-card style3">
                                      <div class="counter-text">
                                          <h2 class="counter-num">
                                              <span class="odometer" data-count="9450"></span>
                                          </h2>
                                          <p>Fun Raised</p>
                                      </div>
                                  </div>
                                  <div class="counter-card style4">
                                      <div class="counter-text">
                                          <h2 class="counter-num">
                                              <span class="odometer" data-count="707"></span>
                                          </h2>
                                          <p>Volunteers</p>
                                      </div>
                                  </div>
                              </div>
                          </div>
                      </div>
                  </div>
              </div>
              <!-- Counter Section End -->

              <!-- CTA Section Start -->
              <section class="cta-wrap style1 bg-f ptb-100">
                  <img src="assets/img/bg-shape-5.png" alt="Image" class="cta-shape-two">
                  <div class="container">
                      <div class="row">
                          <div class="col-xl-8 offset-xl-2 col-lg-8 offset-lg-2">
                              <div class="content-title style1 text-center mb-40">
                                  <span>Crowd-Funding <img src="assets/img/section-shape.png" alt="Image"></span>
                                  <h2>Best Way To Make A Difference In The Lives Of Others
                                  </h2>
                              </div>
                              <div class="cta-btn">
                                  <a href="login.html" class="btn style1">Get Started now</a>
                                  <a href="register.html" class="btn style2">Join Our Community</a>
                              </div>
                          </div>
                      </div>
                  </div>
              </section>
              <!-- CTA Section End -->

          </div>
          <!-- Content wrapper end -->
{% endblock content %}


"""

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")


# Iterate through all 'a' tags and update the 'href' attribute
for a_tag in soup.find_all("a", href=True):
    a_tag["href"] = f'{{% url "home" %}}'

# Print the modified HTML content
print(soup.prettify())
