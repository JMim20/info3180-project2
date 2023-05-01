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
        newpost(){

            let postForm = document.getElementById('postForm');
            let form_data = new FormData(postForm);

            fetch("/api/v1/users/{user_id}/posts", {
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


<template>
    <h1>New Post</h1>
    <form @submit.prevent="newpost" id="postForm" method="POST">
        <div class="postb">
            <label class="photo">Photo</label><br>
            <input type="file" class="file">
            <br><br>
            <label>Caption</label><br>
            <textarea  placeholder="Write a caption..."></textarea>
            <br>
            <input type="submit" class="submit">
        </div>
    </form>
</template>

<style>
    .postb{
        border: 1px solid black;
        background-color:whitesmoke;
        position: absolute;
        width: 30%;
        height: 45%;
        top: 30%;
        right: 23%;
        overflow:visible;
        border-radius: 8px;
        box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
        padding-left: 1.5%;
        padding-top: 3%;
        margin:0% 12em ;
        
        
    }

    h1{
        font-family: 'Times New Roman', Times, serif;
        position: absolute;
        top:25%;
        right:55%;

    }

    label{
        font-family:Arial Black;
        font-size: 20px;
        margin-left: 40px;
       
    }
    .file{
        margin-left: 40px;
    }

    textarea{
        width: 85%;
        height: 100px;
        padding: 12px 20px;
        box-sizing: border-box;
        border: 2px solid #ccc;
        border-radius: 4px;
        background-color: #f8f8f8;
        font-size: 16px;
        margin-left: 40px;
        resize: none;

    }

    .submit{
        border: none;
        color: white;
        padding: 15px 38%;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 40px;
        cursor: pointer;
        border-radius: 1px;
        background-color:lawngreen;
    }

</style>


