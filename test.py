from bs4 import BeautifulSoup
from django.urls import reverse

# Assuming you have the HTML content in a variable named 'html_content'
# You can replace this with your actual HTML content

html_content = """
<!DOCTYPE html>


{% load static %}
{% load i18n %}
{% get_current_language as LANGUAGE_CODE %}

<html dir="ltr" lang="{{ LANGUAGE_CODE }}">
<head>
<meta content="ie=edge" http-equiv="X-UA-Compatible"/>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>
      {% block title %}
      {% endblock title %}
    </title>
<meta content="Rahman Begjanov" name="author"/>
<meta content="" name="keywords"/>
<meta content="" name="description">

    {% block css %}
      <link href="assets/css/bootstrap.min.css" rel="stylesheet"/>
<link href="assets/css/flaticon.css" rel="stylesheet"/>
<link href="assets/css/remixicon.css" rel="stylesheet"/>
<link href="assets/css/owl.carousel.min.css" rel="stylesheet"/>
<link href="assets/css/owl-theme-default-min.css" rel="stylesheet"/>
<link href="assets/css/odometer.min.css" rel="stylesheet"/>
<link href="assets/css/fancybox.css" rel="stylesheet"/>
<link href="assets/css/aos.css" rel="stylesheet"/>
<link href="assets/css/style.css" rel="stylesheet"/>
<link href="assets/css/responsive.css" rel="stylesheet"/>
<link href="assets/css/dark-theme.css" rel="stylesheet"/>
    {% endblock css %}
  </meta></head>
<body>
<!--Preloader starts-->
<div class="loader js-preloader">
<div></div>
<div></div>
<div></div>
</div>
<!--Preloader ends-->
<!-- Theme Switcher Start -->
<div class="switch-theme-mode">
<label class="switch" id="switch">
<input id="slider" onchange="toggleTheme()" type="checkbox"/>
<span class="slider round"></span>
</label>
</div>
<!-- Theme Switcher End -->
<!-- Page Wrapper End -->
<div class="page-wrapper">
<!-- Header Section Start -->
<header class="header-wrap">
<div class="header-top">
<div class="container">
<div class="row align-items-center">
<div class="col-lg-8 col-md-8">
<div class="header-top-left">
<ul class="contact-info list-style">
<li>
<i class="flaticon-phone-call"></i>
<a href="tel:666999888">+666-999-888</a>
</li>
<li>
<i class="flaticon-email-2"></i>
<a href="https://templates.hibotheme.com/cdn-cgi/l/email-protection#0c65626a634c6f606561226f6361"><span class="__cf_email__" data-cfemail="bad3d4dcd5fad9d6d3d794d9d5d7">[email protected]</span></a>
</li>
<li>
<i class="flaticon-pin"></i>
<p>2767 Sunrise Street, NY 1002, USA</p>
</li>
</ul>
</div>
</div>
<div class="col-lg-4 col-md-4">
<div class="header-top-right">
<div class="select-lang">
<i class="ri-earth-fill"></i>
<div class="navbar-option-item navbar-language dropdown language-option">
<button aria-expanded="false" aria-haspopup="true" class="dropdown-toggle" data-bs-toggle="dropdown" type="button">
<span class="lang-name"></span>
</button>
<div class="dropdown-menu language-dropdown-menu">
<a class="dropdown-item" href="#">
<img alt="flag" src='{% static "assets/img/uk.png" %}'/>
                          Eng
                        </a>
<a class="dropdown-item" href="#">
<img alt="flag" src='{% static "assets/img/china.png" %}'/>
                          简体中文
                        </a>
<a class="dropdown-item" href="#">
<img alt="flag" src='{% static "assets/img/uae.png" %}'/>
                          العربيّة
                        </a>
</div>
</div>
</div>
<ul class="social-profile list-style style1">
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
<a href="https://linkedin.com/" target="_blank">
<i class="ri-linkedin-fill"></i>
</a>
</li>
<li>
<a href="https://pinterest.com/">
<i class="ri-pinterest-line"></i>
</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>
<div class="header-bottom">
<div class="container">
<nav class="navbar navbar-expand-md navbar-light">
<a class="navbar-brand" href="index.html">
<img alt="logo" class="logo-light" src='{% static "assets/img/logo.png" %}'/>
<img alt="logo" class="logo-dark" src='{% static "assets/img/logo-white.png" %}'/>
</a>
<div class="collapse navbar-collapse main-menu-wrap" id="navbarSupportedContent">
<div class="menu-close d-lg-none">
<a href="javascript:void(0)"> <i class="ri-close-line"></i></a>
</div>
<ul class="navbar-nav ms-auto">
<li class="nav-item">
<a class="nav-link active" href="#">
                      Home
                      <i class="ri-add-line"></i>
</a>
<ul class="dropdown-menu">
<li class="nav-item">
<a class="nav-link" href="index.html">Home One</a>
</li>
<li class="nav-item">
<a class="nav-link" href="index-2.html">Home Two</a>
</li>
<li class="nav-item">
<a class="nav-link" href="index-3.html">Home Three</a>
</li>
<li class="nav-item">
<a class="nav-link" href="index-4.html">Home Four</a>
</li>
<li class="nav-item">
<a class="nav-link active" href="index-5.html">Home Five</a>
</li>
</ul>
</li>
<li class="nav-item">
<a class="nav-link" href="about.html">About Us</a>
</li>
<li class="nav-item">
<a class="nav-link" href="#">
                      Projects
                      <i class="ri-add-line"></i>
</a>
<ul class="dropdown-menu">
<li class="nav-item">
<a class="nav-link" href="project-one.html">Project One</a>
</li>
<li class="nav-item">
<a class="nav-link" href="project-two.html">Project Two</a>
</li>
<li class="nav-item">
<a class="nav-link" href="project-details.html">Single Project</a>
</li>
</ul>
</li>
<li class="nav-item">
<a class="nav-link" href="#">
                      Pages
                      <i class="ri-add-line"></i>
</a>
<ul class="dropdown-menu">
<li class="nav-item">
<a class="nav-link" href="#">
                          Events
                          <i class="ri-add-line"></i>
</a>
<ul class="dropdown-menu">
<li class="nav-item">
<a class="nav-link" href="event.html">Events</a>
</li>
<li class="nav-item">
<a class="nav-link" href="event-details.html">Single Events</a>
</li>
</ul>
</li>
<li class="nav-item">
<a class="nav-link" href="#">
                          Volunteer
                          <i class="ri-add-line"></i>
</a>
<ul class="dropdown-menu">
<li class="nav-item">
<a class="nav-link" href="team.html">Our Volunteer</a>
</li>
<li class="nav-item">
<a class="nav-link" href="team-details.html">Volunteer Profile</a>
</li>
</ul>
</li>
<li class="nav-item">
<a class="nav-link" href="donation.html">Make Donation</a>
</li>
<li class="nav-item">
<a class="nav-link" href="faq.html">FAQ</a>
</li>
<li class="nav-item">
<a class="nav-link" href="#">
                          User Pages
                          <i class="ri-add-line"></i>
</a>
<ul class="dropdown-menu">
<li class="nav-item">
<a class="nav-link" href="login.html">Login</a>
</li>
<li class="nav-item">
<a class="nav-link" href="register.html">Register</a>
</li>
<li class="nav-item">
<a class="nav-link" href="recover-password.html">Recover Password</a>
</li>
</ul>
</li>
<li class="nav-item">
<a class="nav-link" href="terms-of-service.html">Terms of Service</a>
</li>
<li class="nav-item">
<a class="nav-link" href="privacy-policy.html">Privacy Policy</a>
</li>
<li class="nav-item">
<a class="nav-link" href="error-404.html">404 Error Page</a>
</li>
</ul>
</li>
<li class="nav-item">
<a class="nav-link" href="#">
                      Blog
                      <i class="ri-add-line"></i>
</a>
<ul class="dropdown-menu">
<li class="nav-item">
<a class="nav-link" href="#">
                          Blog Layout
                          <i class="ri-add-line"></i>
</a>
<ul class="dropdown-menu">
<li class="nav-item">
<a class="nav-link" href="blog-no-sidebar.html">Blog Grid</a>
</li>
<li class="nav-item">
<a class="nav-link" href="blog-left-sidebar.html">Blog Left Sidebar</a>
</li>
<li class="nav-item">
<a class="nav-link" href="blog-right-sidebar.html">Blog Right Sidebar</a>
</li>
</ul>
</li>
<li class="nav-item">
<a class="nav-link" href="#">
                          Single Blog
                          <i class="ri-add-line"></i>
</a>
<ul class="dropdown-menu">
<li class="nav-item">
<a class="nav-link" href="blog-details-no-sidebar.html">Blog Details No Sidebar</a>
</li>
<li class="nav-item">
<a class="nav-link" href="blog-details-left-sidebar.html">Blog Details Left Sidebar</a>
</li>
<li class="nav-item">
<a class="nav-link" href="blog-details-right-sidebar.html">Blog Details Right Sidebar</a>
</li>
</ul>
</li>
</ul>
</li>
<li class="nav-item">
<a class="nav-link" href="contact.html">Contact Us</a>
</li>
<li class="nav-item d-lg-none">
<a class="nav-link btn style1" href="donation.html">Donate Now</a>
</li>
</ul>
<div class="other-options md-none">
<div class="option-item">
<button class="searchbtn d-xl-none">
<i class="ri-search-line"></i>
</button>
<div class="searchbox lg-none">
<input placeholder="Search..." type="search"/>
<button>
<i class="flaticon-search-1"></i>
</button>
</div>
</div>
<div class="option-item">
<a class="btn style1" href="donation.html">Donate Now</a>
</div>
</div>
</div>
</nav>
<div class="search-area">
<input placeholder="Search Here.." type="search"/>
<button type="submit">
<i class="ri-search-line"></i>
</button>
</div>
<div class="mobile-bar-wrap">
<button class="searchbtn d-lg-none">
<i class="ri-search-line"></i>
</button>
<div class="mobile-menu d-lg-none">
<a href="javascript:void(0)"><i class="ri-menu-line"></i></a>
</div>
</div>
</div>
</div>
</header>
<!-- Header Section End -->
<div class="container">
        {% block content %}
          <p>Default content...</p>
        {% endblock content %}
      </div>
<!-- Footer Section Start -->
<footer class="footer-wrap">
<div class="footer-top">
<img alt="Image" class="footer-shape-one moveHorizontal" src='{% static "assets/img/footer-shape-2.png" %}'/>
<img alt="Image" class="footer-shape-two rotate" src='{% static "assets/img/sun-2.png" %}'/>
<img alt="Image" class="footer-shape-three flyLeft" src='{% static "assets/img/bird.html" %}'/>
<div class="container">
<div class="row pt-100 pb-75">
<div class="col-xl-4 col-lg-4 col-md-6 col-sm-6 pe-xl-5">
<div class="footer-widget">
<a class="footer-logo" href="index.html">
<img alt="Image" src='{% static "assets/img/logo-white.png" %}'/>
</a>
<p class="comp-desc">
                    Lorem ipsum dolor sit amet consc tetur adicing elit. Dolor emque dicta molest enim beatae ame consequ atur tempo pretium auctor nam.
                  </p>
<div class="newsletter-form">
<input placeholder="Email Address" type="email"/>
<button type="button">Subscribe Now</button>
</div>
</div>
</div>
<div class="col-xl-3 col-lg-3 col-md-6 col-sm-6 ps-xl-5 ps-lg-4 ps-md-5">
<div class="footer-widget">
<h3 class="footer-widget-title">Explore</h3>
<ul class="footer-menu list-style">
<li>
<a href="event-details.html">Fundraise For Health</a>
</li>
<li>
<a href="event-details.html">Shelter For Refuge</a>
</li>
<li>
<a href="event-details.html">Adopt Orphan Child</a>
</li>
<li>
<a href="event-details.html">Education For Poor</a>
</li>
<li>
<a href="event-details.html">Clean Water Project</a>
</li>
</ul>
</div>
</div>
<div class="col-xl-2 col-lg-2 col-md-6 col-sm-6">
<div class="footer-widget">
<h3 class="footer-widget-title">Other Pages</h3>
<ul class="footer-menu list-style">
<li>
<a href="about.html">About us</a>
</li>
<li>
<a href="team.html">Our Team</a>
</li>
<li>
<a href="event.html">Recent Events</a>
</li>
<li>
<a href="donation.html">Make Donation</a>
</li>
<li>
<a href="contact.html">Get In Touch</a>
</li>
</ul>
</div>
</div>
<div class="col-xl-3 col-lg-3 col-md-6 col-sm-6 ps-md-5">
<div class="footer-widget">
<h3 class="footer-widget-title">Official Info</h3>
<ul class="contact-info list-style">
<li>
<i class="flaticon-pin"></i>
<h6>Location</h6>
<p>2767 Sunrise Street, NY 1002, USA</p>
</li>
<li>
<i class="flaticon-mail"></i>
<h6>Email</h6>
<a href="https://templates.hibotheme.com/cdn-cgi/l/email-protection#f49c9198989bb497989d99da979b99"><span class="__cf_email__" data-cfemail="ed8588818182ad8e818480c38e8280">[email protected]</span></a>
</li>
<li>
<i class="flaticon-phone-call"></i>
<h6>Phone</h6>
<a href="tel:13454567877">+1-3454-5678-77</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>
<div class="footer-bottom">
<div class="container">
<div class="row align-items-center">
<div class="col-lg-8 col-md-6 col-sm-7">
<p class="copyright-text">
<i class="ri-copyright-line"></i> Clim is proudly owned by <a href="https://hibotheme.com/">HiboTheme</a>
</p>
</div>
<div class="col-lg-4 col-md-6 col-sm-5">
<ul class="social-profile style1 list-style">
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
</footer>
<!-- Footer Section End -->
</div>
<!-- Page Wrapper End -->
<!-- Back-to-top button Start -->
<a class="back-to-top bounce" href="javascript:void(0)"><i class="ri-arrow-up-s-line"></i></a>
<!-- Back-to-top button End -->

    {% block javascript %}
      <!-- Link of JS files -->
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script src="assets/js/jquery.min.js"></script>
<script src="assets/js/bootstrap.bundle.min.js"></script>
<script src="assets/js/form-validator.min.js"></script>
<script src="assets/js/contact-form-script.js"></script>
<script src="assets/js/aos.js"></script>
<script src="assets/js/owl.carousel.min.js"></script>
<script src="assets/js/owl-thumb.min.js"></script>
<script src="assets/js/odometer.js"></script>
<script src="assets/js/circle-progressbar.min.js"></script>
<script src="assets/js/fancybox.js"></script>
<script src="assets/js/jquery.appear.js"></script>
<script src="assets/js/tweenmax.min.js"></script>
<script src="assets/js/main.js"></script>
    {% endblock javascript %}
  </body>
</html>


"""

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")


# Iterate through all 'a' tags and update the 'href' attribute
for a_tag in soup.find_all("a", href=True):
    a_tag["href"] = f'{{% url "home" %}}'

# Print the modified HTML content
print(soup.prettify())
