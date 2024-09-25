# Venture Vibes
<a name="top"></a>
Welcome to [Venture Vibes!](https://venture-vibes-e0fcf8943946.herokuapp.com/)
![Venture Vibes](./readme-files/images/amiresponsive.png)

## Description
**Venture Vibes** is an adventure blog dedicated to showcasing the travel experiences of my partner and me, inspiring wanderlust, and providing valuable insights for fellow explorers.<br>
This project features a user-friendly platform where readers can discover captivating stories, and detailed destination guides. The blog aims to document our adventures and create an engaging community for travel enthusiasts. Venture Vibes invites you to join our journey and ignite your passion for travel.

## User Experience

### Wireframes

All wireframes were created using [Balsamiq](https://balsamiq.com/wireframes/). The purpose was to outline the basic structure and layout of the website.

<details>
<summary><strong>Homepage</strong></summary>

![Homepage Wireframe](./readme-files/images/wireframes/homepage-wireframe.png)
</details>

<details>
<summary><strong>Blog</strong></summary>

![Blog Wireframe](./readme-files/images/wireframes/blog-wireframe.png)
</details>

<details>
<summary><strong>Blog Post</strong></summary>

![Blog Post Wireframe](./readme-files/images/wireframes/blog-post-wireframe.png)
</details>

<details>
<summary><strong>About</strong></summary>

![About Wireframe](./readme-files/images/wireframes/about-wireframe.png)
</details>

### User Stories

For this part of the project, I used [Notion](https://www.notion.so/) to work on my [project board](https://www.notion.so/Venture-Vibes-Project-Management-561b1b85789f49ce8c0ad37801c98188?pvs=4) using an agile approach.

<details>
<summary><strong>Project Board</strong></summary>

![Project Board](./readme-files/images/project-board.png)
</details>

The project was guided by the following user story structure:
- **Title:** of the User Story
- **Description:** As a *role* I can *capability* so that *received benefit*
- **Acceptance Criteria:** Clear, measurable conditions that must be done in order for the user story to be considered complete
- **Tasks:** Actionable items needed to implement the user story

<details>
<summary><strong>User Story Example</strong></summary>

![User Story](./readme-files/images/user-story.png)
</details>

For a full list of user stories, visit the [User Stories](https://intriguing-caper-d96.notion.site/a850adf08793496bb36409cc238f0533?v=dd73d186fa8e4a9f85ccfa0c624279c8) or the previous link above.

### Design Choices

#### Color Scheme
The color scheme was created using [coolors](https://coolors.co/). I chose these colors to fit the feeling of exploration, nature and adventure. On top, since the first adventure is taking place in Iceland, I went for a cooler tone.

<details>
<summary><strong>Color Palette</strong></summary>

![Color Palette](./readme-files/images/color-palette.png)
</details>

#### Typography

I decided to keep the typography simple by using a clean and readable sans-serif font. **Verdana** was the choice for me. Due to limitations with the Summernote editor in Django, I opted for
**Helvetica Neue**, a similar sans-serif font for the blog posts.

[Back to Top](#top)

## Features

### Existing Features

- **Stunning Visuals:** Captivating pictures accompany each story to immerse the reader in the experience
- **Commenting Capability:** Readers can share their experiences by commenting on posts
- **Like Functionality:** Show appreciation for favorite posts by liking them
- **Responsive Design:** Ensures optimal view across various devices
- **User-friendly Interface:** An intuitive website for browsing

#### Homepage
The **homepage** serves as the hub of **Venture Vibes** with an eye-catching banner, stunning travel images and featuring the latest blog post.

![Full Homepage](./readme-files/images/home-full.png)

<details>
<summary><strong>Navbar and Hero section</strong></summary>
The navigation bar will be visible throughout every page you are visiting on the website. When clicking on the logo "Venture Vibes", you get redirected to the homepage.
In the middle of the bar you will find a "Home" button, a dropdown menu "Adventures" that has the current adventure as an item and the "About" page. In the Hero section, we welcome the user to our homepage.
<details>
<summary>User is authenticated</summary>
When the User is logged in, the navigation bar includes personalized options such as "Profile" and "Sign out", allowing the user to access their profile account.
Furthermore, the Hero Section is displaying buttons to the "Blog" and the "Contact Us" page.

![Logged in User View Homepage](./readme-files/images/home-navhero-authuser.png)
</details>

<details>
<summary>User is not authenticated</summary>
When the User is not logged in, the navigation bar features buttons to "Login" and "Sign-up", animating to engage further with the website. The Hero Section is displaying buttons to the "Blog" and the "Join Us" page.

![Logged out User View Homepage](./readme-files/images/home-navhero-nonauthuser.png)
</details>
</details>

<details>
<summary><strong>Carousel Images</strong></summary>

The homepage features a carousel of three travel images, showcasing various destinations from the recent trip to Iceland. The goal is to entice them to explore the blog further.

![Third Carousel Image](./readme-files/images/home-carousel.png)
</details>

<details>
<summary><strong>Latest Blog Post</strong></summary>

The homepage highlights the most recent blog post, giving readers a glimpse of the latest adventure, encouraging engagement with the freshest stories on the blog.
</details>

<details>
<summary><strong>Footer</strong></summary>

The footer provides essential links for staying connected. It includes social media icons, allowing users to follow the blog on platforms like X, Instagram and Facebook. And lets not forget the copyright notice.
</details>

#### Blog

The **Blog** section is the heart of Venture Vibes, where users can explore a variety of travel posts. This section features a hero section, card-based blog previews, and pagination to navigate through multiple posts with ease.

![Full Blog Page](./readme-files/images/blog-full.png)

<details>
<summary><strong>Hero Section</strong></summary>

The blog section begins with a Hero Section that is used as an introduction to the chosen adventure. In this example, it's an epic road trip across Iceland, offering a preview of the adventure and inviting readers to join the journey.

The hero image complements the post, giving a visual glimpse of what readers can expect.
</details>

<details>
<summary><strong>Blog Cards</strong></summary>

Below the Hero section, the blog is organized into a series of Blog Cards. Each card contains:
- The title of the Blog Post
- The name of the author and the date the post was published
- A brief excerpt, meant to entice the user
- A call to action that takes the user to the full blog post
</details>

<details>
<summary><strong>Pagination Controls</strong></summary>

The blog page features Pagination Controls at the bottom, allowing users to navigate between different pages of blog posts.
</details>

#### Post Detail

The **Post Detail** page allows readers to dive deeper into each individual blog post. Users get a rich narrative that is supported by a stunning picture and opportunities to engage.
![Full Post Detail Page](./readme-files/images/post-full.png)
<details>
<summary><strong>Hero Section</strong></summary>

The hero section features the title of the post prominently along with a captivating image that sets the scene for the adventure discussed in the blog.
![Post Hero](./readme-files/images/post-hero.png)
</details>

<details>
<summary><strong>Post Content</strong></summary>
The body of the post provides an engaging narrative. The publish date and author information are displayed at the bottom.
</details>

<details>
<summary><strong>Like Button</strong></summary>
Authenticated users can express their appreciation for the post by clicking the like button. The button visually indicates whether the user has liked the post and displays the total number of likes. For a visual, check the upcoming "Comments Section" pictures.
</details>

<details>
<summary><strong>Comments Section</strong></summary>
Authenticated user can engage with the content by leaving comments. The section displays the total number of comments, allowing users to read and interact with fellow travelers. Underneath is a simple comment form to do so. A post can be awaiting approval or you have the option to edit and delete your own post.

<details>
<summary>User is authenticated</summary>

![Logged in User View](./readme-files/images/post-authuser.png)
</details>

<details>
<summary>User is not authenticated</summary>

![Logged out User View](./readme-files/images/post-nonauthuser.png)
</details>
</details>

#### About

The **About** page provides users with insights into the creators of **Venture Vibes**, sharing the passion and motivation behind the blog. It serves as a personal touchpoint, helping readers connect with the authors and understand the purpose of the platform. It features an image of the bloggers in a stunning location, visually representing the adventures that the blog discusses. A "Contact Us" button allows visitors to reach out for inquiries or collaborations for further engagement.

![Full About Page](./readme-files/images/about-full.png)

#### User Profile

The **User Profile** page allows users to view and manage their activity on **Venture Vibes**. It provides a personalized experience, showcasing approved and unapproved comments as well as posts the user has liked.

![Full User Profile Page](./readme-files/images/profile-full.png)

#### Admin Panel

The **Admin Panel** of **Venture Vibes** provides a django backend interface for managing content, users, and site settings. This allows the administrator to oversee all aspects of the website.

![Full Admin Panel](./readme-files/images/admin-full.png)

Important for managing Blog Posts:
<details>
<summary><strong>Post Management</strong></summary>
This section allows admins to create, edit, and delete blog posts, including an image.
</details>

<details>
<summary><strong>Comment Moderation</strong></summary>
Admins can review and approve or reject user comments. This feature helps to filter out inappropriate content.
</details>

### Features in Planning

The primary goal of **Venture Vibes** is to continuously add more adventures and enhance the user experience. With this growth in mind, the backend has been designed for modularity, breaking it down into smaller, manageable apps. If you're curious what is planned next, check out [User Stories](https://intriguing-caper-d96.notion.site/Venture-Vibes-Project-Management-561b1b85789f49ce8c0ad37801c98188).

[Back to Top](#top)

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

Manual testing was performed to ensure the application meets the acceptance criteria outlined in the [User Stories](https://intriguing-caper-d96.notion.site/Venture-Vibes-Project-Management-561b1b85789f49ce8c0ad37801c98188).<br>
**Each User Story includes a dedicated task for testing.**<br>
I reviewed each user story and tested the corresponding features to ensure everything works as expected. Through manual testing, I confirmed that the application functions well and is user-friendly, meeting the needs and expectations of users.

### Peer Review

Friends, colleagues, and my mentor tested the application across various devices to ensure its functionality and usability. Their feedback helped identify areas for improvement, contributing to a more robust iteration of the application.

[Back to Top](#top)

## Deployment

**Venture Vibes** was deployed using [Heroku](https://www.heroku.com/) and is built upon a template from [Code Institute](https://github.com/Code-Institute-Org/ci-full-template).

1. **Heroku Setup**: 
- Create an account on Heroku and log in
- Click on **New** and choose **Create a new app**
- Follow the steps and click **Create app**

    <details>
    <summary><strong>Create app</strong></summary>

    ![Start Deployment](./readme-files/images/deployment-start.png)
    ![Create App Form Deployment](./readme-files/images/deployment-start-steps.png)
    </details>

2. **Connect to Github Repository**:
- Go to the Deploy tab and look for Deployment method and select **Github**
- Search for your repository and click **Connect**

    <details>
    <summary><strong>Connect to Repository</strong></summary>

    ![Github Connect Repository](./readme-files/images/deployment-github-connect.png)
    </details>


3. **Configure Heroku Settings**:
- Go to the Settings tab and select **Reveal Config Vars**
- Here, add sensitive but necessary data from your `env.py` file, such as database URLs and your secret key
- Ensure that all required environment variables are set for your application to function properly
- Scroll down to Buildpacks and click **Add buildpack**
- Choose **python** and click **Add Buildpack**

    <details>
    <summary><strong>Settings Config & Buildpacks</strong></summary>

    ![Config Vars](./readme-files/images/deployment-config.png)
    ![Buildpacks](./readme-files/images/deployment-buildpack.png)
    </details>

4. **Deploy with Heroku**:
- Deploy the application using git push bash command in your IDE
- Go to Heroku Deploy tab and look for Manual Deploy and click **Deploy Branch**
- There is also an option to Enable Automatic Deploys

    <details>
    <summary><strong>Manual Deploy</strong></summary>

    ![Deploy Branch](./readme-files/images/deployment-branch.png)
    </details>

5. **Finalizing Deployment**:
- Once the deployment is complete, you will see a confirmation message, a new button called **View** will appear and the app will be live
- Click on **View** to open your live website

    <details>
    <summary><strong>Deployment Success</strong></summary>

    ![Successful Deployment](./readme-files/images/deployment-success.png)
    </details>

[Back to Top](#top)

# Credits

## Content

- **Django 5 By Example**:
    Recommended by my [mentor](https://5pence.net/), this book by Antonio Melé was instrumental in boosting my understanding of Django.

- **Code Institute Walkthrough Project**:  
    Portions of code were reused from Code Institute’s walkthrough project, *"I think therefore I blog."* This served as a foundational resource for my blog functionality.

- **Walking the Wainwrights**:
    My cohort facilitator introduced me to Martin Bradbury's [Walking the Wainwrights](https://github.com/MartinBradbury/walking-the-wainwrights), which provided creative inspiration.

- **Images**:
    All images regarding the blog are original and were taken by myself.

- **README**:
    My README structure was inspired by my [previous project](https://github.com/yanidruffy/stratagem-hero) and insights from my colleague [Sebastian](https://github.com/Mienjung97/PROject-GOLFblog/blob/main/README.md).

## Development Tools

- **Bootstrap**:
    I used [Bootstrap](https://getbootstrap.com/) for styling and responsiveness, particularly benefiting from its grid system and components.

- **Black**:
    Code formatter [Black](https://pypi.org/project/black/) was used for the python files to ensure code consistency.

- **Beautify**:
    I used [Beautify](https://beautifier.io/) for formatting my HTML, CSS, and JavaScript code.

- **Perplexity**:
    Assisted in generating text for blog posts using [Perplexity](https://www.perplexity.ai/).

## References

- **Balsamiq**:
    Wireframes for the project were designed using [Balsamiq](https://balsamiq.com/wireframes/).

- **Coolors**:
    The color scheme was created using [Coolors](https://coolors.co/).

- **ImageResizer**:
    Image optimization and resizing were handled using [ImageResizer](https://imageresizer.com/).

- **Heroku**:
    The project was successfully deployed on [Heroku](https://www.heroku.com/).

- **Notion**:
    I organized my project through [Notion](https://www.notion.so/).

## Acknowledgements

- A big thank you to my [mentor](https://5pence.net/) and my friends and colleagues for reviewing the project and providing invaluable feedback that greatly improved both the design and functionality.
- Special thanks to Roo from the Code Institute's Support Team for his guidance.
- I also want to express my gratitude to my partner, who accompanied me on this adventure. Your support has been invaluable.

[Back to Top](#top)