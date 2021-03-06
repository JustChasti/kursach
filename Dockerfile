FROM python:3
WORKDIR /
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY / /
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]