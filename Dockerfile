FROM python
# using python image from docker hub
WORKDIR /sunilcode
# creating and changing folder in docker image
COPY automate.py /sunilcode/
CMD [ "python" , "automate.py" ]
# run the python code while creating container