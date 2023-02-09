  # Backend Assignment | FamPay
  
  <h3> # Problem Statement </h3>
  <p>To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.</p>
  
  <h3> Tech / Framework Used </h3>
  <ul>
  <li>Python (Django, DRF)</li>
  <li>Postgres</li>
  <li>Celery</li>
  <li>Celery Beat</li>
  <li>Redis -> Broker</li>
  </ul>
  
  <h3># APIs Details</h3>
  
  <h4>1. Get Videos API</h4>
  <p>curl request with default pagination:- </p>
  
  ```
  curl --location --request GET 'http://127.0.0.1:8000/youtube/getVideos'
  ```
  
  <p>curl request with passing page limit in query params:- </p>
  
  ```
  curl --location --request GET 'http://127.0.0.1:8000/youtube/getVideos?page_limit=15'
  ```
  
  <h4>2. Search Videos API</h4>
  <p>curl request:-</p>
  
  ```
  curl --location --request GET 'http://127.0.0.1:8000/youtube/searchVideos?query=puri food'
  ```
  
  <h4>3. Add Auth Key API</h4>
  <p>curl request:-</p>
  
  ```
  curl --location --request POST 'http://127.0.0.1:8000/youtube/addAuthKey' \
--header 'Content-Type: application/json' \
--data-raw '{
    "auth_key": "your_key"
}'
  ```
 
<h3># How to run the Project? </h3>
  <p> I have dockerize the project as mentioned in the assignment requirements. So it is simple to run the project through docker. </p>
  <h4>Steps to run</h4>
  <ol>
  <li>Clone the project</li>
  <li>Should have docker installed on the system (If not, download it from official site) </li>
  <li>Move to the root of project</li>
  <li>Run command 
  
    $ docker-compose build
    
  </li>
  
  <li>Then Run 
  
    $ docker-compose up
    
  </li>
  </ol>
  
  <p>Project will start running in docker container</p>
  
<h3># How to Test? </h3>
<p>As soon as you run the project in docker, cron job will start every 30 sec and try to fetch data from youtube. But as there is no auth key in database, it will throw error no api key found </p>
<p> So as a next step, hit the 3rd API (Add Auth Key API) with valid api key and wait for atleast 30 seconds as scheduler will run every 30 seconds. </p>
<p> Now you can test 1st and 2nd API as well </p>

<h3># Dashboard to see all the stored videos</h4>
<p> For this task I have used django admin portal, which provides all the feature liking listing of video, filtering, sorting etc.</p>
<p> To see dashboard, we have to first create superuser. Run the below command to create superuser</p>

```
$ docker-compose run app python manage.py createsuperuser
```

<p>>It will ask User, email and password. After entering all the details, hit the below url in any browser</p>

```
127.0.0.1:8000/admin/
```

<p>Login with the credentials and check the dashboard for videos</p>
  
