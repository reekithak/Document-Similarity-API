# API - For Documents Similarity

The Modules are implemented into a separate Repo. This Repo is part of Completely Different project and contributes to 50% of it. As Document Similarity is a major Aspect in NLP-World.

The application hasn't been deployed to any servers, considering the cost applicable,Size of SLUG (Therefore can't deploy to free services) and also since its an easy-go, anybody with some basic-flask experience can deploy it if needed.

## Run the Application in your own Device ?

### Step 1:
Install [Python 3.7](https://www.python.org/downloads/release/python-370/)  
Don't forget to add Path o Environment Varibales [Doubt?](https://www.educative.io/edpresso/how-to-add-python-to-path-variable-in-windows)

Completely Optional:
Install [Git](https://git-scm.com/downloads)

### Step 2:
Clone this Repository [Tutorial](https://www.youtube.com/watch?v=O72FWNeO-xY)

### Step 3:
From the root folder of the repository, open a commandline terminal/powershell and run the following commands:<br />


`pip install virtualenv` :- Installs Virtualenv Python Module<br />
`virtualenv ANY_NAME` :- Replace ANY_NAME with your choice of environment name<br />
`.\ANY_NAME\Scripts\activate` :- Activates the Virtual Environment we just created<br />
`pip install -r requirements.txt` :- Installs the Required Liraries , Takes time & Needs Space ("A lot")<br />


### Step 4:
Once all the Above is Completed , Lets run our Application.

simply type in `python app.py` into the console / terminal.
The application will be hosted into the local server.

There are Two Text Fields where you'll have to input / paste the texts.! 

First one is the Source Text ( Representing the base Document )
Second is the Target ( Which is our actual input )
Press Submit and wait for the results ! 


The score is in JSON format & will be disaplayed onto the Screen.

NOTE:
CORS Support is added.
OpenSource Code-Snippets are part of this project.
