# Bloglife

Simple blogging platform project I made using Django and Javascript.

### Live Demo On
https://blogllife.herokuapp.com/

### App Features and Functionality

-   Unregister/anonymous users can view all posts and comments
-   Tagging, Comment and blog post Moderation
-   Users can write comments to any particular post.
-   Home page is paginated to return few list of blog posts.
-   Admin can moderate posts and comments
-   Admin can login through the admin panel, add more post update any post or comment

### How to run
Open terminal and use git clone command to download the remote Github repository to your computer
```bash
  1. git clone https://github.com/Jibril14/Bloglife.git
  2. cd book_store
  3. python3 -m venv venv
  4. venv/bin/activate
  5. pip3 install -r requirements.txt
  6. Generate a new secret key
  7. python manage.py makemigrations
  8. python manage.py migrate
  9. python manage.py createsuperuser
  10. python manage.py runserver
```

### Live Demo
This application is deployed on heroku. Visit the link to view
https://blogllife.herokuapp.com/
