# Learning Management System



## Prerequisites

* Register for an [IBM Cloud](https://www.ibm.com/account/reg/us-en/signup?formid=urx-42793&eventid=cfc-2020?cm_mmc=OSocial_Blog-_-Audience+Developer_Developer+Conversation-_-WW_WW-_-cfc-2020-ghub-starterkit-education_ov75914&cm_mmca1=000039JL&cm_mmca2=10008917) account.
* Install [`Python 3.6`](https://www.python.org/downloads/).
* Install the [`Pipenv`](https://pypi.org/project/pipenv/) Python packaging tool.
* Install [`Node.js`](https://nodejs.org).
* Install [`Yarn`](https://classic.yarnpkg.com/en/docs/install/).
* Install [Flask](https://flask.palletsprojects.com/en/1.1.x/) .

## Instructions

## 1. Clone the repository

```bash
git clone https://github.com/zacharyselk/Interns-be-Hacking.git
cd Interns-be-Hacking
```

### Run Server

TYPE HERE

### Server

1. This tutorial uses [pipenv](https://github.com/pypa/pipenv). If you are using another python distribution or package manager, you will need to install the dependencies located in the `Pipfile`. Alternatively, using pipenv, from the root project directory, create a pipenv virtual environment.

   ```bash
   pipenv --python <path to python executable>
   ```

   Note. If python 3.6 is installed in the default location, this can be specified as:

   ```bash
   pipenv --python 3.6
   ```

2. Activate the pipenv shell:

   ```bash
   pipenv shell
   ```

3. Install the project dependencies: 

   ```bash
   pipenv install
   ```

4. To run your application locally, use:  

   ```bash 
   python manage.py start
   ```

   The `manage.py` utility offers a variety of different run commands to match your situation:

     * `start`: Starts a server in a production setting using `gunicorn`.
     * `run`: Starts a native Flask development server. This includes backend reloading upon file saves and the Werkzeug stack-trace debugger for diagnosing runtime failures in-browser.
     * `livereload`: Starts a development server using the `livereload` package. This includes backend reloading as well as dynamic frontend browser reloading. The Werkzeug stack-trace debugger will be disabled, so this is only recommended when working on frontend development.
     * `debug`: Starts a native Flask development server, but with the native reloader/tracer disabled. This leaves the debug port exposed to be attached to an IDE (such as PyCharm's `Attach to Local Process`).

   There are also a few utility commands:

     * `build`: Compiles `.py` files within the project directory into `.pyc` files.
     * `test`: Runs all unit tests inside of the project's `test` directory.

   The server is running at: `http://localhost:3000/` in your browser. 

### Frontend UI Development

1. If you have not done so already, install [`Node.js`](https://nodejs.org) and [`Yarn`](https://classic.yarnpkg.com/en/docs/install/).

2. In a new terminal, change to the `frontend` directory from the project root and install the dependencies:

   ```bash 
   cd frontend
   yarn install
   ```

3. Launch the frontend application:  
   **Compiles and hot-reloads for development**

   ```bash
   yarn serve
   ```

   **Compiles and minifies for production**

   ```bash
   yarn build
   ```

   **Lints and fixes files**

   ```bash
   yarn lint
   ```

   The frontend UI is now running at `http://localhost:8080/` in your browser. 
