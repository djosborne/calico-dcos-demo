FROM python:slim
RUN pip install flask redis
ADD frontend.py /root/frontend.py
CMD ["python", "/root/frontend.py"]
