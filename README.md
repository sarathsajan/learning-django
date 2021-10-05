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
      <p>as the tutorial progresses i can now understand why Django is so much more powerful at the same time very much rule based compared to Flask. That is with more automation comes more difficulty in customisation. But the good side is the so called customisations are only hardcore settings so we don't have any need to customise them unless really really necessary.</p>
      <p>Yea, i am talking about database models and migrations. I previously had used Flask to build a couple web apps and database creation was the most boring part of it. But in Django all you have to so is provide the blueprint and the name database you are using and viola! Django has created those tables and relations in few lines of codes.</p>
      <p><em>Can't wait to accidently drop live database in style! </em>🤟</p>
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