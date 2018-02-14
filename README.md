

## CI
The CI system the only thing it does right now is to create a docker container 
and push it to the registry. Then it notifies other project(stakeholders of these
 tests) that a new version of the tests has been released for them to consume.

## The way in which ```gitlab-runner``` was started in ```spinoza```(CI server for this project)

```
sudo gitlab-runner register -n \
  --url http://192.168.14.50/ \
  --registration-token zbcEtKMxWthudB4vxHDS \
  --executor docker \
  --description "entel_ws_soap_docker_elf" \
  --docker-image "docker:latest" \
  --docker-volumes /var/run/docker.sock:/var/run/docker.sock
```
