<template>
    <div class = "container-login">
        <h2> Login </h2>
            <LoginForm/>
    </div>
</template>
<script>
import LoginForm from "../components/LoginForm.vue";
export default{
    name:"LoginView",
    components:{ LoginForm}
}
</script>
<style>
</style>