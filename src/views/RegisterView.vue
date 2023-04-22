<template>
    <div class = "container-register">
        <h2> Register </h2>
            <RegsterForm/>
    </div>
</template>
<script>
import RegisterForm from "../components/RegisterForm.vue";
export default{
    name:"RegisterView",
    components:{ RegisterForm}
}
</script>
<style>
</style>