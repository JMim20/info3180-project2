<template>
    <div id="error_message"></div>
    <h5> Register </h5>
    <div class= "register-container" > 
    <form @submit.prevent="registerUser" id="registerForm" method="POST" enctype="multipart/form-data">
        <div class="alert alert-danger" v-if="errorM">
            <ul>
                <li v-for="aError in errorM" v-bind:key="aError.id" >
                    {{ aError }}
                </li>
            </ul>
        </div>
        <div class="alert alert-success" v-if="successM">
            {{successM}}
        </div>
        <div class ="registerform">
            <div class="registerfield col">
                <label for="username">Username</label>
                <input
                name="username"
                type="text"
                class="submits"
                placeholder="Enter username"
                required>
            </div>
            <div class="registerfield col">
                <label for="password">Password</label>
                <input
                name="password"
                type="password"
                class="submits"
                placeholder="Enter password"
                required>
            </div>
            <div class="registerfield col">
                <label for="firstname">Firstname</label>
                <input
                name="firstname"
                type="text"
                class="submits"
                placeholder="Enter Firstname"
                required>
            </div>
            <div class="registerfield col">
                <label for="lastname">Lastname</label>
                <input
            
                name="lastname"
                type="text"
                class="submits"
                placeholder="Enter lastname"
                required>
            </div>
            <div class="registerfield col">
                <label for="email">Email</label>
                <input
            
                name="email"
                type="text"
                class="submits"
                placeholder="Enter email"
                required>
            </div>
            <div class="registerfield col">
                <label for="location">Location</label>
                <input
            
                name="location"
                type="text"
                class="submits"
                placeholder="Enter location"
                required>
            </div>
            <div class="registerfield col">
                <label for="biography">Biography</label>
                <input
            
                name="biography"
                type="text"
                class="submits"
                placeholder="Enter biography"
                required>
            </div><br>
            <div class="form-group mb-3">
                <label for="profile_photo" class="form-label">Profile Picture</label>
                <input id="file" name="profile_photo" type="file" class="submits" required>
            </div>
            <div>
                <button type="submit" class="submit-btn" > Register </button>
                <!-- onclick="window.location.href='/login'" -->
            </div>
        </div>
    </form>
    </div>
</template>

<script setup>
        import { ref, onMounted} from "vue";
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
        
        const registerUser=() =>{
            let registerForm = document.getElementById('registerForm');
            let form_data = new FormData(registerForm);

            fetch("/api/v1/register", {
                method: 'POST',
                body: form_data,
                headers: {
                    'X-CSRFToken': csrf_token.value
                }
                
            })
            .then(function (response) {
                console.log("response");
                console.log(data);
                return response.json();
            })
            .then(function (data) {   
                if("message" in data){
                    console.log(data);
                    successM.value =data.message
                }else if ("errors" in data){
                    console.log(data);
                    errorM.value=data.errors
                }
            })
            .catch(function (error) {
                console.log('error');
            });
        }
        
        onMounted(() => {
            getCsrfToken();
        });
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
