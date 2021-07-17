<template>
  <div class="home">
    <div v-if='step' class="home">
      <div class="logo-container">
        Select Topics
      </div>
      <div v-on:click='toggleAdd'>
        <button :class ="add_enabled ? 'pixel-button-enabled' : 'pixel-button'">
          Addition
        </button>
      </div>
      <div v-on:click='toggleSub'>
        <button :class ="sub_enabled ? 'pixel-button-enabled' : 'pixel-button'">
          Subtraction
        </button>
      </div>
      <div v-on:click='toggleMul'>
        <button :class ="mul_enabled ? 'pixel-button-enabled' : 'pixel-button'">
          Multiplication
        </button>
      </div>
      <div v-on:click='toggleDiv'>
        <button :class ="div_enabled ? 'pixel-button-enabled' : 'pixel-button'">
          Division
        </button>
      </div>
      <div class='continue-button'>
        <img class='continue-button-image' v-on:click="generateCode" src="../assets/green-arrow-right.png"/>
      </div>
    </div>
    <div v-else class="home">
      <div class="logo-container">
        The code is 
        <h1>ABCDEF</h1>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TeacherPortal',
  components: {
  },
  data() {
    return {
      add_enabled: false,
      sub_enabled: false,
      mul_enabled: false,
      div_enabled: false,
      step: 1,
    };
  },
  methods: {
    toggleAdd() {
      this.add_enabled = !this.add_enabled;
    },
    toggleSub() {
      this.sub_enabled = !this.sub_enabled;
    },
    toggleMul() {
      this.mul_enabled = !this.mul_enabled;
    },
    toggleDiv() {
      this.div_enabled = !this.div_enabled;
    },
    generateCode () {
      this.step = 0;
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

  .continue-button {
    height: 100px;
    width: 100px;
    right: 10px;
    position: absolute;
    margin-right: 35px;
  }

  .continue-button-image {
    height: 100%;
    width: 100%;
    image-rendering: pixelated;
    -webkit-filter: drop-shadow(5px 5px 5px #222);
    filter: drop-shadow(5px 5px 5px #222);
  }

  .logo-container {
    /* background-color: blue; */
    font-family: 'Press Start 2P', cursive;
    font-size: 3em;
    color: rgb(225, 225, 225);
    text-align: center;
    margin-bottom: 64px;
    text-shadow: 2px 4px rgba(0, 0, 0, 0.653);
    margin-top: -75px;
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

  .pixel-button-enabled {
    margin: 16px 0px;
    padding: 32px;
    font-family: 'Press Start 2P', cursive;
    color: rgb(23, 23, 23);
    width: 300px;
    height: 72px;
    background-color: rgba(225, 225, 225,0);
    border: 0px;
    background-image: url(../../src/assets/blue_button_pressed.png);
    -webkit-box-shadow: 0px 5px 16px 1px rgba(0,0,0,0.72); 
    box-shadow: 0px 5px 16px 1px rgba(0,0,0,0.72);
  }

  .pixel-button:hover {
      background-image: url(../../src/assets/grey_button_pressed.png);
  }

  .checkbox-img {
    width: 100%;
    height: 100%;
    image-rendering: pixelated;
  }

</style>
