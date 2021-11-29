var express = require('express');
var router = express.Router();

const User = require('../controllers/user')

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

router.post('/register', function(req, res, next){
  console.log('POST /register')
  var user = {
    username: req.body.username,
    password: req.body.password,
    email: req.body.email
  }
  User.findByUserName(user.username)
    .then( d => {
      res.status(403)
      res.send('Error Username já existe')
    })
    .catch( err => {
      User.findByUserEmail(user.email)
        .then( dat => {
          res.status(403)
          res.send('Error Email já existe')
        })
        .catch( erro => {
          User.inserir(user)
            .then(dados => {
              res.status(200)
              res.send('User Created!')
            })
            .catch(e => res.render('error', {
              error: e
            }))
        })
    })
  
});
router.post('/login', function(req, res, next){
  console.log('POST /login')
  res.send('respond with a resource');
});
module.exports = router;
