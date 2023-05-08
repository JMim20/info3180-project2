<template>
  <header>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" id="header" href="/"><i class="fa fa-camera" style="font-size:36px; text-shadow: 0 0 3px #000;color:#D3D3D3"></i>  Photogram</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto" id="right">
            <li class="nav-item">
              <RouterLink to="/"  class="nav-link active">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/explore">Explore</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/users/{user_id}">My Profile</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/logout">Logout</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink } from "vue-router";
</script>

<style>
  #header{
    font-family:Brush Script MT, Brush Script Std, cursive;
    font-size: 40px;
  }

  #right{
    position: absolute;
    right: 10px;
    font-size: 15px;
    font-family: Arial Black;

  }
</style>