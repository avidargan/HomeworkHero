<template>
  <div class="home">
    <home-header></home-header>
    <div class="code-menu">
      <div class="code-header">Enter Quiz Code</div>
      <div class="code-input">
        <input
        :value="code"
        @input="updateCode"
        class="code-text"
        type="text">
      </div>
      <div class="code-desc">
        <p>Enter the 6-digit quiz code provided to you by your teacher!</p>
      </div>
      <button class="pixel-button">
        Submit
      </button>
      <div class="character">
        <div class="nameplate">Zoe</div>
        <div class="character-img"></div>
      </div>
      <div class="tts-controls">
        <div class="tts-checkbox">
            <img class="checkbox-img" src="../../src/assets/shoppingCart.png">
        </div>
        Shop + Customise!
      </div>

    </div>
  </div>
</template>

<script>
import HomeHeader from "../components/HomeHeader.vue";

export default {
  name: 'StudentCode',
  components: {
    HomeHeader,
  },
  data() {  
    return {
      code: '',
    };
  },
  methods: {
    updateCode(event) {
      const value = event.target.value;
      if (String(value).length <=6) {
        this.code = value;
      }
      this.$forceUpdate();
    }
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
  }

  .character {
    /* background-color: red; */
    position: absolute;
    bottom: 30px;
    right: 200px;
    transition: 0.2s;
  }

  .character-img {
    width: 200px;
    height: 260px;
    /* background-image:  url("../../src/assets/Zoe_Jump.svg");   */
    background-repeat: no-repeat;
    background-image:  url("../../src/assets/Zoe.svg");  
  }

  .character:hover .character-img {
    background-image:  url("../../src/assets/Zoe_Jump.svg");
    background-repeat: no-repeat;
  }

  .character:hover {
    transform: translateY(-32px);
  }

  .nameplate {
    text-align: center;
    margin-bottom: 16px;
    font-size: 1.1em;
    padding: 8px;
    color: rgb(225, 225, 225);
    font-family: 'Press Start 2P', cursive;
    text-shadow: 1px 2px rgba(0, 0, 0, 0.653);
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
    height: 32px;
    width: 32px;
  }

  .checkbox-img {
    width: 100%;
    height: 100%;
  }

</style>
