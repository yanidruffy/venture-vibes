# Venture Vibes
<a name="top"></a>
Welcome to [Venture Vibes!](https://venture-vibes-e0fcf8943946.herokuapp.com/)
![Venture Vibes](./readme-files/images/amiresponsive.png)

## Description
**Venture Vibes** is an adventure blog dedicated to showcasing my partner and I's travel experiences, inspiring wanderlust, and providing valuable insights for fellow explorers.<br>
This project features a user-friendly platform where readers can discover captivating stories, and detailed destination guides. The blog aims to document our adventures and create an engaging community for travel enthusiasts. Venture Vibes invites you to join our journey and ignite your passion for travel.

## Testing

### HTML Validator

HTML files have been validated using [W3C Markup Validation Service](https://validator.w3.org/)<br>
A common theme and the only error throughout the validation checks is a CSS error caused by using a newer CSS feature by summernote.

<details>
<summary><strong>HTML Validator Results</strong></summary>

<details>
<summary>Homepage</summary>

![Homepage Result](./readme-files/images/validation/html/homepage-check.png)
</details>

<details>
<summary>Blog Page</summary>

![post-list Result](./readme-files/images/validation/html/post-list-check.png)
</details>

<details>
<summary>Post Detail</summary>

![post-detail Result](./readme-files/images/validation/html/post-detail-check.png)
</details>

<details>
<summary>About</summary>

![About Result](./readme-files/images/validation/html/about-check.png)
</details>

<details>
<summary>Contact Us</summary>

![Contact Result](./readme-files/images/validation/html/contact-check.png)
</details>

<details>
<summary>User Profile</summary>

![Profile Result](./readme-files/images/validation/html/profile-check.png)
</details>

<details>
<summary>404 Error</summary>

![404 Result](./readme-files/images/validation/html/404-check.png)
</details>

<details>
<summary>500 Error</summary>

In order to test this page, a 500 error has been simulated by raising an Exception in about views.
![500 Result](./readme-files/images/validation/html/500-check.png)
</details>
</details>

### CSS Validator
CSS file has been validated using [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

<details>
<summary><strong>CSS Validator Result</strong></summary>

![CSS Validator Result](./readme-files/images/validation/css/css-check.png)
</details>

### Javascript Code Analyzer
JS file has been analyzed by using [JSHint](https://jshint.com/)

<details>
<summary><strong>JS Hint Analysis</strong></summary>

![JS Hint Analysis](./readme-files/images/validation/js/js-check.png)
</details>

### Python Code Linter
All altered Python files have been validated using [CI Python Linter](https://pep8ci.herokuapp.com/)

<details>
<summary><strong>CI Python Linter Analysis</strong></summary>

<details>
<summary>About</summary>

<details>
<summary>admin.py</summary>

![About Admin Linter Result](./readme-files/images/validation/py/about-admin-check.png)
</details>

<details>
<summary>models.py</summary>

![About Models Linter Result](./readme-files/images/validation/py/about-model-check.png)
</details>

<details>
<summary>urls.py</summary>

![About URLs Linter Result](./readme-files/images/validation/py/about-urls-check.png)
</details>

<details>
<summary>views.py</summary>

![About Views Linter Result](./readme-files/images/validation/py/about-views-check.png)
</details>
</details>

<details>
<summary>Blog</summary>

<details>
<summary>admin.py</summary>

![Blog Admin Linter Result](./readme-files/images/validation/py/blog-admin-check.png)
</details>

<details>
<summary>forms.py</summary>

![Blog Forms Linter Result](./readme-files/images/validation/py/blog-forms-check.png)
</details>

<details>
<summary>models.py</summary>

![Blog Models Linter Result](./readme-files/images/validation/py/blog-model-check.png)
</details>

<details>
<summary>urls.py</summary>

![Blog URLs Linter Result](./readme-files/images/validation/py/blog-urls-check.png)
</details>

<details>
<summary>views.py</summary>

![Blog Views Linter Result](./readme-files/images/validation/py/blog-views-check.png)
</details>

</details>

<details>
<summary>Contact</summary>

<details>
<summary>admin.py</summary>

![Contact Admin Linter Result](./readme-files/images/validation/py/contact-admin-check.png)
</details>

<details>
<summary>forms.py</summary>

![Contact Forms Linter Result](./readme-files/images/validation/py/contact-forms-check.png)
</details>

<details>
<summary>models.py</summary>

![Contact Models Linter Result](./readme-files/images/validation/py/contact-model-check.png)
</details>

<details>
<summary>urls.py</summary>

![Contact URLs Linter Result](./readme-files/images/validation/py/contact-urls-check.png)
</details>

<details>
<summary>views.py</summary>

![Contact Views Linter Result](./readme-files/images/validation/py/contact-views-check.png)
</details>
</details>

<details>
<summary>Profiles</summary>

<details>
<summary>urls.py</summary>

![Profiles URLs Linter Result](./readme-files/images/validation/py/profiles-urls-check.png)
</details>

<details>
<summary>views.py</summary>

![Profiles Views Linter Result](./readme-files/images/validation/py/profiles-views-check.png)
</details>
</details>

<details>
<summary>Venture_Vibes</summary>

Altough settings.py has been altered, I have not included it in the validation as it is focused on configurations


<details>
<summary>urls.py</summary>

![Venture_Vibes URLs Linter Result](./readme-files/images/validation/py/venture_vibes-urls-check.png)
</details>

<details>
<summary>views.py</summary>

![Venture_Vibes Views Linter Result](./readme-files/images/validation/py/venture_vibes-views-check.png)
</details>
</details>
</details>

### Responsiveness Test
I have tested the website on its responsiveness using [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) and ui.dev's [amiresponsive](https://ui.dev/amiresponsive)

### Lighthouse

The Lighthouse reports have been generated to audit the website for performance, accessibility, best practices, and SEO across various key pages.

<details>
<summary><strong>Homepage</strong></summary>

<details>
<summary>Desktop</summary>

![Homepage Desktop Lighthouse Score](./readme-files/images/lighthouse/homepage-desktop-check.png)
</details>

<details>
<summary>Mobile</summary>

![Homepage Mobile Lighthouse Score](./readme-files/images/lighthouse/homepage-mobile-check.png)
</details>

</details>

<details>
<summary><strong>Blog Page</strong></summary>

<details>
<summary>Desktop</summary>

![Iceland Roadtrip Desktop Lighthouse Score](./readme-files/images/lighthouse/blog-desktop-check.png)
</details>

<details>
<summary>Mobile</summary>

![Iceland Roadtrip Mobile Lighthouse Score](./readme-files/images/lighthouse/blog-mobile-check.png)
</details>

</details>

<details>
<summary><strong>Post Detail</strong></summary>

<details>
<summary>Desktop</summary>

![Post Detail Desktop Lighthouse Score](./readme-files/images/lighthouse/post-desktop-check.png)
</details>

<details>
<summary>Mobile</summary>

![Post Detail Mobile Lighthouse Score](./readme-files/images/lighthouse/post-mobile-check.png)
</details>
</details>

<details>
<summary><strong>About</strong></summary>

<details>
<summary>Desktop</summary>

![About Desktop Lighthouse Score](./readme-files/images/lighthouse/about-desktop-check.png)
</details>

<details>
<summary>Mobile</summary>

![About Mobile Lighthouse Score](./readme-files/images/lighthouse/about-mobile-check.png)
</details>
</details>

<details>
<summary><strong>Contact Us</strong></summary>

<details>
<summary>Desktop</summary>

![Contact Us Desktop Lighthouse Score](./readme-files/images/lighthouse/contact-desktop-check.png)
</details>

<details>
<summary>Mobile</summary>

![Contact Us Mobile Lighthouse Score](./readme-files/images/lighthouse/contact-mobile-check.png)
</details>
</details>

<details>
<summary><strong>User Profile</strong></summary>

<details>
<summary>Desktop</summary>

![User Profile Desktop Lighthouse Score](./readme-files/images/lighthouse/profile-desktop-check.png)
</details>

<details>
<summary>Mobile</summary>

![User Profile Mobile Lighthouse Score](./readme-files/images/lighthouse/profile-mobile-check.png)
</details>
</details>

### Manual Testing

Manual testing was performed to ensure the application meets the acceptance criteria outlined in the [User Stories](https://intriguing-caper-d96.notion.site/a850adf08793496bb36409cc238f0533?v=dd73d186fa8e4a9f85ccfa0c624279c8).<br>
I reviewed each user story and tested the corresponding features to ensure everything works as expected. Through manual testing, I was able to confirm that the application functions well and is user-friendly, meeting the needs and expectations of users.

### Peer Review

Friends, colleagues, and my mentor tested the application across various devices to ensure its functionality and usability. Their feedback helped identify areas for improvement, contributing to a more robust final product.

[Back to Top](#top)