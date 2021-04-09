FROM ubuntu:latest

EXPOSE 80
EXPOSE 8000

WORKDIR ./

COPY ./

ENTRYPOINT ["python"]
CMD ["uvicorn", "main:app"]