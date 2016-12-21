FROM continuumio/anaconda
ADD ./environment.yml /environment.yml
RUN conda env create -f /environment.yml