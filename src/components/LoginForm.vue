<template>
    <div class="loginPage">
        <h1>Login </h1>
        <div class="login-container">
            <form @submit.prevent="loginUser" id="loginForm" method="post" enctype="multipart/form-data">       
                <div class="alert alert-danger" v-if="errorM">
                    <ul>
                        <li v-for="aError in errorM" v-bind:key="aError.id" >
                            {{ aError }}
                        </li>
                    </ul>
                </div>
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
                    required
                    />
                    </div>
                    <div>
                        <button type="submit" class="submit-btn">LOGIN</button>
                    </div>
                    
            </form>
            <!-- <p v-if="showError" id="error">Username or Password is incorrect</p> -->
        </div>
    </div>
</template>

<script setup>
    import { ref, onMounted} from "vue";
    import {useRouter} from "vue-router";
    const router = useRouter()
    let csrf_token = ref("");
    let successM = ref("");
    let errorM =ref("");

    function getCsrfToken() {
        fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            csrf_token.value = data.csrf_token;
        });
    }

    const loginUser=() => {
        let loginForm = document.getElementById('loginForm');
        let form_data = new FormData(loginForm);
    
        fetch("/api/v1/auth/login", {
            method: 'POST',
            body: form_data,
            headers: {
                'X-CSRFToken': this.csrf_token
            }
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            console.log(data);
            successM.value=data;
            localStorage.setItem("token", data.token)
            router.push({ path : '/explore' })
                        .then(() =>{
                             router.go() 
                            });
           
        })
        .catch(function (error) {
            console.log('error');
            errorM.value=data.errors;
        });
    }
    
    onMounted(() => {
        getCsrfToken();
    });
    
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
