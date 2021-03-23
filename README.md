# nginx-setting
배포를 위한 nginx 도커 파일 및 셋팅 파일입니다    

배포를 위해서는 다음과 같은 형태가 되어야 합니다.    
```
📦배포하려는 앱    
 ┣ 📂flask서버    
 ┃ ┣ 📜app.py    
 ┃ ┣ 📜wsgi.py   
 ┃ ┣ 📜config.py   
 ┃ ┣ 📜requirements.txt   
 ┃ ┗ 📜Dockerfile    
 ┣ 📂nginx   
 ┃ ┣ 📜nginx.conf   
 ┃ ┣ 📜project.conf   
 ┃ ┗ 📜Dockerfile     
 ┗ 📜docker-compose.yml
 ```
