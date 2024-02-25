# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
COPY ./wrappers /code/wrappers

# 
COPY ./models /code/models

# 
CMD ["uvicorn", "app.main:app"]