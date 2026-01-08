# app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """Hello, World from automation using below scenarios <br><br>
This has been implemented by using my Mobile and PC. My PC has low configuration machine to implement devops so I am using my mobile which is high configurations to install Jenkins. Docker and Kubernetes can't run in mobile because docker build needs real linux kernal. So I have installed Docker and kuberenetes which ever require full linux support and these can be handled by machine with little slowness. <br><br>

In Mobile:<br><br>

1) Installed Termux(Mobile acts as linux machine with limited features).  <br>
2) Inside Termux, installed open ssh so that i can access PC from mobile. <br>
3) Installed jenkins and configured Nodes(with my PC wifi ip and linux credentials) and Pipeline  <br><br>

In PC: <br><br>

1) Since My PC is Windos, I have enabled WSL2 which acts as linux in windows. <br>
2) Installed all required tools and softwares like ssh,java,git,docker,kubernetes(docker compose) etc<br>
3) Write or pull Source code in PC built using docker then push to docker hub, finally run the docker to see outuput in local browser.<br><br>

Steps:<br>
    Write Jenkinsfile along with your source code in PC. Configure the jenkins pipeline (access jenkins in your mobile or in PC with ip)
Once the pipeline started to build, Jenkinsfiles triggered then executes the stages as per the below stages. <br><br>

Initially connects the Node(PC) <br>
|<br>
pull code from git hub in PC's configured location<br>
|<br>
Builds the code<br>
|<br>
Docker hub login and Push the docker image to docker hub<br>
|<br>
Docker run<br>
|<br>
Access the app in local broser<br><br>

This is how CI has been implemented except automatic trigger.<br><br><br>


Next steps:<br>
___________<br><br>

-> Automatic integration setup while pushing the changes to github<br>
Status:Implemented in this changeing by using Webhookrelay tool which gives a public url for localhost:8080/github-webhook/ <br><br>

-> Continuous Deploy<br>
Status: Yet to start<br><br>

===============================================================================================================================================<br><br>
Faced ssh issues in my PC so switched to PC only mode, excluding mobile setup from here onwards. Installed Jenkins in my PC and implementing now whole setup in PC <br><br>

---END----

"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
