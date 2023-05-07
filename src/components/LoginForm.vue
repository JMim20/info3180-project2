<template>
    <h5>Login </h5>
    <h5>Login </h5>
    <div class="login-container">
        <form @submit.prevent="loginUser" id="loginForm" method="post" enctype="multipart/form-data">       
            <div id="LoginForm">
                <label for="username">Username</label>
                <input id="username" name="username" type="text" placeholder="Enter username" required/>
                <label for="password">Password</label>
                <input id="password" name="password" type="password" placeholder="Enter password" required/>
                <input type="hidden" name="token" v-bind:value="csrf">
                <button type="submit" class="submit-btn" >LOGIN</button>
      
                </div>
        </form>
    </div>
</template>

<script set>
    import { ref, onMounted} from "vue";
    let csrf = ref("");

    function getCsrfToken() {
        fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then(function(data) {
            csrf = JSON.stringify(data);
            console.log(csrf);

        });
        return csrf;
    }
        export default {
            data() {
                return {
                    username:'',
                    password:'',
                    csrf:''
                    

                };
            },
       
        methods : { 
             loginUser(){
                let loginForm = document.getElementById('loginForm');
                let form_data = new FormData(loginForm);
                let token =getCsrfToken();
                var token_ =JSON.parse(token);
                let mytoken=token_["csrf_token"]
                console.log(mytoken);
                
                fetch("/api/v1/auth/login", {
                     method: 'POST',
                     body: form_data,
                     headers: {'X-CSRFToken': mytoken}
             })
                     
                .then((response) => {
                    if (!response.ok) {
                        throw new Error("HTTP status " + response.status);
                }  else{
                    this.$router.push({ path: '/explore' })
                }
                })
                .catch((error) =>{
                    console.log(error);
                })
             }
    },

             mounted() {
                getCsrfToken();
            },
        }
    
   
    
</script>
<style>
h5{
  margin-top:10%;
   margin-left:35%;
   font-weight:bold;
    
}
    .login-container{
        width: 25%;
        margin: 2em auto 0 auto;
        background: #fff;
        border-radius: 5px;
        border: 1px solid black;
    }
    #LoginForm{
        display: flex;
        flex-direction: column;
        gap: 0.5em;
        width: 85%;
        margin: 0 auto;
        padding-top: 2em;
    }
    label{
        font-weight: bold;
    }
    .submit-btn{
        border: none;
        border-radius: 5px;
        height: 2.5em;
        background: rgb(92, 221, 122);
        margin-bottom: 2em;
        font-weight: bold;
        color: #fff;
        padding-top:2%;
        padding-bottom:10%;

}
     .submit-btn:active,
     .submit-btn:focus,
     .submit-btn:hover {
	border-color: #6A679E;
	outline: none;
    color: blue;
}
</style>