FROM        debian:unstable
MAINTAINER  Paul Tagliamonte <paultag@debian.org>

RUN apt-get update && apt-get install -y \
    build-essential devscripts

COPY cb-wrapper  /usr/local/bin/

ENTRYPOINT ["/usr/local/bin/cb-wrapper"]
