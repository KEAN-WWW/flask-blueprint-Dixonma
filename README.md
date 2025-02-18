[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/o9D7GOOs)
# simple-flask-app
To finish this assignment, you will need to know how to make Blueprint for flask application.
1. Use `git clone` to clone your repository to local. You can refer to Announcement how to do this step.
2. Create your Blueprint script under `application/bp/homepage` folder.  
3. Declare Blueprint object, use `homepage` as the Blueprints object name and add keywords parameter `template_folder='templates'` to object.
4. In Blueprint script, create default route page with `render_template` HTML renderer to render with template `homepage.html`.
5. In Blueprint script, create `about` route page with `render_template` HTML renderer to render with template `about.html`.
6. Edit `application/app.py` to register your Blueprint to Flask app
7. This time you will need to edit 
8. push it back for the grade.




Don't forget to use `pytest --pylint` to see if local tests are passed before you do the push.
