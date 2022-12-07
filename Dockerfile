FROM jerinka/opencv:1

# Setting up working directory 
RUN mkdir /paint
WORKDIR /paint

COPY . .

CMD ["python3", "paint.py"]
