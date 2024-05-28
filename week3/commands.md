*** WEEK3 OCHESTRATION

* to start MAGE: sh ./scripts/start.sh

debuging links: 
    * https://stackoverflow.com/questions/51451095/git-warning-unable-to-access-home-user-gitconfig-is-a-directory

Stop all the containers
docker stop $(docker ps -a -q)

Remove all the containers
docker rm $(docker ps -a -q)