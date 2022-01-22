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
      <strong><em><p>22 - 01 - 2022</p></em></strong>
      <p>So finally we have completed the Django tutorial document from the official django website. Did some final touch-ups in the django admin site. added some cool advanced features but the catch being they were all pre-built. so all i had to do was just load them in the code. Django admin site and its features are too OP that i feel like its much of a pain in the ass to hassle around tweaking it or implementing it for a small project. But if properly understood it can really take away that pain in jiffy.</p>
      <p>Truth be told, I had previous experience in building 3 Flask Webapps back in 2020, so i thought i would be able to churn out webapps day in and day out after learning django. But it turns out that django is so much more deep than flask. So completing a single basic tutorial wont be enough. I am going to have start building small webapps with django, nothing fancy, in order to get some practical grip on it. Like for example in the tutorial they did so much ready-made stuff with the auto-generated django-admin site and it was confusing AF. And i realised that i have only scratched the skin.</p>
      <p>And right now i am thinking of doing some practical shit with django other than this tuorial, which alone is not enough. Like building a project with django would be a great start. And for practical hands-on project there is no other better alternative than Traversy media. I learned flask framework from their YT videos. So i have faith that they might be able to help me bridge this gap from django tutorial-hell to django practical-builds. So as a closing note to this tutorial-repository, i might continue learning django but may not document it here as this tutorial is over now. If i am going to make another repo for continued learning i will that repo link here in the future. so wait for it.</p>
    </li>
    <br>
    <li>
      <strong><em><p>11 - 01 - 2022</p></em></strong>
      <p>So finally we are inching closer and closer towards the end of this Django tutorial. Today we saw how to add static files (images, audio, CSS, JS etc) on to your webapp. So basically we can say that the back-end functionality of the webapp is almost over. Now the all that is left is your creativity on the front-end. Django can't do anything about it. I am thinking of building a small website to get a feel of the django webdev path after the tutorial. Right now all thats coming to my mind is a simple website for Forza Horizon game share-codes. Well we will see how it pans out.</p>
    </li>
    <br>
    <li>
      <strong><em><p>11 - 01 - 2022</p></em></strong>
      <p>Today was boring. Entered the unglamorous but highly useful world of testing. From the very little "testing" i experienced in this tutorial, i can clearly say that testing is in another world of its own. Other than being written in python, "test code" had a very different style of code compared to what was being written so far for the webapp. It almost feels like we can completely skip the entire "testing" section and we would be able to live with that (barely). But right now my priorities are to learn django and grasp all the CRUD functionalities that can be implemented using django and built very small webapps. So i am sorry to say that i have ran through this testing section and will surely comeback to this section in future when the need comes.</p>
    </li>
    <br>
    <li>
      <strong><em><p>02 - 01 - 2022</p></em></strong>
      <p><span><em>Happy New Year.</em></span></p>
      <p>So far we wrote the backend code for the site. Now we will focus on the front-end part. It wont be a fancy front-end but instead will be a <span><em>"get things done with minimal code"</em></span> front-end.</p><p>In this section we focussed on improving the 'details' and 'results' page of the voting app. Also we built the voting system, so from now on users can vote and the vote counter will actually get updated in the database.</p>
    </li>
    <br>
    <li>
      <strong><em><p>28 - 12 - 2021</p></em></strong>
      <p>The views can be hardcoded in the views.py file which is a bad practice. So we use templates for that. Templates are basically ready made files with gaps or blanks. These blanks are filled by django with required data provided in the backend. Thus we dont need to manually hardcode each view, instead can reuse whenever possible.</p>
      <br>
      <p>HttpResponse is the function that is used to render the final thing, that is we provid context data, complate path to the template file and the request data. Together HttpResponse function will create the necessary HTTP object which is then send to the browser of the user. For error handling, similar to HttpResponse there is another function called Http404. This function is used or called when the context data or the requested content doesn't exist</p>
    </li>
    <br>
    <li>
      <strong><em><p>10 - 12 - 2021</p></em></strong>
      <p>This section was more of code focussed than theory. so less to write here. So basically a View has 2 duties - <span><ul><p>Return content in HttpResponse if content found</p><p>return exception in Http404 if content not found or likewise errors.</p></ul></span>This HttpResponse is kind of like a dress/package/wrapper that Django can recognise. So all we have to do is wrap our required content(image or video or audio or file etc) in this wrapper send it to Django.</p>
    </li>
    <br>
    <li>
      <strong><em><p>26 - 11 - 2021</p></em></strong>
      <p>Started Part 3 of the tutorial. I hope i dont get stuck in this tutorial hell. So basically today was mainly focused on Views. Views basically means what the data the public gets to see when on different urls. For eg, On index page page the view is homepage data, on Detail Entry page the view is a form for data entry. In Detail page the view is text data about the details of the object. So in general we can say, Views are priovides data and structure of the page that is given sent the front-end to be shown to public.</p>
      <p>Next up Templates.</p>
    </li>
    <br>
    <li>
      <strong><em><p>11 - 11 - 2021</p></em></strong>
      <p>It feels good to be back after such a long time. And ohh by the way the reason for such a long absence was that I got selected for a job at Tata Consultancy Services and the past month was hectic with all the documents and background checks and mandatory courses to be completed before "starting to work". I was so busy that I forgot about this django thing. Now that I am a bit relieved from all that chaos, I can continue learning django. Well to be frank this is hard to come one month later and then look at the codebase and dont know what shit is on screen. So today was mostly me catching up on the django code of the past to understand what scrambled egg omelette had I made. Once that was done, there wasn't much to do in the 2nd section of the tutorial. Just familiarised with the built-in API provided by django to access the database and then towards the end, the creation of the admin site and all the mumbo jumbo related to that.</p>
      <p>So that was it. There was no hardcore code section just some theory and dabbling with the database using the interactive python shell and familiarisation of the django admin site and its working and its purpose and how we can register our Polls app with the admin site. Kids stuff.</p>
    </li>
    <br>
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
