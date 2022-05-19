![Theme: Connect May 2022](https://res.cloudinary.com/djdefbnij/image/upload/v1651743047/Hackathons/May_-_SODA_Social_Hackathon_2_Mental_Health_3_1_arzjpd.jpg)

# Team_7
A social blogging website with iteractive useful features
The team members for this project were: Daniel PR, Alissa Troiano, Andrew Curley,Oliver Cadman & Sandra Atino

![Mock-up of site]()

Deployed website can be viewed [here]().

## Project Goals
  

## UX Design

### Site Owner Goals

### User Stories
- As a user, I want to understand the purpose of the site easily.
- As a user, I want to navigate throughout the site easily and efficiently.
- As a user, I want to experience responsive design, so I can use the site on different devices.
- As a user, I want to find easy to understand content about social connections & interactivity.
- As a user, I want to enjoy simple and streamlined design that emulates the purpose of the site.
- As a user, I want to find social media links so i can easily reach out to the company for any queries.



### **Existing Features**
* **Responsive design** - the site has been developed using Bootstrap and custom CSS to ensure the site is responsive across all devices.


* **Header**
    ![Header](static/images/header.jpg)


* **Landing Page**
    ![Landing page](static/images/landing-page.jpeg)

* **Footer**
    ![Footer](static/images/footer.jpg)
    • There are the avatars of the team members and facilitator who have worked towards the development of this website, and they can be connected at their GitHub platform.
    • There a hover effect on each avatar with tooltip pop up displaying names of the team members 
    • A copyright statement with team name.
    • Social media links to follow the website.


    

### Wireframes
The wireframes for this project were developed using [Balsamiq](https://balsamiq.com/).

* **Desktop Wireframes:**
        
    Home page
    ![Home page](wireframes/Landing%20page.png) 
    Game page
    
    About page
    ![About page](wireframes/About.png)

## Design

### Structure

A simple clean design with easy to use buttons handles the navigation throughout the app.

### Colour Scheme

[shutterstock color palettes](https://www.shutterstock.com/blog/color-palettes-for-websites)
![color palette](/static/images/colorpalette.png)

### Database Schema
### Images
 * All images used are from pexels ,freepik , Canva and are free to used for educational purposes.


### Typography

 [Google Fonts](https://fonts.google.com/) was used to select the fonts.


## Technologies
### Backend functionality


### Languages
- HTML
- CSS3
- JavaScript
- Flask
- Python

### Frameworks and Libraries
- hover css for hover effects through out the site.
- animate.css

- [Am I Responsive?](http://ami.responsivedesign.is/) was used to create the mock ups.
- [Balsamiq](https://balsamiq.com/) was used to create the wireframes.
- [Bootstrap 5.1.3](https://getbootstrap.com/) was used to contribute to responsiveness and styling of the site.
- [Font Awesome](https://fontawesome.com/) was used for the icons.
- Git was used for version control ad to push code to GitHub.
- [GitHub](https://github.com/) was used to store the repository.
- [GitPod](https://www.gitpod.io/) was used as the IDE to develop the project.
- [GitHub Projects]() was used to manage the workflow of the project.
- [Google Fonts](https://fonts.google.com/) were used to select fonts for the site.
- <a href="https://developers.google.com/maps/documentation" target="_blank">Google Maps</a> (used to choose a specific location on the map)
- [MongoDB](https://www.mongodb.com/1) is the fully managed cloud database service used for the project.
- [Heroku](https://dashboard.heroku.com/) is the cloud platform to deploying the app.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) is the web framework used to provide libraries, tools and technologies for the app.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) is used for Python templating
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) is used for password hashing and authentication and autohorization.

## Testing

### [HTML Validator:](https://validator.w3.org/)
 passed


### [CSS Validator:](https://jigsaw.w3.org/css-validator/)
passed


### [JSHint:](https://jshint.com/)
no error


### [Python Syntax Checker PEP8](https://www.pythonchecker.com/)
no error

### Lighthouse: 
![Home page](static/images/lighthouse_home.png)


## Bugs

## Deployment

#### Requirements 
- Python3 
- Github account 
- MongoDB account 
- Heroku account

#### Clone the project 
To make a local clone, follow the following steps. 
1. Log in to GitHub and go to the repository. 
2. Click on the green button with the text **"Code".**
3. Click on **"Open with GitHub Desktop"** and follow the prompts in the GitHub Desktop Application or follow the instructions from **[this link](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)** to see how to clone the repository in other ways. 

#### Working with the local copy
1. Install all the requirements: Go to the workspace of your local copy. In the terminal window of your IDE type: **pip3 install -r requirements.txt**.
2. Create a database in MongoDB  
    - Signup or login to your MongoDB account.
    - Create a new Database called "mother_earth" in [MongoDB Atlas](https://www.mongodb.com/). .
    - In the "mother_earth" database create the **quiz_rewards** collection.
        ###### quiz_rewards
        ```
        {
            _id: <ObjectId>,
            name: <String>,
            lat: <Decimal>,
            lng: <Decimal>,
            score: <Integer32>,
        }
3. Create the environment variables 
    - Create a .gitignore file in the root directory of the project.
    - Add the env.py file in the .gitignore.
    - Create the file env.py. This  will contain all the environment variables.
    ```
    import os
    os.environ.setdefault("IP", "Added by developer")
    os.environ.setdefault("PORT", "Added by developer")
    os.environ.setdefault("SECRET_KEY", "Added by developer")
    os.environ.setdefault("MONGO_URI", "Added by developer")
    os.environ.setdefault("MONGO_DBNAME", "Added by developer")
    ```
4. Run the app: Open your terminal window in your IDE. Type python3 app.py and run the app.

#### Heroku Deployment  
1. Set up local workspace for Heroku 
    - In terminal window of your IDE type: ```pip3 freeze -- local > requirements.txt.``` (Heroku detects this as a Python app. The reason that they've been able to detect Python is because we have a requirements.txt file)

    - In terminal window of your IDE type: ```echo "python app.py" > Procfile``` (The file is needed for Heroku to know which file is needed as entry point.)
1. Set up Heroku: create a Heroku account, create a new app and select your region. 
2. Deployment method 'Github'
    - Click on the **Connect to GitHub** section in the deploy tab in Heroku. 
        - Search your repository to connect with it.
        - When your repository appears click on **connect** to connect your repository with the Heroku. 
    - Go to the settings app in Heroku and go to **Config Vars**. Click on **Reveal Config Vars**.
        - Enter the variables contained in your env.py file. it is about: **IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME**
3. Push the requirements.txt and Procfile to the repository. 
     ```
    $ git add requirements.txt
    $ git commit -m "Add requirements.txt"

    $ git add Procfile 
    $ git commit -m "Add Procfile"
    ```
4. Automatic deployment: Go to the deploy tab in Heroku and scroll down to **Automatic deployments**. Click on **Enable Automatic Deploys**. By **Manual deploy** click on **Deploy Branch**.

Heroku will receive the code from Github and host the app using the required packages. 
Click on **Open app** in the right corner of your Heroku account. The app wil open and the live link is available from the address bar. 


### Forking the GitHub Repository
The repository can be forked on GitHub, this creates a copy of the repository that can be viewed or amended without affecting the original repository. This can be done using the following steps:

- Login to GitHub and locate the repository as before.
- At the top right of the repository (under your avatar) locate the Fork button and click this button.
- There should now be a copy of the repository in your own GitHub account, which you can amend.

### Cloning the GitHub Repository
A clone of the repository can be made, which will create a local copy on your own computer. Changes can be made to this local copy and it will not affect the original repository. Follow these steps to clone the Sunrise Yoga repository.

- Login to GitHub and locate the repository as before.
- Click the button called "Code".
- Under HTTPS copy the link provided, in this case ().
- Go to Gitpod or whichever IDE you are using and open the Terminal.
- Change the current working directory to the location where you want the cloned directory to be made.
- Type 'git clone' followed by the url you copied in step 3.
- Press "Enter" to create the local clone.
- You can refer to the GitHub documentation for more detailed information on the above process [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

## Credits

### Content

#### Website Content
    
#### Fonts
- Fonts used are from [Google Fonts](https://fonts.google.com/)
- Icons used are from [Font Awesome](https://fontawesome.com/)

#### Code Content
- [Stack Overflow](https://stackoverflow.com/)

### Media

#### Images
* Hero image used from [Pexels](https://www.pexels.com/@rostislav/)
* some images from: [freepik](https://www.freepik.com/search?format=search&query=animatedtoilet&type=vector)
* Hackathon banner designed & modified  from[canva](https://www.canva.com/)
*  background logo images in contact ,quiz splash screen and quiz are from [Canva](https://www.canva.com)
* Images gif in the resource section are from google Commons
* Illustrations from [UnDraw](https://undraw.co/illustrations)


#### Audio


## Acknowledegments:
We thank [Code Institute](https://codeinstitute.net/se/5-day-coding-challenge/?utm_term=code%20institute&utm_campaign=CI+-+SWE+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=14660337051&hsa_grp=134087657984&hsa_ad=546251838362&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQiArt6PBhCoARIsAMF5wajobw5RmzmDSvl-nqpJtRaVQKF-Znj4iDi1CR3oW-l9rBFnjMP_T1QaAvkOEALw_wcB) for organizing this Hackathon.
* All the Team members


