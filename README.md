This Project uses Django, Django Rest Api and Scraping methods.

It contains two api  
  1) Post: the user needs to run the code using python manage.py runserver.
         - With the obtained (localhost) link add /postScrap/.
         - select body-> JSON and write
             {
               "coin": ["Name of the coin"]
             }
         - This array contains the name of the coin user want to perform scraping on.
         - After selecting the POST method, send the API.
         - It will return the job id of the recently posted request.
  2) GET: with the obtained job_id used the link + /getScrap/<int:job_id>/.
         - This will provide the information related to the recently posted request. 
