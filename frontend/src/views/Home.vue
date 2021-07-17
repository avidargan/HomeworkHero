<template>
  <div class="home">
    <div class="logo-container">
      Homework<br>Hero
    </div>
    <button v-on:click="goToStudentLogin" class="pixel-button">
      I'm a Student!
    </button>
    <button v-on:click="goToTeacher" class="pixel-button">
      I'm a Teacher!
    </button>
    <div class="tts-controls">
      <div v-on:click="toggleTTS" class="tts-checkbox">
          <img v-if="tts_enabled" class="checkbox-img" src="../../src/assets/checkbox-on.png">
          <img v-else class="checkbox-img" src="../../src/assets/checkbox-off.png">
      </div>
      Text-to-Speech
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  components: {
  },
  data() {
    return {
      tts_enabled: true,
    };
  },
  methods: {
    toggleTTS() {
      if (this.tts_enabled) {
        this.tts_enabled = false;
      } else {
        this.tts_enabled = true;
      }
    },
    goToTeacher() {
      this.$router.push('teacher')
    },
    goToStudentLogin() {
      this.$router.push('studentlogin')
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
    z-index: 10;
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

  .tts-controls {
    display: flex;
    font-family: 'Press Start 2P', cursive;
    font-size: 12px;
    align-items: center;
    justify-content: center;
    color: rgb(225, 225, 225);
    text-shadow: 1px 1px rgba(0, 0, 0, 0.653);
    position: absolute;
    top: 16px;
    right: 16px;
  }

  .tts-checkbox {
    padding: 0px 8px 0px 0px;
    height: 16px;
    width: 16px;
  }

  .checkbox-img {
    width: 100%;
    height: 100%;
    image-rendering: pixelated;
  }

  .character {
    height: 300px;
    position: absolute;
    right: 0px;
    margin-right: 400px;
    bottom: 108px;
    z-index: 1;
  }

</style>
