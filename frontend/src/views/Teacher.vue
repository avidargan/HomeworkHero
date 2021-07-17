<template>
  <div class="home">
      teacher
    <!-- <div class="logo-container">
      Homework<br>Hero
    </div> -->
    <!-- <button class="pixel-button">
      I'm a Student!
    </button>
    <button class="pixel-button">
      I'm a Teacher!
    </button> -->
  </div>
</template>

<script>
export default {
  name: 'TeacherPortal',
  components: {
  },
  data() {
    return {
    };
  },
  methods: {
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

</style>
