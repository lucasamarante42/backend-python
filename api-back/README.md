
#installing dependencies
sudo pip3 install -r requirements.txt

#running project
python3 manage.py runserver

#build/running with docker
docker build -t lucas/sysestoque .
docker run -d -p 7777:8000 lucas/sysestoque