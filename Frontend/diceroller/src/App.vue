<template>
  <!-- https://www.w3schools.com/css/css_navbar_horizontal.asp -->
  <div class="nav">
  <ul>
    <li><a @click="changePage(1)">Home</a></li>
    <li><a @click="changePage(2)">Presets</a></li>
    <li><a @click="changePage(3)">About</a></li>
    <li style="float:right"><a @click="changePage(4)">Help</a></li>
  </ul>
  </div>
  
  <div class="content">
    <HelloWorld class="main" v-if="page==1" msg="Welcome to DiceRoller"/>
    <Preset v-if="page==2"/>
    <About v-if="page==3"/>
    <HelpTab v-if="page==4"/>
  </div>

</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import About from './components/About.vue'
import Preset from './components/Preset.vue'
import HelpTab from './components/HelpTab.vue';

export default {
  name: 'App',
  components: {
    HelloWorld, About, Preset, HelpTab
  },data (){
   return {
    page : 1,
   }
  },
  methods: {
    changePage(page_num){
      this.page = page_num
      console.log(this.page)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}

ul {
  list-style-type: none;
  margin-left: auto;
  margin-right: auto;
  padding: 0;
  overflow: hidden;
  background-color: #333;  
  position: -webkit-sticky; /* Safari */
  position: sticky;
  top: 0;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

/* Change the link color to #111 (black) on hover */
li a:hover {
  background-color: #111;
} 

/* .content {
  background-image: url('assets/dice_wallpaper.jpg');
  background-size: cover;
  background-repeat: repeat;
  background-blend-mode: lighten;
  background-color: rgba(255,255,255,0.7);
  min-height: 600px;
}

.main {
  backdrop-filter: blur(7px)
} 
*/

</style>