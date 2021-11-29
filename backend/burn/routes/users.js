var express = require('express');
var router = express.Router();
var jwt = require('jsonwebtoken')

const User = require('../controllers/user')

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

router.post('/register', function(req, res, next){
  console.log('POST /register')
  console.log(req.body)
  var user = {
    username: req.body.username,
    password: req.body.password,
    email: req.body.email
  }
  User.findByUserName(user.username)
    .then( d => {
      res.status(403)
      console.log(d)
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
  var user = {
    username: req.body.username,
    password: req.body.password,
    email: req.body.email
  }
  console.log(req.body)
  User.findByUserName(user.username)
    .then(user => {
      if(user && user.password === req.body.password) {
        jwt.sign({ user: req.body }, 'secretkey', { expiresIn: '300s' }, (err, token) => {
          res.json({
            token
          });
        });
      } else {
        res.jsonp({ msg: 'Credenciais inválidas' })  
      }
    })
    .catch(err => res.jsonp(err));
});

router.get('/authenticated', verifyToken, (req, res) => {  
  jwt.verify(req.token, 'secretkey', (err, authData) => {
    if(err) {
      res.sendStatus(403);
    } else {
      res.json({
        message: 'Utilizador autenticado!',
        authData
      });
    }
  });
});


// FORMAT OF TOKEN
// Authorization: Bearer <access_token>

// Verify Token
function verifyToken(req, res, next) {
  // Check if bearer is undefined
  if(req.headers['authorization']) {
    // Set the token
    req.token = req.headers['authorization']
    // Next middleware
    next();
  } else {
    // Forbidden
    res.sendStatus(403);
  }

}


module.exports = router;

