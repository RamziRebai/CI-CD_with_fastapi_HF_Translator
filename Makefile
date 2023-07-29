install:
		pip install --upgrade pip &&\
			pip install -r requirements.txt
test:
		python -m pytest -vv -cov=tests tests.py 
lint:
		pylint --disable=R,C app/main.py
format:
		black *.py
run:	
		python app/main.py
run-uvicorn:
		uvicorn app.main:app --reload
killweb:
		sudo killall uvicorn
all:	
		install lint pytest run-uvicorn

