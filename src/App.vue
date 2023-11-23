<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <div class="background">
    <div id="”layout”">
      <header class="wrapper">
        <div>
          <nav>
            <RouterLink to="/">Home</RouterLink>
            <RouterLink to="/about"> About</RouterLink>
          </nav>
        </div>
      </header>
    </div>
    <RouterView />
  </div>
</template>

<style scoped>
@import url("https://fonts.cdnfonts.com/css/8bit-wonder");
* {
  font-family: "8BIT WONDER", sans-serif;
}

#layout {
  font-family: Avenir, Arial, Helvetica, sans-serif;
  -webkit-font-smooting: antialiased;
  -moz-osx-font-smooting: grayscale;
  text-align: center;
  color: #2c3e50;
}
.background {
  background-color: rgb(218, 218, 218);
}
nav {
  padding: 30px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  gap: 10px;
}
nav a {
  font-weight: bold;
  color: #2c3e50;
}
nav a.router-link-exact-active {
  color: #ff6363;
}
</style>
