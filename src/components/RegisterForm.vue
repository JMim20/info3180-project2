<template>  
    <h5> Register </h5>
    <div class= "register-container" > 
    <form @submit.prevent="registerUser" id="registerForm" method="POST" enctype="miultipart/form-data" >
    <div class ="registerform">
        <div class="registerfield col">
        <label for="username">Username</label>
        <input
        v-model="title"
        name="username"
        type="text"
        class="submits"
        placeholder="Enter username"
        required
        >
        </div>
        <div class="registerfield col">
        <label for="password">Password</label>
        <input
        v-model="title"
        name="password"
        type="text"
        class="submits"
        placeholder="Enter password"
        required
        >
    </div>
        <div class="registerfield col">
        <label for="firstname">Firstname</label>
        <input
        v-model="title"
        name="firstname"
        type="text"
        class="submits"
        placeholder="Enter Firstname"
        required
        >
    </div>
        <div class="registerfield col">
        <label for="lastname">Lastname</label>
        <input
        v-model="title"
        name="lastname"
        type="text"
        class="submits"
        placeholder="Enter lastname"
        required
        >
    </div>
        <div class="registerfield col">
        <label for="email">Email</label>
        <input
        v-model="title"
        name="email"
        type="text"
        class="submits"
        placeholder="Enter email"
        required
        >
    </div>
        <div class="registerfield col">
        <label for="location">Location</label>
        <input
        v-model="title"
        name="location"
        type="text"
        class="submits"
        placeholder="Enter location"
        required
        >
    </div>
        <div class="registerfield col">
        <label for="biography">Biography</label>
        <input
        v-model="title"
        name="biography"
        type="text"
        class="submits"
        placeholder="Enter biography"
        required
        >
    </div>
        <input id="file" name="image" type="file" @change="onSelect" class="submits">
        <button type="submit" class="submit-btn"> Register </button>
    </div>
    </form>
    </div>
    </template>
    <script>
     import { ref, onMounted } from "vue";
    onMounted(() => {
    getCsrfToken();
    });
    let csrf_token = ref("");
    export default{
        name: 'RegisterForm',
        data(){
            return{
                csrf_token: '',
                errors: [],
                success:false
            }
        },
        created(){
            this.getCsrfToken();
        },
        methods : {
            registerUser(){
                let registerForm = document.getElementById('registerForm');
                let form_data = new FormData(registerForm);
                fetch("/api/v1/register", {
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
        margin-top:3%;
   margin-left:35%;
   font-weight:bold;


}
.register-container{
        width: 25%;
        margin: 2em auto 0 auto;
        background: #fff;
        border-radius: 5px;
        border: 1px solid black;
    }
    
.registerfield{
    border: none;
	border-bottom: 2px solid #D1D1D4;
	background: none;
	padding: 10px;
	padding-left: 24px;
	font-weight: 700;
	width: 75%;
	transition: .2s;
}
.registerfield input{
    display: block;
    border: 1px solid #cccccc;
    border-radius: 6px;
    padding-left: 95px;
}
.submit-btn{
        padding-left: 35%;
        border: none;
        border-radius: 5px;
        height: 2.5em;
        background: rgb(92, 221, 122);
        margin-bottom: 2em;
        font-weight: bold;
        color: #fff;
        margin-top:5%;
        padding-top:1%;
        padding-bottom:7%;
        margin-left:7%;
        padding-right:35%;

}
     .submit-btn:active,
     .submit-btn:focus,
     .submit-btn:hover {
	border-color: #6A679E;
	outline: none;
    color: blue;
}
</style>
