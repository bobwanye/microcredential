fetch('https://catfact.ninja/fact'),{
method: 'POST',
hearders:{
  'Content-Type':
}
body: JSON.stringify{{
  name: 'User 1'
}}
}}.then(res=>{
  return res.json()
})
.then(data => console.log(data))
.catch(error=> console.log('ERROR'))
