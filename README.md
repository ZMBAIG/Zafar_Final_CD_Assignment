# Zafar_Final_CD_Assignment
This is a CI/CD pipeline python project with the help of Github actions. These enable to create a custom workflows which can be used to automate software development cycle with wide range of tools and services, which are widely shared by Github community. 
Building and testing a series of code requires a server. For this purpose I have a cloud server that is made to deploy a flask app to the Digital Ocean.
The main goal of this assignment is to create a simple flask python project, using Github action, SSH and Digital Ocean server.
1. Github Actions: After pushing code to repository in Github, the CI/CD process starts to test and deploy our code in the specified repo. This leads to perform a number of Github actions with different tasks. It checks out code and runs the test that originates a work flow. 
2. SSH: A deploy key is an SSH key that gives permission to access a repository with remote server. This process is performed with Github Secrets e.g. ${{secrets.SSH_PRIVATE_KEY}}. These protect credentials of our project in the Github community. I preferred to create a ssh-key on VPS server rather than on a local machine. 
3. Digital Ocean VPS: Having an account with Digital Ocean, a cloud base server “Droplet” with an authenticated password was created. This is a Linux-based virtual machine (Ubuntu) where my all project activities are performed to install and upgrade with “apt packages”.<br>
**PROBLEMS**:
I confronted a lack of insufficient literature about deployment with Digital Ocean. I experienced with actions like “appleboy/ssh-action@v0.1.2 and shimataro/ssh-key-action@v2”.  Finally I succeeded to deploy with appleboy.<br>
The connection with VPS with SSH key also made me annoy to generate and store private key. That makes error in regard with copy and paste mistakes.<br>
I have attempted more than 50 commits in the project “Repository” to deploy my app to VPS. But every time I learned a new thing.
