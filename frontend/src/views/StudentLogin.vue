<template>
  <div class="home">
    <home-header></home-header>
    <div class="code-menu">
      <div class="code-header">Student Login</div>
      <div class="code-input">
        <input
        class="code-text"
        type="email"
        placeholder="email address">
      </div>
    <div class="code-input">
        <input
        class="code-text"
        type="password"
        placeholder="password">
      </div>

      <div class="code-desc">
        <p>I forgot my password!</p>
      </div>
      <button v-on:click="goToStudentCode" class="pixel-button">
        Login!
      </button>
    </div>
  </div>
</template>

<script>
import HomeHeader from "../components/HomeHeader.vue";

export default {
  name: 'StudentLogin',
  components: {
    HomeHeader,
  },
  data() {  
    return {
    };
  },
  methods: {
    goToStudentCode() {
      this.$router.push('studentcode')
    },
  },
}
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

  .home {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-image: url(../../src/assets/background.svg);
    background-size: 1920px 1080px;
    background-repeat: repeat-y;
    background-position: left;
  }
  
  .home-header {
    position: absolute;
    top: 16px;
    left: 16px;
  }

  .logo-container {
    /* background-color: blue; */
    width: 450px;
    font-family: 'Press Start 2P', cursive;
    font-size: 3em;
    color: rgb(225, 225, 225);
    text-align: center;
    margin-bottom: 64px;
    text-shadow: 2px 4px rgba(0, 0, 0, 0.653);
  }

  .pixel-button {
    margin: 16px 0px;
    padding: 32px;
    font-family: 'Press Start 2P', cursive;
    color: rgb(23, 23, 23);
    width: 300px;
    height: 72px;
    background-color: rgba(225, 225, 225,0);
    border: 0px;
    background-image: url(../../src/assets/grey_button.png);
    -webkit-box-shadow: 0px 5px 16px 1px rgba(0,0,0,0.72); 
    box-shadow: 0px 5px 16px 1px rgba(0,0,0,0.72);
  }

  .pixel-button:hover {
      background-image: url(../../src/assets/blue_button.png);
      transform: scale(1.1);
  }

  .pixel-button:active {
      background-image: url(../../src/assets/blue_button_pressed.png);
      transform: translateY(3px);
      transform: scale(1.05);
  }

  .checkbox-img {
    width: 100%;
    height: 100%;
    image-rendering: pixelated;
  }

  .code-menu {
    /* background-color: red; */
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .code-header {
    font-family: 'Press Start 2P', cursive;
    font-size: 1.5em;
    color: rgb(225, 225, 225);
    text-shadow: 1px 2px rgba(0, 0, 0, 0.653);
    margin-bottom: 32px;
  }

  .code-text {
    width: 400px;
    height: 50px;
    padding: 0px;
    margin: 0px;
    text-align: center;
    font-family: 'Press Start 2P', cursive;
    font-size: 1.5em;
    border: 0px;
    margin-bottom: 32px;
    color: rgb(23, 23, 23);
  }

  .code-desc {
    font-family: 'Press Start 2P', cursive;
    font-size: 0.8em;
    max-width: 300px;
    text-align: center;
    color: rgb(225, 225, 225);
    text-shadow: 1px 2px rgba(0, 0, 0, 0.653);
    margin-bottom: 32px;
    cursor: pointer;
  }

</style>
