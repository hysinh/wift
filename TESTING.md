# Wimpleton House Booking Application
  Back to [README](https://github.com/hysinh/wift/blob/main/README.md)

## Testing Overview
## CONTENTS  

* [User Story Testing](#user-story-testing)
* [Testing](#testing)
  * [HTML Validation](#html-validation)
  * [CSS Validation](#css-validation)
  * [Javascript Validation](#javascript-validation)
  * [Python Validation](#python-validation)
  * [Google Lighthouse Audits](#google-lighthouse-audits)
  * [Unit Testing](#unit-testing)
  * [Manual Testing](#manual-testing)
  * [Bugs and Fixes](#bugs-and-fixes)
  * [Unfixed Bugs](#unfixed-bugs)

  
---   

## User Story Testing
| User Story | Pass/Fail |
| ---- | --------- |
| As a Site User, I can view information about the organisation so that I can get more information about the organisation. | Pass |
|  As a Site User, I can view membership levels and benefits so that I can quickly find out how to sign up for membership and the different levels of membership. | Pass |
|  As a Site User, I can find information on public programs such as the Fellowships and Mentorships so that I participate in educational and professional programs designed for the greater WIFT community. | Pass |
|  As a Site User, I can contact the organisation so that I can submit questions or queries to the organisation. | Pass |
|  As a Site User, I view public events so that I can attend WIFT events. | Pass |
| As a Potential Registered User, I can register for an account so that I can easily register for a user account as the first step of membership. | Pass |
| As a Registered User, I can seasily sign in or out so that I can purchase a membership or if I already purchased a member, can easily access my personal account information and the member directory. | Pass |
| As a Registered user, I can see that I am logged into the website on the navbar. | Pass |
| As a Registered user, I can easily recover my password in case I forget it so that I can recover access to my account. | Pass |
| As a Registered user, I will receive an email confirmation after registering so that I can verify that my account registration was successful. | Pass |
| As a Registered User, I can purchase a membership so that I can join the WIFT organisation. | Pass |
| As a Registered User, I can easily select the membership level that I want and easily make changes to my membership selection before checkout. | Pass |
| As a Registered user, I can view the selected membership level to be purchased and its annual cost in the basket. | Pass |
| As a Registered user, I can easily enter my payment information so that I can check out quickly and with no hassles. | Pass |
| As a Registered user, I can efeel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase. | Pass |
| As a Registered user, I can view an order confirmation after checkout so that I can verify that I have not made any mistakes in my purchase. | Pass |
| As a Registered user, I will receive an email confirmation after checkout so that I can keep the confirmation of my purchase for my records. | Pass |
| As an Active Member, I can have a personalised user profile so that I can view my membership level, records of membership purchases, and my user profile and public directory profile. | Pass |
| As an Active Member, I can easiliy update my private profile so that I keepy my personal account information up-to-date. | Pass |
| As an Active Member, I can easily update my publicly displayed profile so that I can update professional information to be displayed in the Membership Directory. | Pass |
| As an Active Member, I can easily delete my publicly displayed profile data so that I can delete the professional information to be displayed. | Pass |
| As an Active Member, I can easily see my membership level and when it was purchased and when it expires so that I can view my current membership levels and details of which memberships I had purchased before. | Pass |
| As an Active Member, I can see when my membership is going to expire so that I can easily renew my membership. | Pass |
| As a site admin, I can create and manage any booking so that I can manage the bookings for the venue | Pass |
| As a site admin, I add/update/delete members and their private and public data so that I can manage the member database | Pass |
| As a site admin, I can access the admin panel/dashboard so that I can update Membership categories, check for messages sent via the contact form, and view membership purchases. | Pass |


## Testing
### Validator Testing
This application was developed with HTML, CSS, Javascript, and Python using the Django Web Framework.
  - #### HTML Validation
    The [W3C HTML validator](https://validator.w3.org/) was used for the HTML validation. I copied the page source of the fully rendered page into the validator for testing.
    #### Public Pages
    <details >
    <summary>Home page (base.html and index.html)</summary>  

    ![Hpme page](documentation/testing/html/screenshot_html_validation_index.png)
    </details>
    <details >
    <summary>About page (about.html)</summary>  

    ![about page](documentation/testing/html/screenshot_html_validation_about.png)
    </details>
    <details>
    <summary>Events page (events.html)</summary>  

    ![events page](documentation/testing/html/screenshot_html_validation_events.png)
    </details>
    <details>
    <summary>Fellowships page (fellowships.html)</summary>  

    ![fellowships page](documentation/testing/html/screenshot_html_validation_fellowships.png)
    </details>
    <details>
    <summary>Mentoring page (mentoring.html)</summary>  

    ![mentoring page](documentation/testing/html/screenshot_html_validation_mentoring.png)
    </details>
    <details>
    <summary>Contact page (contact.html)</summary>  

    ![Contact page](documentation/testing/html/screenshot_html_validation_contact.png)
    </details>
    <details>
    <summary>Sign up page (signup.html)</summary>  

    ![Signup page](documentation/testing/html/screenshot_html_validation_signout.png)
    </details>
    <details>
    <summary>Sign In page (login.html)</summary>  

    ![signin page](documentation/testing/html/screenshot_html_validation_login.png)
    </details>
    <details>
    <summary>Log Out page (logout.html)</summary>  

    ![ogout page](documentation/testing/html/screenshot_html_validation_signout.png)
    </details>    

    #### Registered User Pages (Logged in)
    <details >
    <summary>Member Dashboard page (dashboard.html)</summary>  

    ![Member Dashboard page](documentation/testing/html/screenshot_html_validation_dashboard.png)
    </details>
    <details >
    <summary>Membership Purchases page (membership_purchases.html)</summary>  

    ![receipts page](documentation/testing/html/screenshot_html_validation_dashboard_purchase_receipts.png)
    </details>
    <details >
    <summary>Edit Account Info page (edit_private_data.html) - ERROR Detail - See error in the Unresolved Bugs Table below</summary>  

    ![edit account page](documentation/testing/html/screenshot_html_validation_dashboard_edit_profile_error.png)
    </details>
    <details>
    <summary>Sign out page (signout.html)</summary>  

    ![Signout page](documentation/testing/html/screenshot_html_validation_signout.png)
    </details>

    <details>
    <summary>Sign up page (signup.html) - ERRORS Detail - See error in Linter Error Table below</summary>  

    ![Signup page](documentation/testing/html/screenshot_html_signup.png)
    </details>
    <details>
    <summary>Sign Up page (signup.html) - ERRORS Detail 2 - See error in Linter Error Table below</summary>  

    ![Signup page](documentation/testing/html/screenshot_html_signup_errors2.png)
    </details>
    
    #### Custom Error Pages
    <details >
    <summary>404 Error Page (404.html)</summary>  

    ![404 Error page](documentation/testing/html/screenshot_html_404page.png)
    </details>
    <details >
    <summary>500 Error page (500.html)</summary>  

    ![500 page](documentation/testing/html/screenshot_html_404page.png)
    </details>
    
  - #### CSS Validation
    I used the [W3C Jigsaw](https://jigsaw.w3.org/css-validator/) for CSS validation.
    <details >
    <summary>CSS Validation</summary>  

    ![screenshot of CSS validation](documentation/testing/css/screenshot_css_validation.png)
    </details>
  - #### Javascript Validation
    I used the [Jshint Linter](https://jshint.com/) for Javascript code validation.
    <details >
    <summary>Javascript Validation</summary>  

    ![screenshot of Javascript code validation](documentation/testing/js/screenshot_javascript_validation.png)
    </details>
  - #### Python Validation
    I used the [Code Institute PEP8 Python Linter](https://pep8ci.herokuapp.com/) for code validation. Unresolved bugs are noted in the bug table.
    #### Wimpleton Project
    <details><summary>urls.py</summary>

    ![urls.py](documentation/testing/python/screenshot_python_wimpleton_urls.png)
    </details>
    <details><summary>settings.py</summary>

    ![urls.py](documentation/testing/python/screenshot_python_wimpleton_settings.png)
    </details>

    #### Booking App
    <details><summary>urls.py</summary>

    ![urls.py](documentation/testing/python/screenshot_python_booking_urls.png)
    </details>
    <details><summary>views.py</summary>

    ![views.py](documentation/testing/python/screenshot_python_booking_views.png)
    </details>
    <details><summary>models.py</summary>

    ![models.py](documentation/testing/python/screenshot_python_booking_models.png)
    </details>
    <details><summary>forms.py</summary>

    ![forms.py](documentation/testing/python/screenshot_python_booking_forms.png)
    </details>
    <details><summary>admin.py</summary>

    ![admin.py](documentation/testing/python/screenshot_python_booking_admin.png)
    </details>
    <details><summary>test_forms.py</summary>

    ![test_forms.py](documentation/testing/python/screenshot_python_booking_test_forms.png)
    </details>
    <details><summary>test_views.py</summary>

    ![test_views.py](documentation/testing/python/screenshot_python_booking_test_views.png)
    </details>

  ### Search Engine Optimization, Accessibility, Best Practices, & Performance
  - #### Google Lighthouse Audits
    Google Lighthouse was used to assess each page on it's performance, accessibility, Best Practices, and SEO. Using google fonts, font awesome as well as an Google maps embed all affected the performance of different pages as they are considered render-blocking resources. For my mobile performance assessments, the ratings were a little low due to the featured image file size. Although I used a smaller image set to 800px x 450px which affected the ratings only a little, the file size was still a bit larger than the Lighthouse standard. I decided that I didn't want to compromise the image size or quality further as it is an integral part of the website branding.
    #### Home Page
    - <details >
      <summary>mobile</summary>  

      ![Hpme page](documentation/testing/lighthouse/screenshot_lighthouse_home_mobile.png)
      </details>
    - <details >
      <summary>desktop</summary>  

      ![Hpme page](documentation/testing/lighthouse/screenshot_lighthouse_home_desktop.png)
      </details>

    #### Venue Hire Page
    Using images from Cloudinary had a big impact on Best Practices assessments as they are considered insecure requests. 
    - <details >
      <summary>mobile</summary>  

      ![Venue Hire page](documentation/testing/lighthouse/screenshot_lighthouse_venuehire_mobile.png)
      </details>
    - <details >
      <summary>mobile - details</summary>  

      ![Venue Hire page](documentation/testing/lighthouse/screenshot_lighthouse_venuehire_bestpractices_issue.png)
      </details> 
    - <details >
      <summary>desktop</summary>  

      ![Venue Hire page](documentation/testing/lighthouse/screenshot_lighthouse_venuehire_desktop.png)
      </details>

    #### About Page
    - <details>
      <summary>mobile</summary>  

      ![About page](documentation/testing/lighthouse/screenshot_lighthouse_about_mobile.png)
      </details>
    - <details>
      <summary>desktop</summary>  

      ![About page](documentation/testing/lighthouse/screenshot_lighthouse_about_desktop.png)
      </details>
    
    #### Contact Page
    Best Practices assessment was affected by the Google Maps embed that I used in the contact information section.
    - <details>
      <summary>mobile</summary>  

      ![Contact page](documentation/testing/lighthouse/screenshot_lighthouse_contact_mobile.png)
      </details>
    - <details>
      <summary>desktop</summary>  

      ![Contact page](documentation/testing/lighthouse/screenshot_lighthouse_contact_desktop.png)
      </details>
    - <details>
      <summary>Best Practices detail - Google Maps</summary>  

      ![Contact page](documentation/testing/lighthouse/screenshot_lighthouse_contact_bestpractices_issues.png)
      </details>
    #### Sign Up Page
    - <details>
      <summary>mobile</summary>  

      ![Register page](documentation/testing/lighthouse/screenshot_lighthouse_signup_mobile.png)
      </details>
    - <details>
      <summary>desktop</summary>  

      ![Register page](documentation/testing/lighthouse/screenshot_lighthouse_signout_desktop.png)
      </details>
    #### Sign in Page
    - <details>
      <summary>mobile</summary>  

      ![Login page](documentation/testing/lighthouse/screenshot_lighthouse_signin_mobile.png)
      </details>
    - <details>
      <summary>desktop</summary>  

      ![Login page](documentation/testing/lighthouse/screenshot_lighthouse_signin_desktop.png)
      </details>
    
    #### Registered User Pages (Logged in)
    #### Booking Dashboard page
    - <details>
      <summary>mobile</summary>  

      ![Booking Dashboard page](documentation/testing/lighthouse/screenshot_lighthouse_bookingdashboard_mobile.png)
      </details>
    - <details>
      <summary>desktop</summary>  

      ![Booking Dashboard page](documentation/testing/lighthouse/screenshot_lighthouse_bookingdashboard_desktop.png)
      </details>
    
    #### Request Booking page
    - <details >
      <summary>mobile</summary>  

      ![Request Booking page](documentation/testing/lighthouse/screenshot_lighthouse_requestbooking_mobile.png)
      </details>
    - <details >
      <summary>desktop</summary>  

      ![Request Booking page](documentation/testing/lighthouse/screenshot_lighthouse_requestbooking_desktop.png)
      </details>
    
    #### Edit Booking page
    - <details >
      <summary>mobile</summary>  

      ![Edit Booking page](documentation/testing/lighthouse/screenshot_lighthouse_editbooking_mobile.png)
      </details>
    - <details >
      <summary>desktop</summary>  

      ![Edit Booking page](documentation/testing/lighthouse/screenshot_lighthouse_requestbooking_desktop.png)
      </details>

    #### Sign Out Page
    - <details>
      <summary>mobile</summary>  

      ![Signout page](documentation/testing/lighthouse/screenshot_lighthouse_signout_mobile.png)
      </details>
    - <details>
      <summary>desktop</summary>  

      ![Signout page](documentation/testing/lighthouse/screenshot_lighthouse_signout_desktop.png)
      </details>
    
    #### Custom Error Pages
    - <details >
      <summary>404 Error Page - mobile</summary>  

      ![404 Error page](documentation/testing/lighthouse/screenshot_lighthouse_404error_mobile.png)
      </details>
    - <details >
      <summary>404 Error Page - desktop</summary>  

      ![404 Error page](documentation/testing/lighthouse/screenshot_lighthouse_404error_desktop.png)
      </details>
    - <details >
      <summary>500 Error page - mobile</summary>  

      ![500 page](documentation/testing/lighthouse/screenshot_lighthouse_500error_mobile.png)
      </details>
    - <details >
      <summary>500 Error page - desktop</summary>  

      ![500 page](documentation/testing/lighthouse/screenshot_lighthouse_500error_desktop.png)
      </details>
  
  
  ### Unit Testing
  I was able to successfully execute unit testing on the booking form and the email contact form. 

  #### Unit Tests Run
  - Forms: Test EmailForm .is_valid()
  - Forms: Test EmailForm if no data
  - Forms: Test BookingForm .is_valid()
  - Forms: Test BookingForm if not data

  <details><summary>Unit Testing Results</summary>
  
  ![unit testing](documentation/testing/unit_test/screenshot_unit_test.png)
  </details>


  ### Manual Testing
  Manual testing was performed on the website checking to ensure pages rendered correctly, input forms worked correctly, and a user was able to create, view, edit, and delete their bookings.

  #### Browsers
  Browser compatibility was checked on Google Chrome, Microsoft Edge, Brave, and Opera. For manual testing, the following browsers were used:
  1. Microsoft Edge
  2. Google Chrome
  3. Opera

  #### The results of testing are as follows:
  | Page | Test | Pass/Fail |
  | ---- | ---- | --------- |
  | Home page | Does the Home page load correctly? | Yes |
  | Home page (base.html) | Do all the navigation links work? | Yes |
  | | Do all the footer links work? | Yes |
  | | Is the user able to see a notification in the navbar that they are currently logged in? | Yes |
  | Venue Hire page | Does the Venue Hire page render correctly? | Yes |
  | | Do all the venues render correctly? | Yes |
  | | Does the generic booking link take you the booking form page (or Sign in page if not signed in? | Yes |
  | | Do each of the booking links at the bottom of each venue link correctly to the Booking form page and set the initial value for the venue in the form? | Yes |
  | About page | Does the About page render correctly? | Yes |
  | Contact page | Does the Contact page render correctly? | Yes |
  | | Does the Contact Email Contact form work correctly? | Yes |
  | | Does the Contact Email Contact form display error and confirmation messages appropriately? | Yes |
  | Venue Bookings page | Does the Venue Booking page correctly render the Booking Dashboard | Yes |
  | | Do approved, pending approval, and expired bookings display in the correct sections? | Yes |
  | | Does the Request a booking button work correctly? | Yes |
  | | Do the edit and delete bookings buttons work correctly? | Yes |
  | Request Booking page | Does the Request Booking page render correctly? | Yes |
  | | Does the Request Booking form work correctly and allow a user to request a booking? | Yes |
  | | Do the form error messages display correctly? | Yes |
  | | Does a successful request redirect correctly to the booking dashboard and display a success message? | Yes |
  | | Does the event date input validated and display the correct error handling? | Yes |
  | | Does the number of guests input validated and display the correct error handling? | Yes |
  | Edit Booking page | Does the Edit booking page render correctly? | Yes |
  | | Does the Edit booking page allow the user to edit a specific existing booking? | Yes |
  | | Is the input validated and display an error messages when not valid? | Yes |
  | Delete Booking button | Does the Delete booking button open a Deletion modal correctly? | Yes |
  | | Does the Delete booking button allow the user to delete a selected booking associated with that user? | Yes |
  | Register page | Does the Register user page render correctly? | Yes |
  | | Does the Register user page allow a visitor to register as a user? | Yes |
  | Sign out page | Does the Sign out page render correctly? | Yes |
  |  | Does the sign out page allow a user to sign out? | Yes |
  | 404 Error page | Does the 404 error page render correctly when visitor attempts to navigate to a page that doesn't exist? | Yes |
  | 500 Error page | Does the 500 error page render correctly when there is a server error | Yes |
  | Admin panel | Can only access the admin panel if any authorised user? | Yes |
  

  #### Bugs and Fixes
  | Bug | Page | Fix |
  | --- | ---- | --- |
  | The placeholder placed on the country field in the mode | Edit Account Info page | Updated error message to be more appropriate |
  | 500 Error message has wrong copy | 500 Error page | Updated error message to be more appropriate |
  | Parse error | styles.css | Remove errant character |
  | Family Name for font family | style.css | Add quotes around family name |
  | One undefined variable | bookings.js | Add "globals bootstrap" to top of code to remove warning |
  | Form method set to POST causing form errors on render | venue_list.html template | Change method to GET |

  
  ### Unfixed Bugs
  - Although there were some spots where I could have found a better solution, there were no bugs that I was able to find that I could not resolve unless otherwise noted.
  | The placeholder placed on the country field in the member private data model is not acceptable though it was something in the Boutique Ado walkthrough project. | Edit Account Info page | Updated error message to be more appropriate |
  
  ### Unresolved Linter Code Errors
  | Bug | Line | Unresolved Reason |
  | --- | ---- | --- |
  | There were a few places that were greater than the 79 character length max | settings.py - line 129 | Was unable to resolve as caused more errors when shortened |
  | There were a few places that were greater than the 79 character length max | views.py | Could not reduce error strings further and was unable to break up the line without causing further problems |
  | HTML errors | account/signup.html | These html errors were inside the built in Django signup form |