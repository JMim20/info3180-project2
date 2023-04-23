<script>   
  
</script>

<template>
      <div class="bg-img"></div>
      <div class="photogram">
        <br>
        <h1 class="title"><i class="fa fa-camera" style="font-size:36px; text-shadow: 0 0 3px #000;color:#D3D3D3"></i>  Photogram</h1>
        <hr>
        <p>Share photos of your favourite moments with friends, family and the world</p>
        <br>
        <button type="submit" class="reg" onclick="window.location.href='/register'">Register</button> <button type="submit" class="login" onclick="window.location.href='/login'">Login</button>
      </div>
</template>

<style>
  .bg-img{
   background-image:url("/src/assets/homepage.jpg") ;
   background-repeat: no-repeat;
   background-position: center center;
   background-size:cover; 
   position: absolute;
   width: 30%;
   height: 45%;
   top: 30%;
   left: 15%;
   overflow:visible;
   border-radius: 5px;
   box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;;
  }
  

  .photogram {
   border: 1px solid whitesmoke;
   background-color:whitesmoke;
   position: absolute;
   width: 30%;
   height: 45%;
   top: 30%;
   right: 23%;
   overflow:visible;
   border-radius: 5px;
   box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
    
  }

  .title{
    font-family:Brush Script MT, Brush Script Std, cursive;
    color:black;
    text-align: center;
    top:0%;
  }

  hr{
    height: 2px;
    margin-left: 20px;
    margin-right: 20px;
  }

  p{
    font-family: 'Times New Roman', Times, serif;
    font-size: 20px;
    margin-left: 10px;
  }

  button{
    border: none;
    color: white;
    padding: 15px 15%;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 1px;
    

  }

  .reg{
    background-color: forestgreen;
    margin-left: 10%;
   
  }

  .login{
    background-color: dodgerblue;
  }



</style>