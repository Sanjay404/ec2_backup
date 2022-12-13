# ec2_backup
## This codebase contains a public backup to my personal website and scripts that I run regularly on my EC2 instance.

### Technologies: 
- Python
- JavaScript
- HTML
- CSS
- nginx
- AWS ec2
- Gunicorn


#### a) Personal Website
Within the /flaskapp folder, there is a file called app.py. The code in this file is a web application written in Python using the Flask framework. The code creates an instance of the Flask class, which is a web application framework written in Python. The code then sets up several different routes, which are URLs that the web application can handle. For each route, a function is defined that returns some HTML to be displayed on the corresponding web page. For example, the route "/" is associated with the index() function, which returns the HTML for the web application's home page. The other routes include "/Resume", which redirects to a PDF of the my resume, "/about", which returns the HTML for an "About Me" page, and "/Projects" and "/Contact", which return the HTML for pages with information about the developer's projects and contact information, respectively. The code also includes a catch-all route that returns a "This page does not exist" message for any URL that doesn't match one of the other routes.
  Beyond that, the folder called "static" contains the css, js, and images used to create my website. On the other hand, the folder names "static" contains all the html for my website.

#### b) get_classes.py AND testudo.py
This code is a Python script that is used to monitor the availability of specific sections of classes at the University of Maryland. The script uses the requests and BeautifulSoup libraries to fetch and parse the HTML of web pages on the university's course registration system, Testudo. The script also uses a custom API provided by Planetary to fetch information about the courses and professors, such as the number of credits and average GPA. The script looks for specific classes and sections, and when it finds an open seat in one of those classes, it sends a text message to the user using the Twilio API. The classes and sections to be monitored are specified in a dictionary at the bottom of the code. The script also uses a list of professors to determine whether a particular section is taught by a professor of interest to the user. When a class of interest becomes available, the script sends a text message to the user with information about the class, such as the professor, number of credits, and average GPA.


#### c) stock_recap.py
This code is a Python script that is used to monitor the stock prices of certain companies and send a text message to the user with the current prices at specified times. The code uses the requests and BeautifulSoup libraries to fetch and parse the HTML of web pages on Yahoo Finance for the specified companies. The code then uses the Twilio API to send a text message to the user with the current prices of the stocks. The code is set to send a text message in the morning and evening, with different information included in each message. The specific companies to be monitored and the phone numbers to send the messages to are specified in the code.

