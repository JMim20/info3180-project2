<template>
    <div
        v-if="errorMessage"
        class="alert alert-danger">
        {{ errorMessage }}
    </div>

    <div
        v-if="successMessage"
        class="alert alert-success">
        {{ successMessage }}
    </div>

    <div class="logout-container">
        
        <div class="logout-box">
        
        <h1>Logging Out?</h1>
        <p>Are you sure you want to logout?</p>

        <div class="buttons">
            <a href="/"> <button @click="logout()" class="btn btn-lg btn-primary">YES</button></a>

            <a href="/explore"> <button class="btn btn-lg btn-primary ">NO</button></a>

        </div>
       

        </div>
    </div>

</template>

 <script>
  
  export default {
    name: 'Logout',
    methods: {
      logoutUser() {
        fetch('http://127.0.0.1:8080/api/v1/auth/logout', {
                method: "POST",
            })
                .then(response => {
                    localStorage.removeItem('token')
                    localStorage.removeItem('user_id')
                    setTimeout(() => {
                        console.log(localStorage.getItem('token'))
                        console.log('Timer completed!');
                        window.location.href = '/';
                    }, 1500);
                })
                .catch(error => {
                    console.log(error.response.data)
                })
      },
      lastPage() {
        this.$router.back()
      },
      
    }
  }
  </script>

<style>
.logout-container{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 350px;
    padding: 300px;

}

.logout-box{
    border: 1px solid #bbbab8;
    border-radius: 6px;
    box-shadow: 0px 4px 10px 2px #bbbab8;
    padding: 1rem;
    text-align: center;
    width: 450px;
    height: 350px;
}


h1{
    padding-top: 40px;
    padding-bottom: 30px;
}

p{
    padding: 10px;
}

.button-container{
    display: flex;
    justify-content: space-between;
    margin-top: 1rem;
}
</style>
