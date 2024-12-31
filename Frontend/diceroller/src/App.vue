<template>
  <div class="nav">
  <ul>
    <li><a>Home</a></li>
    <li><a>News</a></li>
    <li><a>Contact</a></li>
    <li><a>About</a></li>
  </ul>
  </div>
  
  <HelloWorld msg="Welcome to DiceRoller"/>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
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
  margin-top: 60px;
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

</style>
