const express = require('express');
const app = express();
const path = require('path');

app.use(express.static('public'));

app.get('/',function(req,res){
  res.sendFile(path.resolve(__dirname,'views','index.html'))
})

app.get('*',function(req,res){
  res.redirect('/');
})

app.listen(3000, function(){
  console.log('listen on 3000')
})