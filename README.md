# banao-assignment 
Steps I follow to complete the Task-2

1. First I created a EC2 instance on my AWS and setup the jenkins on it.
2. Login the jeknins via 'http://localhost:8080' .
3. Go to New Item and create a pipeline.
4. Write the pipeline script in which I fetch the python code from GitHub and run it and then build the pipeline.
5. Go to jenkins ec2 server and install httpd.
6. Made a conf file for reverse proxy server to run jenkins on Port 80.
7. Restart the jenkins and httpd service.
8. Then go to Route53 service and select hosted zone in which the docker container is running.
9. Create a new Record of subdomain "jenkins.jyotioffset.ml" and paste the jenkins server's public IP.
10. Finally, when you search www.jyotioffset.ml on browser it shows hellow world page and jenkins.jyotioffset.ml shows jenkins web console.
