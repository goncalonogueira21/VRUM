var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/register', function(req, res, next){
  console.log('POST /register')
});
router.post('/login', function(req, res, next){
  console.log('POST /login')
});


module.exports = router;
