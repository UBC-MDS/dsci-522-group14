# Use rocker tidyverse as base to get make, base r and tidyverse
FROM rocker/tidyverse

# R dependencies for final report
RUN apt-get update -qq && apt-get -y --no-install-recommends install \
  && install2.r --error \
    --deps TRUE \
    here

# install kableExtra
RUN Rscript -e "install.packages('kableExtra')"

# install anaconda & put it in the PATH
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh 
ENV PATH /opt/conda/bin:$PATH

# install conda forge packages
RUN conda install -y -c conda-forge \
    docopt \
    requests \
    pandas \
    altair \
    matplotlib \
    numpy \
    altair_saver

RUN conda install -y -c conda-forge scikit-learn

# update to get latest sciit learn. Do before npm install to make sure altair_saver works
RUN conda update -y --all

# install npm packages for altair_saver
RUN npm install -g --unsafe-perm vega-lite vega-cli canvas
