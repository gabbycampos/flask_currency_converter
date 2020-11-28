### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

Python runs on servers but not in the browser. JavaScript is a front-end language that
allows you to create dynamic webpages. 

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  
  By using the get() method or the setdefault() method.

- What is a unit test?

Unit test is to verify that a single function returns an expected value based on an argument.

- What is an integration test?

Integration test verify that multiple functions are working together properly.

- What is the role of web application framework, like Flask?

Flask help us create web servers. We follow a set of rules for how we should build an application.
Flask provides us the the tools and libraries that allow us to build a web application easier.. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  It is best to use a query param to filter a search (adding '?') and use a route param for specificity like 
  /:id

- How do you collect data from a URL placeholder parameter using Flask?

By adding less than and greater sign: <name>

- How do you collect data from the query string using Flask?

By using request.args.get()

- How do you collect data from the body of the request using Flask?

By using request.data

- What is a cookie and what kinds of things are they commonly used for?

A cookie stores data from the browser. Cookies communicate from server to browser and browser to server.

- What is the session object in Flask?

The session object stores data from cookies.

- What does Flask's `jsonify()` do?

It exports JSON files with Flask.
