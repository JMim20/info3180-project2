<template>
    <H5>Login </H5>
    <div class="login-container">
        <form @submit.prevent="loginUser" id="loginForm" method="post" enctype="multipart/form-data">
            <div id="LoginForm">
                <label for="username">Username</label>
                <input 
                id="username" 
                 name="username" 
                 type="text" 
                 v-model="title"
                 placeholder="Enter username"
                 required
                 />
                 
                <label for="password">Password</label>
                <input 
                 id="password"
                 name="password"
                 type="password"
                 v-model="title"
                placeholder="Enter password"
                equired
                />

                <button type="submit" class="submit-btn">LOGIN</button>
            </div>
        </form>
    </div>
</template>
<script>
 export default {
    created(){
        this.getCsrfToken();
    },
    
    data(){
        return {
            csrf_token: ''
        }
    },
    methods : {
        loginUser(){
            let loginForm = document.getElementById('loginForm');
            let form_data = new FormData(loginForm);
            fetch("/api/v1/auth/login", {
                method: 'POST',
                body: form_data,
                headers: {'X-CSRFToken': this.csrf_token}
            })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                // display a success message
                
                if (data.status == 200){
                    
                }
                
            })
            .catch(function (error) {
                console.log(error);
            });
        },
        getCsrfToken() {
            let self = this;
            fetch('/api/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                self.csrf_token = data.csrf_token;
            })
        }
    },   
}
</script>
<style>
h5{
  
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