<template>
    <div v-on:click="goToHome" class="home-header">
      <a href="#">Homework Hero</a>
    </div>
</template>

<script>
export default {
  name: 'HomeHeader',
  methods: {
    goToHome() {
      this.$router.push("/");
    },
  },
}
</script>

<style scoped>
  .home-header {
    font-family: 'Press Start 2P', cursive;
    font-size: 1em;
    color: rgb(225, 225, 225);
    text-shadow: 1px 1px rgb(24, 24, 24);
    cursor: pointer;
    transition: 0.1s;
  }

  .home-header:hover {
    transform: scale(1.05);  
  }

  a:link {
    text-decoration: inherit;
    color: inherit;
  }

  a:visited {
    text-decoration: inherit;
    color: inherit;
  }

</style>