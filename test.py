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
          <h2>Contact Us</h2>
          <ul class="breadcrumb-menu list-style">
            <li>
              <a href="index.html">Home</a>
            </li>
            <li>Contact Us</li>
          </ul>
        </div>
      </div>
    </div>
    <!-- Breadcrumb End -->

    <!-- Contact Us section Start -->
    <section class="contact-us-wrap ptb-100">
      <div class="container">
        <div class="section-title style1 text-center mb-40">
          <span>Contact Us
            <img src="assets/img/section-shape.png" alt="Image">
          </span>
          <h2>Get In Touch With Us</h2>
        </div>
        <div class="row gx-5 justify-content-center">
          <div class="col-lg-8">
            <div class="contact-form">
              <form class="form-wrap" id="contactForm">
                <div class="row">
                  <div class="col-md-6 col-sm-6">
                    <div class="form-group">
                      <input type="text"
                             name="name"
                             placeholder="Name*"
                             id="name"
                             required
                             data-error="Please enter your name">
                      <div class="help-block with-errors"></div>
                    </div>
                  </div>
                  <div class="col-md-6 col-sm-6">
                    <div class="form-group">
                      <input type="email"
                             name="email"
                             id="email"
                             required
                             placeholder="Email*"
                             data-error="Please enter your email">
                      <div class="help-block with-errors"></div>
                    </div>
                  </div>
                  <div class="col-md-6 col-sm-6">
                    <div class="form-group">
                      <input type="email"
                             name="phone"
                             id="phone"
                             required
                             placeholder="Phone*"
                             data-error="Please enter your phone">
                      <div class="help-block with-errors"></div>
                    </div>
                  </div>
                  <div class="col-md-6 col-sm-6">
                    <div class="form-group">
                      <input type="text"
                             name="msg_subject"
                             placeholder="Subject*"
                             id="msg_subject"
                             required
                             data-error="Please enter your subject">
                      <div class="help-block with-errors"></div>
                    </div>
                  </div>
                  <div class="col-md-12">
                    <div class="form-group v1">
                      <textarea name="message"
                                id="message"
                                placeholder="Your Messages.."
                                cols="30"
                                rows="10"
                                required
                                data-error="Please enter your message"></textarea>
                      <div class="help-block with-errors"></div>
                    </div>
                  </div>
                  <div class="col-12">
                    <div class="form-group">
                      <div class="form-check checkbox">
                        <input name="gridCheck"
                               value="I agree to the terms and privacy policy."
                               class="form-check-input"
                               type="checkbox"
                               id="gridCheck"
                               required>
                        <label class="form-check-label" for="gridCheck">
                          I agree to the <a class="link style1" href="terms-of-service.html">Terms &amp; Conditions</a> and <a class="link style1" href="privacy-policy.html">Privacy Policy</a>
                        </label>
                        <div class="help-block with-errors gridCheck-error"></div>
                      </div>
                    </div>
                  </div>
                  <div class="col-12">
                    <button type="submit" class="btn style1 w-100 d-block">Send Message</button>
                    <div id="msgSubmit" class="h3 text-center hidden"></div>
                    <div class="clearfix"></div>
                  </div>
                </div>
              </form>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="contact-item-wrap">
              <div class="contact-item">
                <h3>Our Address</h3>
                <p>2767 Sunrise Street, 127 St. Josef Avenue, Florida, USA</p>
              </div>
              <div class="contact-item">
                <h3>Email Address</h3>
                <a href="https://templates.hibotheme.com/cdn-cgi/l/email-protection#87efe2ebebe8c7e4ebeeeaa9e4e8ea"><span class="__cf_email__" data-cfemail="254d4049494a6546494c480b464a48">[email&#160;protected]</span></a>
                <a href="https://templates.hibotheme.com/cdn-cgi/l/email-protection#5a292f2a2a35282e1a3936333774393537"><span class="__cf_email__"
      data-cfemail="d0a3a5a0a0bfa2a490b3bcb9bdfeb3bfbd">[email&#160;protected]</span></a>
              </div>
              <div class="contact-item">
                <h3>24/7 Support</h3>
                <a href="tel:9094630378">909-463-0378</a>
                <a href="tel:tel:4074386389">407-438-6389</a>
              </div>
              <div class="contact-item">
                <h3>Follow us</h3>
                <ul class="social-profile style2 list-style">
                  <li>
                    <a href="https://facebook.com/">
                      <i class="ri-facebook-fill"></i>
                    </a>
                  </li>
                  <li>
                    <a href="https://twitter.com/">
                      <i class="ri-twitter-fill"></i>
                    </a>
                  </li>
                  <li>
                    <a href="https://instagram.com/">
                      <i class="ri-instagram-line"></i>
                    </a>
                  </li>
                  <li>
                    <a href="https://linkedin.com/">
                      <i class="ri-linkedin-fill"></i>
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- Contact Us section End -->

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
