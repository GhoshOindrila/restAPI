# restAPI

Pre-requisite
1.MySQL for DB \n
2.Postman for testing POST methods 


Instructions:
1.Execute the mydatabase.sql file to create the restaurant database.
2.Open command prompt or anaconda prompt(preferable). Open the directory where you have the API.py file. Run the file with command python API.py
3.You will get the message on your prompt as - "Running on http://127.0.0.1:3000/"
4.There will be nine routes created.
5.1. To get all menu sections - http://127.0.0.1:3000/mainmenu
5.2. To get menu section by sectionid - http://127.0.0.1:3000/menuname/1001
5.3. To add new menu section - http://127.0.0.1:3000/addmenu (Here you need to use Postman to send the json request)
5.4. To edit a menu section - http://127.0.0.1:3000/editmenu (Here you need to use Postman to send the json request)
5.5. To delete a menu section - http://127.0.0.1:3000/deletemenu (Here you need to use Postman to send the json request)
6. Additionally you can do the same actions for another table the Item section which shows the items belonging to a particular menu section.
6.1. To get all item sections by section id - http://127.0.0.1:3000/itemmenu/1001
6.2. To add new item section - http://127.0.0.1:3000/additem (Here you need to use Postman to send the json request)
5.3. To edit a item section - http://127.0.0.1:3000/edititem (Here you need to use Postman to send the json request)
5.4. To delete a item section - http://127.0.0.1:3000/deleteitem (Here you need to use Postman to send the json request)
