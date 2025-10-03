# BluInsights Frontend

## Overview

BluInsights Frontend is a modern, responsive web interface for the BluInsights Tech Blog, powered by BluDive Technologies. It connects seamlessly to the backend services (User Service, Blog Service, Comment Service) and provides an interactive experience for both general users and admin users.

The frontend is built using HTML, CSS, and JavaScript with a clean, minimalistic design, responsive layout, and intuitive UI/UX patterns. It includes features such as blog browsing, post creation and management (admin-only), commenting, profile viewing, and hero carousel slides.

---

## Features

### Public User Features

* View all blog posts with excerpts and featured images.
* Search blog posts by keywords in title or content.
* Browse categories and tags (filtering placeholders for future enhancement).
* View full blog post details including comments.
* Responsive design for mobile and desktop.

### Admin Features

* Login and registration (admin accounts only).
* Create new blog posts with title, tags, content, and header image.
* Edit existing posts authored by the admin.
* Delete posts authored by the admin.
* Admin-only visibility for post management UI elements.

### UI Components

* **Header Navigation**: Home, Categories, Create Post, Profile, Login.
* **Hero Section**: Sliding carousel with three hero images and overlays.
* **Blog Feed**: Vertical card layout showing latest blog posts.
* **Sidebar**: Search bar, categories list, popular tags.
* **Post Detail View**: Full post content, image, comments, and action buttons (edit/delete) for admins.
* **Forms**: Create Post, Login, Register, Comment.
* **Profile View**: Displays logged-in admin profile and authored posts.

---

## File Structure

```
frontend/
│
├── index.html            # Main frontend page
├── admin.html            # Admin Page
├── images/               # Hero and uploaded header images
```

---

## Setup & Usage

1. **Clone the frontend repository** (or copy the files into your project folder):

```bash
git clone <repo_url>
```

2. **Place images** in the `images/` folder. Example images:

```
images/Image_1.png
images/Image_2.png
images/Image_3.png
```

These images are used in the hero carousel.

3. **Open the index.html** in a browser (no build process required for plain HTML/JS frontend):

```bash
open index.html
```

4. **Ensure backend services are running** and accessible at the configured endpoints:

   * User Service: `http://localhost:5050`
   * Blog Service: `http://localhost:5001`
   * Comment Service: `http://localhost:5002`

5. **Login as admin** to enable post creation, editing, and deletion. Public users will not see these controls.

---

## Hero Carousel

* The hero section features a sliding carousel with 3 images.
* Images are located in the `images/` folder and referenced in `index.html`.
* You can replace `Image_1.png`, `Image_2.png`, `Image_3.png` with your own hero images.
* The carousel automatically transitions every 4 seconds.

---

## Search Functionality

* The search input in the sidebar allows live filtering of blog cards.
* Users can search by keywords present in the blog title or excerpt.
* Results update in real-time without page refresh.

---

## Admin Functionality

* Admins login using credentials from the User Service.
* Admin-only UI elements include:

  * Create Post form
  * Edit Post button
  * Delete Post button
* Admin username is displayed on posts authored by them.
* Multiple admin accounts can be created via the registration form.
* Admin controls are hidden for general users.

---

## Commenting System

* Comments are displayed for each post in the Post Detail view.
* Logged-in users (admins in this implementation) can post comments.
* Comments are sent to the Comment Service endpoint and displayed immediately on submission.

---

## Notes

* Frontend is lightweight and static; no framework required.
* Can be enhanced with a bundler or framework for future scalability (React, Vue, etc.).
* Ensure all API URLs in `index.html` match the running backend ports.

---

## Future Enhancements

* Pagination and infinite scroll for blog feed.
* Filtering by category and tags.
* Admin dashboard page for post management.
* Enhanced comment moderation.
* Integration with authentication tokens for admin-only access.
* Responsive mobile menu improvements.

---

## License

This frontend is part of the BluInsights POC project by BluDive Technologies and may be used internally for demonstration and learning purposes.
