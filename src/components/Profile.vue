<template>
    <div class="container">
        <div v-for="user in users_" :key='user.id' class="profile">
            <div v-if="user_id == user.id" class="profile-image">
                <img v-bind:src="`../app/Uploads/{{user.profile_photo}}`" alt="">
             </div>
             <div class="profile-user-settings">
                <h1 class="profile-user-name">{{user.username}}</h1>
                <button class="follow-btn">Follow</button>
            </div>
            <div class="stats">
                <ul>
                    <li v-for="post in posts" :key="post.id"><span class="profile-stat-count">164</span> posts</li>
                    <li v-for="follow in follows" :key="follow.id"><span class="profile-stat-count">188</span> followers</li>
                </ul>
           </div>
            <div class="profile-bio">
                <p>{{ user.biography }}</p>
            </div>
        </div>
    </div>
    <div class="container"> 
        <div class="gallery">
            <div tabindex="1">
                 <img src="/src/assets/bio2.jpg" class="gallery-image" alt="">
            </div>
          </div>
    </div>
</template>

<script set>
     import { ref, onMounted} from "vue";
        let csrf_token = ref("");
        function getCsrfToken() {
            fetch('/api/v1/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                csrf_token.value = data.csrf_token;
            });
        }
        export default {
            data() {
                return {
                    user_id:this.$route.params.user_id,
                    username: '',
                    biography:'',
                    photo: ''
             };

                },
            created() {
                fetch('/api/profile', {
                    method: 'GET',
                    headers: {'X-CSRFToken': csrf_token.value,
                    'Content-Type': "application/json",
                    "Authorization": `Bearer ${localStorage.getItem('token')}`}
                    
                })
                .then(function (response) {
                    return response.json();
                })
                .then(function (data) {   
                    if (data.status == 200){
                        console.log("successful");
                           
                    }
                    
                })
                .catch(function (error) {
                    console.log('error');
                });
            },
            mounted() {
                getCsrfToken();
            }
        }
        
</script>

<style>

:root {
    font-size: 10px;
}

*,
*::before,
*::after {
    box-sizing: border-box;
}

body {
    font-family: "Open Sans", Arial, sans-serif;
    min-height: 100vh;
    background-color: #fafafa;
    color: #262626;
    padding-bottom: 3rem;
}

img {
    display: block;
}

.container {
    max-width: 93.5rem;
    margin: 0 auto;
    padding: 0 2rem;
}


.visually-hidden {
    position: absolute !important;
    height: 1px;
    width: 1px;
    overflow: hidden;
    clip: rect(1px, 1px, 1px, 1px);
}


.profile {
    padding: 5rem 0;
}

.profile::after {
    content: "";
    display: block;
    clear: both;
}

.profile-image {
    float: left;
    width: calc(33.333% - 1rem);
    display: flex;
    justify-content: center;
    align-items: center;
    margin-right: 3rem;
}

.profile-image img {
    border-radius: 50%;
}

.profile-user-settings,
.stats,
.profile-bio {
    float: left;
    width: calc(66.666% - 2rem);
}

.profile-user-settings {
    margin-top: 1.1rem;
}

.profile-user-name {
    display: inline-block;
    font-size: 3.2rem;
    font-weight: 300;
}

.follow-btn {
    font-size: 1.8rem;
    line-height: 1.8;
    border: 0.1rem solid #dbdbdb;
    border-radius: 0.3rem;
    padding: 0 2.4rem;
    margin-left: 2rem;
    padding: 1% 15%;
    background-color: deepskyblue;
}

.profile-settings-btn {
    font-size: 2rem;
    margin-left: 1rem;
}

.stats {
    margin-top: 2.3rem;
}

.stats li {
    display: inline-block;
    font-size: 1.6rem;
    line-height: 1.5;
    margin-right: 4rem;
    cursor: pointer;
}

.stats li:last-of-type {
    margin-right: 0;
}

.profile-bio {
    font-size: 1.6rem;
    font-weight: 400;
    line-height: 1.5;
    margin-top: 2.3rem;
}

.profile-real-name,
.profile-stat-count,
.follow-btn {
    font-weight: 600;
}

/* Gallery Section */

.gallery {
    display: flex;
    flex-wrap: wrap;
    margin: -1rem -1rem;
    padding-bottom: 3rem;
}

.gallery-item {
    position: relative;
    flex: 1 0 22rem;
    margin: 1rem;
    color: #fff;
    cursor: pointer;
}


.gallery-item-type {
    position: absolute;
    top: 1rem;
    right: 1rem;
    font-size: 2.5rem;
    text-shadow: 0.2rem 0.2rem 0.2rem rgba(0, 0, 0, 0.1);
}

.fa-clone,
.fa-comment {
    transform: rotateY(180deg);
}

.gallery-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Loader */

.loader {
    width: 5rem;
    height: 5rem;
    border: 0.6rem solid #999;
    border-bottom-color: transparent;
    border-radius: 50%;
    margin: 0 auto;
    animation: loader 500ms linear infinite;
}

/* Media Query */

@media screen and (max-width: 40rem) {
    .profile {
        display: flex;
        flex-wrap: wrap;
        padding: 4rem 0;
    }

    .profile::after {
        display: none;
    }

    .profile-image,
    .profile-user-settings,
    .profile-bio,
    .stats {
        float: none;
        width: auto;
    }

    .profile-image img {
        width: 7.7rem;
    }

    .profile-user-settings {
        flex-basis: calc(100% - 10.7rem);
        display: flex;
        flex-wrap: wrap;
        margin-top: 1rem;
    }

    .profile-user-name {
        font-size: 2.2rem;
    }

    .follow-btn {
        order: 1;
        padding: 0;
        text-align: center;
        margin-top: 1rem;
    }

    .follow-btn {
        margin-left: 0;
    }

    .profile-bio {
        font-size: 1.4rem;
        margin-top: 1.5rem;
    }

    .follow-btn,
    .profile-bio,
    .stats {
        flex-basis: 100%;
    }

    .stats {
        order: 1;
        margin-top: 1.5rem;
    }

    .stats ul {
        display: flex;
        text-align: center;
        padding: 1.2rem 0;
        border-top: 0.1rem solid #dadada;
        border-bottom: 0.1rem solid #dadada;
    }

    .stats li {
        font-size: 1.4rem;
        flex: 1;
        margin: 0;
    }

    .profile-stat-count {
        display: block;
    }
}


@supports (display: grid) {
    .profile {
        display: grid;
        grid-template-columns: 1fr 2fr;
        grid-template-rows: repeat(3, auto);
        grid-column-gap: 3rem;
        align-items: center;
    }

    .profile-image {
        grid-row: 1 / -1;
    }

    .gallery {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(22rem, 1fr));
        grid-gap: 2rem;
    }

    .profile-image,
    .profile-user-settings,
    .stats,
    .profile-bio,
    .gallery-item,
    .gallery {
        width: auto;
        margin: 0;
    }

    @media (max-width: 40rem) {
        .profile {
            grid-template-columns: auto 1fr;
            grid-row-gap: 1.5rem;
        }

        .profile-image {
            grid-row: 1 / 2;
        }

        .profile-user-settings {
            display: grid;
            grid-template-columns: auto 1fr;
            grid-gap: 1rem;
        }

        .follow-btn,
        .stats,
        .profile-bio {
            grid-column: 1 / -1;
        }

        .profile-user-settings,
        .profile-bio,
        .stats {
            margin: 0;
        }
    }
}


</style>
