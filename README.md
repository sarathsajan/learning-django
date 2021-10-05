<h1>Learning Django Web Framework</h1>

<strong><em><h2>Materials</h2></em></strong>
<ul>
  <li>
    <p><a href='https://docs.djangoproject.com/en/3.2/intro/tutorial01/'>Writing your first Django app</a></p>
    <p>Django Documentation, ver 3.2<p>
    <p>Django Software Foundation<p>
    <p>Text based tutorial</p>
  </li>
</ul>

<br>

<strong><em><h2>Progress</h2></em></strong>
<div>
  <ul>
    <li>
      <strong><em><p>05 - 10 - 2021</p></em></strong>
      <p>As the tutorial progresses i can now understand why Django is so much more powerful at the same time very much rule based compared to Flask. A feature, that helps fulfil the plug-and-play philosophy of django.</p>
      <p>Yes, i am talking about database models and migrations provided in Django. With more automation comes more difficulty in customisation but for django the good side of this dilemma is that, the so called customisations are only applicable hardcore settings so in real life scenarios we wont be touching those parameters unless its really really really necessary.</p>
      <p>I had previously used Flask webframework to build a couple of web apps and in those projects, database creation was the most boring part. But in Django all you have to do is -</p>
      <ul>
        <li>provide the blueprint and the name of the database you are using by editing the <code>settings.py</code> and <code>models.py</code> file</li>
        <li>run the <code>makemigrations</code> command to generate the the overview of operations to be executed inside the databse</li>
        <li>run the <code>sqlmigrate</code> to preview the actual code that is required to be run inside the database engine in order to create the required tables and relations. This execution code will be generated for the database engine you chose. In my case SQL.</li>
        <li>Finally just run <code>python manage.py migrate</code> and voila! just like that Django has done its magic and the database is now live and ready to use.</li>
      </ul>
      <br>
      <p><em>Can't wait to accidently drop the live database in style! </em>🤟</p>
    </li>
    <br>
    <li>
      <strong><em><p>30 - 09 - 2021</p></em></strong>
      <p>today was more of theory than coding for me. Databse setup was the prime topic today. Learned how in django we don't have to specifically create tables each time instead just create the blueprints for the tables and django will take care of the rest.</p>
      <p>Django supports many database engines but by default it prefers SQLite as it doesn't require any installations but long term projects proper databse os recommended for easy scaleability. By running the <code>migrate</code> command, django will look in the the <code>INSTALLED_APPS</code> and use their corresponding blueprints to create the required tables in the database. Once we create an app that requires a table, all we have to do is create the blueprints and include the app name in the <code>INSTALLED_APPS</code> list.</p>
    </li>
    <br>
    <li>
      <strong><em><p>24 - 09 - 2021</p></em></strong>
      <p>Aptly following the tutorial, so far so good. Initialised the Polls webapp inside the django project. Made the first view and connected it by url path using the URLconf file. Now the webapp has an index page and one url path</p>
    </li>
    <br>
    <li>
      <strong><em><p>23 - 09 - 2021</p></em></strong>
      <p>Installed Django and initialised the working directory with the command <code>djgano-admin startproject mysite</code></p>
      <p>Wasted too much time by mixing up <code>virtual environment</code>, <code>git repo</code> and <code>gitignore</code> at various stages and finally destroying the repo with unwanted commits and total chaos.</p>
    </li>
    <br>
    <li>
      <strong><em><p>14 - 09 - 2021</p></em></strong>
      <p>Created the repository and a MD file to track my progress</p>
    </li>
  </ul>
</div>