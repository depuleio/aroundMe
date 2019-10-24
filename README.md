aroundUB

AroundMe is an elegant website built to connect users to events around them. This website not only shows you what and were the events are going on but also allows users to create event for others to see. University at Buffalo is home to more than 30,000 students and there are cultural, social and academic events going on everyday.

Installation

(Has only been tested with Mac OS)
Requirements
## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/depuleio/aroundMe.git
```

Install the requirements:

3. Have Python 2.7

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py makemigrations 
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.
