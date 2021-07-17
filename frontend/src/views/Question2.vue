<template>
  <div class="home">
    <home-header></home-header>
    <div class="progress">
      <div class="filled-progress"></div>
      <div class="filled-progress"></div>
      <div class="empty-progress"></div>
      <div class="empty-progress"></div>
      <div class="empty-progress"></div>
      <div class="empty-progress"></div>
      <div class="empty-progress"></div>
      <div class="empty-progress"></div>
      <div class="empty-progress"></div>
      <div class="empty-boss-progress"></div>
    </div>
    
    <transition name="slide-fade">
    <div v-if="!finished" class="question">What's 16 - 9?</div>
    </transition>

    <transition name="slide-fade">
    <div v-if="finished" class="question">YOU WIN!</div>
    </transition>

    <transition name="slide-fade">
    <div v-if="!finished" class="answers">
      <transition name="slide-fade">
      <button v-if="showA" v-on:click="rightAnswerA" class="pixel-button">
        A) 7
      </button>
      </transition>
      <button v-if="showB" v-on:click="wrongAnswerB" class="pixel-button">
        B) 8
      </button>
      <button v-if="showC" v-on:click="wrongAnswerC" class="pixel-button">
        C) 9
      </button>
      <button v-if="showD" v-on:click="wrongAnswerD" class="pixel-button">
        D) 6
      </button>
    </div>
    </transition>
    
    <transition name="slide-fade">
    <div v-if="finishedfinishing" class="answers">
      <button v-on:click="nextQuestion" class="pixel-button">
        Next Question!
      </button>
    </div>
    </transition>

    <div class="character">
      <div class="nameplate">Zoe</div>
      <div v-if="hurt" class="hurt-character-img"></div>
      <div v-else class="character-img"></div>
    </div>
    <div class="enemy">
      <div v-if="enemy_hurt" class="hurt-enemy-img"></div>
      <div v-else class="enemy-img"></div>
    </div>

    <div v-if="finished" class="star-gain">
      <img class="star-img" src="../../src/assets/star.png">
    </div>

    <div class="tts-controls">
      <div class="tts-checkbox">
        <img class="checkbox-img" src="../../src/assets/star.png">
      </div>
        {{ stars }} Stars
    </div>
  </div>
</template>

<script>
import HomeHeader from "../components/HomeHeader.vue";

export default {
  name: 'Question2',
  components: {
    HomeHeader,
  },
  data() {  
    return {
      showA: true,
      showB: true,
      showC: true,
      showD: true,
      hurt: false,
      enemy_hurt: false,
      finished: false,
      finishedfinishing: false,
      stars: 0,
      starGain: [100, 75, 50, 20],
      starIndex: 0,
    };
  },
  methods: {
    rightAnswerA() {
      this.enemy_hurt = true;
      setTimeout(() => this.finished = true, 250);
      setTimeout(() => this.stars = Number(this.stars) + Number(this.starGain[this.starIndex]), 500);
      setTimeout(() => this.finishedfinishing = true, 1000);
      setTimeout(() => this.enemy_hurt = false, 500);
    },
    wrongAnswerB() {
      this.showB = false;
      this.starIndex++;
      this.hurt = true;
      setTimeout(() => this.hurt = false, 500);
    },
    wrongAnswerC() {
      this.showC = false;
      this.starIndex++;
      this.hurt = true;
      setTimeout(() => this.hurt = false, 500);
    },
    wrongAnswerD() {
      this.showD = false;
      this.starIndex++;
      this.hurt = true;
      setTimeout(() => this.hurt = false, 500);
    },
    nextQuestion() {
      this.$router.push('q3');
      localStorage.stars = this.stars;
    }
  },
  mounted() {
    if (localStorage.stars) {
      this.stars = localStorage.stars;
    }
  }
}
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

  .home {
    width: 100%;
    height: 100%;
    background-image: url(../../src/assets/background.svg);
    background-size: 1920px 1080px;
    background-repeat: repeat-y;
    background-position: bottom;
  }

  .question {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: 'Press Start 2P', cursive;
    font-size: 1.8em;
    color: rgb(225, 225, 225);
    text-align: center;
    margin-bottom: 64px;
    text-shadow: 1px 2px rgba(0, 0, 0, 0.653);

  }
  
  .home-header {
    position: absolute;
    top: 16px;
    left: 16px;
    z-index: 100;
  }

  .answers {
    width: 100%;
    position: absolute;
    bottom: 0px;
    height: 140px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .pixel-button {
    margin: 0px 16px;
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
      /* transform: scale(1.1); */
  }

  .pixel-button:active {
      background-image: url(../../src/assets/blue_button_pressed.png);
      /* transform: translateY(3px);
      transform: scale(1.05); */
  }

  .enemy {
    height: 200px;
    width: 200px;
    position: absolute;
    bottom: 190px;
    right: 200px;
  }

  .character {
    /* background-color: red; */
    position: absolute;
    bottom: 214px;
    left: 300px;
  }

  .character-img {
    width: 200px;
    height: 260px;
    background-repeat: no-repeat;
    background-image:  url("../../src/assets/Zoe.svg");  
  }

  .hurt-character-img {
    width: 200px;
    height: 260px;
    background-repeat: no-repeat;
    background-image:  url("../../src/assets/Zoe_Hurt.svg");
    animation: hurt 0.8s both;
  }


  .enemy {
    /* background-color: red; */
    position: absolute;
    bottom: 274px;
    right: 300px;
    transition: 0.2s;
  }

  .enemy-img {
    width: 200px;
    height: 260px;
    background-repeat: no-repeat;
    background-image:  url("../../src/assets/q2_enemy.svg");
  }

  .hurt-enemy-img {
    width: 200px;
    height: 260px;
    background-repeat: no-repeat;
    background-image:  url("../../src/assets/q2_enemy_hurt.svg");
    animation: enemy-hurt 0.8s both;
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

  .progress {
    position: absolute;
    top: 25px;
    z-index: 1;
    width: 100%;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .filled-progress {
    height: 20px;
    width: 20px;
    background-color: rgb(225, 225, 225);
    border-radius: 50px;
    border: 4px solid rgb(225, 225, 225);
    margin: 0px 8px;
  }

  .empty-progress {
    height: 20px;
    width: 20px;
    background-color: rgba(225, 225, 225, 0);
    border-radius: 50px;
    border: 4px solid rgb(225, 225, 225);
    margin: 0px 8px;
  }

  .empty-boss-progress {
    height: 20px;
    width: 20px;
    background-color: rgba(225, 225, 225, 0);
    border-radius: 8px;
    border: 4px solid rgb(225, 225, 225);
    margin: 0px 8px;
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

  .star-gain {
    height: 40px;
    width: 40px;
    /* background-color: red; */
    z-index: 20;
    position: absolute;
    bottom: 474px;
    right: 380px;
    animation: flip-2-hor-top-1 0.2s cubic-bezier(0.455, 0.030, 0.515, 0.955) 10 both;  }

  .star-img {
    height: 100%;
    width: 100%;
  }

@keyframes hurt {
  12.5% {
    background-image: url(../../src/assets/Zoe_Hurt.svg), url(../../src/assets/Zoe_Hurt_Red.svg);
    background-blend-mode: multiply;
    transform: translate(15px, 15px);
  }
  25% {
    background-image: url(../../src/assets/Zoe_Hurt.svg), url(../../src/assets/Zoe_Hurt_Red.svg);
    background-blend-mode: multiply;
    transform: translate(0px, 0px);
  }
  37.5% {
    background-image: url(../../src/assets/Zoe_Hurt.svg), url(../../src/assets/Zoe_Hurt_Red.svg);
    background-blend-mode: multiply;
    transform: translate(-15px, -15px);
  }
  50% {
    background-image: url(../../src/assets/Zoe_Hurt.svg);
    transform: translate(0px, 0px);
  }
  62.5% {
    background-image: url(../../src/assets/Zoe_Hurt.svg), url(../../src/assets/Zoe_Hurt_Red.svg);
    background-blend-mode: multiply;
    transform: translate(15px, -15px);
  }
  75% {
    background-image: url(../../src/assets/Zoe_Hurt.svg);
    transform: translate(0px, 0px);
  }
  87.5% {
    background-image: url(../../src/assets/Zoe_Hurt.svg), url(../../src/assets/Zoe_Hurt_Red.svg);
    background-blend-mode: multiply;
    transform: translate(-15px, 15px);
  }
  100% {
    background-image: url(../../src/assets/Zoe.svg);
    transform: translate(0px, 0px);
  }
}

@keyframes enemy-hurt {
  12.5% {
    background-image: url(../../src/assets/q2_enemy_hurt.svg), url(../../src/assets/q2_enemy_hurt_red.svg);
    background-blend-mode: multiply;
    transform: translate(15px, 15px);
  }
  25% {
    background-image: url(../../src/assets/q2_enemy_hurt.svg);
    background-blend-mode: multiply;
    transform: translate(0px, 0px);
  }
  37.5% {
    background-image: url(../../src/assets/q2_enemy_hurt.svg), url(../../src/assets/q2_enemy_hurt_red.svg);
    background-blend-mode: multiply;
    transform: translate(-15px, -15px);
  }
  50% {
    background-image: url(../../src/assets/q2_enemy_hurt.svg);
    transform: translate(0px, 0px);
  }
  62.5% {
    background-image: url(../../src/assets/q2_enemy_hurt.svg), url(../../src/assets/q2_enemy_hurt_red.svg);
    background-blend-mode: multiply;
    transform: translate(15px, -15px);
  }
  75% {
    background-image: url(../../src/assets/q2_enemy_hurt.svg);
    transform: translate(0px, 0px);
  }
  87.5% {
    background-image: url(../../src/assets/q2_enemy_hurt.svg), url(../../src/assets/q2_enemy_hurt_red.svg);
    background-blend-mode: multiply;
    transform: translate(-15px, 15px);
  }
  100% {
    background-image: url(../../src/assets/q2_enemy.svg);
    transform: translate(0px, 0px);
  }
}

.slide-fade-leave-active {
  transition: all .5s;
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateY(100px);
  opacity: 0;
}

/* ----------------------------------------------
 * Generated by Animista on 2021-7-17 20:32:52
 * Licensed under FreeBSD License.
 * See http://animista.net/license for more info. 
 * w: http://animista.net, t: @cssanimista
 * ---------------------------------------------- */

/**
 * ----------------------------------------
 * animation flip-2-hor-top-1
 * ----------------------------------------
 */
@keyframes flip-2-hor-top-1 {
  0% {
    transform: translateY(0) rotateX(0);
    transform-origin: 50% 0%;
  }
  100% {
    transform: translateY(-400%) scale(0) rotateY(300deg);
    opacity: 0;
  }
}


</style>
