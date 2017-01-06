# Test
Vue app generated with vue cli and routes. 

Deployed in two sites: 
https://antonelepfl.gitlab.io/bpo/
https://bluepyopt.firebaseapp.com/bpo

# To build for GitLab: 
```
$ npm run build 
```
* Commit changes and update the mirror repository (https://github.com/antonelepfl/testghpages)
* Go to GitLab project.
* Click on Commits 
* Update (from mirror repository) 
* Run pipeline form Master

# To build for Firebase 
```
$ npm run firebase 
```
* Login in firebase with (firebase-cli installed)
```
$ sudo npm install -g firebase-cli 
$ firebase login:cl 
```
* Deploy with 
```
$ firebase deploy
```