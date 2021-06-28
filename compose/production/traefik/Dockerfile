FROM alekitto/traefik-alpine
# COPY ./compose/production/traefik/traefik.yml /etc/traefik
# COPY traefik_ecs.yaml /etc/traefik/traefik.yaml
# RUN touch /etc/traefik/acme.json
# RUN chmod +x /etc/traefik/acme.json

# FROM traefik:v2.2.11
RUN mkdir -p /etc/traefik/acme \
  && touch /etc/traefik/acme/acme.json \
  && chmod 600 /etc/traefik/acme/acme.json
COPY ./compose/production/traefik/traefik.yml /etc/traefik


