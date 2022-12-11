# ec2_backup

## This codebase contains a public backup to my personal website and scripts that I run regularly on my EC2 instance.

### Technologies: 
- Python
- JavaScript
- HTML
- CSS


#### a) Personal Website
The folder named flaskapp, contains a lightweight flask application thats hosts my personal website. Within the /flaskapp folder, there is a file called app.py.
The code in this file is a web application written in Python using the Flask framework. The code creates an instance of the Flask class, which is a web application framework written in Python. The code then sets up several different routes, which are URLs that the web application can handle. For each route, a function is defined that returns some HTML to be displayed on the corresponding web page. For example, the route "/" is associated with the index() function, which returns the HTML for the web application's home page. The other routes include "/Resume", which redirects to a PDF of the developer's resume, "/about", which returns the HTML for an "About Me" page, and "/Projects" and "/Contact", which return the HTML for pages with information about the developer's projects and contact information, respectively. The code also includes a catch-all route that returns a "This page does not exist" message for any URL that doesn't match one of the other routes.

